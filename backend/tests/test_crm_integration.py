import pytest
import responses as responses_lib
from apps.integrations.crm.models import CrmWebhook
from apps.integrations.crm.dispatcher import WebhookDispatcher


@pytest.mark.django_db
def test_webhook_create(api_client, admin_user):
    api_client.force_authenticate(admin_user)
    response = api_client.post("/api/integrations/crm/webhooks/", {
        "organisation_name": "TestCRM",
        "url": "https://crm.example.com/webhook",
        "is_active": True,
    })
    assert response.status_code == 201
    assert CrmWebhook.objects.filter(organisation_name="TestCRM").exists()


@pytest.mark.django_db
@responses_lib.activate
def test_dispatcher_success(sample_compliance_record):
    webhook = CrmWebhook.objects.create(
        organisation_name="CRM",
        url="https://crm.example.com/hook",
        is_active=True,
    )
    responses_lib.add(responses_lib.POST, "https://crm.example.com/hook", status=200)
    WebhookDispatcher().dispatch(webhook, sample_compliance_record)
    from apps.integrations.crm.models import WebhookDeliveryLog
    log = WebhookDeliveryLog.objects.get(webhook=webhook)
    assert log.status == "SUCCESS"
