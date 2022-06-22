import React from 'react';
import {useNavigate} from "react-router-dom"

const Home = () => {
const navigate = useNavigate();
	
return (
	<>
		<button onClick={()=>navigate("/")}>Home</button>
	</>
)
};

export default Home;
