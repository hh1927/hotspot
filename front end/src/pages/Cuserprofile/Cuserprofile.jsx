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
      <div>
        <form>
          <label>
            Location: <input type="text" /> 
          </label> //need to find way to get current location
          <br />
          <label>
            Bar Type <input type="text" />
          </label> //need to imput method where cuser can add photos
        </form>

      </div>
      
      <button
        onClick={() => navigateToPage('/home')} //need to return to homepage to scroll
        className="page-button"
      >
        RSVP
      </button>
    </div>
  );
};