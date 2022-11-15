# from django.contrib import admin
from django.contrib.gis import admin
from maps.models import Marker, Point
from leaflet.admin import LeafletGeoAdmin
from leaflet.admin import LeafletGeoAdminMixin

# Register your models here.

@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    exclude = ['created_date']
    search_fields = ['nama']
    list_display = ['nama', 'deskripsi', 'created_date']

@admin.register(Point)
class PointAdmin(admin.OSMGeoAdmin):
    exclude = ['created_date']
    search_fields = ['nama']
    list_display = ['nama', 'deskripsi', 'created_date']