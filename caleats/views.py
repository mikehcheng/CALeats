from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from caleats.models import Entree, MenuItem

def index(request):
    return render(request, 'caleats/index.html')

def detail(request, hall):
    menuitems = MenuItem.objects.filter(hall = hall)
    br_menuitems = menuitems.filter(meal = "Breakfast")
    lu_menuitems = menuitems.filter(meal = "Lunch")
    di_menuitems = menuitems.filter(meal = "Dinner")
    context = {
    	'hall': hall,
    	'br_menuitems': br_menuitems,
    	'lu_menuitems': lu_menuitems,
    	'di_menuitems': di_menuitems
    	}
    return render(request, 'caleats/detail.html', context)

