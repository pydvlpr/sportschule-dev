from django.db import models
from .kunde import Kunde
from .trainer import Trainer
from .kurs import Kurs

class Buchung(models.Model):
    """
    # die Prüfung auf freie Kursplätze erfolgt im entsprechenden Buchungs-View
    # Prüfung auf Doppelbuchung ebenfalls im View
    kurs_nr = models.ForeignKey(Kurs.id, on_delete= models.CASCADE)
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE)

    #kurs = models.ForeignKey(Kurs.beschreibung, on_delete= models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete= models.SET_DEFAULT, default = 0)
    """
