import React, { Component } from 'react';
import './App.css';
import Map from './Map';
import * as MapsService from './service/MapsService';
import fetchGoogleMaps from 'fetch-google-maps';

class App extends Component {
  state = {
    markers: []
  }
  map = {}
  largeInfowindow = {}
  bounds = {}
  points = {}
  Maps = {}
  componentDidMount() {
    this.points = MapsService.getAll()
    fetchGoogleMaps({
      apiKey: 'AIzaSyBwYJGyuQEKS-pq5okWCCjI7djeiQwhvVk',
      language: 'en'
    }).then(( Maps ) => {
        this.map = new Maps.Map(document.getElementById('map'), {
            zoom: 13,
            center: new Maps.LatLng(41.2277042, -8.6329876)
        });
        this.Maps = Maps;
        this.largeInfowindow = new Maps.InfoWindow();
        this.bounds = new Maps.LatLngBounds();
        this.bind(this.Maps);
    });
  }
  bind = (Maps) => {
    for (var i = 0; i < this.points.length; i++) {
      this.add(Maps, this.points[i]);
    }
    // Extend the boundaries of the map for each marker
    this.map.fitBounds(this.bounds);
  }
  add = (Maps, point) => {
    // Get the position from the location array.
    var position = point.location;
    var title = point.title;
    // Create a marker per location, and put into markers array.
    var marker = new Maps.Marker({
      map: this.map,
      position: position,
      title: title,
      animation: Maps.Animation.DROP,
      id: point.id
    });
    // Push the marker to our array of markers.
    this.addMarker(marker);
    // Create an onclick event to open an infowindow at each marker.
    let self = this;
    marker.addListener('click', function() {
      self.populateInfoWindow(this, self.largeInfowindow);
    });
  } 
  populateInfoWindow = (marker, infowindow) => {
    // Check to make sure the infowindow is not already opened on this marker.
    if (infowindow.marker !== marker) {
      infowindow.marker = marker;
      this.selectPoint(marker)
      // Make sure the marker property is cleared if the infowindow is closed.
      infowindow.addListener('closeclick',function(){
        infowindow.setMarker = null;
      });
    }
  }
  addMarker = (marker) => {
      this.setState((currentState) => ({
        markers: currentState.markers.concat([marker])
      }))
      this.bounds.extend(marker.position);
  }
  updateMaker = (markers) => {
    if(this.state.markers.length >= markers.length)
      this.remove(markers)
    else
      alert("deve adicionar")
    return markers
  }
  remove = (ma) => {
    this.state.markers.filter((c) => {
      return ma.indexOf(c) < 0
    }).map((item) => (
      item.setMap(null)
    ))
  }
  selectPoint = (point) => {
    this.largeInfowindow.setContent('<div>' + point.title + '</div>');
    this.largeInfowindow.open(this.map, point);
  }
  render() {
    return (
      <div>
        <Map 
          markers={this.state.markers}
          selectPoint={this.selectPoint}
          update={this.updateMaker}/>
        <div id="map" className="App-maps"></div>
      </div>
    );
  }
}

export default App;
