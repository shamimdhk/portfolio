
from django.urls import path, include
from. import views

urlpatterns = [
   
    path('',views.employee),
    path('profile/',views.profile, name='employee.profile'),
]