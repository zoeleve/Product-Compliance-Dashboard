from rest_framework import viewsets
from apps.accounts.permissions import IsAdmin
from .models import CrmWebhook
from .serializers import CrmWebhookSerializer


class CrmWebhookViewSet(viewsets.ModelViewSet):
    queryset = CrmWebhook.objects.all()
    serializer_class = CrmWebhookSerializer
    permission_classes = [IsAdmin]
    http_method_names = ["get", "post", "delete", "head", "options"]
