import "./GuestList.css";
import "./propics/ally.png";
import "./propics/brandon.png";
import "./propics/riley.png";
import "./propics/marie.png";
import "./propics/hannah.png";
import "./propics/donovan.png";
import "./propics/isaac.png";
import "./propics/lucas.png";
import "./propics/julianna.png";
import "./propics/ava.png";



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
        <button id="resButton" className="button1"> VIEW EVENT </button>
      </a>
      <a href="/venueInfo">
        <button id="nextButton" className="button1" > VIEW VENUE </button>
      </a>
      <a href='/eventInfo'>
        <button onClick={handleBquota} id="resButton" className="button2" > VIEW CUSTOMER LIST </button>
      </a>
    </>
  );
}

export default GuestList;
