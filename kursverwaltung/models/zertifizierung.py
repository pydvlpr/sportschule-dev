from django.db import models
from .trainer import Trainer

"""
    Zertifizierung

    Abbildung der Zertifizierung zu Trainer
"""

class Zertifizierung(models.Model):

    class Meta:
        unique_together = (("name", "trainer"),)

    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE,default=0)
    gueltig_bis = models.DateField(verbose_name="Gültig bis:")


    def __str__(self):
        return (self.name+" " +str(self.gueltig_bis))
