# Django URL Shortener

Este es un proyecto Django que implementa un acortador de URLs. Permite a los usuarios acortar URLs largas en otras más cortas y manejables. El proyecto sigue la funcionalidad CRUD (Create, Read, Update, Delete).

## Estructura del Proyecto

```
mi-django-url-acortador
├── manage.py
├── myapp
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations
│ │ └── __init__.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── myproject
│ ├── __init__.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3
└── README.md
```

## Archivos

- `manage.py`: Utilidad de línea de comandos para interactuar con el proyecto Django.
- `myapp/__init__.py`: Archivo vacío que marca el directorio `myapp` como paquete Python.
- `myapp/admin.py`: Fichero para registrar modelos con la interfaz de administración de Django.
- `myapp/apps.py`: Fichero de configuración para la aplicación Django `myapp`.
- `myapp/migrations/__init__.py`: Fichero vacío que marca el directorio `migrations` como paquete Python.
- `myapp/models.py`: Fichero que define los modelos de la aplicación acortadora de URLs.
- `myapp/tests.py`: Fichero que contiene los casos de prueba de la aplicación acortadora de URLs.
- `myapp/urls.py`: Fichero que define los patrones de URL para la aplicación acortadora de URLs.
- `myapp/views.py`: Fichero que contiene las vistas de la aplicación acortadora de URLs.
- `myproject/__init__.py`: Fichero vacío que marca el directorio `myproject` como paquete Python.
- `myproject/settings.py`: Fichero que contiene la configuración del proyecto Django.
- `myproject/urls.py`: Fichero que define los patrones URL para el proyecto Django.
- `myproject/wsgi.py`: Fichero que sirve como punto de entrada para el servidor WSGI.
- `db.sqlite3`: Archivo de base de datos SQLite para almacenar los datos.
- `README.md`: Archivo de documentación del proyecto.

## Configuración

1. Clona el repositorio.
2. Instala las dependencias necesarias.
3. Ejecuta las migraciones para crear las tablas de base de datos necesarias.
4. Iniciar el servidor de desarrollo.

## Uso

- Accede a la aplicación acortadora de URLs a través de la URL proporcionada.
- Crear nuevas URLs acortadas introduciendo la URL larga y enviando el formulario.
- Ver la lista de URLs acortadas existentes.
- Actualice o elimine las URL acortadas existentes según sea necesario.
