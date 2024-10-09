from django.db import models

# Create your models here.

class Tarea (models.Model):
    titulo = models.CharField(max_length=200)
    descripcion= models.TextField(blank=True)
    hecho=models.BooleanField(default=False)
    
    
    def __str__(self): #acceder a la instancia del objeto
        return self.titulo #quiero que me muestre el titulo de cada tarea creada
    
    
#que datos seran seleccionanos para enviarlos del backen en json para el front
#en django son serializados en objetos y luego son en querysets (dato complejo)
#django-python-json 

#que campos queremos en un json?