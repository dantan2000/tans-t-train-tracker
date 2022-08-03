import { Link } from "react-router-dom";

const RouteListItem = ({
  route = {
    "attributes": {
      "color": "DA291C",
      "description": "Rapid Transit",
      "direction_destinations": [
        "Ashmont/Braintree",
        "Alewife"
      ],
      "direction_names": [
        "South",
        "North"
      ],
      "fare_class": "Rapid Transit",
      "long_name": "Red Line",
      "short_name": "",
      "sort_order": 10010,
      "text_color": "FFFFFF",
      "type": 1
    },
    "id": "Red",
    "links": {
      "self": "/routes/Red"
    },
    "relationships": {
      "line": {
        "data": {
          "id": "line-Red",
          "type": "line"
        }
      }
    },
    "type": "route"
  }
}) => {
  return (
    <Link className="text-decoration-none" to={`${route.id}`}>
      <li className="list-group-item list-group-item-action">
        <div>
          {route.attributes.long_name}
        </div>
      </li>
    </Link>
  )
}
export default RouteListItem;