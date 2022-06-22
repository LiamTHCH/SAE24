from django.shortcuts import render
from .models import *
import datetime
def index(request):
	if request.method == 'POST':
		start = request.POST.get('start')
		stop = request.POST.get('stop')
		print(request.POST.get('capteur'))
		if (request.POST.get('start') == ""):
			print("NO START")
			start = datetime.date(1800, 10, 1)
		if (request.POST.get('stop') == ""):
			print("NO STOP")
			stop = (datetime.date.today()+datetime.timedelta(days=1))

		print(start)
		print(stop)
		if request.POST.get('capteur') != "*":
			query = Data.objects.filter(timestamp__range=(start, stop),capteur=request.POST.get('capteur'))
		else:
			query = Data.objects.filter(timestamp__range=(start, stop))
		cap = Capteur.objects.all()
		return render(request, "index.html",{"data":query,"cap":cap})
	else:
		query = Data.objects.all()
		cap = Capteur.objects.all()
		return render(request, "index.html",{"data":query,"cap":cap})


