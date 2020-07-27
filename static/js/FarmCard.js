import React from 'react'
import ReactDOM from 'react-dom'

class FarmCard extends React.Component {
  render () {
    return (
      <div>
        <h3>Farm Card React App</h3>
      </div>
    )
  }
}
ReactDOM.render(<FarmCard />, document.getElementById('farm-card'))
