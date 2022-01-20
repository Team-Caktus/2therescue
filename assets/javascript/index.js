import React from 'react';
import ReactDOM from "react-dom";

const jsonData = JSON.parse(document.querySelector('#pets').textContent)

ReactDOM.render(
  <h1>Hello {jsonData[0]}!</h1>,
  document.getElementById('root')
);