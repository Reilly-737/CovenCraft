import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import { useOutletContext } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  const { setSnackMessage, setSnackType, setSnackOpen } = useOutletContext();
  const [credentials, setCredentials] = useState({
    username: "",
    password: "",
  });

  const handleChange = (e) => {
    setCredentials({
      ...credentials,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      });

      if (response.ok) {
        const user = await response.json();
        console.log("Login successful. User:", user);
        navigate(`/profile/${user.id}`);
        setSnackMessage("Welcome back!🔮");
        setSnackType("success");
        setSnackOpen(true);
      } else {
        console.error("Login failed");
        setSnackMessage("Login failed. Please check your credentials.");
        setSnackType("error");
        setSnackOpen(true);
      }
    } catch (error) {
      console.error("Error during login:", error);
      setSnackMessage("An error occurred during login.");
      setSnackType("error");
      setSnackOpen(true);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <label>Username:</label>
        <input
          type="text"
          name="username"
          value={credentials.username}
          onChange={handleChange}
        />
        <label>Password:</label>
        <input
          type="password"
          name="password"
          value={credentials.password}
          onChange={handleChange}
        />
        <button type="submit">Login</button>
      </form>

      <div>
        <h2>New to CovenCraft?</h2>
        <p>No problem! Click below to sign up for a free account!</p>
        <Link to={"/signup"}>
          <button>Sign up</button>
        </Link>
      </div>
    </div>
  );
};

export default Login;
