from mySAE24.views import DataDeleteView
from mySAE24.views import DataUpdateView
from mySAE24.views import DataDetailView
from mySAE24.views import DataCreateView
from mySAE24.views import DataListView
from mySAE24.views import CapteurDeleteView
from mySAE24.views import CapteurUpdateView
from mySAE24.views import CapteurDetailView
from mySAE24.views import CapteurCreateView
from mySAE24.views import CapteurListView
import mySAE24.views as views
from django.urls import path

urlpatterns = [
path('',views.index),
path('csv/',views.csv_export),
path('data/',views.data),
path('capteur/',views.capteur),
path('capteur/list/', CapteurListView.as_view(), name='capteur_list'),
path('capteur/create/', CapteurCreateView.as_view(), name='capteur_create'),
path('capteur/detail/<str:pk>/', CapteurDetailView.as_view(), name='capteur_detail'),
path('capteur/update/<str:pk>/', CapteurUpdateView.as_view(), name='capteur_update'),
path('capteur/delete/<str:pk>/', CapteurDeleteView.as_view(), name='capteur_delete'),
path('data/list/', DataListView.as_view(), name='data_list'),
path('data/create/', DataCreateView.as_view(), name='data_create'),
path('data/detail/<int:pk>/', DataDetailView.as_view(), name='data_detail'),
path('data/update/<int:pk>/', DataUpdateView.as_view(), name='data_update'),
path('data/delete/<int:pk>/', DataDeleteView.as_view(), name='data_delete'),
]
