from django.db import models
from .kunde import Kunde
from .kurs import Kurs

"""
    Buchung

    Zusammenführung von Kunde zur Kurs

    Die Prüfung auf freie Kursplätze erfolgt im entsprechenden Buchungs-View
    Prüfung auf Doppelbuchung ebenfalls im View

"""

class Buchung(models.Model):

    class Meta:
        #schauen, ob das funktioniert
        ordering = ["-datum"]
        unique_together = (("kurs", "kunde"),)

    datum = models.DateField(verbose_name="Datum",auto_now_add=True,help_text="Datum der Buchung")
    kurs = models.ForeignKey(Kurs, on_delete= models.CASCADE, default = 0, verbose_name="Kurs", help_text="Kurs zur Buchung auswählen.")
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE, default = 0, help_text="Kunde zur Buchung auswählen.")




    def __str__(self):
        return ("Datum: "+str(self.datum)+", Kunde: "+str(self.kunde))


    """
        delete

        Aktualisierung der Teilnehmerzahl eines Kurses, wenn Buchung gelöscht wird.
        Wird nicht automatisch aufgerufen, bei kaskadierenden Löschungen (über Kurs, Kunde)

    """
    def delete(self, *args, **kwargs):

        kurs = self.kurs

        aktuelle_teilnehmerzahl = kurs.teilnehmerzahl

        # Validierung der Teilnehmerzahl
        if aktuelle_teilnehmerzahl >= 0:
            # neue teilnehmerzahl festlegen und speichern
            kurs.teilnehmerzahl= aktuelle_teilnehmerzahl - 1
            kurs.save()

        super(Buchung, self).delete(*args, **kwargs)
