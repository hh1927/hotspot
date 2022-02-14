import React from 'react';
import {useHistory} from 'react-router-dom';

import './createAcc.css';

export default function createAcc(){
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
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
        </form>

      </div>
      
      <button
        onClick={() => navigateToPage('/homepage')} //need to decide on page after login
        className="page-button"
      >
        Create
      </button>
    </div>
  );
};

