import React from 'react'
import ReactDOM from 'react-dom'
class App extends React.Component {
  render () {
    return (
      <div>
        <h1>Hello, Hello world!</h1>
        <h3>Goodbye World</h3>
      </div>
    )
  }
}
ReactDOM.render(<App />, document.getElementById('react-app'))
