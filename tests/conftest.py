import os
import pytest 
import django
# import os
# import sys

# print("HERE")
# sys.path.append(os.path.dirname(__file__))

# from django.conf import settings
import sys 
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.config.settings'

def pytest_addoption(parser):
    parser.addoption(
        "--sqlite", action="store_true", help="Run tests using an in-memory sqlite3 (faster)"
    )

# if '--sqlite3' in sys.argv:
#     settings.DATABASES = {
#         'default': {
#             'ENGINE':'django.db.backends.sqlite3',
#             'NAME': ':memory:'
#         }
#     }

def pytest_configure(config):
    use_sqlite = config.getoption('--sqlite')
    if use_sqlite:
        settings.DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    }
    # print(config)
    # import pdb; pdb.set_trace()

# def pytest_configure(config):
#     print(config)
#     from django.conf import settings
#     db_settings = {
#         'default': {
#             'ENGINE':'django.db.backends.sqlite3',
#             'NAME': ':memory:'
#         }
#     }
#     settings.DATABASES = db_settings
    # django.setup()
#     from app.config import settings as project_setting
#     from django.conf import settings
#     print(project_setting)
#     settings.configure(project_setting)
    # print("pytest_configure called\n")
#     settings.DATABASES['default'] = {
#             'ENGINE':'django.db.backends.sqlite3',
#             'NAME': ':memory:',
#         }
#     print(os.environ.get('DJANGO_SETTINGS_MODULE'))
    # settings.configure()

    # settings.DEBUG = False
@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(early_config, parser, args):
    print("pytest_load_initial_conftests called q\n")
    import pdb; pdb.set_trace()

def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print("setting up", item)
    
# def pytest_addoption(parser):
#     parser.addoption(
#         "--sqlite3", action="store_true", help="Run tests using an in-memory sqlite3 (faster)"
#     )
from unittest import mock 

@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(request):
    print ("callattr_ahead_of_alltests called\n")

# @pytest.fixture(scope='session')
# def django_db_modify_db_settings(request):
#     print("django_db_modify_db_settings called\n")
#     from django.conf import settings
#     db_settings = {
#         'default': {
#             'ENGINE':'django.db.backends.sqlite3',
#             'NAME': ':memory:'
#         }
#     }
    # import django 
    # django.setup()
    # from django.test.utils import connections 
    # del connections.__dict__['databases']
    # override = mock.patch('django.tests.utils.connections.databases', db_settings)
    # override.start()
    # settings.DATABASES = db_settings
    # from django.db import connections
    # del connections.__dict__['_databases']
    # connections.ensure_defaults('default')
    # connections.prepare_test_settings('default')
    # yield 
    # override.stop()
    
    # del connections['databases']
    # if request.config.getoption("--sqlite3"):
    #     from django.conf import settings
    # settings.DATABASES = {'default': {'TEST': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': ':memory:',
    # }}}
    # print(settings.DATABASES)

# @pytest.fixture(autouse=True)
# def override_settings(settings):
#     # if request.config.getoption("--sqlite3"):
#     #     from django.conf import settings
#     settings.DATABASES['default'] = {
#         'ENGINE':'django.db.backends.sqlite3',
#         'NAME': ':memory:',
#     }