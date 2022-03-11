import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './Confirmation.css';

export default function Confirmation(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="invite">
      <h1>HotSpot </h1>
      <div>
        <p className="quote">"You're Signed Up For"</p>
      </div>
      <div>
      <p className="content">"Event Name / Date / Location / Party Size / Etc Will Go Here"</p> 
      </div>
      //infomation should be taken from the invite they selected. Will be stuck on this page for rest of 24 hr span.
    </div>
  );
};