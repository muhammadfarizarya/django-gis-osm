from django.urls import path
  
from maps import views
  
urlpatterns = [
    path('', views.index, name="maps_index" ),
]