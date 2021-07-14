# -*- coding: utf-8 -*-
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from textify import models
from textify.api import serializers


class NoteViewSet(ModelViewSet):
    """Note model for storing notes

    Attributes:
        queryset (QuerrySet): QuerySet that ModelViewSet require for operate on. Retrieved from db.
        serializer_class (NoteSerializer): Serializer for model.
        permission_classes (:obj:`list` of :obj:`BasePermission`): List of permissions for authenticated requests.

    """
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        """Override for ListModelMixin.

        Note:
            It overrides default behavior of ListModelMixin.list() function. After GET request this function
            increase view_count of all messages. Then it calls default behavior of ListModelMixin.list()

        Args:
            request: HTTP GET request for /api/v1/notes/.
            *args: args
            **kwargs: key-word args

        Returns:
            ListModelMixin.list()

        """
        all_notes_instances = self.get_queryset()
        for note in all_notes_instances:
            note.view_count = note.view_count + 1
        self.get_queryset().bulk_update(all_notes_instances, ['view_count'])
        return ListModelMixin.list(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Override for RetrieveModelMixin.

        Note:
            It overrides default behavior of RetrieveModelMixin.retrieve() function. After GET request this function
            increase view_count of message with specified id. Then it calls default behavior of
            RetrieveModelMixin.retrieve()

        Args:
            request: HTTP GET request for /api/v1/notes/{number}/.
            *args: args
            **kwargs: key-word args

        Returns:
            RetrieveModelMixin.retrieve()

        """
        instance = self.get_object()
        instance.view_count = instance.view_count + 1
        instance.save()
        return RetrieveModelMixin.retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Override for UpdateModelMixin.

        Note:
            It overrides default behavior of UpdateModelMixin.update() function. After PUT request this function
            reset view_count of message with specified id. Then it calls default behavior of UpdateModelMixin.update()

        Args:
            request: HTTP PUT request for /api/v1/notes/{number}/.
            *args: args
            **kwargs: key-word args

        Returns:
            UpdateModelMixin.update()

        """
        instance = self.get_object()
        if request.data['message'].strip() != instance.message:
            instance.view_count = 0
            instance.save()
        return UpdateModelMixin.update(self, request, *args, **kwargs)
