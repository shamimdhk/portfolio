from django.http import HttpResponse
from django.shortcuts import render
from .models import AboutUs, Slider, Service

def home(request):
    aboutdata = AboutUs.objects.all()
    sliderdata = Slider.objects.all()
    servicedata = Service.objects.all()
    contex = {
        'AboutUs':aboutdata,
        'Slider' :sliderdata,
        'Service':servicedata
    }

    return render(request,'index.html', contex)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')