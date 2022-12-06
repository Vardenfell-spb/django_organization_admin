from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Profile


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'groups')


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('organization',)
