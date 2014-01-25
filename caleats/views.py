from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.utils import simplejson

from caleats.models import Entree, MenuItem

def index(request):
    return render(request, 'caleats/index.html')

def detail(request, hall):
    menuitems = MenuItem.objects.filter(hall = hall.lower())
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

def vote(request):
    print("bye")
    results = {'success':False}
    if request.method == u'GET':
    	print("byebye")
        GET = request.GET
        if GET.has_key(u'pk') and GET.has_key(u'vote'):
            print("byebyebye")
            pk = int(GET[u'pk'])
            vote = GET[u'vote']
            entree = MenuItem.objects.get(pk=pk).entree
            if vote == u"up":
                entree.votes += 1
                print("{0}, {1}".format(entree.name, entree.votes))
            elif vote == u"down":
                entree.votes -= 1
            entree.save()
            results = {'success':True}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')