import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import './App.css';
import App from './App';
import Login from './Componentes/Login';
import Me from './Componentes/Me';
import Cadastro from './Componentes/Cadastro';
import Header from './Componentes/Header';
import  'bootstrap/dist/css/bootstrap.min.css' ;



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
    <Header/>
      <Routes>
        <Route path="/me" element={<Me />}/>
        <Route path="/login" element={<Login />}/>
        <Route path="/" element={<App />}/>
        <Route path="/cadastro" element={<Cadastro />}/>
      </Routes>
    </Router>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

