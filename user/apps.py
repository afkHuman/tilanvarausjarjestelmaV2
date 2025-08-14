from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

class SpaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'space'
