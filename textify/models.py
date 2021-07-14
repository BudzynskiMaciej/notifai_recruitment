# -*- coding: utf-8 -*-
from django.db import models


class Note(models.Model):
    """Note model for storing notes

    Attributes:
        message (django.db.models.CharField): Note message, can't be blank and no longer than 160 characters. Required.
        view_count (django.db.models.BigIntegerField): View count of message, increse after GET request for all messages
            or single message.
        created_at (django.db.models.DateTimeField): Time and date of create message
        updated_at (django.db.models.DateTimeField): Time and date of update message. Updated when view_count changes.

    """

    message = models.CharField(max_length=160)
    view_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
