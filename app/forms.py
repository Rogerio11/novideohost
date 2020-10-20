from django import forms
from .models import *
from django.forms import ModelForm


class TutoForm(ModelForm):

    clientName = forms.CharField(max_length = 50,
        label="Nom client",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))

    idTutoVideo = forms.CharField(max_length = 50,
        label="id Video Tuto",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))

    client_url = forms.CharField(max_length = 50,
        label="Client Url",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    
    clientName = forms.CharField(max_length = 50,
        label="Nom client",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    
    class Meta:
        model = Tuto
        fields = ['cle_tuto','idTutoVideo','client_url','clientName']