from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'apps.auth_user'


class EmpConfig(AppConfig):
    name = 'apps.emp'


class OrgsConfig(AppConfig):
    name = 'apps.orgs'


class JobConfig(AppConfig):
    name = 'apps.job'


class AttendConfig(AppConfig):
    name = 'apps.attend'
