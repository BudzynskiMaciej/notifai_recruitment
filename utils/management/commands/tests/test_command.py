from io import StringIO

from django.contrib.auth.models import User
from django.test import TestCase
from django.core.management import call_command


class InitAdminAccTest(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "initadminacc",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_first_run_when_there_are_no_super_users(self):
        out = self.call_command()
        self.assertEqual(out.strip(), "SuperUser successfully created")
        self.assertEqual(User.objects.count(), 1)

    def test_not_first_run_when_there_are_super_user(self):
        User.objects.create_superuser("Test")
        out = self.call_command()
        self.assertEqual(out.strip(), "Administrator accounts can only be initialized when no user exists!")
        self.assertEqual(User.objects.count(), 1)

