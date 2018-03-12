import os
from decouple import config


# Base

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost', '{{cookiecutter.domain_name}}']


# Storage

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE'),
        'NAME': config('MYSQL_DATABASE_NAME'),
        'USER': config('MYSQL_USER', ''),
        'PASSWORD': config('MYSQL_PASSWORD', ''),
        'HOST': config('MYSQL_HOST', ''),
        'PORT': config('MYSQL_PORT', default=3306, cast=int),
    }
}


# Apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd apps
    'social.apps.django_app.default',
    'compressor',
    'widget_tweaks',
    'rosetta'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(
                BASE_DIR,
                '{{cookiecutter.project_slug}}',
                'templates'
            )
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': ('%(levelname)s %(asctime)s '
                       '%(module)s %(process)d %(thread)d %(message)s')
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'console': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logconsole': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': config(
                'LOG_FILE_PATH',
                default='{{cookiecutter.project_slug}}.log'
            ),
            'maxBytes': 50 * 1024 * 1024,  # 50 MB
            'backupCount': 2,
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['logconsole'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['logconsole'],
            'level': 'INFO',
        },
        'logconsole': {
            'handlers': ['logconsole'],
            'level': 'INFO',
            'propagate': False,
        },
        'logfile': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}


# Internationalization

LANGUAGE_CODE = '{{cookiecutter.language_code}}'

TIME_ZONE = config('TIME_ZONE')

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en_US', ('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Security and Access

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'MinimumLengthValidator'),
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'NumericPasswordValidator'),
    },
]


# Assets

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_ENABLED = config('COMPRESS_ENABLED', cast=bool, default=False)
COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', cast=bool, default=False)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
