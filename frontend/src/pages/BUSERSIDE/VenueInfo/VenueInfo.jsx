import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./VenueInfo.css";
import settingsimg from "/Users/ramonaflowers/hotspot/frontend/src/pages/BUSERSIDE/settings.png";

export default function VenueInfo() {
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
          <img src={settingsimg} />
        </button>
      </a>
      <div>
        <form>
          <label>
            Vibe: <input type="text" />
          </label>
          <br />
          <label>
            Age Requirement: <input type="text" />
          </label>
          <br />
          <label>
            Bar Type: <input type="text" />
          </label>
          <br />
          <label>
            Venue Image: <input type="file" />
          </label>
          <br />
        </form>
      </div>

      <button
        onClick={() => navigateToPage("/bHome")} // must remove event from list of events
        className="button1"
      >
        Delete
      </button>
      <button
        onClick={() => navigateToPage("/bHome")} //needs to prevent users from updating w/o hitting edit beyond this point
        className="button1"
      >
        Publish
      </button>
      <button
        onClick={() => navigateToPage("/bHome")} //needs to allow users to update info. MUST UPDATE
        className="button1"
      >
        Save
      </button>

      <br />
    </div>
  );
}
