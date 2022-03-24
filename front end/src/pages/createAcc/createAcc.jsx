import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './createAcc.css';

export default function CreateAcc(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="login">
      <h1>Create an Account </h1>
      <div>
        <form>
          <label>
            Username: <input type="text" />
          </label>
          <br />
          <label>
            Password: <input type="text" />
          </label>
          <br />
          <label>
            First Name: <input type="text" />
          </label>
          <br />
          <label>
            Last Name: <input type="text" />
          </label>
          <br />
          <label>
            Date of Birth (MM/DD/YYYY): <input type="text" />
          </label>
          <br />
          <label>
            Email: <input type="text" />
          </label>
          <br />
          <label>
            Phone Number: <input type="text" />
          </label>
          <br />
          <label>
            Type of Account: 
            <select id="dropdown" >
            <option >Select...</option>
            <option value="Customer">Customer</option>
            <option value="Business">Business</option> //next need to handle the value and pass it
          </select>
          </label>
        </form>

      </div>
      
      <button
        onClick={() => navigateToPage('/home')} //need to decide on page after login
        className="page-button"
      >
        Create
      </button>
    </div>
  );
};

