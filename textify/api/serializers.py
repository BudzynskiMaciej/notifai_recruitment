# -*- coding: utf-8 -*-
from rest_framework import serializers

from textify.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for Note model

    This class determines serialization of note object. The serialized fields are ``id``, ``message`` and ``view_count,
    but only message is writeable, the other ones are read only fields.

    """
    class Meta:
        model = Note
        fields = ('id', 'message', 'view_count')
        read_only_fields = ('id', 'view_count')
