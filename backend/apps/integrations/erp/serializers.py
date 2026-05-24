from rest_framework import serializers
from .models import ErpSyncLog


class ErpSyncLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErpSyncLog
        fields = ["id", "started_at", "completed_at", "status", "records_synced", "error_message"]
