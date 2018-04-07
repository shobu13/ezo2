"""Module servant à afficher les pages composant l'application Core."""
from django.shortcuts import render
import global_var


def home(request):
    """affiche la page d'acceuil du core"""
    return render(request, 'core/home.html', {'global': global_var})


def a_propos(request):
    """vue affichant diverse informations sur la communauté et ses membres."""
    return render(request, 'core/aPropos.html', {'global': global_var})
