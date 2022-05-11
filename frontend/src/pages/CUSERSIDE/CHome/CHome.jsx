import "./CHome.css";
import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
//import invite from "./eventpics.json";

function CHome() {
  /*
    const [post, setPost] = React.useState(null);
    React.useEffect(() => {
        axios.get(baseURL).then((response) => {
            SVGTextPositioningElement(response.data);
        });
    } );
    if(!post) return null;
    //would return post.promo for event promo pic
    */
  const [interest, setInterest] = useState()
  const [neighborhood, setNeighborhood] = useState()
  const history = useHistory();
  const [newVenueProfile, setVenueProfile] = useState(undefined);

  /*
  useEffect(() => {
      axios.get('https://teamhotspot.herokuapp.com/cHome/bList')
      .then((response) => {
          if (response.data){
          setUsers(response.data);
          }
      })
      .catch(error => {
          setError(error);
          console.log(error);
      });
  }, [refresh])

  const handleBlist = () => {
      axios.post(`https://teamhotspot.herokuapp.com/cHome/bList`)
      .then(() => {
          setIsModalOpen(false);
          setRefresh(refresh + 1);
      })
      .catch(error => {
          setError(error);
          console.log(error);
      })
  }
*/
  /*
    useEffect(() => {
        axios
          .post("website.heroku.com/deletecUser/", {
            username: "SELECT username from cuser",
            age: "SELECT age from cuser",
            interests: "SELECT interests from cuser",
            neighborhood: "SELECT neighborhood from cuser",
          })
          .then(function () {
            // handle success
            console.log("deleted cuser");
          })
          .catch(function (error) {
            // handle error
            console.log("error in deleting cuser");
          })
          .then(function () {
            // always executed
          });
    }, []);
    */
  /*
   useEffect(() => {
     axios
       .post(
         "website.heroku.com/cDaily/",
         {
           username: ,
           new_interests: ,
           new_neighborhood: ,
         },
         []
       )
       .then(function () {
         // handle success
         console.log("updated cDaily");
       })
       .catch(function (error) {
         // handle error
         console.log("error in updating customer preferences");
       })
       .then(function () {
         // always executed
       });
   });
   */
  return (
    <div>
      <div className="heading">
        <a href="/cHome">
          <h1>HotSpot </h1>
        </a>

        <a href="/csettings">
          <button id="settings">
            {" "}
            <img src="https://img.icons8.com/nolan/64/apple-settings.png" />{" "}
          </button>
        </a>
        <a href="/cuserprofile">
          <button id="profButton"> Profile </button>
        </a>
      </div>
      <div>
        <div id="invite">
          {/* <div>
            {invite(
              map((name, i) => (
                <div key={i}>
                  <img src={record.path} />
                </div>
              ))
            )}
            <a href="/venueprofile"></a>
          </div>{" "} */}
        </div>
        <div className="buttoncentering">
          <a href="/rSVP">
            <button id="resButton" className="button1"> RSVP </button>
          </a>
          <a href="/cHome">
            <button id="nextButton" className="button1"> Next </button>
          </a>
          <a href='/cHome'>
            <button id="nextButton" className="page-button"> Business List </button>
          </a>
        </div>
      </div>
    </div>
  );
}
export default CHome;
//onClick={handleBlist}