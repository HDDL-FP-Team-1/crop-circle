import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
// import './styles.css'

class Index extends React.Component {
  render () {
    return (
      <div>

        <h3>Farm Stand Map Data (--this is index.js)</h3>

      </div>
    )
  }
}
ReactDOM.render(<App />, document.getElementById('react-app'))

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
