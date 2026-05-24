from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.permissions import IsAdmin
from .models import ErpSyncLog
from .serializers import ErpSyncLogSerializer


class ErpSyncView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        from celery_app.tasks import sync_erp_products
        task = sync_erp_products.delay()
        return Response({"status": "sync started", "task_id": task.id}, status=status.HTTP_202_ACCEPTED)


class ErpStatusView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        log = ErpSyncLog.objects.first()
        if not log:
            return Response({"status": "no sync performed yet"})
        return Response(ErpSyncLogSerializer(log).data)
