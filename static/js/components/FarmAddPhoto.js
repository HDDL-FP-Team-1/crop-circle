import React from "react";
import ReactDOM from 'react-dom';

export default class FarmAddPhoto extends React.Component {
    render() {
        return (
            <!-- Switch -->
            <div className="row">
            <div className="col s12 m2">
              <div className="card ">
                <span className="card-title">Add a photo</span>
                <div className="card-content">
                    <a className="btn-floating btn-large waves-effect waves-light red pulse"><i class="material-icons">add</i></a>
                </div>
              </div>
            </div>
          </div>
        )
    }