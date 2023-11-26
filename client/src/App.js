import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import Header from "./components/Header";

const App = () => {

    return (
        <div>
            <Header />
            <div className="outlet">
            <Outlet context={ctx} />
            </div>
        </div>
    )
}

export default App