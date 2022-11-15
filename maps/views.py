from django.shortcuts import render
from maps.models import Marker, Point
from django.core.serializers import serialize
import json

# Create your views here.

def index(request):
    polygons = json.loads(serialize("geojson", Marker.objects.all()))
    points = json.loads(serialize("geojson", Point.objects.all()))
    return render(request, "index.html", locals())