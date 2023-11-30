import { Link, NavLink, useNavigate } from "react-router-dom";

const Header = ({ user, updateUser, setAlertMessage, handleSnackType }) => {
  const navigate = useNavigate()

  const handleLogout = () => {
    fetch("/logout", {method: "DELETE"})
    .then(() => {
      updateUser(null)
      navigate("/")
    })
    .catch(err => {
      handleSnackType("error")
      setAlertMessage(err.message)
    })
  }

  return (
    <div id="header">
      <NavLink to={"/"}>
        <h1>CovenCraft</h1>
      </NavLink>
      <>
        {user ? (
          <div>
            <Link to={`/profile/${user.id}`}>
              <button>Profile</button>
            </Link>
            <button onClick={handleLogout}>Logout</button>
          </div>
        ) : (
          <Link to={"/login"}>
            <button>Login</button>
          </Link>
        )}
      </>
    </div>
  );
}

export default Header