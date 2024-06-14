from django.apps import AppConfig


class UserboxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userbox'

    def ready(self):
        import userbox.signals