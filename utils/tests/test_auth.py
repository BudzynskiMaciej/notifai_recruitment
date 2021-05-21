# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import exceptions
from rest_framework import status
from rest_framework.test import APITestCase

from notifai_recruitment.settings import MASTER_KEY
from textify.models import Note


class AuthTests(APITestCase):

    def setUp(self):
        Note.objects.create(message="Hello World!")

    def test_unauthorized_access_without_master_key(self):
        """Requests that require authorization should fail if there is no header with Bearer token (Master Key)"""

        url = reverse('note-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        error_msg = "Authentication credentials were not provided."
        self._check_is_thrown_authentication_failed_with_specified_error_message_for_response(response, error_msg)

    def test_unauthorized_access_with_wrong_master_key(self):
        """Requests that require authorization should fail if there header with wrong Bearer token (Master Key)"""

        User.objects.create_superuser("Test")
        url = reverse('note-detail', kwargs={'pk': 1})
        self.client.credentials(HTTP_BEARER="WRONG_MASTER_KEY")
        response = self.client.delete(url)
        error_msg = "Wrong Bearer token!"
        self._check_is_thrown_authentication_failed_with_specified_error_message_for_response(response, error_msg)
        self.client.credentials()

    def test_authorized_access_when_there_is_no_super_user_but_master_key_is_correct(self):
        """Requests that require authorization should fail if there is no super user with good
        Bearer token (Master Key)"""

        url = reverse('note-detail', kwargs={'pk': 1})
        self.client.credentials(HTTP_BEARER=MASTER_KEY)
        response = self.client.delete(url)
        error_msg = "You do not have permission to perform this action."
        self.assertRaises(exceptions.AuthenticationFailed)
        self.assertEqual(response.data['detail'], error_msg)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.credentials()

    def _check_is_thrown_authentication_failed_with_specified_error_message_for_response(self, response, error_message):
        self.assertRaises(exceptions.AuthenticationFailed)
        self.assertEqual(response.data['detail'], error_message)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.headers['WWW-Authenticate'], 'Bearer: <MASTER_KEY>')
