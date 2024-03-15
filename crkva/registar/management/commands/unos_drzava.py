from django.core.management.base import BaseCommand
from registar.models import Drzava

drzave_i_regexi = {
    "Србија": r"^\d{5}$",
    "Босна и Херцеговина": r"^\d{5}$",
    # ...
}


def unesi_drzavu(naziv) -> tuple[Drzava, bool]:
    regex = drzave_i_regexi.get(naziv, "")
    return Drzava.objects.get_or_create(
        naziv=naziv,
        defaults={"postkod_regex": regex},
    )


class Command(BaseCommand):
    help = "Унос држава, ако већ нису у бази података"

    def handle(self, *args, **kwargs):
        for naziv in drzave_i_regexi.keys():
            drzava, uneta = unesi_drzavu(naziv)
            if uneta:
                info = f"Додата држава `{drzava}`"
                self.stdout.write(self.style.SUCCESS(info))
            else:
                info = f"Држава `{drzava}` већ постоји."
                self.stdout.write(self.style.WARNING(info))
