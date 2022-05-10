import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./BSettings.css";

export default function BSettings() {
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <a href="/bHome">
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
            Change Password: <input type="text" />
          </label>
          <br />
        </form>
      </div>

      <button
        onClick={() => navigateToPage("/bHome")} // must remove event from list of events
        className="page-button"
      >
        Back
      </button>
    </div>
  );
}
