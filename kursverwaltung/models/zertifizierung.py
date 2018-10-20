from django.db import models

class Zertifizierung(models.Model):
    name = models.CharField(max_length=100)
    gueltig_bis = models.DateField()
    
