import React from 'react';
import "./static/styles.css"

export default class FarmProfMap extends React.Component {
    constructor() {
        super();
        this.address = "123 Farmville";
        this.city = "Farmurham";
        this.state = "Farmolina";
    }


    render() {
        return (
            <div class='row' id='map'>
            <div class="col s12 m6">
                <div class="card">
                    <span class="card-title">Your farmstand location</span>
                    <script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.min.js"></script>
                    <script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v4.5.1/mapbox-gl-geocoder.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.auto.min.js"></script>
                    <div id="map"></div>
                    <script>
                      mapboxgl.accessToken = 'pk.eyJ1IjoiaGRkbCIsImEiOiJja2NtMGY1ZDgwcTZ5MnN0OGY3ajJjbW4yIn0.qHA8T449zRKiEj4SS9jnuQ';
                    var map = new mapboxgl.Map({
                    container: 'map',
                    style: 'mapbox://styles/mapbox/streets-v11',
                    center: [-78.9013, 35.9958],
                    zoom: 13
                    });
                    map.addControl(
                    new MapboxGeocoder({
                    accessToken: mapboxgl.accessToken,
                    mapboxgl: mapboxgl
                    })
                    );
                    </script>
                </div>
            </div>
        </div> 
        )
    }
}