"""
Django settings for RepoPhone project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


from pathlib import Path
from datetime import timedelta  


'''SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
}'''


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z6dz)lm)hmq(0zwy=wp+0==)fw&$6+7$fiy8fxe(gl*u(pnfyr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

PHONE_LOGIN_ATTEMPTS = 1000
PHONE_LOGIN_OTP_LENGTH = 6
PHONE_LOGIN_MINUTES = 3
PHONE_NUMBER_FIELD = 'phone_number'
SECRET_KEY = '=fdion+*r8yx=25q$zy)wnzx&(l=vl^(gy71^hk@5u(kg80vva'
PHONE_LOGIN_OTP_HASH_ALGORITHM = 'sha256'
ESKIZ_EMAIL = "uone2323@gmail.com"
ESKIZ_PASSWORD = "uGKnO0ptNkleDlJh9CxvjOVr7nTWg7hry9xMgyCq"




# Application definition


INSTALLED_APPS = [
    #app
    'api',
    'work',
    'search',
    'specialty',

    'rest_framework_swagger',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'location_field.apps.DefaultConfig',

    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'RepoPhone.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'RepoPhone.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'job', 
        'USER': 'postgres',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'core.PhoneNumberAbstractUser'




TIME_ZONE = 'Asia/Samarkand'
USE_TZ = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'backend.phone_backend.PhoneBackend',
                           )


LOCATION_FIELD = {
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': '<PLACE YOUR API KEY HERE>',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',
}


AUTH_TOKEN_VALIDITY = timedelta(minutes=1)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.SessionAuthentication',
        #'core.authtoken.ExpiringTokenAuthentication', 

       
    ),
   'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.AllowAny',
   ],


}


   #  'DEFAULT_PAGINATION_CLASS':"api.paginations.CustomPagination",
     #  'PAGE_SIZE' :10"""