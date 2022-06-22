import React from 'react';
import './style.css';
const axios = require('axios').default;

class Me extends React.Component {
    constructor(props){
        super(props)
        this.state = {
            email: "",
            senha: "",
            msg: ""
        }
        
        axios.get('http://localhost:5000/me', {headers: {"Authorization": "Bearer " + sessionStorage.getItem("access_token")}})
        .then((response) => {
            this.setState({msg: "Você fez login como: " + response.data.usuario_logado})
            console.log(response)
        })
        .catch((error) => {
            console.log(error)
            axios.get('http://localhost:5000/refresh-token', {headers: {"Authorization": "Bearer " + sessionStorage.getItem("refresh_token")}})
            .then((response) => {
                console.log('Utilizando o refresh-token...')
                console.log(response);
                sessionStorage.setItem("access_token", response.data.access_token);
                axios.get('http://localhost:5000/me', {headers: {"Authorization": "Bearer " + sessionStorage.getItem("access_token")}})
                .then((response) => {
                    this.setState({msg: "Você fez login como: " + response.data.usuario_logado})
                    console.log(response)
                })
            })
            .catch((error) => {
                console.log(error);
            })
            this.setState({msg: "Faça login para ter acesso a visualização da página."})
        })        
    }
    

    render() {
        return (
            <div>
                <h1>Bem vindo ao /Me.</h1>
                <h2>{this.state.msg}</h2>
            </div>
        )
    }
}

export default Me;