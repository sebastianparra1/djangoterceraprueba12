

from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, null=True, blank= True)
    description = models.TextField(null=True, blank= True)
    imagen_portada = models.ImageField(upload_to='images/') 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self): 
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Post', blank=True)

    def __str__(self):
        return f'Carrito de {self.user.username}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length= 64)
    categoria = models.CharField(max_length= 32)
    precio = models.IntegerField()
    

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
class Productosssss(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    imagen_portada = models.ImageField(null=True, blank=True, default="", upload_to='images/')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.nombre} -> ${self.precio}'