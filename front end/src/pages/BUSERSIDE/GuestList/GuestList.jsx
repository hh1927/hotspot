import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import './GuestList.css';

export default function GuestList() {
    const history = useHistory();
    const [newcList, setcList] = useState(undefined);

    useEffect(() => {
        axios.get('https://teamhotspot.herokuapp.com/GuestList/cList')
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
            <a href = '/bHome'><h1>HotSpot </h1></a>
            <div>

                <div class="guestlist-container">
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                    <a href = '/guestprofile'>
                    <img src="https://picsum.photos/1000" alt= 'guestpropic'/></a>
                </div>

            </div>
            <a href = '/eventInfo'>
            <button id= "resButton"> VIEW EVENT </button>
            </a>
            <a href = '/venueInfo'>
            <button id= "nextButton"> VIEW VENUE </button>
            </a>
            <a href = '/eventInfo'>
            <button onClick={handleBquota} id= "resButton"> VIEW CUSTOMER LIST </button>
            </a>
            </>
    )
}

export default GuestList;