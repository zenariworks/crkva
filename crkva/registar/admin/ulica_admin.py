from django.contrib import admin
from import_export.admin import ImportExportMixin


class UlicaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("naziv", "svestenik")
    search_fields = ("naziv", "svestenik")
    ordering = ("naziv",)
