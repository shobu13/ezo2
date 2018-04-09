"""Module servant à la génération des formulaire de l'application Core."""
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(forms.ModelForm):
    """Formulaire de création d'un utilisateur."""
    class Meta:
        """classe définissant le comportement du formulaire."""
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom d\'utilisateur',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse mail',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mot de passe',
            }),
        }


class ConnexionForm(forms.Form):
    """Formulaire de connexion"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Pseudo',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mot de passe',
    }))