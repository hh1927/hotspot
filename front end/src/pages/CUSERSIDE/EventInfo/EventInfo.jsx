import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './EventInfo.css';

export default function EventInfo(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <div> //need ability to add photos
        <form>
          <label>
            Location: <input type="text" /> 
          </label> //need to establish a drop down to create form for that # of guests
          <br />
          <label>
            Date: <input type="text" />
          </label>
          <br />
          <label>
            Time: <input type="text" />
          </label>
          <br />
          <label>
            Max Guests Allowed: <input type="text" />
          </label>
          <br />
          <label>
            General Description: <input type="text" />
          </label>
          <br />
        </form>

      </div>
      
      <button
        onClick={() => navigateToPage('/chome')} // must remove event from list of events
        className="page-button"
      >
        Delete
      </button>
      <button
        onClick={() => navigateToPage('/chome')} //needs to prevent users from updating w/o hitting edit beyond this point
        className="page-button"
      >
        Publish
      </button>
      <button
        onClick={() => navigateToPage('/chome')} //needs to allow users to update info. MUST UPDATE
        className="page-button"
      >
        Edit
      </button>
    </div>
  );
};