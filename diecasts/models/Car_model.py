from django.db import models


class Car_model(models.Model):
    """
    Model que representa o nome do modelo do carro real, para fins de padronização
    """
    name = models.CharField(max_length=100, blank=True, null=True, default='unnamed') # Ex: 350z, Mustang, etc
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name:
            self.name  = self.name.upper().strip()
        super().save(*args, **kwargs)