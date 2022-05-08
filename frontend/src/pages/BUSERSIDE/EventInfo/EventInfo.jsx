import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
//import Main from './front end/src/components/Main.jsx';

import "./EventInfo.css";

export default function EventInfo() {
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <a href="/cHome">
        <h1>HotSpot </h1>
      </a>
      <a href="/bsettings">
        <button id="settings">
          {" "}
          <img src="https://img.icons8.com/nolan/64/apple-settings.png" />
        </button>
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
          <label>
            File Upload: <input type="file" />
          </label>
          <br />
        </form>
      </div>

      <button
        onClick={() => navigateToPage("/bHome")} // must remove event from list of events
        className="page-button"
      >
        Delete
      </button>
      <button
        onClick={() => navigateToPage("/bHome")} //needs to prevent users from updating w/o hitting edit beyond this point
        className="page-button"
      >
        Publish
      </button>
      <button
        onClick={() => navigateToPage("/bHome")} //needs to allow users to update info. MUST UPDATE
        className="page-button"
      >
        Save
      </button>
    </div>
  );
}
