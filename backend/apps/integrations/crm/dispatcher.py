import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class WebhookDispatcher:
    def dispatch(self, webhook, compliance_record, existing_log=None) -> None:
        from apps.integrations.crm.models import WebhookDeliveryLog
        timeout = getattr(settings, "CRM_WEBHOOK_TIMEOUT_SECONDS", 10)
        payload = self._build_payload(webhook, compliance_record)
        log = existing_log or WebhookDeliveryLog(webhook=webhook, compliance_record=compliance_record)
        log.attempts += 1
        try:
            response = requests.post(
                webhook.url, json=payload, timeout=timeout,
                headers={"X-Webhook-Secret": webhook.secret} if webhook.secret else {},
            )
            log.response_code = response.status_code
            log.status = (
                WebhookDeliveryLog.Status.SUCCESS
                if response.ok
                else WebhookDeliveryLog.Status.FAILED
            )
            response.raise_for_status()
        except requests.RequestException as e:
            log.status = WebhookDeliveryLog.Status.FAILED
            logger.error(f"Webhook to {webhook.url} failed: {e}")
        finally:
            log.save()

    def _build_payload(self, webhook, compliance_record) -> dict:
        base = {
            "product_id": compliance_record.product_id,
            "product_name": compliance_record.product.name,
            "regulation": compliance_record.regulation.code,
            "status": compliance_record.status,
            "last_checked": (
                compliance_record.last_checked.isoformat()
                if compliance_record.last_checked
                else None
            ),
        }
        if webhook.payload_template:
            t = webhook.payload_template.copy()
            t.update(base)
            return t
        return base
