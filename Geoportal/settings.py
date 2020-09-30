"""
Django settings for userstuff project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _
from django.utils.log import DEFAULT_LOGGING
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = "/data/"
SESSION_NAME = 'PHPSESSID'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#m+rso_^a!ii6fg97kd7woxa$ttr&jn^!=_(!wgrukal81q(9+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEFAULT_LOGGING['handlers']['console']['filters'] = []

HOSTNAME = "localhost"
HTTP_OR_SSL = "http://"
SEARCH_API_PROTOCOL = "http"
# HTTPS will fail on self signed certs, uncomment all occurrences of "verify=False"
# in /opt/GeoPortal.rlp/searchCatalogue/utils/searcher.py if you want to bypass validation

ALLOWED_HOSTS = [HOSTNAME, '127.0.0.1', 'localhost']

# Recaptcha Config
USE_RECAPTCHA = 0
GOOGLE_RECAPTCHA_SECRET_KEY = ''
GOOGLE_RECAPTCHA_PUBLIC_KEY = ''

# Mediawiki
INTERNAL_PAGES_CATEGORY = "Portalseite"

# Mapviewer
IFRAME_HEIGHT = 700
IFRAME_WIDTH = 2000

# Set a bool flag if internal API calls shall be verifies via ssl or not
INTERNAL_SSL = False

# Search module settings
PRIMARY_CATALOGUE = 3
PRIMARY_SRC_IMG = "primary_results.png"
DE_CATALOGUE = 4
DE_SRC_IMG = "de_results.png"
EU_CATALOGUE = 7
EU_SRC_IMG = "eu_results.png"
OPEN_DATA_URL = "https://okfn.org/opendata/"

# Mailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = 'server.domain.tld'
EMAIL_HOST_USER = 'geoportal@server.domain.tld'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_PORT = 25
ROOT_EMAIL_ADDRESS = "geoportal-root@server.domain.tld"

# Gui settings
MODERN_GUI = "Geoportal-RLP_2019"
DEFAULT_GUI = "Geoportal-RLP"

# WMC ID that should be loaded on mobile devices
MOBILE_WMC_ID = None
# Directory for inspire Downloads
INSPIRE_ATOM_DIR = "" # eg: "/var/www/html/inspiredownloads/"
INSPIRE_ATOM_ALIAS = "" # eg: "/inspiredownloads/"

# Social networking and news feeds
TWITTER_NAME = "GeoPortalRLP"
RSS_FILE = "http://www.geoportal.rlp.de" + "/mapbender/geoportal/news/georss.xml"

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'useroperations',
    'news',
    'crispy_forms',
    'searchCatalogue',
    'captcha',
    'django_user_agents',
    'resourceManager',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'Geoportal.urls'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Geoportal/static"),  # for generic static files, which are used in all apps
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[
            BASE_DIR + "/templates"
        ],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Geoportal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS' : {
                    'options': '-c search_path=django,mapbender,public'
                    },
        'NAME':'mapbender',
        'USER':'mapbenderdbuser',
        'PASSWORD':'mapbenderdbpassword',
        'HOST':'127.0.0.1',
        'PORT':''
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
]
LANGUAGE_CODE = 'de'  # Default language
MULTILINGUAL = True  # whether to use multiple languages or not

LOCALE_PATHS = [
   os.path.join(BASE_DIR, 'searchCatalogue/locale'),
   os.path.join(BASE_DIR, 'useroperations/locale'),
]

TIME_ZONE = 'UTC'

# These internationalization setting has to be always True
USE_I18N = True

USE_L10N = True

USE_TZ = True


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + "/static/"