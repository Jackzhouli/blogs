"""
Django settings for income_manage project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c@t*%q3dwr9jf8isg=-^#5x4xft(p#equ=3hmk6c_(6!13v#u*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.xadmin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'income_manage_app',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'income_manage.urls'

WSGI_APPLICATION = 'income_manage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'sqlserver',
        'NAME': 'DJANGO_TEST',
        'HOST': '10.105.228.83',
        'PORT': '1433',
        'USER': 'sa',
        'PASSWORD': 'Q!$Sb8t&p@bX',
        'OPTIONS': {
            'DRIVER': 'SQL Server Native Client 11.0',
        },
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'sqlserver',
#        'NAME': 'DJANGO_TEST_DB',
#        'HOST': '192.168.1.40',
#        'PORT': '1433',
#        'USER': 'wikitec_dcc',
#        'PASSWORD': '3bRiRBYKyccbzOFJC7Xi',
#        'OPTIONS': {
#            'DRIVER': 'SQL Server Native Client 11.0',
#        },
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
