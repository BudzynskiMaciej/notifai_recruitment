# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notifai_recruitment.settings import MASTER_KEY
from ..serializers import NoteSerializer
from ...models import Note


class NoteViewSetTests(APITestCase):

    def setUp(self):
        User.objects.create_superuser("Test")
        Note.objects.create(message="Hello World!")
        Note.objects.create(message="Bye World!")
        Note.objects.create(message="Awesome World!")

    def test_get_all_notes_unauthorized(self):
        """HTTP GET to /api/v1/notes/ without authorization should return list of all notes with status 200"""

        url = reverse('note-list')
        all_notes = Note.objects.all()
        serializer = NoteSerializer(all_notes, many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_notes_authorized(self):
        """HTTP GET to /api/v1/notes/ with authorization should return list of all notes with status 200"""

        url = reverse('note-list')
        all_notes = Note.objects.all()
        serializer = NoteSerializer(all_notes, many=True)
        self.client.credentials(HTTP_BEARER=MASTER_KEY)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.client.credentials()

    def test_post_note_create_should_fail_unauthorized(self):
        """HTTP POST to /api/v1/notes/ without authorization should fail and return status 401"""

        url = reverse('note-list')
        data = {'message': 'Hello Tests'}
        expected_token = 'Bearer: <MASTER_KEY>'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.headers['WWW-Authenticate'], expected_token)

    def test_post_note_create_should_success_authorized(self):
        """HTTP POST to /api/v1/notes/ with authorization should create note and return status 201"""

        url = reverse('note-list')
        data = {'message': 'Hello Tests'}
        self.client.credentials(HTTP_BEARER=MASTER_KEY)
        response = self.client.post(url, data)
        created_note = Note.objects.get(id=4)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(created_note.message, 'Hello Tests')
        self.client.credentials()

    def test_get_note_should_increase_view_count_unauthorized(self):
        """HTTP GET to /api/v1/notes/{id} without authorization should return note of specified id with status 200"""

        url = reverse('note-detail', kwargs={'pk': 1})
        viewcount_before_get_call = Note.objects.get(id=1).view_count
        response = self.client.get(url)
        viewcount_after_get_call = Note.objects.get(id=1).view_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(viewcount_before_get_call, 0)
        self.assertEqual(viewcount_after_get_call, 1)

    def test_get_note_should_increase_view_count_authorized(self):
        """HTTP GET to /api/v1/notes/{id} with authorization should return note of specified id with status 200 and
        increase view_counter"""

        url = reverse('note-detail', kwargs={'pk': 1})
        viewcount_before_get_call = Note.objects.get(id=1).view_count
        self.client.credentials(HTTP_BEARER=MASTER_KEY)
        response = self.client.get(url)
        viewcount_after_get_call = Note.objects.get(id=1).view_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(viewcount_before_get_call, 0)
        self.assertEqual(viewcount_after_get_call, 1)
        self.client.credentials()

    def test_put_note_should_fail_unauthorized(self):
        """HTTP PUT to /api/v1/notes/{id} without authorization should fail and return status 401"""

        url = reverse('note-detail', kwargs={'pk': 1})
        data = {'message': 'Hello Tests'}
        expected_token = 'Bearer: <MASTER_KEY>'
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.headers['WWW-Authenticate'], expected_token)

    def test_put_note_should_success_and_reset_view_count_authorized(self):
        """HTTP GET to /api/v1/notes/{id} with authorization should update note of specified id with status 200 and
        reset view_counter"""

        url = reverse('note-detail', kwargs={'pk': 1})
        data = {'message': 'Hello Tests'}
        # Get 5 times to increse the view_counter
        for _ in range(5):
            self.client.get(url)
        note_object_before_put_request = Note.objects.get(id=1)
        self.client.credentials(HTTP_BEARER=MASTER_KEY)
        response = self.client.put(url, data)
        note_object_after_put_request = Note.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(note_object_before_put_request.message, "Hello World!")
        self.assertEqual(note_object_after_put_request.message, "Hello Tests")
        self.assertEqual(note_object_before_put_request.view_count, 5)
        self.assertEqual(note_object_after_put_request.view_count, 0)
        self.client.credentials()

    def test_delete_note_should_fail_unauthorized(self):
        """HTTP DELETE to /api/v1/notes/{id} without authorization should fail and return status 401"""

        url = reverse('note-detail', kwargs={'pk': 1})
        expected_token = 'Bearer: <MASTER_KEY>'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.headers['WWW-Authenticate'], expected_token)

    def test_delete_should_success_authorized(self):
        """HTTP DELETE to /api/v1/notes/{id} with authorization should delete note and return status 204"""

        url = reverse('note-detail', kwargs={'pk': 1})
        self.client.credentials(HTTP_BEARER=MASTER_KEY)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.credentials()
