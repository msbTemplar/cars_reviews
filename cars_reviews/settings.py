"""
Django settings for cars_reviews project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#DATABASE_URL = 'postgresql://postgres:dEABbCgyqqXRNQvxJZwlKeFtzcCjYFSg@postgres.railway.internal:5432/railway'
DATABASE_URL = 'postgresql://postgres:dEABbCgyqqXRNQvxJZwlKeFtzcCjYFSg@autorack.proxy.rlwy.net:43106/railway'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_w_%6yuef82^8p*gy8le9xj8+(bq%jnr)$6+eco#-p)8jl^6+$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#para desplegar en railway hay que descomentar esto de abajo y para local hay que comentarlo

#CSRF_TRUSTED_ORIGINS = ['https://web-production-0c64.up.railway.app']
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = True
#USE_X_FORWARDED_HOST = True
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


#ALLOWED_HOSTS = ['web-production-0c64.up.railway.app', 'localhost', '127.0.0.1']

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'cars_reviews_app',
    #'django_cron',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'cars_reviews.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'cars_reviews_app/templates/cars_reviews_app/'],
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

WSGI_APPLICATION = 'cars_reviews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'dEABbCgyqqXRNQvxJZwlKeFtzcCjYFSg',
        'HOST': 'postgres.railway.internal',
        'PORT': '5432',
    }
}
"""

""" DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
} """

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL='/media/'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')

STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="msb.duck@gmail.com"
#EMAIL_HOST_PASSWORD="Moha.93345900"
EMAIL_HOST_PASSWORD="sfki wpcn sxib uojk"
#EMAIL_AUTH_PASSWORD="anbc ictn simy cfrq"
#anbc ictn simy cfrq 
#sfki wpcn sxib uojk     24052024


#LOGIN_REDIRECT_URL = 'dentist_form'
LOGIN_REDIRECT_URL = 'cars_reviews_admin'

LOGOUT_REDIRECT_URL = '/'  # Asegúrate de que 'home' esté en tus urls

CRONJOBS = [
    #('0 3 * * *', 'cars_reviews_app.crons.ScrapeNoticiasCronJob'),
    ('*/60 * * * *', 'cars_reviews_app.cron.ObtenerNoticiasCronJob'),
]