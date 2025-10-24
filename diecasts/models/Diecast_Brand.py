from django.db import models

class DiecastBrand(models.Model):
    
    """
    Model que representa a marca da fabricante da miniatura
    """
    name = models.CharField(max_length=100, blank=True, null=True, default='unnamed') # Ex: Hot Wheels, Matchbox, etc
    country = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'DiecastBrand'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name:
            self.name  = self.name.upper().strip()
        super().save(*args, **kwargs)
    