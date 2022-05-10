import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./CSettings.css";

export default function BSettings() {
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="content">
      <a href="/cHome">
        <h1>HotSpot </h1>
      </a>
      <a href="/csettings">
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
        onClick={() => navigateToPage("/cHome")} // must remove event from list of events
        className="page-button"
      >
        Back
      </button>
    </div>
  );
}
