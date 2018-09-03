import os
import pytest 

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.config.settings'


@pytest.fixture(scope='session')
def django_db_modify_db_settings(request):
    from django.conf import settings
    settings.DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    }
    