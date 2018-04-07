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
            'username': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Nom d\'utilisateur',
            }),
            'email': forms.EmailField(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse Mail',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mot de passe',
            }),
        }
