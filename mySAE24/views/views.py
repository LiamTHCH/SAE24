from django.shortcuts import render
from mySAE24.models import *
import datetime
import csv
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect,HttpResponseBadRequest
import mimetypes
def index(request):
	if request.method == 'POST':
		request.session["option"] = []
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
		request.session["option"] = [start,stop,request.POST.get('capteur')]
		return render(request, "index.html",{"data":query,"cap":cap})
	else:
		request.session["option"] = []
		query = Data.objects.all()
		cap = Capteur.objects.all()
		return render(request, "index.html",{"data":query,"cap":cap})



def csv_export(request):
	dic = request.session["option"]
	if len(dic) == 0:
		dic = [datetime.date(1800, 10, 1),(datetime.date.today()+datetime.timedelta(days=1)),"*"]
	start = dic[0]
	stop = dic[1]
	capteur = dic[2]
	print(dic)
	if capteur != "*":
		query = Data.objects.filter(timestamp__range=(start, stop),capteur=capteur)
	else:
		query = Data.objects.filter(timestamp__range=(start, stop))

	fieldnames = ['ID', 'ID_Capteur', 'Temperature', 'Date/Heure','nom','piece','emplacement']
	row = []
	for item in query:
		row = row + [{'ID':item.id, 'ID_Capteur':item.capteur.id, 'Temperature':item.temp, 'Date/Heure':item.timestamp,'nom':item.capteur.nom,'piece':item.capteur.piece,'emplacement':item.capteur.emplacement}]

	print(row)
	with open('export.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(row)

	path = open('export.csv', 'r')
	response = HttpResponse(path)
	response['Content-Disposition'] = "attachment; filename=%s" % 'export.csv'
	return response

def data(req):
	return HttpResponseRedirect("/data/list/")


def capteur(req):
	return HttpResponseRedirect("/capteur/list/")