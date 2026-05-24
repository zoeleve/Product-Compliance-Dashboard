from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="ErpSyncLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("started_at", models.DateTimeField(auto_now_add=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(
                    choices=[("RUNNING","Running"),("SUCCESS","Success"),("FAILED","Failed")],
                    default="RUNNING", max_length=10,
                )),
                ("records_synced", models.IntegerField(default=0)),
                ("error_message", models.TextField(blank=True)),
            ],
            options={"ordering": ["-started_at"]},
        ),
    ]
