from django.contrib import admin
from .models import Regulation, ComplianceRecord

@admin.register(Regulation)
class RegulationAdmin(admin.ModelAdmin):
    list_display = ["code", "name"]

@admin.register(ComplianceRecord)
class ComplianceRecordAdmin(admin.ModelAdmin):
    list_display = ["product", "regulation", "status", "last_checked"]
    list_filter = ["status", "regulation"]
