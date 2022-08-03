import React from "react";
import StopListItem from "./StopListItem";

const StopList = ({ stops, sError, sLoading, directionId }) => {
  return (
    <>
      {sLoading && <div>Loading...</div>}
      {!sError && !sLoading &&
        <ul className="list-group">
          {
            stops.map(stop =>
              <StopListItem
                stop={stop}
                directionId={directionId} />)
          }
        </ul>
      }
      {sError && !sLoading && <div>An unexpected error occured. Please try again later.</div>}
    </>
  )
}

export default StopList;