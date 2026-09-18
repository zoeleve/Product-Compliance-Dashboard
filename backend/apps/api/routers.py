from rest_framework.routers import DefaultRouter

from apps.compliance.views import ComplianceRecordViewSet, RegulationViewSet
from apps.integrations.crm.views import CrmWebhookViewSet
from apps.notifications.views import NotificationViewSet
from apps.products.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"compliance/regulations", RegulationViewSet, basename="regulation")
router.register(
    r"compliance/records", ComplianceRecordViewSet, basename="compliance-record"
)
router.register(r"notifications", NotificationViewSet, basename="notification")
router.register(r"integrations/crm/webhooks", CrmWebhookViewSet, basename="crm-webhook")
