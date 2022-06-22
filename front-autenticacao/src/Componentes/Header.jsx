import { Link, useNavigate } from "react-router-dom";
// import Home from "./Navigate";
import React,{ useState } from 'react';
import './style.css';
// const axios = require('axios').default;

function Header(){
    let navigate = useNavigate()

    return (
        <div>
            
            <header>
                <p><Link to="/me">Acessar conta</Link></p>
                <p><Link to="/cadastro">Fazer Cadastro</Link></p>
                <p><Link to="/login">Fazer Login</Link></p>
                <button onClick={() => {sessionStorage.clear(); navigate('/')}}>Sair</button>

            </header>
        </div>
    )
}

export default Header;