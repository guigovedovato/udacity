import React, { Component } from 'react';
import './App.css';
import Map from './Map';
import * as MapsService from './service/MapsService';
import * as FoursquareService from './service/FoursquareService'

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
    this.Maps = MapsService.getMaps().then(( Maps ) => {
      this.map = new Maps.Map(document.getElementById('map'));
      this.Maps = Maps;
      this.largeInfowindow = new Maps.InfoWindow();
      this.bounds = new Maps.LatLngBounds();
      this.bind(this.Maps);
  });
    this.points = MapsService.getAll()
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
      let self = this;
      infowindow.addListener('closeclick',function(){
        infowindow.setMarker = null;
        self.resetAnimation();
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
    this.remove(markers)
    return markers
  }
  removeAll = () => {
    for (var i = 0; i < this.state.markers.length; i++) {
      this.state.markers[i].setMap(null);
    }
  }
  addAll = () => {
    for (var i = 0; i < this.state.markers.length; i++) {
      this.state.markers[i].setMap(this.map);
    }
    return this.state.markers
  }
  remove = (marker) => {
    this.removeAll()
    this.state.markers.filter((c) => {
      return marker.indexOf(c) >= 0
    }).map((item) => (
      item.setMap(this.map)
    ))
  }
  resetAnimation = () => {
    for (var i = 0; i < this.state.markers.length; i++) {
      this.state.markers[i].setAnimation(null);
    }
  }
  selectPoint = async (point) => {
    this.resetAnimation();
    this.largeInfowindow.setContent('<div>' + point.title + '</div>' + await this.setContent(point));
    this.largeInfowindow.open(this.map, point);
    point.setAnimation(this.Maps.Animation.BOUNCE);
  }
  setContent = async (location) => {
    return await FoursquareService.getLocation(location);
  }
  render() {
    return (
      <div>
        <Map 
          markers={this.state.markers}
          selectPoint={this.selectPoint}
          update={this.updateMaker}
          add={this.addAll}/>
        <div id="map" className="App-maps"></div>
      </div>
    );
  }
}

export default App;
