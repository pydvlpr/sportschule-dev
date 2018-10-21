from django.db import models

class Raum(models.Model):
    raum_nr = models.IntegerField()
    gebaeude = models.CharField(max_length=100)
    bemerkung = models.CharField(max_length=32767)
    sitzplaetze = models.IntegerField()
    ansprechpartner = models.CharField(max_length=100)
    geraeteverantwortlicher = models.CharField(max_length=100)
    strasse = models.CharField(max_length=100)
    hausnummer = models.CharField(max_length=100)
    stadt = models.CharField(max_length=100)
