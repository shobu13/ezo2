from django.contrib import admin
from django.utils.text import Truncator

from .models import Categorie, Article


class ArticleAdmin(admin.ModelAdmin):
    #liste des champs à afficher
    list_display=('titre', 'auteur','date','categorie', 'apercu_contenu', 'slug')
    #remplie le champ apssé en paramètre en fonction du champ donné au format slug
    prepopulated_fields = {'slug': ('titre', ), }
    #liste des champs par lequels nous pouvons filtrer la liste
    list_filter=('auteur', 'categorie')
    #champs à utiliser pour le trie par date intuitif
    date_hierarchy='date'
    #champs de recherche
    search_fields=('titre', 'contenu')
    #trie par défaut
    ordering=['date']
    #liste des champs éditables
    #fields=('titre', 'auteur', 'categorie', 'contenu')
    #liste des champs éditable sous forme de sous zones
    fieldsets=(
        #sous champ 1
        ('Informations Générales', {
            #définis le comportement du sous champ
            'classes':['collapse',],
            #définis les champs qui y sont représenter
            'fields':('titre','slug', 'auteur', 'categorie')
        }),
        #sous champ 2
        ('Contenu de l\'article', {
            'description':'le formulaire accepte les balises html',
            'fields':['contenu',]
        }),
    )


    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        On pourrait le coder nous même, mais Django fournit déjà la
        fonction qui le fait pour nous !
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    #définie un entête pour la colonne crée
    apercu_contenu.short_description="Aperçu du contenu"


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)