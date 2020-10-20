from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Identifiant"
            }
        ))
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Mot de passe"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        label="Email ",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label="Confirmer votre mot de passe",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')