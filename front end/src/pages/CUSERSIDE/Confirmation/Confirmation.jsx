import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

import './Confirmation.css';

export default function Confirmation() {
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="invite">
      <a href='/cHome'><h1>HotSpot </h1></a>
      <a href='/bsettings'>
        <button id="settings"> <img src="https://img.icons8.com/nolan/64/apple-settings.png" /></button>
      </a>
      <div>
        <a href='/cuserprofile'>
          <button id="profButton"> Profile </button>
        </a>
      </div>
      <div>
        <p className="quote">"You're Signed Up For"</p>
      </div>
      <div>
        <div id="invite">
          <img src="https://picsum.photos/1000" />
        </div>
      </div>

      <div>
        <p> Share Invites with Other Guests</p>
        <form>
          <label>
            Name: <input type="text" />
          </label>
          <br />
          <label>
            Phone: <input type="text" />
          </label>
          <br />
          <label>
            Message: <input type="text" />
          </label>
          <br />
        </form>

        <button
          onClick={() => navigateToPage('/cHome')} // must route to function
          className="page-button"
        >
          Send
        </button>

      </div>
      <div>
        <p className="content">"Event Name / Date / Location / Party Size / Etc Will Go Here"</p>
        <p className="content">"Content Wont Disapear for 24 hours"</p>
      </div>
    </div>
  );
};