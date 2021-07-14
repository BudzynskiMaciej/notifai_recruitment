# -*- coding: utf-8 -*-
from django.apps import AppConfig


class TextifyConfig(AppConfig):
    """Configuration class for textify application.

    Attributes:
        default_auto_field (str): Default primary key for models in app.
        name (str): Name of application.

    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'textify'
