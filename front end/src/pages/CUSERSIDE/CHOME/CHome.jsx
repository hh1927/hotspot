import './CHome.css';
import React from 'react';
import axios from 'axios';
//const baseURL = //our API

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
    
    useEffect(() =>
    {
      axios
         .post('website.heroku.com/deletecUser/',
    {
          username: "SELECT username from cuser"
          age:  "SELECT age from cuser"
          interests:  "SELECT interests from cuser"
          neighborhood: "SELECT neighborhood from cuser"
    })
        .then(function () 
        {
        // handle success
        console.log("deleted cuser);
        })
        .catch(function (error) {
        // handle error
        console.log("error in deleting cuser");
        })
        .then(function () {
        // always executed
        });
        
    return (
        <div>
           <div className='heading'>
            <a href = '/cHome'><h1>HotSpot </h1></a>
            
            <a href = '/bsettings'>
            <button id= "settings"> icon here</button>
            </a>
            <a href = '/cuserprofile'>
            <button id= "profButton"> Profile </button>
            </a>
            </div>
            <div>
                <div id="invite">
                    <a href = '/venueprofile'>
                    <img src="https://picsum.photos/1000" /></a>
                </div>

            </div>
            <div className='buttoncentering'>
            <a href = '/rSVP'>
            <button id= "resButton"> RSVP </button>
            </a>
            <a href = '/cHome'>
            <button id= "nextButton"> Next </button>
            </a>
            </div>
        </div>
    )
}
export default CHome;
