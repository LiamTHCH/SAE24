from django.views.generic import ListView

from mySAE24.models import Capteur

class CapteurListView(ListView):
    model = Capteur
    template_name = "capteur/capteur_list.html"
