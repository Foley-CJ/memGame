from django.shortcuts import render

#create views here

def landing(request):
	from memGame.dataETLS2 import *


	dataMaster = []

	request.session["dataMaster"] = dataMaster


	return render(request, "../other/landing.html",{})