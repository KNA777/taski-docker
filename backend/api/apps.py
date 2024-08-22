"""Apps."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Public class."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
