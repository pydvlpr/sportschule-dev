from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .raum import Raum
from .trainer import Trainer

"""
    Kurs

    Abbildung eines Kurses der Sportschule
"""
class Kurs(models.Model):

    class Meta:
        # Sortierung
        ordering = ["id", "-anfangszeit"]
        unique_together = (("raum", 'anfangszeit' ),)

    titel = models.CharField(max_length=100, unique=True,help_text="Titel des Kurses eingeben.")
    beschreibung = models.CharField(max_length=32767, help_text="Beschreibung des Kurses eingeben.")

    # Datum/Zeit-Erfassung sollte mit Javascrip Widget erfolgen
    anfangszeit = models.DateTimeField(help_text="Anfangszeit des Kurses eingeben. (Format: Tag.Monat.Jahr Stunde:Minute)")
    endzeit = models.DateTimeField(help_text="Anfangszeit des Kurses eingeben. (Format: Tag.Monat.Jahr Stunde:Minute)")

    raum = models.ForeignKey(Raum, blank=True, null=True, on_delete=models.CASCADE,help_text="Raum des Kurses auswählen.")
    trainer = models.ForeignKey(Trainer, blank=True, null=True, on_delete=models.CASCADE, help_text="Trainer des Kurses auswählen.")

    max_teilnehmer = models.IntegerField(default=10, verbose_name="Max. Teilnehmer",help_text="Maximale Teilnehmerzahl festlegen.")

    teilnehmerzahl = models.IntegerField(default=0,help_text="Aktuelle Zahl der Teilnehmer.")

    # 6 Stellen vor dem Komma, zwei danach
    gebuehr = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Gebühr",help_text="Gebühr des Kurses (€) eingeben.")

    def __str__(self):
        return ( self.titel+" (Kurs-Nr. "+str(self.id)+")"+ ", Trainer: "+str(self.trainer)   )
