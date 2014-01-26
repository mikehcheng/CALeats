# -*- coding: utf-8 -*-
import time
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.utils import simplejson
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from caleats.models import Entree, MenuItem#, UserInfo

def index(request):
    return render(request, 'caleats/index.html')

def detail(request, hall):
    hall = hall.lower()
    menuitems = MenuItem.objects.filter(hall = hall)
    br_menuitems = menuitems.filter(meal = "Breakfast").order_by('-entree__votes')
    lu_menuitems = menuitems.filter(meal = "Lunch").order_by('-entree__votes')
    di_menuitems = menuitems.filter(meal = "Dinner").order_by('-entree__votes')
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

@csrf_exempt #TRASH.PY
def _login(request):
    results = {'success' : False}
    user = authenticate(username = request.POST['login_email'], 
                        password = request.POST['login_password'])
    if user:
        login(request, user)
        results = {'success' : True}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

@csrf_exempt #TRASH.PY
def _register(request):
    results = {'failure' : "Could not get email."}
    username = request.POST['login_email2']
    password = request.POST['login_password2']
    confirm_pass = request.POST['confirm_password2']
    if User.objects.filter(username = username):
        results = {'failure': "Email already in use."}
    elif str(password) != str(confirm_pass):
        results = {'failure': "Passwords don't match."}
    else:
        print('here')
        user = User(username = username, password = make_password(password))
        user.save()
        user = authenticate(username = username, password = password)
        login(request, user)
        results = {'failure': False}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

@csrf_exempt #TRASH.PY
def _logout(request):
    logout(request)
    return HttpResponse(True)


