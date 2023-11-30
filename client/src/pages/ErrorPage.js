import React from 'react'
import { Link } from 'react-router-dom'
import Header from '../components/Header'

const ErrorPage = () => {
  return (
    <>
      <Header />
      <div id="outlet">
        <div className="one_craft">
          <img src="https://images.unsplash.com/photo-1516035054744-d474c5209db5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="smoke" />
          <h2>Oops!</h2>
          <h3>Seems what you're looking for has gone up in a puff of smoke!</h3>
          <Link to="/">
            <button>Return home</button>
          </Link>
        </div>
      </div>
    </>
  )
}

export default ErrorPage