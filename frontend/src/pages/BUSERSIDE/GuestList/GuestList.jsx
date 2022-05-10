import "./GuestList.css";
import ally from "./propics/ally.png";
import brandon from "./propics/brandon.png";
import riley from "./propics/riley.png";
import marie from "./propics/marie.png";
import hannah from "./propics/hannah.png";
import donovan from "./propics/donovan.png";
import isaac from "./propics/isaac.png";
import lucas from "./propics/lucas.png";
import julianna from "./propics/julianna.png";
import ava from "./propics/ava.png";



function GuestList() {
  return (
    <>
      <a href="/bHome">
        <h1>HotSpot </h1>
      </a>
      <div>
        <div class="guestlist-container">
          <a href="/guestprofile">
            <img src="/propics/ally.png" alt="ally" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/brandon.png" alt="brandon" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/riley.png" alt="riley" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/marie.png" alt="marie" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/hannah.png" alt="hannah" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/donovan.png" alt="donovan" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/isaac.png" alt="isaac" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/lucas.png" alt="lucas" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/julianna.png" alt="julianna" />
          </a>
          <a href="/guestprofile">
            <img src="/src/propics/ava.png" alt="ava" />
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
