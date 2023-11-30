import { useState } from "react";
import { useNavigate, Link, useOutletContext } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  const { updateUser, setAlertMessage, handleSnackType } = useOutletContext()
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

    fetch("/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(credentials),
    })
    .then(resp => {
      if (resp.ok) {
        resp.json().then(userObj => {
          updateUser(userObj)
          return userObj
        })
        .then(userObj => navigate(`/profile/${userObj.id}`))
      } else {
        resp.json().then(err => {
          handleSnackType("error")
          setAlertMessage(err.message)
        })
      }
    })
    .catch(errObj => {
      handleSnackType("error");
      setAlertMessage("An error occurred during login.")
    })
  };

  return (
    <div className="main">
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
