# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from notifai_recruitment import settings


class MasterKeyNaiveAuthentication(authentication.BaseAuthentication):
    """Authentication model for master key.

    Note:
        It was done the way I understood the assignment.In the task it was written that the authorization will be
        performed by the key in the email exchange. This solution allows you to set the master key as requested in the
        email. You could also set the authorization using the ready-made implementation included in the Django Rest
        Framework, which is TokenAuthentication. This authorization would allow tokens to be assigned to specific users.
        DRF requires any user to be returned upon authorization. For this authorization it will always be the first
        SuperUser, therefore at least one super user account is required. It may not be the best authorization for use
        in production, but it meets the assumption of a token sent by e-mail. In my opinion, a good authentication
        mechanism would be JWT(Json Web Token).

    """
    def authenticate(self, request):
        request_master_key = request.META.get('HTTP_BEARER')
        if not request_master_key:
            return None

        super_user = User.objects.filter(is_superuser=True).first()
        if request_master_key != settings.MASTER_KEY:
            raise exceptions.AuthenticationFailed('Wrong Bearer token!')
        return super_user, None

    def authenticate_header(self, request):
        return 'Bearer: <MASTER_KEY>'
