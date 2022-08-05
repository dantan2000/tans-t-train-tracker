import { GET_STOPS }
from "../actions/mbta-actions";

const stopsReducer = (state = [], action) => {
  switch (action.type) {
    case GET_STOPS:
      return [
        ...state,
        action.stops
      ];
    default:
      return state;
  }
}

export default stopsReducer;