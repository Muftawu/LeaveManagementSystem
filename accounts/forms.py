from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from leave.models import Staff, Leave

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", )


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ("phone", "photo", )

class NewLeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ("reason", "description", )