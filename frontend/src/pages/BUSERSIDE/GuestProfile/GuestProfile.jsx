import "./GuestProfile.css";
import ally from "./ally.png";
import settingsimg from "/Users/ramonaflowers/hotspot/frontend/src/pages/BUSERSIDE/settings.png";

function GuestProfile() {
  return (
    <>
      <a href="/bHome">
        <h1>HotSpot </h1>
      </a>

      <div>
        <div id="invite">
          <a href="/guestList">
            <img id="event" src={ally} />
          </a>
        </div>
        <div>
          <p className="content">Name </p>
          <p className="content">Age</p>
          <p className="content">Number of Guests</p>
        </div>
        <a href="/guestList">
          <button
            className="button1"
          >
            Return
          </button>
        </a>
      </div>
    </>
  );
}
//<a href="/bsettings">
//<button id="settings">
//  {" "}
//  <img src={settingsimg} />
//</button>
//</a>

export default GuestProfile;
