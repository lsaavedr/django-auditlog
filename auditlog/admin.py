from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from auditlog.filters import ResourceTypeFilter
from auditlog.mixins import LogEntryAdminMixin
from auditlog.models import LogEntry


class LogEntryAdmin(admin.ModelAdmin, LogEntryAdminMixin):
    list_display = ["created", "resource_url", "action", "msg_short", "user_url"]
    search_fields = [
        "timestamp",
        "object_repr",
        "changes",
        "actor__first_name",
        "actor__last_name",
        "actor__username",
    ]
    list_filter = ["action", ResourceTypeFilter]
    readonly_fields = ["created", "resource_url", "action", "user_url", "msg"]
    fieldsets = [
        (None, {"fields": ["created", "user_url", "resource_url"]}),
        (_("Changes"), {"fields": ["action", "msg"]}),
    ]


admin.site.register(LogEntry, LogEntryAdmin)
