import React, { useEffect, useState } from "react";
import { getRoutes } from "../../services/mbta-services"

import RouteList from "./RouteList";

const Routes = () => {
  // Whether the list of routes is loading
  const [rLoading, setRLoading] = useState(true);
  // Whether an error occurred loading the list of routes
  const [rError, setRError] = useState(false)
  // State variable for the list of routes
  const [routes, setRoutes] = useState([]);

  // Initialize state variables
  useEffect(() => {
    // Check if routes is empty and no error has occurred
    if (routes.length == 0 && !rError) {
      getRoutes()
        .then(response => setRoutes(response)) // Update routes with response
        .catch(() => setRError(true)) // Set error state on error
        .finally(() => setRLoading(false)); // Set loading state to false
    }
  }, [])

  return (
    <>
      <div>
        <h2 className='my-4'>Select a Route:</h2>
        <RouteList routes={routes} rError={rError} rLoading={rLoading}/>
      </div>
    </>
  );
}
export default Routes;