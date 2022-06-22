import { Link, useNavigate } from "react-router-dom";
import React,{ useState } from 'react';
import './style.css';
const axios = require('axios').default;

const Login = () => {
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [msg, setMsg] = useState('');
    let navigate = useNavigate()
    // constructor(props){
    //     super(props)
    //     this.state = {
    //         email: "",
    //         senha: "",
    //         msg: ""
    //     }
    //     this.handleChange = this.handleChange.bind(this);
    //     this.handleSubmit = this.handleSubmit.bind(this);
    // }

    const handleChange =() => {
    
        setEmail(document.getElementById("email").value);
        setSenha(document.getElementById("senha").value);
        
    }
    
    const handleSubmit = (event) => {   
        event.preventDefault();
        axios.post('http://localhost:5000/login', {"email": email, "password": senha})
        .then((response) => {
            
            if (response.data.error === true) {
                setMsg(response.data.message)
            }

            else {
                // console.log(response.data)
                sessionStorage.setItem("access_token", response.data.access_token);
                sessionStorage.setItem("refresh_token", response.data.refresh_token);
                setMsg('Login efetuado com sucesso!')
                navigate('/me')
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
            setMsg('Preencha todos os campos corretamente.')
            console.log(error);
        })
    }

    
    return (
        <div>
            <form>
                <h1>Login</h1>
                <h2>{msg}</h2>
                <label>Email</label>
                <input type="email" name="email" id="email" onChange={handleChange}/>
                <label>Senha</label>
                <input type="password" name="password" id="senha" onChange={handleChange}/>
                <input type="submit" value="Enviar" onClick={handleSubmit} />
                {/* <Home/> */}
            </form>
        </div>
            
    )
    
}

export default Login