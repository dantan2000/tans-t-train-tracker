import { GET_ROUTES, GET_STOPS, GET_DEPARTURE_TIMES }
from "../actions/mbta-actions";

const routesReducer = (state = [], action) => {
  switch (action.type) {
    case GET_ROUTES:
      return [
        ...state,
        action.routes
      ];
    default:
      return state;
  }
}

export default routesReducer;