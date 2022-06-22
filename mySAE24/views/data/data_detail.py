from django.views.generic import DetailView

from mySAE24.models import Data


class DataDetailView(DetailView):
    model = Data
    template_name = "data/data_detail.html"
