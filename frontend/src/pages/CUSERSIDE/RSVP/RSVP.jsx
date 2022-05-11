import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./RSVP.css";

export default function RSVP() {
  const [RSVP, setRSVP] = useState(undefined);
  const [error, setError] = useState(undefined);
  const [refresh, setRefresh] = useState(0);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newEvent, setNewEvent] = useState('');
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  useEffect(() => {
    axios.get('https://teamhotspot.herokuapp.com/cList')
      .then((response) => {
        if (response.data) {
          setNewEvent(response.data);
        }
      })
      .catch(error => {
        setError(error);
        console.log(error);
      });
  }, [refresh])

  const handlePartyInfo = () => {
    //Within then block add console.log to test the post request
    axios.post(`https://teamhotspot.herokuapp.com/cList/${user_name}/${party_size}`)
      .then(() => {
        setIsModalOpen(false);
        setRefresh(refresh + 1);
      })
      .catch(error => {
        setError(error);
        console.log(error);
      })
  }


  return (
    <div className="content">
      <a href="/cHome">
        <h1>HotSpot </h1>
      </a>
      <div>
        <form>
          <label>
            Number of Guests: <input type="text" />
          </label>
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
        onClick={handlePartyInfo}
        className="button2"
      >
        Party Size
      </button>
      <button
        onClick={() => navigateToPage("/confirmation")} //need to decide on page RSVP
        className="button1"
      >
        RSVP
      </button>
      <button
        onClick={() => navigateToPage("/cHome")} //returns to homepage to continue scrolling
        className="button1"
      >
        Cancel
      </button>
    </div>
  );
}
