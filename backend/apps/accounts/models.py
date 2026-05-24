from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANUFACTURER = "MANUFACTURER", "Manufacturer"
        VIEWER = "VIEWER", "Viewer"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.VIEWER)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_admin_user(self):
        return self.role == self.Role.ADMIN

    @property
    def is_manufacturer(self):
        return self.role == self.Role.MANUFACTURER
