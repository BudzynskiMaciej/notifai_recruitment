from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from notifai_recruitment.settings import ADMIN_DETAILS


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            email = ADMIN_DETAILS[0]
            username = ADMIN_DETAILS[1]
            password = ADMIN_DETAILS[2]
            print(f"Creating admin account for {username} with email {email}")
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            self.stdout.write("SuperUser successfully created")
        else:
            self.stdout.write("Administrator accounts can only be initialized when no user exists!")
