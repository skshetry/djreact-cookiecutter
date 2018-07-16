from .base import *

# Operating System Environment variables have precedence over variables defined in the .env file,
# that is to say variables from the .env files will only be used if not defined
# as environment variables.
env_file = str(ROOT_DIR / '.env')
print('Loading : {}'.format(env_file))
env.read_env(env_file)
print('The .env file has been loaded. See local.py for more information')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='e%s=1kdk1_+yur9cmpkw8r-z5gd(owqpxbyl+6^)*10-a3c4v')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')


DATABASES = {
    'default': {  # moving to postgres
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DBNAME', default='{{cookiecutter.project_name}}'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    },
}

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
# middleware and installed apps
# ------------------------------------------------------------------------------
THIRD_PARTY_APPS += [
    'debug_toolbar',
]

THIRD_PARTY_MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + LOCAL_MIDDLEWARE


ALLOWED_HOSTS = ['127.0.0.1', '10.0.2.2', 'localhost', '192.168.100.3', '0.0.0.0']
INTERNAL_IPS = ALLOWED_HOSTS

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


if env('DJANGO_BUILD_WEBPACK', default=False):
    STATICFILES_DIRS += [
        os.path.join(ROOT_DIR, "assets"),
    ]

    WEBPACK_LOADER = {
        'DEFAULT': {
                'BUNDLE_DIR_NAME': 'bundles/',
                'STATS_FILE': os.path.join(ROOT_DIR, 'webpack-stats.prod.json'),
            }
    }
