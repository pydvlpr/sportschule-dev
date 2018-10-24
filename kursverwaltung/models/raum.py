from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Raum(models.Model):
    raum_nr = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
            ],
        verbose_name="Raum-Nr."
        )

    gebaeude = models.CharField(max_length=100, verbose_name="Gebäude")
    bemerkung = models.CharField(max_length=32767)
    sitzplaetze = models.IntegerField(verbose_name="Sitzplätze")
    ansprechpartner = models.CharField(max_length=100)
    geraeteverantwortlicher = models.CharField(max_length=100, verbose_name="Geräteverantwortlicher")
    strasse = models.CharField(max_length=100,verbose_name="Straße")
    hausnummer = models.CharField(max_length=100)
    plz = models.CharField(max_length=5,verbose_name="PLZ", default="00000")
    stadt = models.CharField(max_length=100)

    def __str__(self):
        return ("Raum-ID: "+str(self.id)+", Gebäude: " +
                self.gebaeude+", " +self.strasse
                +", " +self.stadt
                )
