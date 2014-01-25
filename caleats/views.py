from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from caleats.models import Entree, MenuItem

def index(request):
    return render(request, 'caleats/index.html')

def detail(request, hall):
    menuitems = MenuItem.objects.filter(hall = hall)
    context = {'menuitems': menuitems, 'hall': hall}
    return render(request, 'caleats/detail.html', context)

