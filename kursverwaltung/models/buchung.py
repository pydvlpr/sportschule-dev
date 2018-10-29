from django.db import models
from .kunde import Kunde
from .trainer import Trainer
from .kurs import Kurs

class Buchung(models.Model):
    """
    # die Prüfung auf freie Kursplätze erfolgt im entsprechenden Buchungs-View
    # Prüfung auf Doppelbuchung ebenfalls im View
    """
    datum = models.DateField(verbose_name="Datum",auto_now_add=True)
    kurs = models.ForeignKey(Kurs, on_delete= models.CASCADE, default = 0, verbose_name="Kurs")
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE, default = 0)

    def __str__(self):
        return ("Datum: "+str(self.datum)+", Kunde: "+str(self.kunde))

    class Meta:
        #schauen, ob das funktioniert
        ordering = ["-datum"]
        unique_together = (("kurs", "kunde"),)
