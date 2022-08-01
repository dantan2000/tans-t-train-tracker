from django.urls import path
from . import views


urlpatterns = [
    path('routes/', views.getAllRoutes, name='routes'),
    path('stops/', views.getStops, name='stops'),
    path('departures/', views.getDepartureTimes, name='departures')
]