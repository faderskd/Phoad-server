import os

import dj_database_url

from .common import Common


class Test(Common):
    DEBUG = True

    DATABASES = {
        'default': dj_database_url.config(
            default='postgres://postgres:@localhost:5432/postgres',
            conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
        )
    }

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = 'test'
