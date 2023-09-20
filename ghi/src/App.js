import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Nav from "./Nav.js";
import MainPage from "./Mainpage.js"



function App() {
    return (
    <BrowserRouter>
        <Nav />
        <Routes>
            <Route path="/" element={<MainPage />} />
        </Routes>
    </BrowserRouter>
    )
}


export default App
