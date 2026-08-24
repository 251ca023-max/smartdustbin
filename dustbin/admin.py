from django.contrib import admin
from .models import WasteData, Alert


@admin.register(WasteData)
class WasteDataAdmin(admin.ModelAdmin):

    list_display = (
        "bin_id",
        "distance",
        "waste_level",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "bin_id",
    )

    ordering = (
        "-created_at",
    )


admin.site.register(Alert)