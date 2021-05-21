# -*- coding: utf-8 -*-
"""API routes config for notifai_recruitment project.

REST framework adds support for automatic URL routing to Django, and provides simple, quick and consistent
way of wiring view logic to a set of URLs.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/routers/

"""
from rest_framework import routers

from textify.api.views import NoteViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
