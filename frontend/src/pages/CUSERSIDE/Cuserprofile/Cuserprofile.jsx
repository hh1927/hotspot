import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./Cuserprofile.css";
import settingsimg from "/Users/ramonaflowers/hotspot/frontend/src/pages/BUSERSIDE/settings.png";

export default function Cuserprofile() {
  const [neighborhood, setNeighborhood] = useState("")
  const [interest, setInterest] = useState("")
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
          <img src={settingsimg} />
        </button>
      </a>
      <div>
        <form>

          <label>
            Profile Picture: <input type="file" />
          </label>
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
            value = {neighborhood}
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
              <option value="Live Music">Live Music</option>
              <option value="LGBTQ">LGBTQ</option>
            </select>
            value = {interest}
          </label>
          <br />
          <label>
            Vibe:
            <select id="dropdown">
              <option>Select...</option>
              <option value="Grunge">Grunge</option>
              <option value="Chill">Chill</option>
              <option value="Romantic">Romantic</option>
              <option value="High Concept">High Concept</option>
              <option value="College">College</option>
              <option value="Exclusive">Exclusive</option>
              <option value="Popular">Popular</option>
            </select>
          </label>
        </form>
      </div>

      <button
        onClick={() => navigateToPage("/cHome")} //need to return to homepage to scroll
        className="button1"
      >
        Return
      </button>
    </div>
  );
}
