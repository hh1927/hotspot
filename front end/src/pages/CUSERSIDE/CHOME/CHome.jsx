import './CHome.css';
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';
//const baseURL = //our API

function CHome() {
    
    const history = useHistory();
    const [newVenueProfile, setVenueProfile] = useState(undefined);

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

    function navigateToPage(path) {
        history.push(path);
    }
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
            <a href = '/cHome'>
            <button onClick={handleBlist} id= "nextButton"> Business List </button>
            </a>
            </div>
        </div>
    )
}
export default CHome;
