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
from django.contrib import admin
from django.urls import path
from website import views       #on importe le module contenant nos vues

urlpatterns = [
    #page d'acceuil (index)
    path('', views.home),
    #formulaire de contact
    path('contact', views.contact, name='contact'),
    #page 404
    path('404', views.e404, name='404'),
    #formulaire d'ajout d'article
    path('article', views.article, name='article'),
]
