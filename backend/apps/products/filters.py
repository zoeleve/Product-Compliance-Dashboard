import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    regulation = django_filters.CharFilter(
        field_name="compliance_records__regulation__code",
        lookup_expr="iexact",
    )
    compliance_status = django_filters.CharFilter(
        field_name="compliance_records__status",
        lookup_expr="iexact",
    )
    category = django_filters.CharFilter(field_name="category__name", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ["regulation", "compliance_status", "category"]
