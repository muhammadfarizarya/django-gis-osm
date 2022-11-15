# from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone

# Create your models here.

class Marker(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    polygon = models.PolygonField()

    class Meta:
        verbose_name_plural = "Marker"

    def __str__(self):
        return self.nama

class Point(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    polygon = models.PointField()

    class Meta:
        verbose_name_plural = "Point"

    def __str__(self):
        return self.nama

