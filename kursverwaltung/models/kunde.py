from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, RegexValidator

from .person import Person

"""
    Kunde:

    Abbildung eines Kunden der Sportschule
"""
class Kunde(Person):

    class Meta:
        unique_together = (("nachname", "vorname", 'strasse', 'hausnummer', 'stadt'),)

    # zusätziche Daten zu Personendaten
    ansprechpartner = models.CharField(max_length=100, validators=[
            RegexValidator('^[a-zA-Z ]+$',"Nur Buchstaben sind erlaubt.")
            ],)

    #CharField wegen internationaler Nummern
    fax = models.CharField(max_length=30, validators=[
            RegexValidator('^[0-9]+$',"Nur Zahlen sind erlaubt.")
            ],)



    def __str__(self):
        return (self.vorname+" " +self.nachname+" (Kd-Nr.: "+str(self.id)+")")

    """
        delete:

        Aktualisierung der Kurs-Teilnehmerzahl, wenn Kunde gelöscht wird, zu welchem Buchungen existieren
    """
    def delete(self, *args, **kwargs):
        from .buchung import Buchung
        kunde = self.id

        kurs_buchungen = Buchung.objects.filter(kunde_id = kunde)

        # Teilnehmerzahl in Kursen mit Buchungen zum Kunden reduzieren
        for buchung in kurs_buchungen:
            kurs = buchung.kurs
            aktuelle_teilnehmerzahl = kurs.teilnehmerzahl

            if aktuelle_teilnehmerzahl >= 0:

                kurs.teilnehmerzahl= aktuelle_teilnehmerzahl - 1
                kurs.save()


        super(Kunde, self).delete(*args, **kwargs)
