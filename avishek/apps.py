from django.apps import AppConfig


class AvishekConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avishek'

    def ready(self):        
        import avishek.signals
