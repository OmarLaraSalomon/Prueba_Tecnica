# 4. API

“Diseña una API simple con Django que permita realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un recurso llamado ‘Tareas’. Proporciona los endpoints necesarios.”

### Requisitos:

    - Tener instalado **Python** en el equipo.
    - Tener instaladas las extensiones de **Django** y **Python** en VSCode.
    - Si necesitas actualizar el pip:

    ```bash
            python -m pip install -U pip
    ```

## Configuración del proyecto

    1. Crear el espacio de trabajo (carpeta).


    2. Comprobar la versión de Python *La versión 4 de Django pide mínimo Python 3.8*.

        ```bash
            python --version
        ```

    3. Instalar el módulo para crear entornos virtuales.

        ```bash
            pip install virtualenv
        ```

    4. Crear el entorno virtual.

        ```bash
            python -m venv venv
        ```

*Si estás trabajando con VSCode, presiona “f1” y escribe “Python interpreter”, da clic a esa opción y selecciona la versión de Python venv (tiene una estrella o aparecerá como la recomendada).*

*Es posible que ahora notes que el indicador del entorno virtual no se ha modificado, es decir, que está ausente o que sigues viendo un indicador existente como (base). No obstante, ten la seguridad de que el entorno sigue activado.*

    5. Instalar las dependencias.

        ```bash
                python -m pip install pipfile 
                python -m pip install pipenv
                pip install django
                pip install pylint
        ```

    6. Crear el proyecto de Django. *El “.” es para que ya no me cree otra carpeta extra*.

        ```bash
                django-admin startproject django_crud_api .
        ```

    7. Correr el servidor para comprobar el levantamiento.

            ```bash
                python manage.py runserver
            ```

    8. Pegar la URL que nos da la terminal en el navegador.

            ```
            http://127.0.0.1:8000/

            ```

*Cancelar la terminal con “ctrl + c”.*


    9. Crear la aplicación.

        ```bash
            python manage.py startapp tareas
        ```

    10. Configurar la aplicación en el proyecto mediante el archivo `settings.py`:

        ```python
            INSTALLED_APPS = [
                "django.contrib.admin",
                "django.contrib.auth",
                "django.contrib.contenttypes",
                "django.contrib.sessions",
                "django.contrib.messages",
                "django.contrib.staticfiles",
                "tareas",
        ]
        ```

    11. Realizar las migraciones.

        ```bash
            python manage.py migrate
        ```


## Django Rest Framework

    1. Instalar Django Rest Framework.

        ```bash
            pip install djangorestframework
        ```

    2. Agregar `rest_framework` en el archivo `settings.py` en el apartado de “INSTALLED_APPS”:

        ```python
            INSTALLED_APPS = [
                
                "django.contrib.staticfiles",
                "rest_framework",
                "tareas",
            ]
        ```

    3. Correr el servidor para comprobar el levantamiento.

        ```bash
            python manage.py runserver
        ```

    4. Pegar la URL que nos da la terminal en el navegador.
        ```
        http://127.0.0.1:8000/
        ```

*Cancelar la terminal con “ctrl + c”.*



## Modelo de Tarea

    1. Ingresar a la carpeta de la aplicación “tareas” y abrir el archivo `models.py`:

        ```python
            class Tarea(models.Model):
                titulo = models.CharField(max_length=200)
                descripcion = models.TextField(blank=True)
                hecho = models.BooleanField(default=False)

                def __str__(self):  # acceder a la instancia del objeto
                return self.titulo  # quiero que me muestre el titulo de cada tarea creada
        ```

    2. Crear la tabla mediante las migraciones.

        ```bash
            python manage.py makemigrations 
        ```

    3. Aplicar la migración.

        ```bash
            python manage.py migrate
        ```

    4. Crear un superusuario para acceder al panel del administrador.

        ```bash
            python manage.py createsuperuser
        ```

        - Crear el nombre de usuario.
        - Añadir correo electrónico.
        - Crear la contraseña.
        - Repetir la contraseña.

*Si aparece "Bypass password validation and create user anyway? [y/N]" confirmar con “y”.*

    5. Añadir el modelo al panel de administrador mediante la carpeta de la aplicación “tareas” y abrir el archivo `admin.py`:

        ```python
            from django.contrib import admin
            from .models import Tarea

            # Register your models here.
            admin.site.register(Tarea)
        ```

    6. Comprobar los resultados corriendo el servidor.

        ```bash
            python manage.py runserver
        ```

    7. Pegar la URL que nos da la terminal en el navegador.

        ```
        http://127.0.0.1:8000/

        ```

    8. Acceder a la ruta del panel administrativo.

        ```
            http://127.0.0.1:8000/admin
        ```

*Ingresar los datos del superusuario que se creó. Se puede acceder a la tabla y crear tareas mediante ese panel.*

*Cancelar la terminal con “ctrl + c”.*



## QuerySet

    1. Crear archivo `serializer.py` en la carpeta de la aplicación “tareas”:

        ```python
            from rest_framework import serializers  # selecciona los campos
            from .models import Tarea

            class TareaSerializer(serializers.ModelSerializer):  # crear modelo serializado
                class Meta:  # información adicional 
                model = Tarea
                fields = '__all__'  # serializar todo
        ```

    2. Crear una clase en el archivo `views.py` de la aplicación “tareas”:

        ```python
            from rest_framework import viewsets  # extender la vista 
            from .serializer import TareaSerializer
            from .models import Tarea

         # Create your views here.
            class TareaView(viewsets.ModelViewSet): 
                serializer_class = TareaSerializer    
                queryset = Tarea.objects.all() 
        ```

    3. Crear archivo `urls.py` dentro de la carpeta de la aplicación “tareas”:

        ```python
            from django.urls import path, include  # crear múltiples rutas 
            from rest_framework import routers  # me va a generar todas las URL de la vista
            from . import views

            router = routers.DefaultRouter()  # a tomar la vista y va a generar todas las URLs 
            router.register(r'tareas', views.TareaView, 'tareas') 

            urlpatterns = [
                path("api/", include(router.urls)),  # todo lo generado por router y quiero esas URLs 
            ]
        ```

    4. Registrar las URLs en el proyecto, para eso ir a `urls.py` del proyecto “django_crud_api”:

        ```python
            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
            path("admin/", admin.site.urls),
            path('tareas/', include('tareas.urls'))  # incluir todas las URLs desde la carpeta tareas el archivo urls
        ]
        ```

    5. Comprobar los resultados corriendo el servidor.

        ```bash
            python manage.py runserver
        ```

    6. Acceder a la interfaz colocando en el navegador la ruta:

        ```
        http://localhost:8000/tareas/api/tareas/
        ```


*Se puede probar con Postman con “Thunder Client”, que es una extensión de VSCode*



### Probamos los request:

- **GET:**
    - `http://localhost:8000/tareas/api/tareas/`
    - `http://localhost:8000/tareas/api/tareas/1`

- **POST:**
    ```json
    {
        "id": 4,
        "titulo": "4ta tarea",
        "descripcion": "Realizando mas pruebas ",
        "hecho": false
    }
    ```



- **PUT:**
    ```json
    {
        "id": 3,
        "titulo": "3ra prueba",
        "descripcion": "Hice una actualización",
        "hecho": false
    }
    ```
    - `http://localhost:8000/tareas/api/tareas/3/`



- **DELETE:**
    - `http://localhost:8000/tareas/api/tareas/4/`



## Documentación de la API

*Cancelar la terminal con “ctrl + c”*.

    1. Instalar módulo coreapi.

        ```bash
                pip install coreapi
        ```

    2. Configurar el módulo coreapi en el archivo `settings.py` en la sección de “INSTALLED_APPS”:

        ```python

            INSTALLED_APPS = [
                "rest_framework",  # django_rest
                "coreapi",
                "tareas",  # la aplicación
            ]
        ```

    3. Al final del `settings.py` colocar el módulo schema:

        ```python
            REST_FRAMEWORK = {
                "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
            }
        ```

    4. Registrar la URL de la documentación en el proyecto, para eso ir a `urls.py` del proyecto “django_crud_api”:

        ```python
            from rest_framework.documentation import include_docs_urls

            urlpatterns = [
            path("api/", include(router.urls)),  # todo lo generado por router y quiero esas URLs 
            path("docs/", include_docs_urls(title="Tareas Api")) 
        ]
        ```

    5. Comprobar los resultados corriendo el servidor.

        ```bash
            python manage.py runserver
        ```

    6. Acceder a la interfaz colocando en el navegador la ruta:

    ```
        http://localhost:8000/tareas/docs/
        
    ```
