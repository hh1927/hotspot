import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './Cuserprofile.css';

export default function Cuserprofile(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <a href = '/cHome'><h1>HotSpot </h1></a>
      <a href = '/bsettings'>
            <button id= "settings"> icon here</button>
            </a>
      <div>
        <form>
          <label>
            Location: <input type="text" /> 
          </label> 
          <br />
          <label>
            Bar Type <input type="text" />
          </label> 
        </form>

      </div>
      
      <button
        onClick={() => navigateToPage('/cHome')} //need to return to homepage to scroll
        className="page-button"
      >
        Return
      </button>
    </div>
  );
};