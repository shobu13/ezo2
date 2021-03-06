"""ezo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='coreHome'),
    path('a_propos', views.a_propos, name='aPropos'),
    path('connexion', views.connexion, name='connexion'),
    path('inscription', views.inscription, name='inscription'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('afficher_profil', views.afficher_profil, name='afficherProfil')
]

urlpatterns += staticfiles_urlpatterns()