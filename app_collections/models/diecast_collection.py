from django.db import models
from client.models.clients import Client
from datetime import date



class DiecastCollection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    beginning_date = models.DateField(default=date.today)
    
    class Meta:
        db_table = 'DiecastCollection'
    
    def __str__(self):
        return f"{self.name} ({self.owner.name})"
    
