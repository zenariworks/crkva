from django.contrib import admin

from import_export.admin import ImportExportMixin


class KrstenjeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        "get_dete_full_name", "datum", "get_hram_name", "get_svestenik_name"
    )
    ordering = ("datum",)
    search_fields = ["dete__ime", "dete__prezime", "hram__name", "svestenik__osoba__ime", "svestenik__osoba__prezime"]

    def get_dete_full_name(self, obj):
        return f"{obj.dete.ime} {obj.dete.prezime}"
    get_dete_full_name.short_description = 'Дете'

    def get_hram_name(self, obj):
        return obj.hram.name
    get_hram_name.short_description = 'Храм'

    def get_svestenik_name(self, obj):
        svestenik_osoba = obj.svestenik.osoba
        return f"{svestenik_osoba.ime} {svestenik_osoba.prezime}" if svestenik_osoba else ''
    get_svestenik_name.short_description = 'Свештеник'
