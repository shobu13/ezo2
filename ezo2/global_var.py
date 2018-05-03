"""Variables globales contenant diverses information du site facilement modifiables."""
from core.models import Parametre

WEBSITE_NOM = "Non définis"  # nom du paramètre : nom du site
COMMU_DESC = "Non définis"  # nom du paramètre : description communautee


def refresh():
    global WEBSITE_NOM
    global COMMU_DESC
    try:
        WEBSITE_NOM = Parametre.objects.get(nom='nom du site').valeur
        COMMU_DESC = Parametre.objects.get(nom='description communautee').valeur
    except:
        WEBSITE_NOM = "Non définis"
        COMMU_DESC = "Non définis"


refresh()
