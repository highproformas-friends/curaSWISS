from curaSWISS.settings.common import *
from django.utils.log import DEFAULT_LOGGING

import logging

logger = logging.getLogger('django')

DEFAULT_LOGGING['handlers']['console']['filters'] = []

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['matchmedisvsvirus.dynalias.org', 'helping-health.from-de.com', 'curaSWISS.de',
                 'curaSWISS.eu', 'curaSWISS.org', 'medis-vs-covid19.de']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', ''),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': 'database',
        'PORT': '5432',
    }
}

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'applogfile': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'run', 'curaSWISS.log'),
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['applogfile'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# =============== MAIL RELAY SERVER CONFIGURATION ===============
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# Normal SMTP
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Using the API
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"