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
    Model que representa o nome do modelo da miniatura, para fins de padronização
    """
    name = models.CharField(max_length=100, unique=True, blank=False, null=False) # Ex: 350z, Mustang, etc
    
    def __str__(self):
        return self.name
    
class Diecast(models.Model):
    """
    Model que representa a miniatura com todos os detalhes
    """
    
    name = models.ForeignKey(Diecast_Model, on_delete=models.CASCADE, related_name='itens') # Nome do modelo da miniatura
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='itens') # Marca da fabricante da miniatura
    car_brand = models.CharField(max_length=100, blank=True, null=True) # Marca do carro real
    series = models.CharField(max_length=100, blank=True, null=True) # Ex: Car Culture, Mainline, RLC etc
    sub_series = models.CharField(max_length=100, blank=True, null=True) # Ex: Fast & Furious, Star Wars, etc
    release_year = models.IntegerField(blank=True, null=True) # Ano de lançamento da miniatura
    base_number = models.CharField(max_length=15, blank=True, null=True) # Número da base da miniatura
    color = models.CharField(max_length=50, blank=True, null=True) # Cor da miniatura
    wheel_type = models.CharField(max_length=50, blank=True, null=True) # Tipo de roda da miniatura
    designer = models.CharField(max_length=100, blank=True, null=True) # Nome do designer da miniatura
    scale = models.CharField(max_length=20, blank=True, null=True) # Ex: 1:64, 1:43, etc
    notes = models.TextField(blank=True, null=True) # Notas adicionais sobre a miniatura
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.scale})"

