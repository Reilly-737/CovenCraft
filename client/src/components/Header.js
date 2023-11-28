import { Link, NavLink } from "react-router-dom";

const Header = () => {
  return (
    <div id="header">
      <NavLink to={"/"}>
        <h1>CovenCraft</h1>
      </NavLink>
      <Link to={"/login"}>
        <button>Login</button>
      </Link>
    </div>
  );
}

export default Header