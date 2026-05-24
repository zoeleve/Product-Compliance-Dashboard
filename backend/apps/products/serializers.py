from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    manufacturer_name = serializers.CharField(source="manufacturer.username", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "sku", "category", "category_name", "manufacturer", "manufacturer_name", "created_at"]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True, required=False
    )
    manufacturer_name = serializers.CharField(source="manufacturer.username", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id", "name", "sku", "category", "category_id", "manufacturer",
            "manufacturer_name", "description", "erp_id", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "manufacturer", "erp_id", "created_at", "updated_at"]
