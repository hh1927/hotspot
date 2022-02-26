import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Home from './pages/Home/Home';
import Create from './pages/CreateAcc/CreateAcc';
import Users from './pages/Users/Users';
import Users from './pages/RSVP/RSVP';

import './App.css';

function App() {
  return (
    <div className="root">
      <div className="content">
        <Router>
          <Switch>
            <Route exact={true} path={'/'}>
              <Home />
            </Route>
            <Route exact={true} path={'/createAcc'}>
              <Create />
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
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
