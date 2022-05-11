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
          <img src="https://img.icons8.com/nolan/64/apple-settings.png" />
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
        <button
          onClick={() => navigateToPage("/guestList")}
          className="button1"
        >
          Return
        </button>
      </div>
    </>
  );
}

export default GuestProfile;
