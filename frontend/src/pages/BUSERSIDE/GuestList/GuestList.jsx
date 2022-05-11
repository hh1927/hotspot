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
  const history = useHistory();
  const [newcList, setcList] = useState(undefined);

  useEffect(() => {
    axios.get('https://teamhotspot.herokuapp.com/GuestList/cList')
      .then((response) => {
        if (response.data) {
          setUsers(response.data);
        }
      })
      .catch(error => {
        setError(error);
        console.log(error);
      });
  }, [refresh])

  const handlecList = () => {
    axios.post(`https://teamhotspot.herokuapp.com/GuestList/cList`)
      .then(() => {
        setIsModalOpen(false);
        setRefresh(refresh + 1);
      })
      .catch(error => {
        setError(error);
        console.log(error);
      })
  }

  function navigateToPage(path) {
    history.push(path);
  }
  return (
    <>
      <a href="/bHome">
        <h1>HotSpot </h1>
      </a>
      <div>
        <div class="guestlist-container">
          <a href="/guestprofile">
            <img src={ally} alt="ally" />
          </a>
          <a href="/guestprofile">
            <img src={brandon} alt="brandon" />
          </a>
          <a href="/guestprofile">
            <img src={riley} alt="riley" />
          </a>
          <a href="/guestprofile">
            <img src={marie} alt="marie" />
          </a>
          <a href="/guestprofile">
            <img src={hannah} alt="hannah" />
          </a>
          <a href="/guestprofile">
            <img src={donovan} alt="donovan" />
          </a>
          <a href="/guestprofile">
            <img src={isaac} alt="isaac" />
          </a>
          <a href="/guestprofile">
            <img src={lucas} alt="lucas" />
          </a>
          <a href="/guestprofile">
            <img src={julianna} alt="julianna" />
          </a>
          <a href="/guestprofile">
            <img src={ava} alt="ava" />
          </a>
        </div>
      </div>
      <a href="/eventInfo">
        <button id="resButton" className="button1"> VIEW EVENT </button>
      </a>
      <a href="/venueInfo">
        <button id="nextButton" className="button1" > VIEW VENUE </button>
      </a>

      <button onClick={handleBquota} id="resButton" className="button2" > VIEW CUSTOMER LIST </button>

    </>
  );
}

export default GuestList;
