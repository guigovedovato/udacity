import {CLIENT_ID, CLIENT_SECRET} from './config'

export const getLocation = async (location) => {
    const basseURL = "https://api.foursquare.com/v2/";
    
    var lat = location.getPosition().lat();
    var lng = location.getPosition().lng();
    
    const wikiURL = `${basseURL}venues/search?client_id=
                     ${CLIENT_ID()}&client_secret=
                     ${CLIENT_SECRET()}&ll=
                     ${lat},${lng}&v=20180323&limit=1`;

    return await fetch(wikiURL)
    .then(response => response.json())
    .then(
        result => {
            let location = result.response.venues[0].location;
            let image = result.response.venues[0].categories[0].icon;
            let venue = result.response.venues[0];

            return `<div>
                        <img scr="${image.prefix}${image.suffix}" alt="${venue.name}" />
                        </p>
                            ${location.address}, ${location.city} - ${location.state} - ${location.country}
                        </p>
                        <div class="disclaimer">by <a href="https://foursquare.com/" target="_blank">FourSquare</a></div>
                    </div>`;
        }
    )
    .catch(
        error => {
            console.log("error=" + error)
            return '<div class="disclaimer">It was not possible retrieve information about '+location.title+'</div>';
        }
    )
}