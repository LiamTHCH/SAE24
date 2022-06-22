from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from mySAE24.models import Capteur

class CapteurDeleteView(DeleteView):
    model = Capteur
    template_name = "capteur/capteur_delete.html"
    success_url = reverse_lazy('capteur_list')