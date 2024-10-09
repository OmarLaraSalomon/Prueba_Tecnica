from rest_framework import viewsets #extender la vista 
from .serializer import TareaSerializer
from .models import Tarea
# Create your views here.


#con una sola clase creamos el crud de forma automatica, django lo hace 
class TareaView(viewsets.ModelViewSet) : #nos va permitir extender
    #ejecuta esete serializer
    serializer_class= TareaSerializer #que traiga la clase 
    queryset= Tarea.objects.all() #traigo todas las tareas y s ele asignan al query