import "./GuestProfile.css";

function GuestProfile() {
  return (
    <>
      <a href="/bHome">
        <h1>HotSpot </h1>
      </a>
      <a href="/bsettings">
        <button id="settings">
          {" "}
          <img src="https://img.icons8.com/ios-filled/50/000000/settings.png" />
        </button>
      </a>
      <div>
        <div id="invite">
          <a href="/guestList">
            <img id="event" src="https://picsum.photos/1000" />
          </a>
        </div>
        <div>
          <p className="content">Name</p>
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

export default GuestProfile;
