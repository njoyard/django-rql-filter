DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}

INSTALLED_APPS = (
    'rql_filter',
    'tests',
)

SECRET_KEY = 'not_so_secret'
