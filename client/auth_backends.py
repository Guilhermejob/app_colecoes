from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


Client = get_user_model()

class EmailOrNicknameBackend(ModelBackend):
    """
    permite autenticação por nickname ou email
    """
    
    def authenticate(self, request, username = None, password = None, **kwargs):
        
        try:
            user = Client.objects.get(email=username)
        except Client.DoesNotExist:
            try:
                user = Client.objects.get(nickname=username)
            except Client.DoesNotExist:
                return None
            
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None