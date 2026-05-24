from rest_framework import serializers
from .models import CrmWebhook, WebhookDeliveryLog


class CrmWebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmWebhook
        fields = ["id", "organisation_name", "url", "secret", "payload_template", "is_active", "created_at"]
        extra_kwargs = {"secret": {"write_only": True}}


class WebhookDeliveryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookDeliveryLog
        fields = ["id", "webhook", "compliance_record", "status", "attempts", "last_attempted_at", "response_code"]
