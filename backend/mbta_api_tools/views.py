from http.client import HTTPResponse
from xmlrpc.client import SERVER_ERROR
from django.shortcuts import render
from django.http import JsonResponse, HTTPResponse
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
    r = requests.get(url, header=apiHeader, params=params)
  except:
    # Catch HTTP exception or non-json response from MBTA API
    return HTTPResponse(status=503, reason='MBTA API Unavailable')
  else:
    # If the API response data is empty, the route or direction_id is invalid
    data = r.json().data
    if (data & data.len() > 0):
      return JsonResponse(data)
    else:
      return HTTPResponse(status=400, reason=badRequestReason)



allRoutesParameters = {
  'filter[type]': [0, 1]
}

# Gets all Light and Heavy MBTA Routes
# Returns a JSONResponse with MBTA data when successful
# Returns an HTTP Response with error codes otherwise
def getAllRoutes(request):
  return mbtaGetHelper(routesUrl, allRoutesParameters, routesBadRequestReason)

# Gets all stops along a given route in a given direction
# Returns a JSONResponse with MBTA data when successful
# Returns an HTTP Response with error codes otherwise
def getStops(request):
  # Get parameters from request
  params = {
    'filter[route]': request.GET['filter[route]'],
    'filter[direction_id]': request.GET['filter[direction_id']
  }
  return mbtaGetHelper(routesUrl, allRoutesParameters, stopsBadRequestReason)

# Gets the predicted times the next trains will depart from 
# a given stop and a given direction, sorted by time
# Returns a JSONResponse with MBTA data when successful
# Returns an HTTP Response with error codes otherwise
def getDepartureTimes(request):
  # Get parameters from request
  params = {
    'filter[stop]': request.GET['filter[stop]'],
    'filter[direction_id]': request.GET['filter[direction_id'],
    'sort': 'departure_time'
  }
  return mbtaGetHelper(routesUrl, allRoutesParameters, predictionsBadRequestReason)
