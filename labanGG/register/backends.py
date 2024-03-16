from django.contrib.auth import get_user_model
from register.models import Account

class EmailOrUsernameModelBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = Account.objects.get(username=username)
        except Account.DoesNotExist:
            try:
                user = Account.objects.get(email=username)
            except Account.DoesNotExist:
                return None
        if user:
            return user
        return None