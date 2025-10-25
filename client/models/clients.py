from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import ClientManager
from datetime import date
class Client(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, null=False, blank=False)
    nickname = models.CharField(max_length=50, null=False, blank=False, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    age = models.IntegerField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=False, null=False)  # Formato: 000.000.000-00
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    neighborhood = models.CharField(max_length=50, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Campos Obrigatórios para AbstractUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    #Definiçao de Login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'name', 'cpf']
    
    class Meta:
        db_table = 'Client'
    
    #Manager Personalizad
    objects = ClientManager()

    def __str__(self):
        return f"{self.name} ({self.nickname or self.email})"