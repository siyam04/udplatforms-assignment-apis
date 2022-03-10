# Default app config
from django.apps import AppConfig


class ParentChildConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parent_child'

