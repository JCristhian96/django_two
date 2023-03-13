from .base import BASE_DIR, get_secret_env


SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('config', 'db', get_secret_env('DB_LOCAL')),
    }
}


POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret_env('POSTGRES_DB'),
        'USER': get_secret_env('POSTGRES_USER'),
        'PASSWORD': get_secret_env('POSTGRES_PASS'),
        'HOST': "localhost",
        'PORT': 5432
    }
}
