import { Link, useNavigate } from "react-router-dom";
import Home from "./Navigate";
import React from 'react';
import './style.css';
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
        
    }
    
    handleSubmit(event){   
        event.preventDefault();
        axios.post('http://localhost:5000/login', {"email": this.state.email, "password": this.state.senha})
        .then((response) => {
            
            if (response.data.error === true) {
                this.setState({msg: response.data.message})
            }

            else {
                // console.log(response.data)
                sessionStorage.setItem("access_token", response.data.access_token);
                sessionStorage.setItem("refresh_token", response.data.refresh_token);
                this.setState({msg: 'Login efetuado com sucesso!'})
                // axios.get('http://localhost:5000/me', {headers: {"Authorization": "Bearer " + response.data.access_token}})
                // .then((response) => {
                //     this.setState({msg: "Você fez login como: " + response.data.usuario_logado})
                // })
                // .catch((error) => {
                //     this.setState({msg: "A senha digitada está incorreta."})
                //     console.log(error)
                // })
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
                    {/* <Home/> */}
                </form>
            </div>
            
        )
    }
}

export default Login