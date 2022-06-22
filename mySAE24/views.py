from django.shortcuts import render
from .models import *
def index(request):
	query = Data.objects.all()
	return render(request, "index.html",{"data":query})


