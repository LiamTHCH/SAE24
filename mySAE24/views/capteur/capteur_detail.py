from django.views.generic import DetailView

from mySAE24.models import Capteur


class CapteurDetailView(DetailView):
    model = Capteur
    template_name = "capteur/capteur_detail.html"
