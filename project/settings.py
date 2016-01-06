"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import dj_database_url
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

SECRET_KEY = os.environ.get('SECRET_KEY', '1234567890')

DEBUG = os.environ.get('DEBUG', 'true').lower() == 'true'


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'project.game',
    'rest_framework',
    'opbeat.contrib.django',
)

MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///tmp.db')
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'project.game.renderers.CoreAPIJSONRenderer',
        'project.game.renderers.CoreAPIHTMLRenderer'
    ],
    'EXCEPTION_HANDLER': 'project.game.exceptions.custom_exception_handler',
    'UNAUTHENTICATED_USER': None
}

OPBEAT = {
    'ORGANIZATION_ID': 'a90a815ce7ea407f84b2b9a9ed8378c5',
    'APP_ID': '957af31684',
    'SECRET_TOKEN': os.environ.get('OPBEAT_SECRET_TOKEN'),
}
