import { Link } from "react-router-dom";
import React from 'react';
const axios = require('axios').default;


class Login extends React.Component {
    
    constructor(props){
        super(props)
        this.state = {
            email: "",
            senha: "",
            msg: ""
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
        this.setState({email: document.getElementById("email").value});
        this.setState({senha: document.getElementById("senha").value});
        console.log(this.state.email)
        console.log(this.state.senha)
    }
    
    handleSubmit(event){
        event.preventDefault();
        axios.post('http://localhost:5000/login', {"email": this.state.email, "password": this.state.senha})
        .then((response) => {
            
            if (response.data.error === true) {
                this.setState({msg: response.data.message})
            }

            if (response.status === 200) {
                // console.log(response.data)
                axios.get('http://localhost:5000/me', {headers: {"Authorization": "Bearer " + response.data.access_token}})
                .then((response) => {
                    this.setState({msg: "Você fez login como: " + response.data.usuario_logado})
                    
                    console.log(response)
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        }
        )
        .catch((error) => {
            this.setState({msg: 'Preencha todos os campos corretamente.'})
            console.log(error);
        })
    }

    render() {
        return (
            <div>
                <form>
                    <h1>Login</h1>
                    <h2>{this.state.msg}</h2>
                    <label>Email</label>
                    <input type="email" name="email" id="email" onChange={this.handleChange}/>
                    <label>Senha</label>
                    <input type="password" name="password" id="senha" onChange={this.handleChange}/>
                    <input type="submit" value="Enviar" onClick={this.handleSubmit} />
                    <Link to="/me">Entrar</Link>
                </form>
            </div>
            
        )
    }
}

export default Login