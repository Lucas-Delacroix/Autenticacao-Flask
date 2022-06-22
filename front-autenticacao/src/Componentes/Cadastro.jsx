import { Link, useNavigate } from "react-router-dom";
import React,{ useState } from 'react';
import './style.css';
const axios = require('axios').default;

const Cadastro = () => {
    const [email, setEmail] = useState();
    const [senha, setSenha] = useState();
    const [confirmar_senha, setConfirmar_senha] = useState();
    const [msg, setMsg] = useState();
    let navigate = useNavigate()
    // constructor(props){
    //     super(props)
    //     this.state = {
    //         email: "",
    //         senha: "",
    //         confirmar_senha: "",
    //         msg: ""
    //     }
    //     this.handleChange = this.handleChange.bind(this);
    //     this.handleSubmit = this.handleSubmit.bind(this);
    // }

    const handleChange = () => {
        setEmail(document.getElementById("email").value);
        setSenha(document.getElementById("senha").value);
        setConfirmar_senha(document.getElementById("confimar_senha").value);
    }
    
    const handleSubmit = (event) => {   
        event.preventDefault();
        if (senha != confirmar_senha) {
            setMsg("As senhas não são iguais.")
        }
        if (senha == confirmar_senha) {
            setMsg("")
            axios.post('http://localhost:5000/user/add', {"email": email, "password": senha})
            .then((response) => {
                console.log(response)
                setMsg(response.data.message)
                
            }
            )
            .catch((error) => {
                console.log(error);
            })
        }
    }

    
    
        return (
            <div>
                <form>
                    <h1>Faça seu cadastro.</h1>
                    <h2>{msg}</h2>
                    
                    <label>Email</label>
                    <input type="email" name="email" id="email" onChange={handleChange}/>
                    
                    <label>Senha</label>
                    <input type="password" name="password" id="senha" onChange={handleChange}/>
                    
                    <label>Confimar Senha</label>
                    <input type="password" name="password" id="confimar_senha" onChange={handleChange}/>
                    
                    <input type="submit" value="Enviar" onClick={handleSubmit} />
                    {/* <Home/> */}
                </form>
            </div>
            
        )
    
}

export default Cadastro;