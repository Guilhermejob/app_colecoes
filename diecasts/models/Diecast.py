from django.db import models
from .Diecast_Model import DiecastModel
from .Car_Brand import CarBrand
from .Car_model import Carmodel
from .Diecast_Brand import DiecastBrand

class Diecast(models.Model):
    """
    Model que representa a miniatura com todos os detalhes
    """
    
    name = models.ForeignKey(DiecastModel, on_delete=models.CASCADE, related_name='diecast_name') # Nome do modelo da miniatura
    brand = models.ForeignKey(DiecastBrand, on_delete=models.CASCADE, related_name='diecast_brand') # Marca da fabricante da miniatura
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='car_brand') # Marca do carro real
    car_model = models.ForeignKey(Carmodel, on_delete=models.CASCADE, related_name='car_model') # Modelo do carro real
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
    
    class Meta:
        db_table = 'Diecast'
    
    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.scale})"