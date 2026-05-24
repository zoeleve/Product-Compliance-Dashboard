from django.db import models


class Regulation(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)  # ESPR, REACH, RoHS
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class ComplianceRecord(models.Model):
    class Status(models.TextChoices):
        COMPLIANT = "COMPLIANT", "Compliant"
        NON_COMPLIANT = "NON_COMPLIANT", "Non-Compliant"
        PENDING = "PENDING", "Pending"
        EXEMPTED = "EXEMPTED", "Exempted"

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="compliance_records"
    )
    regulation = models.ForeignKey(
        Regulation, on_delete=models.CASCADE, related_name="compliance_records"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    last_checked = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("product", "regulation")

    def __str__(self):
        return f"{self.product.name} - {self.regulation.code}: {self.status}"
