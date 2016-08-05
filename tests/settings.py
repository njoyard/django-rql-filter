# coding: utf-8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}

INSTALLED_APPS = (
    # rest framework
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework',

    # filter and test project
    'rql_filter',
    'tests',
)

SECRET_KEY = 'not_so_secret'
ROOT_URLCONF = 'tests.urls'
