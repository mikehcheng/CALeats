# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.utils import simplejson

from caleats.models import Entree, MenuItem

def index(request):
    return render(request, 'caleats/index.html')

def detail(request, hall):
    hall = hall.lower()
    menuitems = MenuItem.objects.filter(hall = hall)
    br_menuitems = menuitems.filter(meal = "Breakfast")
    lu_menuitems = menuitems.filter(meal = "Lunch")
    di_menuitems = menuitems.filter(meal = "Dinner")
    hallname_dict = {
        "cafe_3": u"Café 3",
        "clark_kerr": "Clark Kerr",
        "crossroads": "Crossroads",
        "foothill": "Foothill"
        }
    context = {
    	'hall': hallname_dict[hall],
    	'br_menuitems': br_menuitems,
    	'lu_menuitems': lu_menuitems,
    	'di_menuitems': di_menuitems,
    	}
    return render(request, 'caleats/detail.html', context)

def vote(request):
    results = {'success':False}
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'pk') and GET.has_key(u'vote'):
            pk = int(GET[u'pk'])
            vote = GET[u'vote']
            entree = MenuItem.objects.get(pk=pk).entree
            if vote == u"up":
                entree.votes += 1
            elif vote == u"down":
                entree.votes -= 1
            entree.save()
            results = {'success':True}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')