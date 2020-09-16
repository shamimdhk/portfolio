from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=False)
    year = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='aboutimg/', blank=False)
   
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='aboutimg/', blank=False)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='serviceimg/', blank=False)
    description = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return self.title