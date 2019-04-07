import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Map extends Component {
  static propTypes = {
    markers: PropTypes.array.isRequired,
    showMarkerInfo: PropTypes.func.isRequired,
    update: PropTypes.func.isRequired,
    add: PropTypes.func.isRequired
  }
  state = {
    query: ''
  }
  updateQuery = (query) => {
    this.setState(() => ({
      query: query.trim()
    }))
  }
  render() {
    const { query } = this.state
    const { markers, showMarkerInfo, update, add } = this.props

    // Validate if it was applied some filter to show the markers
    const showingmarkers = query === ''
      ? add()
      : update(markers.filter((c) => (
          c.title.toLowerCase().includes(query.toLowerCase())
        )))

    return (
      <div className="App-content">
        <div className='list-markers'>
            <div>
                <input
                    className='search-markers'
                    type='text'
                    placeholder='Search Points'
                    value={query}
                    onChange={(event) => this.updateQuery(event.target.value)}
                />
            </div>
            <ol>
                {showingmarkers.map((marker) => (
                    <li key={marker.id}  className="marker">
                        <p
                            onClick={() => showMarkerInfo(marker)}>
                            {marker.title}
                        </p>
                    </li>
                ))}
            </ol>
        </div>
      </div>
    )
  }
}

export default Map
