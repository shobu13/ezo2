"""Variables globales contenant diverses information du site facilement modifiables."""
from core.models import Parametres

WEBSITE_NOM = Parametres.objects.get(nom='nom du site').valeur
WEBSITE_DESC = Parametres.objects.get(nom='description communautee').valeur


def refresh():
    global WEBSITE_DESC
    global WEBSITE_NOM
    WEBSITE_NOM = Parametres.objects.get(nom='nom du site').valeur
    WEBSITE_DESC = Parametres.objects.get(nom='description communautee').valeur

