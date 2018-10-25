from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .raum import Raum
from .trainer import Trainer

class Kurs(models.Model):

    titel = models.CharField(max_length=100, unique=True)
    beschreibung = models.CharField(max_length=32767, default=" ")

    # Datum/Zeit-Erfassung sollte mit Javascrip Widget erfolgen
    anfangszeit = models.DateTimeField(help_text="Format: Tag.Monat.Jahr Stunde:Minute")
    endzeit = models.DateTimeField(help_text="Format: Tag.Monat.Jahr Stunde:Minute")

    raum = models.ForeignKey(Raum, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    # Teilnehmerzahl darf max. Teilnehmer nicht überschreiten,
    # das soll aber das Form prüfen (d.h. dort max_value setzen)
    max_teilnehmer = models.IntegerField(default=10, verbose_name="Max. Teilnehmer")

    teilnehmerzahl = models.IntegerField(default=1)
    """
    ,
            validators=[
                MaxValueValidator(num),
                MinValueValidator(1)
                ],
            )
    """

    # 6 Stellen vor dem Komma, zwei danach
    gebuehr = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Gebühr")

    def __str__(self):
        return ("Kurs-ID: "+str(self.id)+"<br>"+
                "Titel: "+self.titel+"<br>"+
                "Trainer: "+str(self.trainer)
                )


    class Meta:
        # Sortierung
        ordering = ["id", "-anfangszeit"]
