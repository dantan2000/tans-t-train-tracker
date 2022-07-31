from django.urls import path
from . import views


urlpatterns = [
    path('routes/', views.getAllRoutes),
    path('stops/', views.getStops),
    path('departures/', views.getDepartureTimes)
]