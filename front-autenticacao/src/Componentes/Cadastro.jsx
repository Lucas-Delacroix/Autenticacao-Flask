import { Link, useNavigate } from "react-router-dom";
import Home from "./Navigate";
import React from 'react';
import './style.css';
const axios = require('axios').default;

class Cadastro extends React.Component {
    
    constructor(props){
        super(props)
        this.state = {
            email: "",
            senha: "",
            confirmar_senha: "",
            msg: ""
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
        this.setState({email: document.getElementById("email").value});
        this.setState({senha: document.getElementById("senha").value});
        this.setState({confirmar_senha: document.getElementById("confimar_senha").value});
        
        
        
    }
    
    handleSubmit(event){   
        event.preventDefault();
        if (this.state.senha != this.state.confirmar_senha) {
            this.setState({msg: "As senhas não são iguais."})
        }
        if (this.state.senha == this.state.confirmar_senha) {
            this.setState({msg: ""})
            axios.post('http://localhost:5000/user/add', {"email": this.state.email, "password": this.state.senha})
            .then((response) => {
                console.log(response)
                this.setState({msg: response.data.message})
            }
            )
            .catch((error) => {
                console.log(error);
            })
        }
    }

    render() {
        return (
            <div>
                <form>
                    <h1>Faça seu cadastro.</h1>
                    <h2>{this.state.msg}</h2>
                    
                    <label>Email</label>
                    <input type="email" name="email" id="email" onChange={this.handleChange}/>
                    
                    <label>Senha</label>
                    <input type="password" name="password" id="senha" onChange={this.handleChange}/>
                    
                    <label>Confimar Senha</label>
                    <input type="password" name="password" id="confimar_senha" onChange={this.handleChange}/>
                    
                    <input type="submit" value="Enviar" onClick={this.handleSubmit} />
                    {/* <Home/> */}
                </form>
            </div>
            
        )
    }
}

export default Cadastro;