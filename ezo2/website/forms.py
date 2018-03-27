from django import forms
from .widgets import BootstrapTextArea
from website.models import Article, Categorie
from django.forms import ModelChoiceField


class ContactForm(forms.Form):
    sujet=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    envoyeur=forms.EmailField(label="Votre adresse e-mail", widget=forms.TextInput(attrs={'class':'form-control'}))
    renvoi=forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyer.", required=False)

#méthode de vérifiation des donnée d'un champ
    def clean_message(self):
    #on vérifie la validitée du champ
        message=self.cleaned_data['message']
        if "anglais" in message:
            raise forms.ValidationError("NOOOOOPE")

        return message

#méthode de vérification des donnée de plusieurs champs
##def clean(self):
##    cleaned_data = super(ContactForm, self).clean()
##    sujet = cleaned_data.get('sujet')
##    message = cleaned_data.get('message')
##
##    if sujet and message:  # Est-ce que sujet et message sont valides ?
##        if "pizza" in sujet and "pizza" in message:
##            #lever une erreur
##            ##raise forms.ValidationError('Il y a pizza dans le sujet ET le message')
##            self.add_error("message",
##                "Vous parlez déjà de pizzas dans le sujet, "
##                "n'en parlez plus dans le message !"
##            )
##
##    return cleaned_data



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['slug', 'date']
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'auteur':forms.TextInput(attrs={'class':'form-control'}),
            'contenu':forms.Textarea(attrs={'class':'form-control'}),
            'categorie':forms.Select(attrs={'class':'form-control'}),
            }