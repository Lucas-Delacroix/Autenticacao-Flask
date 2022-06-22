import { Link, useNavigate } from "react-router-dom";
// import Home from "./Navigate";
import React,{ useState } from 'react';
import './style.css';
import  { Button, ButtonGroup }  from  'react-bootstrap' ;
// const axios = require('axios').default;

function Header(){
    let navigate = useNavigate()

    return (
        <div>
            
            <header>
            <>
            <ButtonGroup size="sm">
                <Button variant="outline-warning" onClick={() => {navigate('/me')}} >Acessar conta</Button>
                <Button variant="outline-warning" onClick={() => {navigate('/cadastro')}}>Fazer Cadastro</Button>
                <Button variant="outline-warning" onClick={() => {navigate('/login')}}>Fazer Login</Button>
                <Button variant="outline-warning" onClick={() => {sessionStorage.clear(); navigate('/')}}>Sair</Button>
            </ButtonGroup>
            </>
               
                

            </header>
        </div>
    )
}

export default Header;