import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDepartureTimes, getRouteById, getStopById } from "../../services/mbta-services"

const Departures = () => {

  const { routeId, stopId, directionId } = useParams();

  // Whether the current route data is loading
  const [rLoading, setRLoading] = useState(true);
  // Whether an error occurred loading the current route
  const [rError, setRError] = useState(false);
  // State variable for the current route
  const [currRoute, setCurrRoute] = useState(null);

  // Initialize current route state variables
  useEffect(() => {
    // Check if the current route is unitialized and no error has occurred
    if (currRoute == null && !rError) {
      getRouteById(routeId)
        .then(response => setCurrRoute(response[0])) // Update route with response
        .catch(() => setRError(true)) // Set error state on error
        .finally(() => setRLoading(false)); // Set loading state to false
    }
  })


  // Whether the current stop data is loading
  const [sLoading, setSLoading] = useState(true);
  // Whether an error occurred loading the current stop
  const [sError, setSError] = useState(false);
  // State variable for the current stop
  const [currStop, setCurrStop] = useState(null);

  // Initialize current stop state variables
  useEffect(() => {
    if (currStop == null && !sError) {
      getStopById(stopId)
        .then(response => setCurrStop(response[0]))
        .catch(() => setSError(true))
        .finally(() => setSLoading(false));
    }
  });


  // Whether the list of departures is loading
  const [dLoading, setDLoading] = useState(true);
  // Whether an error occurred loading the list of stops
  const [dError, setDError] = useState(false);
  // State variable for the list of stops
  const [departures, setDepartures] = useState([]);

  // Initialize departures state variables
  useEffect(() => {
    if (departures.length === 0 && !dError) {
      getDepartureTimes(stopId, directionId)
        .then(response => setDepartures(response))
        .catch(() => setDError(true))
        .finally(() => setDLoading(false));
    }
  });

  return <>
    {(rLoading || sLoading || dLoading) && !(rError || sError || dError) && <div>Loading...</div>}
    {(rError || sError || dError) && <div>An unexpected error occured. Please try again later.</div>}
    {!rLoading && !sLoading && !rError && !sError &&
      <div>
        <h2>{currStop.attributes.name} to {currRoute.attributes.direction_destinations[directionId]}</h2>
        <h4>Next departures:</h4>
        <ul className='list-group'>
          {departures.map((departure) => {
            const departureDate = new Date(departure.attributes.departure_time);
            return <li className='list-group-item' key={departureDate.toISOString()}>{departureDate.getHours()}:{String(departureDate.getMinutes()).padStart(2, '0')}</li>
          })}
        </ul>
      </div>
    }
  </>;
}
export default Departures;