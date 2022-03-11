import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './RSVP.css';

export default function RSVP(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <div>
        <form>
          <label>
            Number of Guests: <input type="text" /> 
          </label> //need to establish a drop down to create form for that # of guests
          <br />
          <label>
            Name of Guest: <input type="text" />
          </label>
          <br />
          <label>
            Date of Birth (MM/DD/YYYY): <input type="text" />
          </label>
          <br />
          <label>
            Phone Number: <input type="text" />
          </label>
          <br />
        </form>

      </div>
      
      <button
        onClick={() => navigateToPage('/homepage')} //need to decide on page RSVP
        className="page-button"
      >
        RSVP
      </button>
      <button
        onClick={() => navigateToPage('/homepage')} //returns to homepage to continue scrolling
        className="page-button"
      >
        Cancel
      </button>
    </div>
  );
};
