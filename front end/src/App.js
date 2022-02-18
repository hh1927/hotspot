import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Home from './pages/Home/Home';
import Create from './pages/createAcc/createAcc';
import Users from './pages/Users/Users';

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
              <createAcc />
            </Route>
            <Route exact={true} path={'/users'}>
              <Users />
            </Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
