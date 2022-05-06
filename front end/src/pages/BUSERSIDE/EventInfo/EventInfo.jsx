import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './EventInfo.css';

export default function EventInfo(){
  const [EventInfo, setEventInfo] = useState(undefined);
  const [error, setError] = useState(undefined);
  const [details, setDetails] = useState({business_name: '',eventName: '',location: '',price: '',hours: ''});

  const [refresh, setRefresh] = useState(0);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newEvent, setNewEvent] = useState('');
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  useEffect(() => {
    axios.get('https://teamhotspot.herokuapp.com/busers/eventInfo')
      .then((response) => {
        if (response.data){
          setNewEvent(response.data);
        }
      })
      .catch(error => {
        setError(error);
        console.log(error);
      });
  }, [refresh])

  const handleEventInfo = () => {
    axios.post(`https://teamhotspot.herokuapp.com/busers/eventInfo/${business_name}/${eventName}/${location}/${price}/${hours}`)
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
        <div className="Update Event Info">
              <button className="button" onClick={handleEventInfo}>Taking event info</button>
              <button className="button" onClick={() => setIsModalOpen(false)}> Cancel </button>
          </div>

      </div>
      
      <button
        onClick={() => navigateToPage('/bHome')} // must remove event from list of events
        className="page-button"
      >
        Delete
      </button>
      <button
        onClick={handleEventInfo}
        //onClick={() => navigateToPage('/bHome')} //needs to prevent users from updating w/o hitting edit beyond this point
        className="page-button"
      >
        Publish
      </button>
      <button
        onClick={() => navigateToPage('/bHome')} //needs to allow users to update info. MUST UPDATE
        className="page-button"
      >
        Save
      </button>
    </div>
  );
};