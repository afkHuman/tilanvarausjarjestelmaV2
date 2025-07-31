from django.apps import AppConfig


class KayttajatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kayttajat'

class TilatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tilat'
