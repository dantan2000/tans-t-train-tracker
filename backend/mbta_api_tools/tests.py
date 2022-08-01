from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse, resolve
import json
from mbta_api_tools.test_data import routesData, stopsData, predictionsData, emptyData
from mbta_api_tools.views import *
import requests
from unittest.mock import patch, Mock
import uuid

# Test API Urls resolve to the proper views
class TestUrls(TestCase):

  def test_routes_url_is_resolved(self):
    url = reverse('routes')
    self.assertEquals(url, '/mbta_api/routes/', '/mbta_api/routes/ url is not properly configured')
    self.assertEquals(
      resolve(url).func, getAllRoutes, '/mbta_api/routes/ is not resolved'
    )

  def test_stops_url_is_resolved(self):
    url = reverse('stops')
    self.assertEquals(url, '/mbta_api/stops/', 'mbta_api/stops/ url is not properly configured')
    self.assertEquals(
      resolve(url).func, getStops, '/mbta_api/stops/ is not resolved'
    )

  def test_departures_url_is_resolved(self):
    url = reverse('departures')
    self.assertEquals(url, '/mbta_api/departures/', '/mbta_api/departures/ url is not properly configured')
    self.assertEquals(
      resolve(url).func, getDepartureTimes, '/mbta_api/departures/ is not resolved'
    )



# Test MBTA API Get Helper Method
@patch('requests.get') # Mock Request Get Method
class TestMbtaGetHelper(TestCase):

  # Helper method for simulating API calls with a mock
  # Mocks the return value of the MBTA API call and verifies it was called
  #   with the proper arguments
  # Returns the response object from the mbtaGetHelper call
  def make_api_call_with_mock(self, mockGet, mockReturnValue, badRequestReason = ''):
    # Mock API Call return
    mockGet.return_value = mockReturnValue

    testUrl = uuid.uuid1()
    testParams = { 
      uuid.uuid1(): uuid.uuid1(),
      uuid.uuid1(): uuid.uuid1()
    }

    r = mbtaGetHelper(testUrl, testParams, badRequestReason)

    # Assert requests.get was called with the proper arguments
    mockGet.assert_called_with(testUrl, headers=apiHeader, params=testParams)

    return r


  # Test a successful MBTA Get Request
  def test_api_get_successful(self, mockGet):
    # Make API call with mock success
    r = self.make_api_call_with_mock(mockGet, Mock(status_code=200, json=lambda: routesData))


    # Assert proper Http response
    self.assertEqual(r.status_code, 200, 'mbtaGetHelper returned non-200 status code on success')
    self.assertEqual(json.loads(r.content), {'data': routesData['data']}, 'mbtaGetHelper returned incorrect data on success')

  # Test a HTTP error from the MBTA API
  def test_api_get_http_error(self, mockGet):
    # Make API call with mock HTTP error
    r = self.make_api_call_with_mock(mockGet, Mock(status_code=404), 'MBTA API Unavailable')

    # Assert proper Http response
    self.assertEqual(r.status_code, 503, 'mbtaGetHelper returned non-503 status code on MBTA API error')
    self.assertEqual(r.reason_phrase, 'MBTA API Unavailable', 'mbtaGetHelper returned incorrect reason on MBTA API error')

    # Make API call with alternate mock HTTP error
    r = self.make_api_call_with_mock(mockGet, Mock(status_code=400), 'MBTA API Unavailable')

    # Assert proper Http response
    self.assertEqual(r.status_code, 503, 'mbtaGetHelper returned non-503 status code on MBTA API error')
    self.assertEqual(r.reason_phrase, 'MBTA API Unavailable', 'mbtaGetHelper returned incorrect reason on MBTA API error')

  # Test an empty data response from the MBTA API
  # Empty data response implies bad query from front end
  def test_api_get_empty_data(self, mockGet):
    # Make API call with mock empty data response
    r = self.make_api_call_with_mock(mockGet, Mock(status_code=200, json=lambda: emptyData), 'Route or Direction is Invalid')

    # Assert proper Http response
    self.assertEqual(r.status_code, 400, 'mbtaGetHelper returned non-400 status code on bad reqeust')
    self.assertEqual(r.reason_phrase, 'Route or Direction is Invalid', 'mbtaGetHelper returned incorrect reason on empty MBTA API data')

    mockData = ['foo']

    # Make API call with mock non-empty data response
    r = self.make_api_call_with_mock(mockGet, Mock(status_code=200, json=lambda: {'data': mockData}))

    # Assert proper Http response
    self.assertEqual(r.status_code, 200, 'mbtaGetHelper returned non-200 status code on non-empty MBTA API data')
    self.assertEqual(json.loads(r.content), {'data': mockData}, 'mbtaGetHelper returned incorrect data on non-empty MBTA API data')



@patch('mbta_api_tools.views.mbtaGetHelper')
class TestGetMethods(TestCase):

  # Helper method to automate testing Get methods
  # Returns the output of the given func to test
  def get_test_helper(self, func, mockHelper, mockReturnValue, request, expectedParams):
    # Mock response from mbtaGetHelper
    mockHelper.return_value = mockReturnValue

    r = func(request)
    # Assert helper was called with the parameters
    mockHelper.assert_called_with(*expectedParams)
    # Assert result from helper was returned properly
    self.assertEqual(r, mockReturnValue, 'Result from mbtaGetHelper was not returned')


  # Test getAllRoutes calls helper method with expected parameters
  def test_get_all_routes(self, mockHelper):
    # Mock response from mbtaGetHelper
    mockReturnValue = Mock(status_code=200, json=lambda: {'data': routesData})

    request = {}

    expectedParams = (
      'https://api-v3.mbta.com/routes/', 
      {
        'filter[type]': '0,1',
        'sort': ''
      },
      'No Routes Found'
    )

    self.get_test_helper(getAllRoutes, mockHelper, mockReturnValue, request, expectedParams)


  # Test getStops calls helper method with expected parameters
  def test_get_stops(self, mockHelper):
    # Mock response from mbtaGetHelper
    mockReturnValue = Mock(status_code=200, json=lambda: {'data': stopsData})

    request = Mock(GET={
      'filter[route]': 'route_name',
      'filter[direction_id]': '0'
    })

    expectedParams = (
      'https://api-v3.mbta.com/stops/', 
      {
        'filter[route]': 'route_name',
        'filter[direction_id]': '0'
      },
      'Route or Direction is Invalid'
    )

    self.get_test_helper(getStops, mockHelper, mockReturnValue, request, expectedParams)


  # Test getDepartureTimes calls helper method with expected parameters
  def test_get_departure_times(self, mockHelper):
    # Mock response from mbtaGetHelper
    mockReturnValue = Mock(status_code=200, json=lambda: {'data': predictionsData})

    request = Mock(GET={
      'filter[stop]': 'stop_name',
      'filter[direction_id]': '1'
    })

    expectedParams = (
      'https://api-v3.mbta.com/predictions/', 
      {
        'filter[stop]': 'stop_name',
        'filter[direction_id]': '1',
        'sort': 'departure_time'
      },
      'Stop or Direction is Invalid'
    )

    self.get_test_helper(getDepartureTimes, mockHelper, mockReturnValue, request, expectedParams)


# Test API connection
class TestAPIConnection(TestCase):

  # Helper to check if sending a get request to a given url is successful
  def assert_connection(self, url, params=None):
    try:
      r = requests.get(url, params=params)
    except:
      # Fail if reqeusts.get throws an exception
      self.assertTrue(False, '{} request failed'.format(url))
    else:
      # Check if the response was successful
      self.assertEqual(
        r.status_code, 
        200, 
        '{} request returned non-200 status code ({})'.format(url, r.status_code)
      )
    

  # Test MBTA API responds to requests
  def test_mbta_api_connection(self):
    self.assert_connection(mbtaApiUrl)
    

  # Test MBTA API responds to routes requests
  def test_mbta_api_routes_connection(self):
    self.assert_connection(routesUrl)
    

  # Test MBTA API responds to stops requests
  def test_mbta_api_stops_connection(self):
    self.assert_connection(stopsUrl)
    

  # Test MBTA API responds to predictions requests
  def test_mbta_api_predictions_connection(self):
    self.assert_connection(predictionsUrl, {'filter[direction_id]': ''})