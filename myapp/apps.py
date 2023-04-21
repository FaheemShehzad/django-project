from django.apps import AppConfig
from time import sleep
from .main import load_path


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        # print("Ready")
        load_path()
