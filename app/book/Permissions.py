import json

from .models import Token

from rest_framework.permissions import BasePermission


class TokenPermission(BasePermission):
    def has_permission(self, request, view):
        body_unicode = '{"' + request.body.decode('utf-8').replace('&', '", "').replace('=', '": "') + '"}'
        if not body_unicode:
            return False

        token = json.loads(body_unicode)['authorization']

        if not token:
            return False

        is_token = Token.objects.filter(token=token)

        if not is_token:
            return False
        return True
