from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager




class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
   

class Contacto(models.Model):
    nombre = models.CharField(max_length=13, blank=False, null = True)
    email = models.EmailField()
    mensaje = models.CharField(max_length=300, blank=False, null= True)
    def __str__(self):
        return self.nombre

class Registrado(models.Model):
    nombre = models.CharField(max_length=13, blank=False, null=True)
    email = models.EmailField()
    rut = models.CharField(max_length=13, blank=False, null=True)
    fechaNacimiento = models.DateField(null = True)
    telefono = models.IntegerField(null=True)
    calle = models.CharField(max_length=100, blank=False, null=True)
    numero_calle = models.CharField(max_length=100, blank=False, null=True)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email


