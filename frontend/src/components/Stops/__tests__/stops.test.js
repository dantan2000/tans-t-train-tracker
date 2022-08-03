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
jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useParams: jest.fn(),
}));


describe('List of T Stops', () => {
  beforeEach(() => {
    services.getStops.mockReset();
    services.getRouteById.mockReset();
    jest.spyOn(Router, 'useParams').mockReturnValue({routeId: routeId});
  });
  it('should properly retrieve and display the list of Stops', async () => {
    // Mock successful Stops Data
    services.getStops.mockResolvedValueOnce(testdata.stopsData);
    services.getRouteById.mockResolvedValueOnce(testdata.routesData);
    render(<Router.BrowserRouter><Stops /></Router.BrowserRouter>);

    // Await component update
    await waitForElementToBeRemoved(() => screen.queryByText(/loading/i));

    // Assert proper services calls
    expect(services.getStops).toBeCalledTimes(1);
    expect(services.getStops).toBeCalledWith(routeId);
    expect(services.getRouteById).toBeCalledWith(routeId)
    // Map over routes data to make sure each stop is displayed properly
    testdata.stopsData.map((stop) => {
      const listElement = screen.getByText(stop.attributes.name);
      expect(listElement).toBeInTheDocument();
    });
  });
  it('should properly display an error message', async () => {
    // Mock error
    services.getStops.mockRejectedValue(new Error());
    services.getRouteById.mockResolvedValueOnce(testdata.routesData);
    render(<Router.BrowserRouter><Stops /></Router.BrowserRouter>);

    // Await component update
    await waitForElementToBeRemoved(() => screen.queryByText(/loading/i))

    // Expect service call
    expect(services.getStops).toBeCalledTimes(1);
    expect(screen.queryByText(/error/i)).toBeInTheDocument();
  });
});