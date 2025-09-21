from django.db import models

class Brand (models.Model):
    """
    Model que representa a marca da fabricante da miniatura
    """
    
    name = models.CharField(max_length=100, unique=True, blank=False, null=False) # Ex: Nissan, Ford, etc
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Diecast_Model(models.Model):
    """
    Model que representa a miniatura
    """
    
    name = models.CharField(max_length=100, blank=False, null=False) # Ex: 350z, Mustang, etc
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='itens') # Marca da fabricante da miniatura
    series = models.CharField(max_length=100, blank=True, null=True) # Ex: Car Culture, Silver Series, Mainline, etc
    release_year = models.IntegerField(blank=True, null=True) # Ano de lançamento da miniatura
    scale = models.CharField(max_length=20, blank=True, null=True) # Ex: 1:64, 1:43, etc
    notes = models.TextField(blank=True, null=True) # Notas adicionais sobre a miniatura
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.scale})"