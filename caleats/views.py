from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from caleats.models import Entree

def index(request):
    all_entrees = Entree.objects.all()
    context = {'all_entrees': all_entrees}
    return render(request, 'caleats/index.html', context)