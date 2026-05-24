from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductDetailSerializer, ProductListSerializer, CategorySerializer
from .filters import ProductFilter
from apps.accounts.permissions import IsAdmin, IsManufacturer, IsOwnerOrAdmin


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category", "manufacturer").all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return ProductDetailSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == "ADMIN":
            return self.queryset
        if user.role == "MANUFACTURER":
            return self.queryset.filter(manufacturer=user)
        return self.queryset

    def get_permissions(self):
        if self.action == "create":
            return [IsManufacturer()]
        if self.action in ("update", "partial_update"):
            return [IsOwnerOrAdmin()]
        if self.action == "destroy":
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(manufacturer=self.request.user)

    @action(detail=True, methods=["get"], url_path="compliance")
    def compliance(self, request, pk=None):
        from apps.compliance.models import ComplianceRecord
        from apps.compliance.serializers import ComplianceRecordSerializer
        product = self.get_object()
        records = ComplianceRecord.objects.filter(product=product).select_related("regulation")
        return Response(ComplianceRecordSerializer(records, many=True).data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
