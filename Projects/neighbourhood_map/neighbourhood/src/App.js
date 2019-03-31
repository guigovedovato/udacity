import React, { Component } from 'react';
import './App.css';
import Map from './Map'
import * as MapsService from './service/MapsService'

class App extends Component {
  state = {
    points: []
  }
  componentDidMount() {
    MapsService.getAll()
      .then((points) => {
        this.setState(() => ({
          points
        }))
      })
  }
  render() {
    return (
      <div className="App">
        <dic className="App-content">
          <Map points={this.state.points}/>
        </dic>
      </div>
    );
  }
}

export default App;
