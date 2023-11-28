import React from 'react'
import {Link} from 'react-router-dom';

const Header = () => {
  return (
    <div id="header">
      <h1>CovenCraft</h1>
      <Link to="/login">
        <button>Login</button>
      </Link>
      <Link to="/profile">
        <button>Profile</button>
      </Link>
    </div>
  );
}

export default Header