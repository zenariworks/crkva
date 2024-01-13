"""
Model class for representing households in the database.
"""
import uuid

from django.db import models

from .slava import Slava
from .ulica import Ulica


class Domacinstvo(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    ime = models.CharField()
    ukuc = models.CharField()

    ulica = models.ForeignKey(Ulica, verbose_name="улица", on_delete=models.SET_NULL, null=True)

    ulbroj = models.IntegerField()
    broj = models.IntegerField()
    oznaka = models.CharField()
    stan = models.IntegerField()
    teldir = models.IntegerField()
    telmob = models.IntegerField()

    slava = models.ForeignKey(Slava, on_delete=models.SET_NULL, null=True, name="слава")

    slavod = models.BooleanField()
    uskvod = models.BooleanField()
    napomena = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.uid}"

    class Meta:
        managed = True
        db_table: str = "domacinstva"
        verbose_name: str = "Домаћинство"
        verbose_name_plural: str = "Домаћинства"
