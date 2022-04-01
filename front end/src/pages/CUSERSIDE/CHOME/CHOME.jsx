import './CHOME.css';

function Home() {
    return (
        <>
            <a href = '/chome'><h1>HotSpot </h1></a>
            <a href = '/cuserprofile'>
            <button id= "profButton"> Profile </button>
            </a>
            <div>

                <div id="invite">
                    <a href = '/eventinfo'>
                    <img src="https://picsum.photos/1000" /></a>
                </div>

            </div>
            <a href = '/rsvp'>
            <button id= "resButton"> RSVP </button>
            </a>
            <a href = '/chome'>
            <button id= "nextButton"> Next </button>
            </a>
            </>
    )
}

export default Home;