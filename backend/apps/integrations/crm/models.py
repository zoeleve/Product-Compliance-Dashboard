from django.db import models


class CrmWebhook(models.Model):
    organisation_name = models.CharField(max_length=100)
    url = models.URLField()
    secret = models.CharField(max_length=255, blank=True)
    payload_template = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organisation_name} - {self.url}"


class WebhookDeliveryLog(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "SUCCESS", "Success"
        FAILED = "FAILED", "Failed"

    webhook = models.ForeignKey(CrmWebhook, on_delete=models.CASCADE, related_name="delivery_logs")
    compliance_record = models.ForeignKey(
        "compliance.ComplianceRecord", on_delete=models.CASCADE, related_name="webhook_logs"
    )
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.FAILED)
    attempts = models.IntegerField(default=0)
    last_attempted_at = models.DateTimeField(auto_now=True)
    response_code = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["-last_attempted_at"]
