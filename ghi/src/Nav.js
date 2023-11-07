import React, {useState, useEffect} from "react";
import { NavLink } from "react-router-dom"
import book from "./img/book.svg"

function Nav(){
    return (
    <nav>
        <NavLink to="/">
            <img src={book} alt="book" />
        </NavLink>
        <NavLink to="/about">
            about
        </NavLink>
        <NavLink to="/signup">
            create account
        </NavLink>
        <NavLink to="/signin">
            sign in
        </NavLink>
    </nav>
    )
}

export default Nav
