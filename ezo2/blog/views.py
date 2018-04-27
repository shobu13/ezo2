"""Django views module, used to display HTMl template and process data"""
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render

import global_var
from blog.models import Article, Categorie


def home(request):
    """Vue permettant l'affichage de la page d'acceuil, renvoie les 4 articles les plus récents."""
    global_var.refresh()
    article_list = Article.objects.order_by('date').reverse()[:4]
    return render(request, 'blog/index.html',
                  {'articleList': article_list, 'global': global_var})


def lire(request, id_article, slug):
    """vue permettant l'affichage d'un article en particulier."""
    global_var.refresh()
    article = get_object_or_404(Article, id=id_article, slug=slug)
    print(article)
    return render(request, 'blog/post.html', {'article': article, 'global': global_var})


def article_liste(request, page=0, keywords="null", selected_cat="null"):
    """vue affichant la liste des articles, 4 article par page, par ordre chronologique et avec
    possibilité de filtrer par mot clé ou par catégorie."""
    global_var.refresh()
    categorie_liste = []
    baked_article_liste = []

    raw = []
    old = ''
    new = ''
    raw_categorie = Categorie.objects.all()
    if request.POST:
        print("POST=")
        print(request.POST['search'])
        keywords = request.POST['search']

    if keywords == 'null' and selected_cat == 'null':
        raw_article_list = Article.objects.order_by('date').reverse()
    else:
        if keywords != 'null' and selected_cat == 'null':
            filtres = Q(titre__contains=keywords) | Q(contenu__contains=keywords)
            raw_article_list = Article.objects.filter(filtres).order_by('date').reverse()

        elif keywords == 'null' and selected_cat != 'null':
            raw_article_list = Article.objects.filter(categorie__nom__contains=selected_cat)
            raw_article_list = raw_article_list.order_by('date').reverse()

        else:
            filtres = (Q(titre__contains=keywords) | Q(contenu__contains=keywords)) &\
                     Q(categorie__nom__contains=selected_cat)
            raw_article_list = Article.objects.filter(filtres).order_by('date').reverse()

    print("raw article liste =")
    print(raw_article_list)

    if raw_article_list:
        for i in range(0, len(raw_article_list), 4):
            baked_article_liste += [raw_article_list[i:i + 4]]

        for i in range(0, len(raw_categorie), 3):
            raw += [raw_categorie[i:i + 3]]
        for i in range(0, len(raw), 2):
            categorie_liste += [raw[i:i + 2]]

        if page == 0:
            new = 'disabled'
        if page == len(baked_article_liste) - 1:
            old = 'disabled'

        print("baked_article_liste=")
        print(baked_article_liste)

        print("sending page")
        return render(request, 'blog/articleListe.html',
                      {'categorieListe': categorie_liste, 'global': global_var,
                       'article_liste': baked_article_liste[page],
                       'page': page, 'oldDisable': old, 'newDisable': new, 'keywords': keywords,
                       'selected_cat': selected_cat, })

    else:
        print("no result")
        return render(request, 'blog/articleListe.html',
                      {'categorieListe': categorie_liste, 'global': global_var,
                       'article_liste': '', 'page': -1,
                       'oldDisable': 'disabled', 'newDisable': 'disabled', 'keywords': keywords,
                       'selected_cat': selected_cat, })
