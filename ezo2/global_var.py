"""Variables globales contenant diverses information du site facilement modifiables."""
from core.models import Parametre

WEBSITE_NOM = Parametre.objects.get(nom='nom du site').valeur
COMMU_DESC = Parametre.objects.get(nom='description communautee').valeur


def refresh():
    global COMMU_DESC
    global WEBSITE_NOM
    WEBSITE_NOM = Parametre.objects.get(nom='nom du site').valeur
    COMMU_DESC = Parametre.objects.get(nom='description communautee').valeur

