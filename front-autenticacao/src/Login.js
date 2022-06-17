import React from 'react'
import './Login.css'
const axios = require('axios').default;

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state ={
            email: "",
            senha: "",
            acessToken: "nulo",
            logado: false,
            msg: ""
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }

    handleChange(event) {
        this.setState({email: document.getElementById("email").value});
        this.setState({senha: document.getElementById("senha").value});
    }

    handleSubmit(event) {
        event.preventDefault();
        
        axios.post("http://localhost:5000/login", {"email": this.state.email, "password": this.state.senha})
        .then((response) => {
            if (response.data.error === true) {
                this.setState({msg: response.data.message})
                console.log(response);
            }
            else {
                console.log(response.data)
                this.setState({acessToken: response.data.access_token});
                this.setState({logado: true});
                
                axios.get('http://localhost:5000/me', {headers: {Authorization: 'Bearer '+ response.data.access_token }})
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {  
                    console.log(error);
                })
            }

        })
        .catch((error) => {
            this.setState({msg: "Por favor preencha todos os campos adequadamente."})
            console.log(error);
        })
        
        
    }

    handleClick(event) {
        console.log(this.state.acessToken)
    }

    render() {
        if (this.state.logado == false) { 
            return (
            <div className="Container">
                <div className="rightlogin">
                    <h1>Login</h1>
                    <h2>{this.state.msg}</h2>
                    <form onSubmit={this.handleSubmit}>
                        <div className='campo'>
                            <label htmlFor="email">Email</label>
                            <input type="email" placeholder="Digite aqui seu email." name="email" id="email" onChange={this.handleChange}/>
                        </div>
                        
                        <div className='campo'>
                            <label htmlFor="password">Senha</label>
                            <input type="password" placeholder="Digite aqui sua senha." name="password" id="senha" onChange={this.handleChange}/>
                        </div>

                        <input type="submit" value="Enviar" />
                        {/* <button onClick={this.handleClick}>Ver Access Token</button> */}
                    </form>
                </div>
            </div>
            );
        }
        if (this.state.logado == true) {
            return (
                <h1>Você fez login com sucesso!</h1>
            )
        }
    }
}

export default Login