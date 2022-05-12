import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./VenueProfile.css";
import kindregards from "./venpics/kindregards.jpeg";
import lebain from "./venpics/lebain.jpg";
import mcsorleys from "./venpics/mcsorleys.jpeg";
import downtime from "./venpics/downtime.jpeg";
import joyface from "./venpics/joyface.jpeg";
import georgiaroom from "./venpics/georgiaroom.jpeg";
import settingsimg from "/Users/ramonaflowers/hotspot/frontend/src/pages/BUSERSIDE/settings.png";


export default function VenueProfile() {
  const history = useHistory();
  const [newVenueProfile, setVenueProfile] = useState(undefined);
  const [refresh, setRefresh] = useState("")
  const [users, setUsers] = useState("")

  function navigateToPage(path) {
    history.push(path);
  }
  /*
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
  */
  return (
    <div className="content">
      <a href="/chome">
        <h1>HotSpot </h1>
      </a>
      <a href="/csettings">
        <button id="settings">
          {" "}
          <img src={settingsimg} />
        </button>
      </a>
      <div id="venue">
        <a href="/venueProfile">
          <img id="example" src={georgiaroom} />
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
        className="button1"
      >
        Return
      </button>
      <button
        // onClick={()  handleBquota }
        className="button1"
      >
        Return
      </button>
    </div >
  );
}
