"""
Configuración de Django para el proyecto proyectotaller.

Generado por 'django-admin startproject' usando Django 5.2.6.

Para más información sobre este archivo, consulte
https://docs.djangoproject.com/en/5.2/topics/settings/

Para la lista completa de configuraciones y sus valores, consulte
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Define la base del directorio del proyecto.
# BASE_DIR es el directorio que contiene manage.py.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de desarrollo rápido - no apto para producción
# Consulte https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: ¡mantenga en secreto la clave secreta utilizada en producción!
# Esta clave se utiliza para la seguridad criptográfica de Django.
SECRET_KEY = 'django-insecure-$kqch7+8lr*k#1eu(t9lh$u2wlb+9ir1ui*+y2_ppf#rhv4=7^'

# ADVERTENCIA DE SEGURIDAD: ¡no ejecute con DEBUG activado en producción!
# DEBUG = True activa el modo de depuración, mostrando errores detallados.
DEBUG = True

# Lista de hosts permitidos para servir la aplicación.
# En producción, esto debería contener los nombres de dominio de su sitio.
ALLOWED_HOSTS = []


# Definición de la aplicación

# Aplicaciones instaladas en el proyecto.
# Incluye aplicaciones de Django por defecto y aplicaciones personalizadas.
INSTALLED_APPS = [
    'django.contrib.admin', # Interfaz de administración de Django
    'django.contrib.auth', # Sistema de autenticación
    'django.contrib.contenttypes', # Tipos de contenido para modelos
    'django.contrib.sessions', # Gestión de sesiones
    'django.contrib.messages', # Framework de mensajes
    'django.contrib.staticfiles', # Gestión de archivos estáticos
    'django.contrib.humanize', # Añadido para formato de números (ej. 1,000)
    'gestion', # Nuestra aplicación personalizada 'gestion'
    'tailwind', # Integración de Tailwind CSS
    'django_browser_reload', # Para recargar el navegador automáticamente durante el desarrollo
]
# Nombre de la aplicación Tailwind CSS.
TAILWIND_APP_NAME = 'theme'

# Middleware de Django.
# Componentes que procesan las solicitudes y respuestas.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Seguridad básica
    'django.contrib.sessions.middleware.SessionMiddleware', # Habilita el soporte de sesiones
    'django.middleware.common.CommonMiddleware', # Reescritura de URL, etc.
    'django.middleware.csrf.CsrfViewMiddleware', # Protección contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Soporte de autenticación
    'django.contrib.messages.middleware.MessageMiddleware', # Soporte de mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Protección contra clickjacking
    'django_browser_reload.middleware.BrowserReloadMiddleware', # Middleware para recarga automática del navegador
]

# URLconf raíz del proyecto.
ROOT_URLCONF = 'proyectotaller.urls'

# Configuración de plantillas de Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Directorios adicionales para buscar plantillas
        'APP_DIRS': True, # Permite que las aplicaciones busquen sus propias plantillas
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', # Añadido para depuración
                'django.template.context_processors.request', # Acceso al objeto request en las plantillas
                'django.contrib.auth.context_processors.auth', # Acceso a la información de autenticación
                'django.contrib.messages.context_processors.messages', # Acceso a los mensajes
            ],
        },
    },
]

# Aplicación WSGI para servir el proyecto.
WSGI_APPLICATION = 'proyectotaller.wsgi.application'


# Base de datos
# Consulte https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Motor de base de datos SQLite
        'NAME': BASE_DIR / 'db.sqlite3', # Ruta al archivo de la base de datos
    }
}


# Validación de contraseñas
# Consulte https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# Consulte https://docs.djangoproject.com/en/5.2/topics/i18n/

# Código de idioma para este proyecto.
LANGUAGE_CODE = 'es-cl' # Español de Chile

# Zona horaria predeterminada.
TIME_ZONE = 'America/Santiago' # Zona horaria de Santiago, Chile

# Habilita el soporte para internacionalización.
USE_I18N = True

# Habilita el soporte para zonas horarias.
USE_TZ = True


# Archivos estáticos (CSS, JavaScript, Imágenes)
# Consulte https://docs.djangoproject.com/en/5.2/howto/static-files/

# URL para referenciar archivos estáticos.
STATIC_URL = 'static/'

# Tipo de campo de clave primaria predeterminado
# Consulte https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# Tipo de campo automático predeterminado para las claves primarias de los modelos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
