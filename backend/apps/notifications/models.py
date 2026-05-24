from django.db import models
from django.conf import settings


class Notification(models.Model):
    class Type(models.TextChoices):
        IN_APP = "IN_APP", "In-App"
        EMAIL = "EMAIL", "Email"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE,
        related_name="notifications", null=True, blank=True,
    )
    message = models.TextField()
    notification_type = models.CharField(
        max_length=10, choices=Type.choices, default=Type.IN_APP
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"[{self.notification_type}] {self.user.username}: {self.message[:50]}"
