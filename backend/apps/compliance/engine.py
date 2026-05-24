import logging
from django.utils import timezone

logger = logging.getLogger(__name__)


class ComplianceEngine:
    def evaluate_product(self, product_id: int) -> None:
        from apps.products.models import Product
        from apps.compliance.models import Regulation, ComplianceRecord
        from apps.notifications.service import NotificationService

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            logger.warning(f"Product {product_id} not found.")
            return

        regulations = Regulation.objects.all()
        notification_service = NotificationService()

        for regulation in regulations:
            record, created = ComplianceRecord.objects.get_or_create(
                product=product,
                regulation=regulation,
                defaults={"status": ComplianceRecord.Status.PENDING},
            )
            old_status = record.status
            new_status = self._evaluate_status(product, regulation)

            if new_status != old_status:
                record.status = new_status
                record.last_checked = timezone.now()
                record.save()
                logger.info(
                    f"Product {product.name} | {regulation.code}: {old_status} -> {new_status}"
                )
                if new_status == ComplianceRecord.Status.NON_COMPLIANT:
                    msg = (
                        f"Product '{product.name}' is now NON-COMPLIANT "
                        f"with {regulation.code}."
                    )
                    notification_service.send_in_app(product.manufacturer, product, msg)
                    notification_service.send_email(product.manufacturer, product, msg)
                self._dispatch_webhooks(record)

    def _evaluate_status(self, product, regulation) -> str:
        from apps.compliance.models import ComplianceRecord
        # Placeholder: extend with real regulation-specific business rules
        if product.erp_id:
            return ComplianceRecord.Status.COMPLIANT
        return ComplianceRecord.Status.PENDING

    def _dispatch_webhooks(self, compliance_record) -> None:
        from apps.integrations.crm.models import CrmWebhook
        from apps.integrations.crm.dispatcher import WebhookDispatcher
        dispatcher = WebhookDispatcher()
        for webhook in CrmWebhook.objects.filter(is_active=True):
            try:
                dispatcher.dispatch(webhook, compliance_record)
            except Exception as e:
                logger.error(f"Webhook dispatch failed for {webhook.url}: {e}")
