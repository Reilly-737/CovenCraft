import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import Header from "./components/Header";
import AlertBar from "./components/AlertBar";

const App = () => {
    const [message, setMessage] = useState(null);
    const [snackType, setSnackType] = useState("");

    const setAlertMessage = (msg) => setMessage(msg);

    const handleSnackType = (type) => setSnackType(type);

    return (
        <div>
            <Header />
            {message && (
                <AlertBar
                    message={message}
                    snackType={snackType}
                    setAlertMessage={setAlertMessage}
                    handleSnackType={handleSnackType}
                />
            )}
            <div id="outlet">
                <Outlet />
            </div>
        </div>
    )
}

export default App
