from django.apps import AppConfig


class WebUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_users'
    
    def ready(self):
        import web_users.signals
