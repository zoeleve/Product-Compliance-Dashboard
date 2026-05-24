from rest_framework import serializers
from .models import Regulation, ComplianceRecord


class RegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulation
        fields = ["id", "name", "code", "description"]


class ComplianceRecordSerializer(serializers.ModelSerializer):
    regulation_code = serializers.CharField(source="regulation.code", read_only=True)
    regulation_name = serializers.CharField(source="regulation.name", read_only=True)

    class Meta:
        model = ComplianceRecord
        fields = [
            "id", "product", "regulation", "regulation_code", "regulation_name",
            "status", "last_checked", "notes", "expires_at",
        ]
        read_only_fields = ["id", "last_checked"]
