import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Map extends Component {
    static propTypes = {
        markers: PropTypes.array.isRequired,
        selectPoint: PropTypes.func.isRequired,
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
        const { markers, selectPoint, update, add } = this.props
    
        const showingPoints = query === ''
          ? add()
          : update(markers.filter((c) => (
              c.title.toLowerCase().includes(query.toLowerCase())
            )))

          return (
            <div className="App-content">
              <div className='list-points'>
                  <div>
                      <input
                          className='search-points'
                          type='text'
                          placeholder='Search Points'
                          value={query}
                          onChange={(event) => this.updateQuery(event.target.value)}
                      />
                  </div>
                  <ol>
                      {showingPoints.map((marker) => (
                          <li key={marker.id}  className="point">
                              <p
                                 onClick={() => selectPoint(marker)}>
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
