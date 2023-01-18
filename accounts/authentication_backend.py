from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class AuthenticationBackend(ModelBackend):
    
    def authenticate(self, username=None, password=None, **kwargs):
        CustomUserModel = get_user_model()

        try:
            user = CustomUserModel.objects.get(username=username)
        except CustomUserModel.DoesNotExist:
            return None 
        else:
            if user.check_password(password):
                return user 
        
        return None 
