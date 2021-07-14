# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.test import TestCase
from ..models import Note


class NoteTest(TestCase):
    def setUp(self):
        Note.objects.create(message="Hello World!")
        Note.objects.create(message="Bye World!")

    def test_note_message(self):
        """Note model with provided message should successfuly create message"""

        first_message = Note.objects.get(id=1)
        second_message = Note.objects.get(id=2)
        self.assertEqual(first_message.message, "Hello World!")
        self.assertEqual(second_message.message, "Bye World!")

    def test_note_message_not_longer_than_160(self):
        """Note model with provided message that exceed 160 characters should throw error and not add to db"""

        too_long_msg = 'x'*161
        note = Note(message=too_long_msg)
        with self.assertRaises(ValidationError):
            note.full_clean()

    def test_note_message_not_blank(self):
        """Note model with provided message of 0 characters should throw error and not add to db"""

        blank_msg = ''
        note = Note(message=blank_msg)
        with self.assertRaises(ValidationError):
            note.full_clean()
