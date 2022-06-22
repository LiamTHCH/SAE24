from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from mySAE24.models import Data

class DataUpdateView(UpdateView):
    model = Data
    fields = '__all__'
    template_name = "data/data_update.html"
    success_url = reverse_lazy('data_list')
