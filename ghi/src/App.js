import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Nav from "./Nav.js";
import MainPage from "./Mainpage.js"
import About from "./About.js";


function App() {
    return (
    <BrowserRouter>
        <Nav />
        <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/about" element={<About />}/>
        </Routes>
    </BrowserRouter>
    )
}


export default App
