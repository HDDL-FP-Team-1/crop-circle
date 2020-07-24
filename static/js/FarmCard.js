import React from 'react'
import ReactDOM from 'react-dom'

class App extends React.Component {
  render () {
    return (
      <div>
        <h3>Farm Card React App</h3>
      </div>
    )
  }
}
ReactDOM.render(<App />, document.getElementById('farm-card'))
