from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "action",
        "module",
        "object_id",
        "timestamp",
    )
    search_fields = (
        "action",
        "module",
    )
    list_filter = (
        "module",
        "timestamp",
    )