from django.db import models

class Diecast_Model(models.Model):
    """
    Model que representa o nome do modelo da miniatura, para fins de padronização
    """
    name = models.CharField(max_length=100, unique=True, blank=True, null=True, default='unnamed') # Ex: 350z, Mustang, etc
    
    def __str__(self):
        return self.name