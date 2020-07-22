import React from 'react'
import ReactDOM from 'react-dom'
import Header from './components/Header'

class App extends React.Component {
  render () {
    return (
      <div>
        <Header />
        <h3>Goodbye World</h3>
      </div>
    )
  }
}
ReactDOM.render(<App />, document.getElementById('react-app'))
