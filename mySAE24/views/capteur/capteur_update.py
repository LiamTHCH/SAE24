from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from mySAE24.models import Capteur

class CapteurUpdateView(UpdateView):
    model = Capteur
    fields = '__all__'
    template_name = "capteur/capteur_update.html"
    success_url = reverse_lazy('capteur_list')
