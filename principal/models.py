#encoding:utf-8
from django.db import models

# Create your models here.
class Imagen(models.Model):
    nombre=models.CharField(primary_key=True,max_length=50,verbose_name='Nombre')
    ejercicio=models.ImageField(upload_to='ejercicios',verbose_name='Imagen')
    descripcion=models.TextField(verbose_name='Descripcion')
    nivel=models.IntegerField()
    
     def __unicode__(self):
        return self.nombre

