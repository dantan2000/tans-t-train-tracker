import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getStops, getRouteById } from "../../services/mbta-services"

import StopList from "./StopList";

const Stops = () => {

  const { routeId } = useParams();

  // Whether the list of routes is loading
  const [rLoading, setRLoading] = useState(true);
  // Whether an error occurred loading the list of routes
  const [rError, setRError] = useState(false)
  // State variable for the list of routes
  const [currRoute, setCurrRoute] = useState(null);

  // Initialize route state variables
  useEffect(() => {
    // Check if routes is empty and no error has occurred
    if (currRoute == null && !rError) {
      getRouteById(routeId)
        .then(response => setCurrRoute(response[0])) // Update route with response
        .catch(() => setRError(true)) // Set error state on error
        .finally(() => setRLoading(false)); // Set loading state to false
    }
  }, [])


  // Whether the list of stops is loading
  const [sLoading, setSLoading] = useState(true);
  // Whether an error occurred loading the list of stops
  const [sError, setSError] = useState(false)
  // State variable for the list of stops
  const [stops, setStops] = useState([]);

  const [directionId, setDirectionId] = useState(0);

  // Initialize stop state variables
  useEffect(() => {
    if (stops.length == 0 && !sError) {
      getStops(routeId)
        .then(response => setStops(response))
        .catch(() => setSError(true))
        .finally(() => setSLoading(false));
    }
  }, []);

  // Event listener for direction selection
  const updateDirectionId = (e) => {
    setDirectionId(e.target.value);
  }

  return (
    <>
      {(rLoading || sLoading) && !(rError || sError) && <div>Loading...</div>}
      {(rError || sError) && <div>An unexpected error occured. Please try again later.</div>}
      {!rLoading && !sLoading && !rError && !sError &&
        <div>
          <div className='my-4 row'>
            <h2 className='col'>Select a Stop:</h2>
              <div class='form-group col'>
                <label for='direction'>Destination</label>
                <select
                  className='form-select'
                  id='direction'
                  onChange={updateDirectionId}
                >
                  {currRoute.attributes.direction_destinations.map((destination, i) => <option value={i}>{destination}</option>)}
                </select>
              </div>
          </div>
          <StopList stops={stops} sError={sError} sLoading={sLoading} directionId={directionId} />
        </div>
      }
    </>
  );
}
export default Stops;