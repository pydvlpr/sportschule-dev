from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, RegexValidator

"""
    Person

    Abstrakte Klasse für Personendetails (Trainer/Kunde)
"""

class Person(models.Model):

    class Meta:
        abstract = True


    nachname = models.CharField(max_length=100)
    vorname = models.CharField(max_length=100)
    strasse = models.CharField(max_length=100, verbose_name="Straße")
    hausnummer = models.CharField(max_length=100)
    # CharField da sonst plz mit 0 nicht gehen
    plz = models.CharField(max_length=5,verbose_name="PLZ", default="00000",validators=[
        MinLengthValidator(5, "Die Postleitzahl muss 5-stellig sein."),
        RegexValidator('^[0-9]{1,5}$',"Nur Zahlen sind erlaubt.")
        ],)

    stadt = models.CharField(max_length=100, validators=[
            RegexValidator('^[a-zA-Z ]+$',"Nur Buchstaben sind erlaubt.")
            ],)

    #CharField wegen internationaler Nummern
    handy = models.CharField(max_length=30, validators=[
            RegexValidator('^[0-9]+$',"Nur Zahlen sind erlaubt.")
            ],)

    #CharField wegen internationaler Nummern
    festnetz = models.CharField(max_length=30, validators=[
            RegexValidator('^[0-9]+$',"Nur Zahlen sind erlaubt.")
            ],)

    e_mail = models.EmailField(verbose_name="E-Mail")
