import React from 'react'

export default class Produce extends React.Component {
  constructor () {
    super()
        this.vegetables = [tomatoes, corn, spinach]
        this.fruits = [cherry, grapes, watermelon]
  }

  render () {
    return (
      <div className='Produce'>
        <ul>
          <li>item 1</li>
          <li>item 2</li>
          <li>item 3</li>
        </ul>
      </div>
    )
  }
}
