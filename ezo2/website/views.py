from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from datetime import datetime
from website.models import Article
from .forms import ContactForm, ArticleForm
from shobu import slugGenerator
from website.globalVar import *

# Create your views here.

def home(request):
    articleList=Article.objects.order_by('date').reverse()[:4]
    return render(request, 'website/index.html', {'articleList':articleList, 'global':globals()})


def contact(request):
    #on construit le formulaire, soit avec les données postée, sois vide si l'utilisateur y accède pour la première fois
    form = ContactForm(request.POST or None)
    #On vérifie que les données du formulaire sont bien valide
    if(form.is_valid()):
        #on lit la valeur des différent champs
        sujet=form.cleaned_data['sujet']
        message=form.cleaned_data['message']
        envoyeur=form.cleaned_data['envoyeur']
        renvoi=form.cleaned_data['renvoi']

        #on valide l'envoie de l'e-mail
        envoi=True

    #quoi qu'il arrive, on retourne la page du formulaire
    return render(request, 'website/contact.html', locals())

def article(request):
    form=ArticleForm(request.POST or None)

    if(form.is_valid()):
        titre=form.cleaned_data['titre']
        auteur=form.cleaned_data['auteur']
        contenu=form.cleaned_data['contenu']
        categorie=form.cleaned_data['categorie']
        #le commit=False permet d'enregister les donnée du formulaire dans un objet avec lequel on peut travailer avant de l'envoyer.
        article=form.save(commit=False)
        article.slug=slugGenerator(form.cleaned_data['titre'])
        article.save()
        return HttpResponse('envoyer')
    return render(request, 'website/articleForm.html', locals())

def e404(request):
    return render(request, '404.html')