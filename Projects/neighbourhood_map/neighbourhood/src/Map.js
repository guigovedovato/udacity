import React, { Component } from 'react';
import PropTypes from 'prop-types'

class Map extends Component {
    static propTypes = {
        points: PropTypes.array.isRequired,
        selectPoint: PropTypes.func.isRequired
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
        const { points, selectPoint } = this.props
    
        const showingPoints = query === ''
          ? points
          : points.filter((c) => (
              c.title.toLowerCase().includes(query.toLowerCase())
            ))

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
                      {showingPoints.map((point) => (
                          <li key={point.id}  className="point">
                              <p
                                 onClick={() => selectPoint(point.title)}>
                                 {point.title}
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
