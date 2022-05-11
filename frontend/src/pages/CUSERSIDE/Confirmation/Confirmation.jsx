import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";

import "./Confirmation.css";

export default function Confirmation() {
  const history = useHistory();

  function navigateToPage(path) {
    history.push(path);
  }

  return (
    <div className="invite">

      <h1>HotSpot </h1>


      <div>
        <p className="quote">"You're Signed Up For"</p>
      </div>
      <div>
        <div id="invite">
          <img src="https://picsum.photos/1000" />
        </div>
      </div>

      <div>
        <p> Share Invites with Other Guests</p>
        <form>
          <label>
            Name: <input type="text" />
          </label>
          <br />
          <label>
            Phone: <input type="text" />
          </label>
          <br />
          <label>
            Message: <input type="text" />
          </label>
          <br />
        </form>

        <button
          onClick={() => navigateToPage("/cHome")} // must route to function
          className="button1"
        >
          Share
        </button>
      </div>
      <div>
        <p className="content">
          "Event Name / Date / Location / Party Size / Etc Will Go Here"
        </p>
        <p className="content">"Content Wont Disapear for 24 hours"</p>
      </div>
    </div>
  );
}
