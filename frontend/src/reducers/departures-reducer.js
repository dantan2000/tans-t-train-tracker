import { GET_DEPARTURE_TIMES }
from "../actions/mbta-actions";

const departuresReducer = (state = [], action) => {
  switch (action.type) {
    case GET_DEPARTURE_TIMES:
      return [
        ...state,
        action.departures
      ];
    default:
      return state;
  }
}

export default departuresReducer;