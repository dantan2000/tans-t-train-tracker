import React from "react";
import RouteListItem from "./RouteListItem";

const RouteList = ({ routes, rError, rLoading}) => {
  return (
    <>
      {rLoading && <div>Loading...</div>}
      {!rError && !rLoading &&
        <ul className="list-group">
          {
            routes.map(route =>
              <RouteListItem route={route} key={route.id}/>)
          }
        </ul>
      }
      {rError && !rLoading && <div>An unexpected error occured. Please try again later.</div>}
    </>
  )
}

export default RouteList;