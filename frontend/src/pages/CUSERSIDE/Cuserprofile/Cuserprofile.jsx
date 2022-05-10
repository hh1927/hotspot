import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./Cuserprofile.css";

export default function Cuserprofile() {
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
          <img src="https://img.icons8.com/nolan/64/apple-settings.png" />
        </button>
      </a>
      <div>
        <form>
          <label>
            Location:
            <select id="dropdown">
              <option>Select...</option>
              <option value="Manhattan">Manhattan</option>
              <option value="Brooklyn">Brooklyn</option>
              <option value="Queens">Queens</option>
              <option value="Bronx">Bronx</option>
              <option value="Staten Island">Staten Island</option>
              <option value="Long Island">Long Island</option>
            </select>
          </label>
          <br />
          <label>
            Bar Type:
            <select id="dropdown">
              <option>Select...</option>
              <option value="Pub">Pub</option>
              <option value="Nightclub">Nightclub</option>
              <option value="Cocktail Lounge">Cocktail Lounge</option>
              <option value="Sports Bar">Sports Bar</option>
              <option value="Wine Bar">Wine Bar</option>
              <option value="Rooftop">Rooftop</option>
            </select>
          </label>
        </form>
      </div>

      <button
        onClick={() => navigateToPage("/cHome")} //need to return to homepage to scroll
        className="page-button"
      >
        Return
      </button>
    </div>
  );
}
