from django.contrib import admin
from import_export.admin import ImportExportMixin


class VencanjeAdmin(admin.ModelAdmin):
    list_display = (
        "knjiga_strana_broj",
        "zenik",
        "nevesta",
        "datum",
        "svestenik",
        "hram",
    )

    def knjiga_strana_broj(self, obj):
        return f"{obj.knjiga}.{obj.strana}.{obj.tekuci_broj}"

    knjiga_strana_broj.short_description = "Књига.страна.број"

    fieldsets = (
        (None, {"fields": (("knjiga", "strana", "tekuci_broj"),)}),
        (
            "Информације о венчању",
            {
                "fields": (
                    "datum",
                    ("zenik",
                    "zenik_rb_brak",),
                    ("nevesta",
                    "nevesta_rb_brak",),
                    "datum_ispita",
                )
            },
        ),
        ("Породичне информације", {"fields": (("tast", "tasta"), ("svekar", "svekrva"))}),
        (
            "Детаљи церемоније",
            {
                "fields": (
                    "hram",
                    "svestenik",
                    "parohija",
                    "kum",
                    "kuma",
                    "napomena",
                )
            },
        ),
    )
    readonly_fields = ("uid",)
