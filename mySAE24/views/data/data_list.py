from django.views.generic import ListView

from mySAE24.models import Data

class DataListView(ListView):
    model = Data
    template_name = "data/data_list.html"
