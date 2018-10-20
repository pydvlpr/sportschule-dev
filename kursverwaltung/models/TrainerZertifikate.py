from django.db import models
from .zertifizierung import Zertifizierung
from .trainer import Trainer

class TrainerZertifikate(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete= models.SET_DEFAULT, default ='')
    zertifizierung  = models.ForeignKey(Zertifizierung, on_delete= models.SET_DEFAULT, default = '')
