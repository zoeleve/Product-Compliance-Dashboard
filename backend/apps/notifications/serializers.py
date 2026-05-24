from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id", "user", "product", "product_name", "message",
            "notification_type", "is_read", "created_at",
        ]
        read_only_fields = ["id", "user", "created_at"]
