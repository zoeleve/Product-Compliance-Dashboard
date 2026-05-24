from rest_framework import viewsets, permissions
from .models import Regulation, ComplianceRecord
from .serializers import RegulationSerializer, ComplianceRecordSerializer


class RegulationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Regulation.objects.all()
    serializer_class = RegulationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComplianceRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ComplianceRecord.objects.select_related("product", "regulation").all()
    serializer_class = ComplianceRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["product", "regulation", "status"]
