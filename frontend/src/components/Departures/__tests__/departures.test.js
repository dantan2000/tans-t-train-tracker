import React from 'react'
import Stops from '../'
import * as services from '../../../services/mbta-services'
import * as testdata from '../../../test_data/test_data'
import { render, screen, waitForElementToBeRemoved } from '@testing-library/react';
import Router from 'react-router-dom';
import { nanoid } from 'nanoid';

jest.mock('../../../services/mbta-services');

// Mock useParams for URL parameters
const routeId = nanoid();
const stopId = nanoid();
const directionId = nanoid();
jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useParams: jest.fn(),
}));


describe('List of T Stops', () => {
  beforeEach(() => {
    services.getStopById.mockReset();
    services.getRouteById.mockReset();
    services.getDepartureTimes.mockReset();
    jest.spyOn(Router, 'useParams').mockReturnValue({routeId: routeId, stopId: stopId, directionId: directionId});
  });
  it('should properly retrieve and display the list of Stops', async () => {
    // Mock successful Data
    services.getStopById.mockResolvedValueOnce(testdata.stopsData);
    services.getRouteById.mockResolvedValueOnce(testdata.routesData);
    services.getDepartureTimes.mockResolvedValueOnce(testdata.predictionsData);
    render(<Router.BrowserRouter><Stops /></Router.BrowserRouter>);
    
    // Await component update
    await waitForElementToBeRemoved(() => screen.queryByText(/loading/i));

    // Assert proper services calls
    expect(services.getStopById).toBeCalledWith(stopId);
    expect(services.getRouteById).toBeCalledWith(routeId);
    expect(services.getDepartureTimes).toBeCalledWith(stopId, directionId);
    
    // Map over routes data to make sure each time is displayed properly
    testdata.predictionsData.map((prediction) => {
      const date = new Date(prediction.attributes.departure_time);
      const dateStr = date.getHours() + ':' + String(date.getMinutes()).padStart(2, '0');
      const listElement = screen.getByText(dateStr);
      expect(listElement).toBeInTheDocument();
    });
  });
  it('should properly display an error message', async () => {
    // Mock error
    services.getDepartureTimes.mockRejectedValue(new Error());
    services.getStopById.mockResolvedValueOnce(testdata.stopsData);
    services.getRouteById.mockResolvedValueOnce(testdata.routesData);
    render(<Router.BrowserRouter><Stops /></Router.BrowserRouter>);

    // Await component update
    await waitForElementToBeRemoved(() => screen.queryByText(/loading/i))

    // Expect service call
    expect(services.getDepartureTimes).toBeCalledTimes(1);

    // Expect error message
    expect(screen.queryByText(/error/i)).toBeInTheDocument();
  });
});