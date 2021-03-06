"""module contenant les modèles de donnée de l'application blog."""
from django.db import models
from django.utils import timezone

from markdownx.models import MarkdownxField


class Article(models.Model):
    """class définissant un article du blog."""
    titre = models.CharField(max_length=100)
    sousTitre = models.CharField(max_length=200, null=False, blank=True, default="")
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = MarkdownxField()
    # le paramètre default existe pour la plupart des champs
    # le paramètre verbose_name est lui aussi commun,
    # il sert à donner une précision quand au nom du champs.
    date = models.DateTimeField(default=timezone.now, verbose_name="date de parution")
    header = models.ImageField(upload_to='blog/img/upload/', null=False, blank=True, default="blog/img/750x300.png")

    # related_name permet de définir un nouveau nom pour la variable de la relation inverse.
    categorie = models.ForeignKey('Categorie', on_delete=models.PROTECT)

    class Meta:
        """Cette classe permet de donner des informations sur le comportement propre au modèle"""
        verbose_name = "Article"
        ordering = [
            'date']  # permet de donner l'odre par défaut de trie des donnée, ici par la date.

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        # cela défini la donnée renvoyée dans les dataSet
        return self.titre


class Categorie(models.Model):
    """class définissant une catégorie du blog."""
    nom = models.CharField(max_length=30)

    class Meta:
        """Cette classe permet de donner des informations sur le comportement propre au modèle"""
        verbose_name = "Categorie"

    def __str__(self):
        return self.nom
