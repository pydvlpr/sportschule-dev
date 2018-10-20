from django.db import models
from .person import Person

class Kunde(Person):
    # zusätziche Daten zu Personendaten

    # AutoField max. Wert ist 2147483647, das reicht
    # wir füllen mit nullen auf, sodass max. 8 stellig wird
    kd_nr = int(str(models.AutoField(primary_key=True)).zfill(8))
    ansprechpartner = models.CharField()
