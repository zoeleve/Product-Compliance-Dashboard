from django.contrib import admin
from .models import ErpSyncLog

@admin.register(ErpSyncLog)
class ErpSyncLogAdmin(admin.ModelAdmin):
    list_display = ["started_at", "completed_at", "status", "records_synced"]
    list_filter = ["status"]
