import "./BHome.css";

function BHome() {
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
        <div class="event-container">
          <div class="gallery">
            <div class="grid-item1">
              <a href="/guestList">
                <img
                  src="kindregardsparty.png"
                  class="gallery_img"
                  alt="event"
                />
              </a>
            </div>
            <div class="grid-item2">
              <a href="/guestList">
                <img
                  src="lebainparty.png"
                  class="gallery_img"
                  alt="event"
                />
              </a>
            </div>
            <div class="grid-item3">
              <a href="/guestList">
                <img
                  src="downtimeparty.png"
                  class="gallery_img"
                  alt="event"
                />
              </a>
            </div>
            <div class="grid-item4">
              <a href="/guestList">
                <img
                  src="joyfaceparty.png"
                  class="gallery_img"
                  alt="event"
                />
              </a>
            </div>
            <div class="grid-item5">
              <a href="/guestList">
                <img
                  src="mcsorelysparty.png"
                  class="gallery_img"
                  alt="event"
                />
              </a>
            </div>
            <div class="grid-item6">
              <a href="/guestList">
                <img
                  src="georgiaroomparty.png"
                  class="gallery_img"
                  alt="event"
                />
              </a>
            </div>
          </div>
        </div>
      </div>
      <a href="/eventinfo">
        <button id="resButton"> CREATE </button>
      </a>
      <a href="/venueinfo">
        <button id="nextButton"> PROFILE </button>
      </a>
    </>
  );
}

export default BHome;
