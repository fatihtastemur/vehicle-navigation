from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('navigation-records/', views.navigation_records, name='navigation_records'),
    path('last-location/', views.last_location, name='last_location'),
]