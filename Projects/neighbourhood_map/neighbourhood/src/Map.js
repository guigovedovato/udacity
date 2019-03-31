import React, { Component } from 'react';
import * as MapsService from './service/MapsService'
import * as WikiService from './service/WikiService'
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
              c.name.toLowerCase().includes(query.toLowerCase())
            ))

          return (
            <div></div>
          )
      }
}

export default Map
