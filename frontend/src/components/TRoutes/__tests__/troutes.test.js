import React from 'react'
import TRoutes from '../'
import * as services from '../../../services/mbta-services'
import * as testdata from '../../../test_data/test_data'
import { render, screen, waitForElementToBeRemoved } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';

jest.mock('../../../services/mbta-services');

let container;

describe('List of T Routes', () => {
  beforeEach(() => {
    services.getRoutes.mockReset();
  });
  it('should properly retrieve and display the list of routes', async () => {
    // Mock successful routesData
    services.getRoutes.mockResolvedValueOnce(testdata.routesData);
    render(<BrowserRouter><TRoutes/></BrowserRouter>);
    // Await component update
    await waitForElementToBeRemoved(() => screen.queryByText(/loading/i))
    expect(services.getRoutes).toBeCalledTimes(1);
    // Map over routes data to make sure each route is displayed properly
    testdata.routesData.map((route) => {
      const listElement = screen.getByText(route.attributes.long_name);
      expect(listElement).toBeInTheDocument();
    });
  });
  it('should properly display an error message', async () => {
    // Mock successful routesData
    services.getRoutes.mockRejectedValue(new Error());
    render(<BrowserRouter><TRoutes/></BrowserRouter>);
    expect(services.getRoutes).toBeCalledTimes(1);
    await waitForElementToBeRemoved(() => screen.queryByText(/loading/i))
    expect(screen.queryByText(/error/i)).toBeInTheDocument();
  });
});