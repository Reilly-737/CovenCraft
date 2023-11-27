import React from 'react'

const Card = ({ title, description, difficulty }) => {
  return (
    <div className="card">
      <img src="" alt={title} />
      <h2>{title}</h2>
      <p>{description}</p>
      <p>{difficulty}</p>
      <button>Learn more</button>
    </div>
  )
}

export default Card