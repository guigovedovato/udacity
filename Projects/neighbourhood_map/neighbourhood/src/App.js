import React, { Component } from 'react';
import './App.css';
import Map from './Map';
import * as MapsService from './service/MapsService';
import * as FoursquareService from './service/FoursquareService'
import ErrorBoundary from './ErrorBoundary'

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
    // Get Google Maps object from API and initialize properties
    this.Maps = MapsService.getMaps().then((Maps) => {
      this.map = new Maps.Map(document.getElementById('map'));
      this.Maps = Maps;
      this.largeInfowindow = new Maps.InfoWindow();
      this.bounds = new Maps.LatLngBounds();
      this.bind(this.Maps);
    }).catch((e) => {
      console.log(e)
      alert("Unfortunately there was an error to load Google Maps!");
    });
    // Get all parameterized point of interest
    this.points = MapsService.getAll()
  }
  // Bind the points into Google Maps as Markers
  bind = (Maps) => {
    for (let i = 0; i < this.points.length; i++) {
      this.add(Maps, this.points[i]);
    }
    // Extend the boundaries of the map for each marker
    this.map.fitBounds(this.bounds);
  }
  // Add markers
  add = (Maps, point) => {
    // Get the position from the location array.
    let position = point.location;
    let title = point.title;
    // Create a marker per location, and put into markers array.
    let marker = new Maps.Marker({
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
  // Create the InfoWindow Object
  populateInfoWindow = (marker, infowindow) => {
    // Check to make sure the infowindow is not already opened on this marker.
    if (infowindow.marker !== marker) {
      infowindow.marker = marker;
      // Create InfoWindow content
      this.showMarkerInfo(marker)
      let self = this;
      // Create the close buttom
      infowindow.addListener('closeclick',function(){
        infowindow.setMarker = null;
        self.resetAnimation();
      });
    }
  }
  // Add Markers into the Map
  addMarker = (marker) => {
    this.setState((currentState) => ({
      markers: currentState.markers.concat([marker])
    }))
    this.bounds.extend(marker.position);
  }
  // Update the markers in the Map
  updateMaker = (markers) => {
    this.remove(markers)
    return markers
  }
  // Remove all markers to be regenerated again
  removeAll = () => {
    for (let i = 0; i < this.state.markers.length; i++) {
      this.state.markers[i].setMap(null);
    }
  }
  // Add all markers again in the Map
  addAll = () => {
    for (let i = 0; i < this.state.markers.length; i++) {
      this.state.markers[i].setMap(this.map);
    }
    return this.state.markers
  }
  // Remove markers from the Map
  remove = (marker) => {
    // Remove all
    this.removeAll()
    this.state.markers.filter((c) => {
      return marker.indexOf(c) >= 0
    }).map((item) => (
      // Insert only the desired markers in the Map
      item.setMap(this.map)
    ))
  }
  resetAnimation = () => {
    for (let i = 0; i < this.state.markers.length; i++) {
      this.state.markers[i].setAnimation(null);
    }
  }
  showMarkerInfo = async (marker) => {
    this.resetAnimation();
    this.largeInfowindow.setContent('<div>' + marker.title + '</div>' + await this.getContent(marker));
    this.largeInfowindow.open(this.map, marker);
    marker.setAnimation(this.Maps.Animation.BOUNCE);
  }
  // Get content from Foursquare API
  getContent = async (location) => {
    return await FoursquareService.getLocation(location);
  }
  render() {
    return (
      <div>
        <ErrorBoundary>
          <Map 
            markers={this.state.markers}
            showMarkerInfo={this.showMarkerInfo}
            update={this.updateMaker}
            add={this.addAll}/>
          </ErrorBoundary>
        <div id="map" className="App-maps"></div>
      </div>
    );
  }
}

export default App;
