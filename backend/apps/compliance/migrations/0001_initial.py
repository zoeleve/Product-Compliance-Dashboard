import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("products", "0001_initial"),
    ]
    operations = [
        migrations.CreateModel(
            name="Regulation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("code", models.CharField(max_length=20, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="ComplianceRecord",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("status", models.CharField(
                    choices=[
                        ("COMPLIANT","Compliant"),("NON_COMPLIANT","Non-Compliant"),
                        ("PENDING","Pending"),("EXEMPTED","Exempted"),
                    ],
                    default="PENDING", max_length=20,
                )),
                ("last_checked", models.DateTimeField(auto_now=True)),
                ("notes", models.TextField(blank=True)),
                ("expires_at", models.DateTimeField(blank=True, null=True)),
                ("product", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="compliance_records", to="products.product",
                )),
                ("regulation", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="compliance_records", to="compliance.regulation",
                )),
            ],
            options={"unique_together": {("product", "regulation")}},
        ),
    ]
