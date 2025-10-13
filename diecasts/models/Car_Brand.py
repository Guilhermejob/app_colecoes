from django.db import models

class Car_Brand (models.Model):
    """
    Model que representa a marca da fabricante da miniatura
    """
    name = models.CharField(max_length=100, unique=True, blank=True, null=True, default='unnamed') # Ex: Nissan, Ford, etc
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name