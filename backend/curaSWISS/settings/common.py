"""
Django settings for curaSWISS project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'widget_tweaks',
    'crispy_forms',
    'django_tables2',
    'apps.mapview',
    'apps.iamstudent',
    'apps.ineedstudent',
    'apps.accounts',
    'apps.ioffer',
    'apps.ineed',
    'apps.role'
    'apps.map'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    
]

ROOT_URLCONF = 'curaSWISS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGIN_REDIRECT_URL = '/accounts/login_redirect'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

NOREPLY_MAIL = 'curaSWISS<noreply@curaSWISS.de>'

WSGI_APPLICATION = 'curaSWISS.wsgi.application'

MAX_EMAIL_BATCH_PER_HOSPITAL = 200

# EMAIL_HOST = 'spahr.uberspace.de'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'noreply@medisvs.spahr.uberspace.de'
# EMAIL_HOST_PASSWORD = 'jonathan'
# EMAIL_USE_TLS = False

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# Normal SMTP
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Using the API
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend" #
"""
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
"""
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

AUTH_USER_MODEL = 'accounts.User'

USE_L10N = True

USE_TZ = True

# Translations
# Provide a lists of languages which your site supports.
LANGUAGES = (
    ('en', _('English')),
    ('de', _('Deutsch')),
)
# Set the default language for your site.
LANGUAGE_CODE = 'de'
# Tell Django where the project's translation files should be.
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname( __file__ )))
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
