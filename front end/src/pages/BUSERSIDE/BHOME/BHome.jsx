import './BHome.css';

function BHome() {
     useEffect(() =>
    {
      axios
         .post('website.heroku.com/deletebUser/',
    {
          username: "SELECT buserName from buser",
    })
        .then(function () 
        {
        // handle success
        console.log("deleted buser");
        })
        .catch(function (error) {
        // handle error
        console.log("error in deleting cuser");
        })
        .then(function () {
        // always executed
        });
    });
    return (
        <>
            <a href = '/bHome'><h1>HotSpot </h1></a>
            <a href = '/bsettings'>
            <button id= "settings"> <img src="https://img.icons8.com/nolan/64/apple-settings.png"/></button>
            </a>
            <div>

                <div class= "event-container">
                    <div class = "gallery">
                    <div class="grid-item1">
                    <a href = '/eventinfo'>
                    <img src="https://picsum.photos/1000" class = 'gallery_img' alt= 'event'/></a></div>
                    <div class="grid-item2">
                    <a href = '/eventinfo'>
                    <img src="https://picsum.photos/1000" class = 'gallery_img' alt= 'event'/></a></div>
                    <div class="grid-item3">
                    <a href = '/eventinfo'>
                    <img src="https://picsum.photos/1000" class = 'gallery_img' alt= 'event'/></a></div>
                    <div class="grid-item4">
                    <a href = '/eventinfo'>
                    <img src="https://picsum.photos/1000" class = 'gallery_img' alt= 'event'/></a></div>
                    <div class="grid-item5">
                    <a href = '/eventinfo'>
                    <img  src="https://picsum.photos/1000" class = 'gallery_img' alt= 'event'/></a></div>
                    <div class="grid-item6">
                    <a href = '/eventinfo'>
                    <img src="https://picsum.photos/1000" class = 'gallery_img' alt= 'event'/></a></div>
                    </div>
                </div>

            </div>
            <a href = '/eventinfo'>
            <button id= "resButton"> CREATE </button>
            </a>
            <a href = '/venueinfo'>
            <button id= "nextButton"> PROFILE </button>
            </a>
            </>
    )
}

export default BHome;
