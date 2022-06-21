import React from 'react';
const axios = require('axios').default;

class Me extends React.Component {
    constructor(props){
        super(props)
        this.state = {
            email: "",
            senha: "",
            msg: ""
        }
        // axios.get('http://localhost:5000/me', {headers: {"Authorization": "Bearer " + response.data.access_token}})
        // .then((response) => {
        //     this.setState({msg: "Você fez login como: " + response.data.usuario_logado})
        //     console.log(response)
        // })
        // .catch((error) => {
        //     console.log(error)
        // })        
    }
    

    render() {
        return (
            <div>
                <h1>Bem vindo ao /Me.</h1>
                <h2>Você está logado como: {this.state.usuario_logado}</h2>
            </div>
        )
    }
}

export default Me;