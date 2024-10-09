
from rest_framework import serializers #selecciona los campos
from .models import Tarea
#que datos seran seleccionanos para enviarlos del backen en json para el front

class TareaSerializer(serializers.ModelSerializer): #crear modelo serializado
    class Meta: #informacion adicional 
        model= Tarea
    # fields=("id", "titulo" ,"descripcion", "hecho")
        fields= '__all__' #serializar todo