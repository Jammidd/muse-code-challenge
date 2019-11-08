"""
Django settings for Muse Job Search project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ
from datetime import timedelta

ROOT_DIR = environ.Path(__file__) - 2

# Load operating system environment variables and then prepare to use them
env = environ.Env()
# .env file, should load only in development environment
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined
    # as environment variables.
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# region APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',

    'django_extensions',
]

LOCAL_APPS = [

]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# endregion

# region MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
# endregion

# region DEBUG CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')
# endregion

# region DOMAIN CONFIGURATION
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
DOMAIN = env.str('DOMAIN')
# endregion

# region EMAIL CONFIGURATION
# ------------------------------------------------------------------------------

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')


# endregion

# region MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ('Richard Middleton', 'richard.middleton@protonmail.com'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# endregion

# region DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
        'NAME': env.str('DB_NAME'),
        
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': '5432'
        
    }
}
# endregion

# region LOCALE CONFIGURATION
# ------------------------------------------------------------------------------
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# endregion

# region STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = [
    str(ROOT_DIR('static')),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# endregion

# region MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(ROOT_DIR('media'))
MEDIA_URL = '/media/'
# endregion

# region URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
# endregion

# region TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': STATICFILES_DIRS,
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# endregion

# region PASSWORD CONFIGURATION
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
# endregion

# region REST CONFIGURATION
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
}
# endregion




