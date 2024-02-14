"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #3th app
    "taggit",
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'drf_yasg',
    'dj_rest_auth',
    "debug_toolbar",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'rosetta',
    "django_bootstrap5",
    
    
    #my apps
    'products',
    'settings',
    'orders',
      
]

SITE_ID = 1


#restapi settings
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        
    ]
    }
        

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    
]

ROOT_URLCONF = 'project.urls'
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.company_context_processor.get_company_data',
                'orders.cart_context_processor.get_cart_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'),conn_max_age=600)
    }


# DATABASES = {
#     "default": {
#     "ENGINE": "django.db.backends.postgresql",
#     "NAME": "postgres",
#     "USER": "postgres",
#     "PASSWORD": "postgres",
#     "HOST": "db",
#     "PORT": "5432",
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
MODELTRANSLATION_LANGUAGES = ('en', 'ar','de')
MODELTRANSLATION_AUTO_REGISTER = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    
]
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/"media"




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CACHES = {
    "default": {
       "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# CACHES = {
#    "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://myredis:6379/0",
#     }
# }

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOCALE_PATHS = ['locale']
gettext = lambda s: s
LANGUAGES = [
    ("ar", "Arabic"),
    ("en", "English"),
    ("de", "German"),
]
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' #service that we buy
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "sweetsyrialeena@gmail.com"
EMAIL_HOST_PASSWORD = "vlllvhvfbmyciezk"

# celery 
CELERY_BROKER_URL ='redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# CELERY_BROKER_URL ='redis://myredis:6379/0'
# CELERY_RESULT_BACKEND = 'redis://myredis:6379/0'

# Stripe 
STRIPE_API_KEY_PUBLISHABLE = 'pk_test_51OZIe5HiBYGBB8vCGhVPGOUDof6ECrdfdM1s6tDQaBHzd7M1GjFrjgPLXKlTABD6h3V3ha3TZVORXXN1qPsGTqP300WWU4be45'
STRIPE_API_KEY_SECRET = 'sk_test_51OZIe5HiBYGBB8vCW9UlQ5AOWKvaj2h17cfgnxKK1eDsVQg0XpzmRpdJXGoptNjiZ4TITrhBcXxxDutDzjKgKniK00OtRjNkIu'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"