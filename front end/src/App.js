import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Login from './pages/Login/Login';
import CreateAcc from './pages/CreateAcc/CreateAcc';
import CHome from './pages/CUSERSIDE/CHOME/CHOME';
import Users from './pages/Users/Users';
import RSVP from './pages/CUSERSIDE/RSVP/RSVP';
import Cuserprofile from './pages/CUSERSIDE/Cuserprofile/Cuserprofile';
import Confirmation from './pages/CUSERSIDE/Confirmation/Confirmation';
import EventInfo from './pages/BUSERSIDE/EventInfo/EventInfo';
import VenueProfile from './pages/CUSERSIDE/VenueProfile/VenueProfile';

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
            <Route exact={true} path={'/chome'}>
              <CHome />
            </Route>
            <Route exact={true} path={'/createacc'}>
              <CreateAcc />
            </Route>
            <Route exact={true} path={'/users'}>
              <Users />
            </Route>
            <Route exact={true} path={'/RSVP'}>
              <RSVP />
            </Route>
            <Route exact={true} path={'/Cuserprofile'}>
              <Cuserprofile />
            </Route>
            <Route exact={true} path={'/Confirmation'}>
              <Confirmation />
            </Route>
            <Route exact={true} path={'/EventInfo'}>
              <EventInfo />
            </Route>
            <Route exact={true} path={'/VenueProfile'}>
              <VenueProfile />
            </Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
