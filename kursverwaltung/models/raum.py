from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, RegexValidator

"""
    Raum

    Veranstaltungsort eines Kurses
"""
class Raum(models.Model):

    class Meta:
        pass

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

    sitzplaetze = models.IntegerField(validators=[
        MaxValueValidator(9999999999, "Sitzplatzzahl darf nur maximal 10-stellig sein."),
        MinValueValidator(1)
        ],verbose_name="Sitzplätze")

    ansprechpartner = models.CharField(max_length=100)
    geraeteverantwortlicher = models.CharField(max_length=100, verbose_name="Geräteverantwortlicher")
    strasse = models.CharField(max_length=100,verbose_name="Straße")
    hausnummer = models.CharField(max_length=100)

    plz = models.CharField(max_length=5,verbose_name="PLZ", default="00000",validators=[
        MinLengthValidator(5, "Die Postleitzahl muss 5-stellig sein."),
        RegexValidator('^[0-9]{1,5}$',"Nur Zahlen sind erlaubt.")
        ],)

    stadt = models.CharField(max_length=100, validators=[
            RegexValidator('^[a-zA-Z ]+$',"Nur Buchstaben sind erlaubt.")
            ],)

    def __str__(self):
        return (self.gebaeude+", " +self.strasse+ " "+ self.hausnummer
                +", " +self.plz +" "+self.stadt
                )
