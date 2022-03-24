import './Home.css';

function Home() {
    return (
        <>
            <a href = '/cuserprofile'>
            <button id= "profButton"> Profile </button>
            </a>
            <div>

                <div id="invite">
                    <img src="https://picsum.photos/1000"/>
                </div>

            </div>
            <a href = '/rsvp'>
            <button id= "resButton"> RSVP </button>
            </a>
            <a href = '/home'>
            <button id= "nextButton"> Next </button>
            </a>
            </>
    )
}

export default Home;