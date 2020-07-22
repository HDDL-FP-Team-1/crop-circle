import React from 'react'
import Header from './components/Header'
import { BrowserRouter as Router, Switch, Route } from 'reaect-router-dom'

class App extends React.Component {
  render () {
    return (
      <div>
        <Router>
          <div className=''>
            <Header />
            {/* <Login /> */}
            <Switch>
              <Route />
            </Switch>
          </div>
        </Router>
      </div>
    )
  }
}
export default App
