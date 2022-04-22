import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './Cuserprofile.css';

export default function Cuserprofile(){
   const [Cuserprofile, setCuserprofile] = useState(undefined);
   const [error, setError] = useState(undefined);

   const [refresh, setRefresh] = useState(0);

   const [isModalOpen, setIsModalOpen] = useState(false);
   const [newEvent, setNewEvent] = useState('');
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }
  
  useEffect(() => {
     axios.get('https://teamhotspot.herokuapp.com/cUsers')
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
     axios.post(`https://demo-repo23.herokuapp.com/cUsers/${user_name}/${age}/${interests}/${neighborhoods}`)
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
