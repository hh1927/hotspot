
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';
import ('./CreateAcc.css');

//const baseURL = //api location here

export default function CreateAcc(){
  /*
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  const[post, setPost] = React.useState({
    user: '',
    password: '',
    firstname: '',
    lastname: '',
    dob: '',
    email: '',
    phone: '',
    type: ''
  });
   
  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setPost(response.data);
    });
  });

  function createAccount(){
    axios.post(baseURL, {
      user,
      password,
      firstname,
      lastname,
      dob,
      email,
      phone,
      type

    }).then((response) => {
      setPost(response.data)
    })
  }
*/

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
            <option value="Business">Business</option>
          </select>
          </label>
        </form>

      </div>
      
      <button
        onClick={() => window.location.href='/cHome'} //need to decide on page after login
        className="page-button"
      >
        Create Personal
      </button>
      <button
        onClick={() => window.location.href='/bHome'} //need to decide on page after login
        className="page-button"
      >
        Create Business
      </button>
    </div>
  );
};

