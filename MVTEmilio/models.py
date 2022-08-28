from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=54)
    edad=models.IntegerField()
    documento=models.IntegerField()
    fecha_nacimiento=models.CharField(max_length=20)
    parentezco=models.CharField(max_length=30)
    
# Create your models here.
