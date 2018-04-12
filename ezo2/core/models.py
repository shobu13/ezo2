"""moduel contenant les modèles de l'application core"""
from django.db import models
from django.contrib.auth.models import User

from markdownx.models import MarkdownxField


class Profil(models.Model):
    """Extension du modèle utilisateur de base pour rajouter des champs de profil."""
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    description = MarkdownxField(null=True, blank=True)
    avatar = models.ImageField(upload_to='core/img/upload/', null=False, blank=True,
                               default="core/img/750x300.png")

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
