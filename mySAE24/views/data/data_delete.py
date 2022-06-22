from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from mySAE24.models import Data

class DataDeleteView(DeleteView):
    model = Data
    template_name = "data/data_delete.html"
    success_url = reverse_lazy('data_list')