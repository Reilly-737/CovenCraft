import { useState } from "react";
import {Outlet, BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import AlertBar from "./components/AlertBar";
import Profile from "./components/pages/Profile";
import Home from "./components/pages/Home";
const App = () => {
    const [message, setMessage] = useState(null);
    const [snackType, setSnackType] = useState("");

    const setAlertMessage = (msg) => setMessage(msg);

    const handleSnackType = (type) => setSnackType(type);

    const ctx = {
        setAlertMessage,
        handleSnackType,
    };

     return (
       <Router>
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
             <Routes>
               <Route path="/" element={<Home />} />
               <Route path="/profile" element={<Profile />} />
             </Routes>
           </div>
         </div>
       </Router>
     );
}

export default App
