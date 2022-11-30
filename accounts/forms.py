from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from account.models import Users

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
                
class LoginForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=['username', 'password']
