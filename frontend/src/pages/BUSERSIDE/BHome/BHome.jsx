import "./BHome.css";
import img1 from "./eventpics/kindregardsparty.png";
import img2 from "./eventpics/lebainparty.png";
import img3 from "./eventpics/mcsorleysparty.png";
import img4 from "./eventpics/downtimeparty.png";
import img5 from "./eventpics/joyfaceparty.png";
import img6 from "./eventpics/georgiaroomparty.png";



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
                  src={img1}
                  class="gallery_img"
                  alt="kindregardspartys"
                />
              </a>
            </div>
            <div class="grid-item2">
              <a href="/guestList">
                <img
                  src={img2}
                  class="gallery_img"
                  alt="lebainparty"
                />
              </a>
            </div>
            <div class="grid-item3">
              <a href="/guestList">
                <img
                  src={img3}
                  class="gallery_img"
                  alt="downtimeparty"
                />
              </a>
            </div>
            <div class="grid-item4">
              <a href="/guestList">
                <img
                  src={img4}
                  class="gallery_img"
                  alt="joyfaceparty"
                />
              </a>
            </div>
            <div class="grid-item5">
              <a href="/guestList">
                <img
                  src={img5}
                  class="gallery_img"
                  alt="mcsorleysparty"
                />
              </a>
            </div>
            <div class="grid-item6">
              <a href="/guestList">
                <img
                  src={img6}
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
