"""
Model class for representing sets in the database.
"""
import uuid

from django.db import models

from .zanimanje import Zanimanje
from .narodnost import Narodnost
from .veroispovest import Veroispovest


class Osoba(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    ime = models.CharField(verbose_name="име")
    prezime = models.CharField(verbose_name="презиме")
    mesto_rodjenja = models.CharField(verbose_name="место рођења")
    datum_rodjenja = models.DateField(verbose_name="датум рођења")
    vreme_rodjenja = models.TimeField(verbose_name="време рођења", blank=True)
    pol = models.CharField(
        verbose_name="пол", choices=[("М", "мушки"), ("Ж", "женски")]
    )

    devojacko_prezime = models.CharField(verbose_name="девојачко презиме", blank=True)
    zanimanje = models.ForeignKey(
        Zanimanje, verbose_name="занимање", on_delete=models.CASCADE, blank=True
    )
    veroispovest = models.ForeignKey(
        Veroispovest, verbose_name="вероисповест", on_delete=models.CASCADE, blank=True
    )
    narodnost = models.ForeignKey(
        Narodnost, verbose_name="народност", on_delete=models.CASCADE, blank=True
    )
    adresa = models.CharField(verbose_name="адреса", blank=True)

    def __str__(self):
        return f"{self.ime} {self.prezime}"

    class Meta:
        managed = True
        db_table = "osobe"
        verbose_name = "Особа"
        verbose_name_plural = "Особе"
