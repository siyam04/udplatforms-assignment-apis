# Default
import os
from pathlib import Path


# (Default) Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# (Default) SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-92nv5ak=z3x3=_yk+j02@6&18rnn4h%#$1*-=tcls(i4v_d1r-'

# (Default) SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# (Default) Hosts config
ALLOWED_HOSTS = []

# (Default) Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # dependencies
    'drf_yasg',
    'corsheaders',
    'rest_framework',

    # custom apps
    'parent_child.apps.ParentChildConfig',
]

# (Default) Middleware config
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # corsheaders config (positional)
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Allowing corsheaders
CORS_ORIGIN_ALLOW_ALL = True

# (Default) Root dir config
ROOT_URLCONF = 'config.urls'

# (Default) Templates config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# (Default) Web-server gateway interface config
WSGI_APPLICATION = 'config.wsgi.application'

# (Default) Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# (Default) Password validation config
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

# (Default) Internationalization config
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

# (Default) Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# (Default) Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF config
REST_FRAMEWORK = {
    # global pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}

