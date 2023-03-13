from .base import *
from . import db


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["www.django-two.com", "192.168.10.16", "django-two.com"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = db.POSTGRESQL


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.child('static'),
]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


# Rest Frameowrk Settings
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
