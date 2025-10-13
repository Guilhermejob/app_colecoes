from django.db import models
from app_collection.models.Diecast import Diecast
from .diecast_collection import DiecastCollection

class DiecastCollectionItem(models.Model):
    collection = models.ForeignKey(DiecastCollection, on_delete=models.CASCADE, related_name='items')
    diecasts = models.ForeignKey(Diecast, on_delete=models.CASCADE, related_name='collection_items')
    created_at = models.DateTimeField(auto_now_add=True)
     
    class Meta:
        unique_together = ('collection', 'diecasts')
        verbose_name = "Diecast Collection Item"
        verbose_name_plural = "Diecast Collection Items"
        
    def __str__(self):
        return f"{self.diecast} in {self.collection.name}"