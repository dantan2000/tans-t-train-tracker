import React from 'react'
import * as services from '../mbta-services'
import axios from 'axios'
import { nanoid } from 'nanoid'

jest.mock('axios')

const examplePayload = nanoid();

describe('Mbta Backend Services', () => {
  beforeEach(() => {
    axios.get.mockReset();
    // Mock payload to ensure services are returning the proper data
    axios.get.mockResolvedValueOnce({data: {data: examplePayload}});
  })
  it('should get the list of routes from the backend', async () => {
    const data = await services.getRoutes();
    expect(data).toEqual(examplePayload); 
    expect(axios.get).toHaveBeenCalledWith(services.BACKEND_BASE + 'routes/');
  });
  it('should get a route based on its id from the backend', async () => {
    const exampleRouteId = nanoid();
    const data = await services.getRouteById(exampleRouteId);
    expect(data).toEqual(examplePayload); 
    expect(axios.get).toHaveBeenCalledWith(services.BACKEND_BASE + 'routes/' + exampleRouteId);
  });
  it('should get a list of stops from the backend', async () => {
    const exampleRouteId = nanoid();
    const data = await services.getStops(exampleRouteId);
    expect(data).toEqual(examplePayload); 
    expect(axios.get).toHaveBeenCalledWith(services.BACKEND_BASE + 'stops/', {params: {'filter[route]': exampleRouteId}});
  });
  it('should get a stop based on its id from the backend', async () => {
    const exampleStopId = nanoid();
    const data = await services.getStopById(exampleStopId);
    expect(data).toEqual(examplePayload); 
    expect(axios.get).toHaveBeenCalledWith(services.BACKEND_BASE + 'stops/' + exampleStopId);
  });
  it('should get a list of departure times from the backend', async () => {
    const exampleStopId = nanoid();
    const exampleDirectionId = nanoid();
    const data = await services.getDepartureTimes(exampleStopId, exampleDirectionId);
    expect(data).toEqual(examplePayload); 
    expect(axios.get).toHaveBeenCalledWith(services.BACKEND_BASE + 'departures/', {params: {'filter[stop]': exampleStopId, 'filter[direction_id]': exampleDirectionId}});
  });
});