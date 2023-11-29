import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import Header from "./components/Header";
import AlertBar from "./components/AlertBar";


const App = () => {
    const [message, setMessage] = useState(null);
    const [snackType, setSnackType] = useState("");
    const [user, setUser] = useState(null); 

    useEffect(() => { 
        fetch("/check_session")
        .then((resp) => { 
            if (resp.ok) { 
                resp.json().then(setUser); 
            } 
        })
    }, []);

    const setAlertMessage = (msg) => setMessage(msg);

    const handleSnackType = (type) => setSnackType(type);

    const ctx = {
        user, 
        setAlertMessage,
        handleSnackType,
    };

    return (
        <div>
            <Header user={user} />
            {message && (
                <AlertBar
                    message={message}
                    snackType={snackType}
                    setAlertMessage={setAlertMessage}
                    handleSnackType={handleSnackType}
                />
            )}
            <div id="outlet">
                <Outlet context={ctx} />
            </div>
        </div>
    )
}

export default App
