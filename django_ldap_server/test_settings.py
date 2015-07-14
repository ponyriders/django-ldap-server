import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

TEST_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tests')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_ROOT = os.path.join(TEST_DIR, 'static')

STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!hg=@!-n0wua=ygl@3jt81&amp;uzj7qqpx_8dhi5dbf@#8rok4@^a'

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_ldap_server',
)
