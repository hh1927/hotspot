import React from 'react';
import {useHistory} from 'react-router-dom';

export default function Home(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <h1>HotSpot </h1>
      <div>
        <p className="quote">"Events for tonight and only tonight."</p>
      </div>
      <div>
        <form>
          <label>
            Username: <input type="text" />
          </label>
          <br />
          <label>
            Password: <input type="text" />
          </label>
        </form>

      </div>
      
      <button
        onClick={() => navigateToPage('/homepage')} //need to decide on page after login
        className="page-button"
      >
        Login
      </button>
      <button
        onClick={() => navigateToPage('/CreateAcc')} //need to talk to backend for create account page
        className="page-button"
      >
        Create Account
      </button>
    </div>
  );
};

