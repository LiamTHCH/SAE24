from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from mySAE24.models import Data

class DataCreateView(CreateView):
    model = Data
    fields = '__all__'
    template_name = "data/data_create.html"
    success_url = reverse_lazy('data_list')
