import { Link } from "react-router-dom";


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Bien Vindo! Escolha uma opção para prosseguir.</h1>
        <Link to="/me">Acessar conta</Link>
        <Link to="/cadastro">Fazer Cadastro</Link>
        <Link to="/login">Fazer Login</Link>
      </header>
    </div>
  );
}

export default App;
