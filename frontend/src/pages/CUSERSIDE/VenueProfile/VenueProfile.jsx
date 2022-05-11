import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./VenueProfile.css";
import "./venpics/kindregards.jpeg"


export default function VenueProfile() {
  const history = useHistory();
  const [newVenueProfile, setVenueProfile] = useState(undefined);

  useEffect(() => {
    axios.get('https://teamhotspot.herokuapp.com/VenueProfile/bQuota')
      .then((response) => {
        if (response.data) {
          setUsers(response.data);
        }
      })
      .catch(error => {
        setError(error);
        console.log(error);
      });
  }, [refresh])

  const handleBquota = () => {
    axios.post(`https://teamhotspot.herokuapp.com/VenueProfile/bQuota`)
      .then(() => {
        setIsModalOpen(false);
        setRefresh(refresh + 1);
      })
      .catch(error => {
        setError(error);
        console.log(error);
      })
  }

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <a href="/chome">
        <h1>HotSpot </h1>
      </a>
      <a href="/csettings">
        <button id="settings">
          {" "}
          <img src="https://img.icons8.com/nolan/64/apple-settings.png" />
        </button>
      </a>
      <div id="venue">
        <a href="/venueProfile">
          <img id="example" src="kindregards.jpeg" />
        </a>
      </div>
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
        onClick={() => navigateToPage("/bSettings")}
        className="page-button"
      >
        Return
      </button>
      <button
        onClick={handleBquota}
        className="page-button"
      >
        Update Quota
      </button>
    </div>
  );
}
