from django.db import models

class Person(models.Model):

    nachname = models.CharField(max_length=100)
    vorname = models.CharField(max_length=100)
    strasse = models.CharField(max_length=100, verbose_name="Straße")
    hausnummer = models.CharField(max_length=5)
    # CharField da sonst plz mit 0 nicht gehen
    plz = models.CharField(max_length=5,verbose_name="PLZ")
    stadt = models.CharField(max_length=100)

    #CharField wegen internationaler Nummern
    handy = models.CharField(max_length=30)

    #CharField wegen internationaler Nummern
    festnetz = models.CharField(max_length=30)

    e_mail = models.EmailField(verbose_name="E-Mail")

    class Meta:
        abstract = True
