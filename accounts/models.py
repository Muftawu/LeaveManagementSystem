from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        username = CustomUser.normalize_username(username)
        user = CustomUser(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user 
    
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("user_type", 2)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", 1)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(username, password, **extra_fields)
        

class CustomUser(AbstractUser):
    USER_TYPE = ((1, 'SUPERVISOR'), (2, 'STAFF'))
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPE, default=2)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username 