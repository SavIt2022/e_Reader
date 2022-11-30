from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
class RegisterUser(UserCreationForm):
    email = forms.EmailField(required=True)
    roll_number = forms.CharField(required=True)
    user_code = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]