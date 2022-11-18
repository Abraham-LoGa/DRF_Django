from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, related_name='mark',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
