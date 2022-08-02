from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import os

apiHeader = { 'api_key': os.environ['MBTA_API_KEY'] }

mbtaApiUrl = 'https://api-v3.mbta.com/'

routesUrl = mbtaApiUrl + 'routes/'
stopsUrl = mbtaApiUrl + 'stops/'
predictionsUrl = mbtaApiUrl + 'predictions/'

# HTTP Error Messages
routesBadRequestReason = 'No Routes Found'
stopsBadRequestReason = 'Route or Direction is Invalid'
predictionsBadRequestReason = 'Stop or Direction is Invalid'

# Makes an API call to the given url with the given parameters
# Returns a JSONResponse data from the API Call when successful
# Returns a HTTP Response with error codes for API HTTP exceptions and empty data
def mbtaGetHelper(url, params, badRequestReason):
  try:

    r = requests.get(url, headers=apiHeader, params=params)

    if (r.status_code == 200):
      # If the API response data is empty, the route or direction_id is invalid
      data = r.json()['data']
      if (data is not None and len(data) > 0):
        return JsonResponse({'data': data})
      else:
        return HttpResponse(status=400, reason=badRequestReason)
    # Handle MBTA API error responses
    else:
      return HttpResponse(status=503, reason='MBTA API Unavailable')

  except:
    return HttpResponse(status=500, reason='Internal Server Error')



allRoutesParameters = {
  'filter[type]': '0,1',
  'sort': ''
}

# Gets all Light and Heavy MBTA Routes
# Returns a JSONResponse with MBTA data when successful
# Returns an HTTP Response with error codes otherwise
def getAllRoutes(request):
  return mbtaGetHelper(routesUrl, allRoutesParameters, routesBadRequestReason)

# Gets an MBTA Route with the given ID
# Returns a JSONResponse with MBTA data when successful
# Returns an HTTP Response with error codes otherwise
def getRouteById(request, route):
  params = {
    'filter[id]': route,
    'filter[type]': '0,1',
    'sort': ''
  }
  return mbtaGetHelper(routesUrl, params, routesBadRequestReason)

# Gets all stops along a given route in a given direction
# Returns a JSONResponse with MBTA data when successful
# Returns an HTTP Response with error codes otherwise
def getStops(request):
  # Get parameters from request
  params = {
    'filter[route]': request.GET['filter[route]']
  }
  return mbtaGetHelper(stopsUrl, params, stopsBadRequestReason)

# Gets the predicted times the next trains will depart from 
# a given stop and a given direction, sorted by time
# Returns a JSONResponse with MBTA data when successful
# Returns an HTTP Response with error codes otherwise
def getDepartureTimes(request):
  # Get parameters from request
  params = {
    'filter[stop]': request.GET['filter[stop]'],
    'filter[direction_id]': request.GET['filter[direction_id]'],
    'sort': 'departure_time'
  }
  return mbtaGetHelper(predictionsUrl, params, predictionsBadRequestReason)
