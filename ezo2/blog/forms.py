"""module contenant les formulaires utilisé par django."""
from django import forms

from blog.models import Article


class ContactForm(forms.Form):
    """un formulaire de contact"""
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    envoyeur = forms.EmailField(label="Votre adresse e-mail",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    renvoi = forms.BooleanField(
        help_text="Cochez si vous souhaitez obtenir une copie du mail envoyer.", required=False)

    # méthode de vérifiation des donnée d'un champ
    def clean_message(self):
        """fonction de vérification des valeurs entrée"""
        # on vérifie la validitée du champ
        message = self.cleaned_data['message']
        if "anglais" in message:
            raise forms.ValidationError("NOOOOOPE")

        return message


class ArticleForm(forms.ModelForm):
    """un formulaire d'ajout d'article"""
    class Meta:
        """class définissant le comportement global du formulaire"""
        model = Article
        exclude = ['slug', 'date']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }
