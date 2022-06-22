from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from mySAE24.models import Capteur

class CapteurCreateView(CreateView):
    model = Capteur
    fields = '__all__'
    template_name = "capteur/capteur_create.html"
    success_url = reverse_lazy('capteur_list')
