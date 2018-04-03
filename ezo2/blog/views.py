from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from ezo2.shobu import slugGenerator
from .forms import ContactForm, ArticleForm
from .models import Article, Categorie
from ezo2.globalVar import *


# Create your views here.

def home(request):
    articleList = Article.objects.order_by('date').reverse()[:4]
    return render(request, 'blog/index.html', {'articleList': articleList, 'global': globals()})


def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    print(article)
    return render(request, 'blog/post.html', {'article': article, 'global': globals()})


def article_liste(request, page=0, keywords="null", selected_cat="null"):
    categorieListe = []
    articleListe = []
    raw = []
    old = ''
    new = ''
    rawCategorie = Categorie.objects.all()
    if (request.POST):
        print("POST=")
        print(request.POST['search'])
        keywords = request.POST['search']

    if (keywords == 'null' and selected_cat == 'null'):
        rawArticleList = Article.objects.order_by('date').reverse()
    else:
        if (keywords != 'null' and selected_cat == 'null'):
            rawArticleList = Article.objects.filter(
                Q(titre__contains=keywords) | Q(contenu__contains=keywords)).order_by('date').reverse()
        elif (keywords == 'null' and selected_cat != 'null'):
            rawArticleList = Article.objects.filter(categorie__nom__contains=selected_cat).order_by('date').reverse()
        else:
            rawArticleList = Article.objects.filter((Q(titre__contains=keywords) | Q(contenu__contains=keywords)) & Q(
                categorie__nom__contains=selected_cat)).order_by('date').reverse()

    print("raw article liste =")
    print(rawArticleList)

    if (len(rawArticleList)):
        for i in range(0, len(rawArticleList), 4):
            articleListe += [rawArticleList[i:i + 4]]

        for i in range(0, len(rawCategorie), 3):
            raw += [rawCategorie[i:i + 3]]
        for i in range(0, len(raw), 2):
            categorieListe += [raw[i:i + 2]]

        if (page == 0):
            new = 'disabled'
        if (page == len(articleListe) - 1):
            old = 'disabled'

        print("articleListe=")
        print(articleListe)

        print("sending page")
        return render(request, 'blog/articleListe.html',
                      {'categorieListe': categorieListe, 'global': globals(), 'articleListe': articleListe[page],
                       'page': page, 'oldDisable': old, 'newDisable': new, 'keywords': keywords,
                       'selectedCat': selected_cat, })

    else:
        print("no result")
        return render(request, 'blog/articleListe.html',
                      {'categorieListe': categorieListe, 'global': globals(), 'articleListe': '', 'page': -1,
                       'oldDisable': 'disabled', 'newDisable': 'disabled', 'keywords': keywords,
                       'selectedCat': selected_cat, })


def a_propos(request):
    return render(request, 'blog/about.html', {'global': globals()})


def contact(request):
    # on construit le formulaire, soit avec les données postée
    # sois vide si l'utilisateur y accède pour la première fois
    form = ContactForm(request.POST or None)
    # On vérifie que les données du formulaire sont bien valide
    if (form.is_valid()):
        # on lit la valeur des différent champs
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # on valide l'envoie de l'e-mail
        envoi = True

    # quoi qu'il arrive, on retourne la page du formulaire
    return render(request, 'blog/contact.html', locals())


def article(request):
    form = ArticleForm(request.POST or None)

    if (form.is_valid()):
        titre = form.cleaned_data['titre']
        auteur = form.cleaned_data['auteur']
        contenu = form.cleaned_data['contenu']
        categorie = form.cleaned_data['categorie']
        # le commit=False permet d'enregister les donnée du formulaire dans un objet
        # avec lequel on peut travailer avant de l'envoyer.
        article = form.save(commit=False)
        article.slug = slugGenerator(form.cleaned_data['titre'])
        article.save()
        return HttpResponse('envoyer')
    return render(request, 'blog/articleForm.html', locals())


def e404(request):
    return render(request, '404.html')
