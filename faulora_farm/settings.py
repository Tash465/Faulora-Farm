from pathlib import Path
import os
from django.contrib.messages import constants as messages

# --------------------------------------------------
# BASE SETTINGS
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Use environment variables for security
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-secret')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'faulora-farm.onrender.com',  # ✅ Correct Render domain
    'localhost',
    '127.0.0.1'
]

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products',
    'cart',
    'accounts',
    'orders',

    # Cloudinary apps (for media hosting)
    'cloudinary',
    'cloudinary_storage',
]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files
]

# --------------------------------------------------
# URL & WSGI
# --------------------------------------------------
ROOT_URLCONF = 'faulora_farm.urls'
WSGI_APPLICATION = 'faulora_farm.wsgi.application'

# --------------------------------------------------
# DATABASE (SQLite for Render)
# --------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC & MEDIA FILES
# --------------------------------------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'products' / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_summary',
            ],
        },
    },
]

# --------------------------------------------------
# DEFAULT AUTO FIELD
# --------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/logout redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Messages styling
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# --------------------------------------------------
# 🌤 CLOUDINARY CONFIGURATION
# --------------------------------------------------
# Make sure to replace the placeholders below with your real API credentials
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dhcwh9q6v',
    'API_KEY': '131213486265151',
    'API_SECRET': 'Ok9t2ycWlqcv86uRt4iytOsYbRY',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
