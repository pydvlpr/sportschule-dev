from django.db import models
from .person import Person

class Kunde(Person):
    # zusätziche Daten zu Personendaten

    # AutoField max. Wert ist 2147483647, das reicht
    # wir füllen mit nullen auf, sodass max. 8 stellig wird
    #id = models.AutoField(primary_key=True)
    ansprechpartner = models.CharField(max_length=100)

    class Meta:
        unique_together = (("nachname", "vorname", 'strasse', 'hausnummer', 'stadt'),)

    def __str__(self):
        return ("Kd-Nr.: "+str(self.id)+", Name: " + self.vorname+" " +self.nachname)
