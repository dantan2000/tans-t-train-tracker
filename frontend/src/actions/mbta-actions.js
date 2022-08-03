import * as services from '../services/mbta-services';

export const GET_ROUTES = 'GET_ROUTES';
export const GET_STOPS = 'GET_STOPS';
export const GET_DEPARTURE_TIMES = 'GET_DEPARTURE_TIMES';

export const getRoutes = async(dispatch) => {
    const routes = await services.getRoutes(queryString);
    dispatch({
        type: GET_ROUTES,
        routes
    });
}

export const getStops = async(dispatch, routeId) => {
    const stops = await services.getStops(routeId);
    dispatch({
        type: GET_STOPS,
        stops
    });
}

export const getDepartureTimes = (dispatch, stopId, directionId) => {
    const departures = await service.getDepartureTimes(stopId, directionId);
    dispatch({
        type: GET_DEPARTURE_TIMES,
        departures
    });
}