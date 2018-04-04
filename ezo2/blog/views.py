"""Django views module, used to display HTMl template and process data"""
from django.db.models import Q
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

import blog.global_var as global_var
# from ezo2.shobu import slug_generator
# from ezo2.blog.forms import ContactForm, ArticleForm
from blog.models import Article, Categorie


def home(request):
    """Vue permettant l'affichage de la page d'acceuil, renvoie les 4 articles les plus récents."""
    article_list = Article.objects.order_by('date').reverse()[:4]
    return render(request, 'blog/index.html',
                  {'articleList': article_list, 'global': global_var})


def lire(request, id_article, slug):
    """vue permettant l'affichage d'un article en particulier."""
    article = get_object_or_404(Article, id=id_article, slug=slug)
    print(article)
    return render(request, 'blog/post.html', {'article': article, 'global': global_var})


def article_liste(request, page=0, keywords="null", selected_cat="null"):
    """vue affichant la liste des articles, 4 article par page, par ordre chronologique et avec
    possibilité de filtrer par mot clé ou par catégorie."""
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


def a_propos(request):
    """vue affichant diverse informations sur la communauté et ses membres."""
    return render(request, 'blog/about.html', {'global': global_var})

# TODO ---------------------------------------------------------------


# def contact(request):
#     # on construit le formulaire, soit avec les données postée
#     # sois vide si l'utilisateur y accède pour la première fois
#     form = ContactForm(request.POST or None)
#     # On vérifie que les données du formulaire sont bien valide
#     if form.is_valid():
#         # on lit la valeur des différent champs
#         sujet = form.cleaned_data['sujet']
#         message = form.cleaned_data['message']
#         envoyeur = form.cleaned_data['envoyeur']
#         renvoi = form.cleaned_data['renvoi']
#
#         # on valide l'envoie de l'e-mail
#         envoi = True
#
#     # quoi qu'il arrive, on retourne la page du formulaire
#     return render(request, 'blog/contact.html', locals())
#
#
# def article(request):
#     form = ArticleForm(request.POST or None)
#
#     if form.is_valid():
#         titre = form.cleaned_data['titre']
#         auteur = form.cleaned_data['auteur']
#         contenu = form.cleaned_data['contenu']
#         categorie = form.cleaned_data['categorie']
#         # le commit=False permet d'enregister les donnée du formulaire dans un objet
#         # avec lequel on peut travailer avant de l'envoyer.
#         article = form.save(commit=False)
#         article.slug = slug_generator(form.cleaned_data['titre'])
#         article.save()
#         return HttpResponse('envoyer')
#     return render(request, 'blog/articleForm.html', locals())
#
#
# def e404(request):
#     return render(request, '404.html')
