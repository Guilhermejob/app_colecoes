from django.db import models
from app_collection.models.Diecast import Diecast
from .diecast_collection import DiecastCollection

class DiecastCollectionItem(models.Model):
    collection = models.ForeignKey(DiecastCollection, on_delete=models.CASCADE, related_name='items')
    diecasts = models.ForeignKey(Diecast, on_delete=models.CASCADE, related_name='collection_items')
    beginning_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
     
    class Meta:
        unique_together = ('collection', 'diecasts')  # evita duplicatas na coleção
        
    def __str__(self):
        self.collection, self.diecasts, self.beginning_date, self.created_at