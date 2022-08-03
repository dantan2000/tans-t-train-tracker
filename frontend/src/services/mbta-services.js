import axios from 'axios';
const BACKEND_BASE = 'http://127.0.0.1:8000/mbta_api/';
const ROUTES_URL = `${BACKEND_BASE}routes/`;
const STOPS_URL = `${BACKEND_BASE}stops/`;
const DEPARTURES_URL = `${BACKEND_BASE}departures/`;

// Get all MBTA T routes from the backend
export const getRoutes = async() => {
  const response = await axios.get(ROUTES_URL);
  return response.data.data;
}

// Get the MBTA T route with the given id
export const getRouteById = async(routeId) => {
  const response = await axios.get(ROUTES_URL + routeId);
  return response.data.data;
}

// Gets all stops along the given MBTA route
export const getStops = async(routeId) => {
  const response = await axios.get(STOPS_URL, {params: {'filter[route]': routeId}});
  return response.data.data
}

// Gets the MBTA T stop with the given id
export const getStopById = async(stopId) => {
  const response = await axios.get(STOPS_URL + stopId);
  return response.data.data
}

// Gets departure times from a given stop in a given direction
export const getDepartureTimes = async(stopId, directionId) => {
  const response = await axios.get(DEPARTURES_URL, {params: {'filter[stop]': stopId, 'filter[direction_id]': directionId}});
  return response.data.data
}