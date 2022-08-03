import React from "react";
import { Link } from "react-router-dom";

const StopListItem = ({
  stop = {
    "attributes": {
      "address": "Heath St and South Huntington Ave, Boston, MA",
      "at_street": null,
      "description": null,
      "latitude": 42.328316,
      "location_type": 1,
      "longitude": -71.110252,
      "municipality": "Boston",
      "name": "Heath Street",
      "on_street": null,
      "platform_code": null,
      "platform_name": null,
      "vehicle_type": null,
      "wheelchair_boarding": 1
    },
    "id": "place-hsmnl",
    "links": {
      "self": "/stops/place-hsmnl"
    },
    "relationships": {
      "facilities": {
        "links": {
          "related": "/facilities/?filter[stop]=place-hsmnl"
        }
      },
      "parent_station": {
        "data": null
      },
      "zone": {
        "data": null
      }
    },
    "type": "stop"
  }, directionId
}) => {
  return <Link className="text-decoration-none" to={`${stop.id}/${directionId}`}>
    <li className="list-group-item list-group-item-action">
      <div>
        {stop.attributes.name}
      </div>
    </li>
  </Link>
}
export default StopListItem;