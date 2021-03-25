from django.http import HttpResponse
from django.core import serializers
from app.models import Vehicle, NavigationRecord
from datetime import datetime, timedelta
from django.template import Context, loader
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("Vehicle Navigation Records App")


def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles.html", {'vehicles': vehicles})


def navigation_records(request):
    data = NavigationRecord.objects.all()

    navigation_records = []
    for item in data:
        latitude = str(item.latitude).replace(',','.')
        longtitude = str(item.longtitude).replace(',','.')
        
        navigation_record = {'id': item.id, 'vehicle' : item.vehicle.plate,
         'latitude' : latitude, 'longtitude' : longtitude, 'datetime' : item.datetime}
        navigation_records.append(navigation_record)
    return render(request, "navigation_records.html", {'navigation_records': navigation_records})


def last_location(request):
    now = datetime.now()
    earlier = now - timedelta(hours=48)
    data = NavigationRecord.objects.filter(datetime__range=(earlier,now))
   
    results = []
    for item in data:
        result = {'latitude': item.latitude, 'longtitude' : item.longtitude,
         'vehicle_plate' : item.vehicle.plate, 'datetime' : item.datetime.strftime('%d.%m.%Y %H:%M:%S')}
        results.append(result)
   
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')
