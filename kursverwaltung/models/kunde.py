from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, RegexValidator
from .person import Person

class Kunde(Person):
    # zusätziche Daten zu Personendaten

    ansprechpartner = models.CharField(max_length=100, validators=[
            RegexValidator('^[A-Za-z]+$',"Nur Buchstaben sind erlaubt.")
            ],)

    #CharField wegen internationaler Nummern
    fax = models.CharField(max_length=30, validators=[
            RegexValidator('^[0-9]+$',"Nur Zahlen sind erlaubt.")
            ],)

    class Meta:
        unique_together = (("nachname", "vorname", 'strasse', 'hausnummer', 'stadt'),)

    def __str__(self):
        return (self.vorname+" " +self.nachname+" (Kd-Nr.: "+str(self.id)+")")
