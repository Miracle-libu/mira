from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add_transport/',views.add_transport,name ='add_transport'),
]