from django.http import HttpResponse
from django.shortcuts import render
from .models import AboutUs

def home(request):
    aboutdata = AboutUs.objects.all()
    contex = {
        'AboutUs':aboutdata
    }

    return render(request,'index.html', contex)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')