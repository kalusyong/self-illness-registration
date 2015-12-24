"""
Django settings for zzghsir project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
from os import environ
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HERE = os.path.dirname(os.path.abspath(__file__))  
HERE = os.path.join(HERE, '../') 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(v8*=@kqq%!e%a(xpy5@gndei(9as$jz5u&g6y%(elus6y^#g9'

debug = not environ.get("zzghsir","")

if debug:
    MYSQL_DB = 'zzghsir'
    MYSQL_USER = 'kalus'
    MYSQL_PASS = 'ky'
    MYSQL_HOST_M = '127.0.0.1'
    MYSQL_HOST_S = '127.0.0.1'
    MYSQL_PORT = 's3306'
else:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB 
    MYSQL_USER = sae.const.MYSQL_USER 
    MYSQL_PASS = sae.const.MYSQL_PASS 
    MYSQL_HOST_M = sae.const.MYSQL_HOST 
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S 
    MYSQL_PORT = sae.const.MYSQL_PORT
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'register',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'zzghsir.urls'

WSGI_APPLICATION = 'zzghsir.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': MYSQL_DB,
    'USER': MYSQL_USER,
    'PASSWORD': MYSQL_PASS,
    'HOST': MYSQL_HOST_M,
    'PORT': MYSQL_PORT,
    }
}

DEFAULT_CHARSET='utf-8' 

ALLOWED_HOSTS = [
                 '.sinaapp.com',
                 ]
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_PATH = os.path.join(os.path.dirname(__file__), '../image').replace('\\','/')
STATIC_URL = '/static/'
TEMPLATE_DIRS = (

    os.path.join(BASE_DIR, '../templates').replace('\\', '/'),
    BASE_DIR + '/templates/',
    )
STATICFILES_DIRS = (
    './image/'
)