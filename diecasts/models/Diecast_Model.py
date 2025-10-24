from django.db import models

class DiecastModel(models.Model):
    """
    Model que representa o nome do modelo da miniatura, para fins de padronizaçao
    """
    name = models.CharField(max_length=100, blank=True, null=True, default='unnamed') # Ex: 350z, Mustang, etc
    
    class Meta:
        db_table = 'DiecastModel'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name:
            self.name  = self.name.upper().strip()
        super().save(*args, **kwargs)