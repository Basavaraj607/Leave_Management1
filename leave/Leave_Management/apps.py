from django.apps import AppConfig

class LeaveMConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Leave_Management'

    def ready(self):
        import Leave_Management.signals
