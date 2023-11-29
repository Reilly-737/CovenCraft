import { Link, NavLink } from "react-router-dom";

const Header = ({ user }) => {

  return (
    <div id="header">
      <NavLink to={"/"}>
        <h1>CovenCraft</h1>
      </NavLink>
      {user ? (
        <Link to={"/logout"}>
        <button>Logout</button>
        </Link>) : (
        <Link to={"/login"}>
        <button>Login</button>
        </Link>
      )}
    </div>
  )
}

export default Header