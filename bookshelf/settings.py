"""
Django settings for bookshelf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
""" # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Required by template dirs
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Overriden by local_settings, no problem.
SECRET_KEY = '1235x=egmif(%(s3e@8j6b#j6u$uqnubmlk0^e)wihnc94+&+x7$l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
        '.flare.privatedns.org',
        '.flare.dnsalias.net',
        '127.0.0.1',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'taggit',
    'markdown',
    'mercator',
#    'utils',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'bookshelf.urls'

WSGI_APPLICATION = 'bookshelf.wsgi.application'

TEMPLATE_DIRS = (
        PROJECT_PATH + '/templates/',
)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Budapest'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/bookshelf/static/'

STATICFILES_DIRS = (
       PROJECT_PATH + '/static/',
)
 
#Required by sites framework, required by flatpages
SITE_ID = 1

# Have local settings loaded when not in production
try: 
    from local_settings import *
except ImportError, e:
    print 'Unable to load local_settings.py: ', e
