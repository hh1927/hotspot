import "./GuestList.css";

function GuestList() {
  return (
    <>
      <a href="/bHome">
        <h1>HotSpot </h1>
      </a>
      <div>
        <div class="guestlist-container">
          <a href="/guestprofile">
            <img src="ally.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="brandon.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="riley.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="marie.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="hannah.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="donovan.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="isaac.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="lucas.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="julianna.png" alt="guestpropic" />
          </a>
          <a href="/guestprofile">
            <img src="ava.png" alt="guestpropic" />
          </a>
        </div>
      </div>
      <a href="/eventInfo">
        <button id="resButton"> VIEW EVENT </button>
      </a>
      <a href="/venueInfo">
        <button id="nextButton"> VIEW VENUE </button>
      </a>
    </>
  );
}

export default GuestList;
