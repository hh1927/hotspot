import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './VenueProfile.css';

export default function VenueProfile(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <a href = '/chome'><h1>HotSpot </h1></a>
      <a href = '/bsettings'>
            <button id= "settings"> icon here</button>
            </a>
      <div>
        <p className="content">Event Name</p>
        <p className="content">Time</p>
        <p className="content">Location</p>
        <p className="content">Max Guests Allowed</p>
        <p className="content">Type</p>
        <p className="content">Vibe</p>
        <p className="content">Party Description</p>
      </div>
      <button
        onClick={() => navigateToPage('/bSettings')}
        className="page-button"
      >
        Return
      </button>
    </div>
  );
};