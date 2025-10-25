from django.db import models
from diecasts.models.Diecast import Diecast
from .diecast_collection import DiecastCollection
from client.models import Client

class DiecastCollectionItem(models.Model):
    
    CONDITIONS_CHOICES = [
        ('MT', 'MINT'),
        ('NM','NEAR MINT'),
        ('EX', 'EXCELLENT'),
        ('VG', 'VERY GOOD'),
        ('GD','GOOD'),
        ('PR','POOR'),
        ('DMG', 'DAMEGED')
    ]
    
    collection = models.ForeignKey(DiecastCollection, on_delete=models.CASCADE, related_name='items')
    diecast = models.ForeignKey(Diecast, on_delete=models.CASCADE, related_name='collection_items')
    created_at = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=30, choices=CONDITIONS_CHOICES, default='NM')
    is_sealed = models.BooleanField(default=False)
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, default=10.99)
     
    class Meta:
        db_table = 'DiecastCollectionItem'
        
    def __str__(self):
        return f"{self.diecast} in {self.collection.name}"