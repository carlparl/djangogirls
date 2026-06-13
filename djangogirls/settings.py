from token import NAME


TIME_ZONE = 'Africa/kampala'
LANGUAGE_CODE = 'en-us'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}