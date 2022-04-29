import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';
//import Main from './front end/src/components/Main.jsx';

import './Csideeventinfo.css';

export default function EventInfo(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <a href = '/cHome'><h1>HotSpot </h1></a>
                  <a href = '/bsettings'>
            <button id= "settings"> <img src="https://img.icons8.com/nolan/64/apple-settings.png"/></button>
            </a>
      <div>
          <p>
            Location: <input type="text" /> 
          </p>
          <br />
          <p>
            Date: <input type="text" />
            </p>
          <br />
          <p>
            Time: <input type="text" />
            </p>
          <br />
          <p>
            Max Guests Allowed: <input type="text" />
            </p>
          <br />
          <p>
            General Description: <input type="text" />
            </p>
          <p>
            File Upload: <input type= "file"/>
            </p>
          <br />

      </div>
    </div>
  );
};