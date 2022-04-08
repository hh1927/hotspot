import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Login from './pages/Login/Login';
import CreateAcc from './pages/CreateAcc/CreateAcc';
import CHome from './pages/CUSERSIDE/CHome/CHome';
import Users from './pages/Users/Users';
import RSVP from './pages/CUSERSIDE/RSVP/RSVP';
import Cuserprofile from './pages/CUSERSIDE/Cuserprofile/Cuserprofile';
import Confirmation from './pages/CUSERSIDE/Confirmation/Confirmation';
import EventInfo from './pages/BUSERSIDE/EventInfo/EventInfo';
import VenueProfile from './pages/CUSERSIDE/VenueProfile/VenueProfile';
import BHome from './pages/BUSERSIDE/BHome/BHome';
import BSettings from './pages/BUSERSIDE/BSettings/BSettings';
import VenueInfo from './pages/BUSERSIDE/VenueInfo/VenueInfo';
import GuestList from './pages/BUSERSIDE/GuestList/GuestList';
import GuestProfile from './pages/BUSERSIDE/GuestList/GuestProfile';

import './App.css';

function App() {
  return (
    <div className="root">
      <div className="content"
      span className="font-link">
        <Router>
          <Switch>
            <Route exact={true} path={'/'}>
              <Login />
            </Route>
            <Route exact={true} path={'/cHome'}>
              <CHome />
            </Route>
            <Route exact={true} path={'/bHome'}>
              <BHome />
            </Route>
            <Route exact={true} path={'/bSettings'}>
              <BSettings />
            </Route>
            <Route exact={true} path={'/createAcc'}>
              <CreateAcc />
            </Route>
            <Route exact={true} path={'/users'}>
              <Users />
            </Route>
            <Route exact={true} path={'/rSVP'}>
              <RSVP />
            </Route>
            <Route exact={true} path={'/cuserprofile'}>
              <Cuserprofile />
            </Route>
            <Route exact={true} path={'/confirmation'}>
              <Confirmation />
            </Route>
            <Route exact={true} path={'/eventInfo'}>
              <EventInfo />
            </Route>
            <Route exact={true} path={'/venueInfo'}>
              <VenueInfo />
            </Route>
            <Route exact={true} path={'/venueProfile'}>
              <VenueProfile />
            </Route>
            <Route exact={true} path={'/guestList'}>
              <GuestList />
            </Route>
            <Route exact={true} path={'/guestProfile'}>
              <GuestProfile />
            </Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
