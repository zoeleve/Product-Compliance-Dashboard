from django.contrib import admin
from .models import CrmWebhook, WebhookDeliveryLog

@admin.register(CrmWebhook)
class CrmWebhookAdmin(admin.ModelAdmin):
    list_display = ["organisation_name", "url", "is_active", "created_at"]

@admin.register(WebhookDeliveryLog)
class WebhookDeliveryLogAdmin(admin.ModelAdmin):
    list_display = ["webhook", "status", "attempts", "last_attempted_at", "response_code"]
    list_filter = ["status"]
