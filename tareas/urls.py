from django.urls import path, include #crear multiples rutas 
from rest_framework import routers #me va a generar todas las url de la vista
from . import views
from rest_framework.documentation import include_docs_urls


router= routers.DefaultRouter() #a tomar la vvista y va a generar todas las urls 
router.register(r'tareas', views.TareaView, 'tareas' ) #registrando un nueva ruta basada en la vista 

#definir las rutas
urlpatterns = [
    path("api/" , include(router.urls)), #todo lo generado por router y quiero esas urls 
    path("docs/" , include_docs_urls(title= "Tareas Api")) #tiodo lo generado por router y quiero esas urls 
]

#va a generar las rutas get post put delete