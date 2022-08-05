import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Departures from './components/Departures';
import NotFound from './components/NotFound';
import Stops from './components/Stops'
import TRoutes from './components/TRoutes'

function App() {
  return <>
    <BrowserRouter>
      <div className="container">
          <Routes>
            <Route path='/' exact={true} element={<TRoutes/>}/>
            <Route path='/:routeId' element={<Stops/>}/>
            <Route path='/:routeId/:stopId/:directionId' element={<Departures/>}/>
            <Route path='*' element={<NotFound/>}/>
          </Routes>
        </div>
    </BrowserRouter>
  </>;
}

export default App;
