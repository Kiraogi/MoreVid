import React from 'react';
import HomePage from './components/HomePage';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UserManagement from './components/UserManagement';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <HomePage />
    </div>
  );
}

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/users" component={UserManagement} />
      </Switch>
    </Router>
  );
}

export default App;