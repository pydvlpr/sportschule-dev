from django.db import models
from .person import Person
from .zertifizierung import Zertifizierung

class Trainer(Person):
    # zusätziche Daten zu Personendaten
    bemerkung = models.CharField(max_length=32767)
    zertifizierung = models.ManyToManyField(Zertifizierung)
    geb_datum = models.DateField(verbose_name="Geburtstag")

    def __str__(self):
        return ("Trainer-ID: "+str(self.id)+", Name: " + self.vorname+" " +self.nachname)
