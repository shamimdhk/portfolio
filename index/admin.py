from django.contrib import admin

# Register your models here.
from .models import AboutUs, Slider, Service

admin.site.register(AboutUs)
admin.site.register(Slider)
admin.site.register(Service)
