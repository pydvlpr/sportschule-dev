from django.db import models
from .raum import Raum
from .trainer import Trainer

class Kurs(models.Model):

    # AutoField max. Wert ist 2147483647, das reicht
    # wir füllen mit nullen auf, sodass max. 8 stellig wird
    #id = str(models.AutoField(primary_key=True)).zfill(8)
    titel = models.CharField(max_length=100, unique=True)
    beschreibung = models.CharField(max_length=32767, default=" ")
    anfangszeit = models.DateTimeField()
    endzeit = models.DateTimeField()
    raum = models.ForeignKey(Raum, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    # Teilnehmerzahl darf max. Teilnehmer nicht überschreiten,
    # das soll aber das Form prüfen (d.h. dort max_value setzten)
    teilnehmerzahl = models.IntegerField()
    max_teilnehmer = models.IntegerField()

    # 6 Stellen vor dem Komma, zwei danach
    gebuehr = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["-id", "-anfangszeit"]

    def __str__(self):
        return self.titel
