import './BHome.css';

function BHome() {
    return (
        <>
            <a href = '/bHome'><h1>HotSpot </h1></a>
            <div>

                <div id="invite">
                    <a href = '/eventinfo'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/eventinfo'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/eventinfo'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/eventinfo'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/eventinfo'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/eventinfo'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                </div>

            </div>
            <a href = '/eventinfo'>
            <button id= "resButton"> CREATE </button>
            </a>
            <a href = '/buserprofile'>
            <button id= "nextButton"> PROFILE </button>
            </a>
            </>
    )
}

export default BHome;