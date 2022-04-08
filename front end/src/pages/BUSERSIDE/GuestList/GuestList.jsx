import './GuestList.css';

function GuestList() {
    return (
        <>
            <a href = '/bHome'><h1>HotSpot </h1></a>
            <div>

                <div id="invite">
                    <a href = '/bHome'> should eventually link to cuserprofile (non mutable)
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/bHome'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/bHome'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/bHome'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/bHome'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                    <a href = '/bHome'>
                    <img id= 'event' src="https://picsum.photos/1000" /></a>
                </div>

            </div>
            <a href = '/eventInfo'>
            <button id= "resButton"> VIEW EVENT </button>
            </a>
            <a href = '/venueInfo'>
            <button id= "nextButton"> VIEW VENUE </button>
            </a>
            </>
    )
}

export default GuestList;