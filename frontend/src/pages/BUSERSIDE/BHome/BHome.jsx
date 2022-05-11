import "./BHome.css";
import "./eventpics/kindregardsparty.png";
import "./eventpics/lebainparty.png";
import "./eventpics/mcsorleysparty.png";
import "./eventpics/downtimeparty.png";
import "./eventpics/joyfaceparty.png";
import "./eventpics/georgiaroomparty.png";



function BHome() {
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
        <div class="event-container">
          <div class="gallery">
            <div class="grid-item1">
              <a href="/guestList">
                <img
                  src="kindregardsparty.png"
                  class="gallery_img"
                  alt="kindregardsparty"
                />
              </a>
            </div>
            <div class="grid-item2">
              <a href="/guestList">
                <img
                  src="lebainparty.png"
                  class="gallery_img"
                  alt="lebainparty"
                />
              </a>
            </div>
            <div class="grid-item3">
              <a href="/guestList">
                <img
                  src="downtimeparty.png"
                  class="gallery_img"
                  alt="downtimeparty"
                />
              </a>
            </div>
            <div class="grid-item4">
              <a href="/guestList">
                <img
                  src="joyfaceparty.png"
                  class="gallery_img"
                  alt="joyfaceparty"
                />
              </a>
            </div>
            <div class="grid-item5">
              <a href="/guestList">
                <img
                  src="mcsorleysparty.png"
                  class="gallery_img"
                  alt="mcsorleysparty"
                />
              </a>
            </div>
            <div class="grid-item6">
              <a href="/guestList">
                <img
                  src="georgiaroomparty.png"
                  class="gallery_img"
                  alt="georgiaroomparty"
                />
              </a>
            </div>
          </div>
        </div>
      </div>
      <a href="/eventinfo">
        <button id="resButton" className="button1"> CREATE </button>
      </a>
      <a href="/venueinfo">
        <button id="nextButton" className="button1"> PROFILE </button>
      </a>
    </>
  );
}

export default BHome;
