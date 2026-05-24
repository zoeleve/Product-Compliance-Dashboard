import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("compliance", "0001_initial"),
    ]
    operations = [
        migrations.CreateModel(
            name="CrmWebhook",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("organisation_name", models.CharField(max_length=100)),
                ("url", models.URLField()),
                ("secret", models.CharField(blank=True, max_length=255)),
                ("payload_template", models.JSONField(blank=True, default=dict)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WebhookDeliveryLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("status", models.CharField(
                    choices=[("SUCCESS","Success"),("FAILED","Failed")],
                    default="FAILED", max_length=10,
                )),
                ("attempts", models.IntegerField(default=0)),
                ("last_attempted_at", models.DateTimeField(auto_now=True)),
                ("response_code", models.IntegerField(blank=True, null=True)),
                ("compliance_record", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="webhook_logs", to="compliance.compliancerecord",
                )),
                ("webhook", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="delivery_logs", to="crm.crmwebhook",
                )),
            ],
            options={"ordering": ["-last_attempted_at"]},
        ),
    ]
