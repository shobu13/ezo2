from django.contrib import admin
from core.models import Profil, Parametres


class ParametreAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Nom', {
            'fields': ['nom']
        }),
        ('Valeur', {
            'classes': ['collapse', ],
            'description': 'le formulaire accepte les balises Markdown',
            'fields': ['valeur']
        }),
    )


admin.site.register(Profil)
admin.site.register(Parametres, ParametreAdmin)
