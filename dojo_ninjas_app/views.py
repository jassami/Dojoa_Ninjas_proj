from django.shortcuts import render, redirect
from .models import *

def index(request):
    context= {
        'all_dojos': Dojo.objects.all(),
        'all_ninjas': Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def process(request, action):
        if request.method == 'POST':
            if action == 'add_dojo':
                Dojo.objects.create(name= request.POST['name'], city= request.POST['city'], state= request.POST['state'])
            if action == 'add_ninja':
                selected_dojo= Dojo.objects.get(name= request.POST['dojo'])
                Ninja.objects.create(dojo= selected_dojo, first_name= request.POST['first_name'], last_name= request.POST['last_name'])
            if action =='delete':
                Dojo.objects.get(name= request.POST['dojo']).delete()
            return redirect('/')

