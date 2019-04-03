import React, { Component } from 'react';
import './App.css';
import Map from './Map'
import * as MapsService from './service/MapsService'
import fetchGoogleMaps from 'fetch-google-maps'

class App extends Component {
  state = {
    points: []
  }
  map = {}
  markers = []
  componentDidMount() {
    this.setState(() => ({
      points: MapsService.getAll()
    }))
    fetchGoogleMaps({
      apiKey: 'AIzaSyBwYJGyuQEKS-pq5okWCCjI7djeiQwhvVk',
      language: 'en',
      libraries: ['geometry']
    }).then(( Maps ) => {
        this.map = new Maps.Map(document.getElementById('map'), {
            zoom: 13,
            center: new Maps.LatLng(41.2277042, -8.6329876)
        });

        let largeInfowindow = new Maps.InfoWindow();
        let bounds = new Maps.LatLngBounds();

        for (var i = 0; i < this.state.points.length; i++) {
          // Get the position from the location array.
          var position = this.state.points[i].location;
          var title = this.state.points[i].title;
          // Create a marker per location, and put into markers array.
          var marker = new Maps.Marker({
            map: this.map,
            position: position,
            title: title,
            animation: Maps.Animation.DROP,
            id: i
          });
          // Push the marker to our array of markers.
          this.markers.push(marker);
          // Create an onclick event to open an infowindow at each marker.
          marker.addListener('click', function() {
            populateInfoWindow(this, largeInfowindow);
          });
          bounds.extend(this.markers[i].position);
        }
        // Extend the boundaries of the map for each marker
        this.map.fitBounds(bounds);

        let self = this;

        function populateInfoWindow(marker, infowindow) {
          // Check to make sure the infowindow is not already opened on this marker.
          if (infowindow.marker !== marker) {
            infowindow.marker = marker;
            infowindow.setContent('<div>' + marker.title + '</div>');
            infowindow.open(self.map, marker);
            // Make sure the marker property is cleared if the infowindow is closed.
            infowindow.addListener('closeclick',function(){
              infowindow.setMarker = null;
            });
          }
        }

    });
  }
  selectPoint = (point) => {
    alert(point)
  }
  render() {
    return (
      <div>
        <Map 
          points={this.state.points}
          selectPoint={this.selectPoint}/>
        <div id="map" className="App-maps"></div>
      </div>
    );
  }
}

export default App;
