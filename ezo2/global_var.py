"""Variables globales contenant diverses information du site facilement modifiables."""
from core.models import Parametres

WEBSITE_NOM = Parametres.objects.get(nom='nom du site').valeur
COMMU_DESC = Parametres.objects.get(nom='description communautee').valeur


def refresh():
    global COMMU_DESC
    global WEBSITE_NOM
    WEBSITE_NOM = Parametres.objects.get(nom='nom du site').valeur
    COMMU_DESC = Parametres.objects.get(nom='description communautee').valeur

