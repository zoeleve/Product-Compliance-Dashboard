from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task(name="run_compliance_checks")
def run_compliance_checks():
    from apps.products.models import Product
    from apps.compliance.engine import ComplianceEngine
    engine = ComplianceEngine()
    products = Product.objects.all()
    for product in products:
        try:
            engine.evaluate_product(product.id)
        except Exception as e:
            logger.error(f"Compliance check failed for product {product.id}: {e}")
    logger.info(f"Compliance checks completed for {products.count()} products.")


@shared_task(name="sync_erp_products")
def sync_erp_products():
    from apps.integrations.erp.sync import sync_products_from_odoo
    try:
        sync_products_from_odoo()
    except Exception as e:
        logger.error(f"ERP sync failed: {e}")


@shared_task(name="retry_failed_webhooks")
def retry_failed_webhooks():
    from apps.integrations.crm.models import WebhookDeliveryLog
    from apps.integrations.crm.dispatcher import WebhookDispatcher
    from django.conf import settings
    max_retries = getattr(settings, "CRM_WEBHOOK_MAX_RETRIES", 3)
    failed_logs = WebhookDeliveryLog.objects.filter(
        status="FAILED", attempts__lt=max_retries
    ).select_related("webhook", "compliance_record")
    dispatcher = WebhookDispatcher()
    for log in failed_logs:
        try:
            dispatcher.dispatch(log.webhook, log.compliance_record, existing_log=log)
        except Exception as e:
            logger.error(f"Webhook retry failed for log {log.id}: {e}")
