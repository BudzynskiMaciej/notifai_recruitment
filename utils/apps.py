# -*- coding: utf-8 -*-
from django.apps import AppConfig


class UtilsConfig(AppConfig):
    """Configuration class for utils application.

    Attributes:
        default_auto_field (str): Default primary key for models in app.
        name (str): Name of application.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utils'
