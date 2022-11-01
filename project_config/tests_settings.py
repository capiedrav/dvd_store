from project_config.settings import *

"""
Disable migration files during testing to avoid error with unmanaged models and speed-up testing.

When testing, the command to use must be:

python manage.py test --settings=myproject_config_folder.tests_settings

More information in:

https://simpleisbetterthancomplex.com/tips/2016/08/19/django-tip-12-disabling-migrations-to-speed-up-unit-tests.html
"""


class DisableMigrations(dict):
    def __contains__(self, item):
        return True

    def __missing__(self, key):
        return None


MIGRATION_MODULES = DisableMigrations()
