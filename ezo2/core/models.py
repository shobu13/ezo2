"""moduel contenant les modèles de l'application core"""
from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    """Extension du modèle utilisateur de base pour rajouter des champs de profil."""
    user = models.OneToOneField(User)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
