from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.integrations.erp.views import ErpSyncView, ErpStatusView
from apps.accounts.views import UserProfileView
from .routers import router

urlpatterns = [
    path("", include(router.urls)),
    path("auth/token/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/profile/", UserProfileView.as_view(), name="user-profile"),
    path("integrations/erp/sync/", ErpSyncView.as_view(), name="erp-sync"),
    path("integrations/erp/status/", ErpStatusView.as_view(), name="erp-status"),
]
