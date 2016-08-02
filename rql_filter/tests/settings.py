import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'notsecret'

DEBUG = True
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = False
USE_L10N = False
USE_TZ = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s[%(module)s]: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'representatives': {
            'handlers': ['console'],
            'level': 'INFO'
        },
    },
}
