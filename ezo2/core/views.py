"""Module servant à afficher les pages composant l'application Core."""
from django.shortcuts import render, redirect, reverse
import global_var
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.core.files.images import get_image_dimensions
from django.core.files import File

from core.forms import CreateUserForm, ConnexionForm
from core.models import Profil

def home(request):
    """affiche la page d'acceuil du core"""
    return render(request, 'core/home.html', {'global': global_var})


def a_propos(request):
    """vue affichant diverse informations sur la communauté et ses membres."""
    staff_group = Group.objects.get(name='staff')
    artistes_group = Group.objects.get(name='artistes')
    staff_liste = User.objects.filter(groups=staff_group, profil__isnull=False).exclude(username='admin').exclude(groups=artistes_group)
    artistes_liste = User.objects.filter(groups=artistes_group, profil__isnull=False).exclude(username='admin')
    # for i in artistes_liste:
    #     try:
    #         i.profil
    #     except:
    #         artistes_liste.get(username=i.username).delete()
    #
    # for i in staff_liste:
    #     try:
    #         i.profil
    #     except:
    #         staff_liste.get(username=i.username).delete()
    return render(request, 'core/aPropos.html', {'global': global_var, 'staff_liste': staff_liste, 'artistes_liste':artistes_liste, })


def connexion(request):
    """vue affichant la page de connexion et traitant les données de cette dernière."""
    msg = ''
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'core/home.html', {'global': global_var, 'connexion': True})
            else:
                msg = "Mot de passe ou nom d'utilisateur inconnu"
    else:
        form = ConnexionForm()

    return render(request, "core/connexion.html", {'global': global_var, 'msg': msg,
                                                   'form': form})


def afficher_profil(request):
    """affiche le profil de l'utilisateur connecté et permet la modification de la description ainsi que de l'image de
    l'utilisateur connecté"""
    error = []
    if request.method == "POST":
        description = request.POST['description']
        print("description= ", description)
        if request.FILES:
            print("FILES= ", request.FILES)
            print("AVATAR= ", request.FILES['avatar'])
            img = request.FILES['avatar']
            image_dimension = get_image_dimensions(img)
            image_size = img.size / 1000000
            if image_dimension[1] > 1000:
                error.append("l'image à une hauteur supérieur à 1000px")
            if image_size > 1:
                error.append("L'image dépasse la taille autorisée (1Mo)")
        print("error", error)
        print(request.POST)
        user = request.user
        if not error:
            try:
                print("desc user= ", user.profil.description)
                user.profil.description = description
                print("nouvelle desc= ", user.profil.description)
                if request.FILES:
                    user.profil.avatar = img
                user.profil.save()
            except:
                if request.FILES:
                    profil = Profil(user=user, description=description, avatar=img)
                else:
                    profil = Profil(user=user, description=description)
                profil.save()

    return render(request, "core/afficherProfil.html", {'global': global_var, "error": error})


def deconnexion(request):
    """vue permetant à l'utilisateur de se déconnecter, renvoie vers la page d'acceuil avec la
    variable déconexion à True pour afficher une popup"""
    logout(request)
    return render(request, 'core/home.html', {'global': global_var, 'deconnexion': True})


def inscription(request):
    """vue affichant la page d'inscription et traitant les données de cette dernière."""
    msg = ''
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = request.POST["confirm-password"]
            if password == confirm_password:
                form.save()
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                msg = 'utilisateur créer'
            else:
                msg = 'les deux mot de passe ne correspondent pas.'
        else:
            msg = 'le formulaire est invalide.'
    else:
        form = CreateUserForm()
    return render(request, "core/inscription.html", {'global': global_var, 'form': form,
                                                     'msg': msg})

