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
    return (
        <>
            <a href = '/cHome'><h1>HotSpot </h1></a>
            <a href = '/bsettings'>
            <button id= "settings"> icon here</button>
            </a>
            <a href = '/cuserprofile'>
            <button id= "profButton"> Profile </button>
            </a>
            <div>

                <div id="invite">
                    <a href = '/venueprofile'>
                    <img src="https://picsum.photos/1000" /></a>
                </div>

            </div>
            <a href = '/rSVP'>
            <button id= "resButton"> RSVP </button>
            </a>
            <a href = '/cHome'>
            <button id= "nextButton"> Next </button>
            </a>
            </>
    )
}
export default CHome;