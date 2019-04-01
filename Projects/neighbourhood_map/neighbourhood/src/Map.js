import React, { Component } from 'react';
import PropTypes from 'prop-types'

class Map extends Component {
    static propTypes = {
        points: PropTypes.array.isRequired
      }
      state = {
        query: ''
      }
      updateQuery = (query) => {
        this.setState(() => ({
          query: query.trim()
        }))
      }
      clearQuery = () => {
        this.updateQuery('')
      }
      render() {
        const { query } = this.state
        const { points } = this.props
    
        const showingPoints = query === ''
          ? points
          : points.filter((c) => (
              c.title.toLowerCase().includes(query.toLowerCase())
            ))

          return (
            <div className='list-points'>
                <div className='list-points-top'>
                    <input
                        className='search-points'
                        type='text'
                        placeholder='Search Points'
                        value={query}
                        onChange={(event) => this.updateQuery(event.target.value)}
                    />
                </div>
                <ol className='point-list'>
                    {showingPoints.map((point) => (
                        <li key={point.id} className='point-list-item'>
                        <div className='point-details'>
                            <p>{point.title}</p>
                        </div>
                        </li>
                    ))}
                </ol>
            </div>
          )
      }
}

export default Map
