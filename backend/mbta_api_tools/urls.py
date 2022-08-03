from django.urls import path
from . import views


urlpatterns = [
    path('routes/', views.getAllRoutes, name='routes'),
    path('routes/<str:route>', views.getRouteById, name='routeById'),
    path('stops/', views.getStops, name='stops'),
    path('stops/<str:stop>', views.getStopById, name='stopById'),
    path('departures/', views.getDepartureTimes, name='departures')
]