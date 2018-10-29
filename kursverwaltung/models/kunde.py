from django.db import models
from .person import Person

class Kunde(Person):
    # zusätziche Daten zu Personendaten

    ansprechpartner = models.CharField(max_length=100)

    #CharField wegen internationaler Nummern
    fax = models.CharField(max_length=30)

    class Meta:
        unique_together = (("nachname", "vorname", 'strasse', 'hausnummer', 'stadt'),)

    def __str__(self):
        return (self.vorname+" " +self.nachname+" (Kd-Nr.: "+str(self.id)+")")
