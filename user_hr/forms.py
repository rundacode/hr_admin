from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        
        fields = UserCreationForm.Meta.fields + ("email",)
