from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre=models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur=models.CharField(max_length=42)
    contenu=models.TextField(null=True)
    #le paramètre default existe pour la plupart des champs
    #le paramètre verbose_name est lui aussi commun, il sert à donner une précision quand au nom du champs.
    date=models.DateTimeField(default=timezone.now, verbose_name="date de parution")

    #related_name permet de définir un nouveau nom pour la variable de la relation inverse.
    categorie=models.ForeignKey('Categorie', on_delete=models.PROTECT)

    class Meta:
        #Cette classe permet de donner des informations sur le comportement propre au modèle
        verbose_name="Article"
        ordering=['date'] #permet de donner l'odre par défaut de trie des donnée, ici par la date.

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        #cela défini la donnée renvoyée dans les dataSet
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    class Meta:
        #Cette classe permet de donner des informations sur le comportement propre au modèle
        verbose_name="Categorie"

    def __str__(self):
        return self.nom