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
  //const history = useHistory();
  //const [newcList, setcList] = useState(undefined);

  //useEffect(() => {
  //  axios.get('https://teamhotspot.herokuapp.com/GuestList/cList')
  //    .then((response) => {
  //      if (response.data) {
  //        setUsers(response.data);
  //      }
  //    })
  //    .catch(error => {
  //      setError(error);
  //      console.log(error);
  //    });
  //}, [refresh])

  //const handlecList = () => {
  //  axios.post(`https://teamhotspot.herokuapp.com/GuestList/cList`)
  //    .then(() => {
  //      setIsModalOpen(false);
  //      setRefresh(refresh + 1);
  //    })
  //    .catch(error => {
  //      setError(error);
  //      console.log(error);
  //    })
  //}

  // function navigateToPage(path) {
  //  history.push(path);
  //}
  return (
    <>
      <a href="/bHome">
        <h1>HotSpot </h1>
      </a>
      <div>
        <div class="guestlist-container">
          <div class="gallery">
            <div class="grid-person1">
              <a href="/guestprofile">
                <img src={ally} class="gallery_img" alt="ally" />
              </a>
            </div>


            <div class="grid-person2">
              <a href="/guestprofile">
                <img src={brandon} class="gallery_img" alt="brandon" />
              </a>
            </div>

            <div class="grid-person3">
              <a href="/guestprofile">
                <img src={riley} class="gallery_img" alt="riley" />
              </a>
            </div>

            <div class="grid-person4">
              <a href="/guestprofile">
                <img src={marie} class="gallery_img" alt="marie" />
              </a>
            </div>

            <div class="grid-person5">
              <a href="/guestprofile">
                <img src={hannah} class="gallery_img" alt="hannah" />
              </a>
            </div>

            <div class="grid-person6">
              <a href="/guestprofile">
                <img src={donovan} class="gallery_img" alt="donovan" />
              </a>
            </div>

            <div class="grid-person7">
              <a href="/guestprofile">
                <img src={isaac} class="gallery_img" alt="isaac" />
              </a>
            </div>

            <div class="grid-person8">
              <a href="/guestprofile">
                <img src={lucas} class="gallery_img" alt="lucas" />
              </a>
            </div>


            <div class="grid-person9">
              <a href="/guestprofile">
                <img src={julianna} class="gallery_img" alt="julianna" />
              </a>
            </div>


            <div class="grid-person10">
              <a href="/guestprofile">
                <img src={ava} class="gallery_img" alt="ava" />
              </a>
            </div>

          </div>
        </div>
      </div>
      <a href="/eventInfo">
        <button id="resButton" className="button1"> VIEW EVENT </button>
      </a>
      <a href="/venueInfo">
        <button id="nextButton" className="button1" > VIEW VENUE </button>
      </a>


    </>
  );
}
// onClick={handleBquota} id="resButton" className="button2" > VIEW CUSTOMER LIST 
export default GuestList;
