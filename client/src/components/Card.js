import React from 'react'

const Card = ({ name, description, difficulty }) => {
  return (
    <div className="card">
      <img src="" alt={name} />
      <h2>{name}</h2>
      <p>{description}</p>
      <p>{difficulty}</p>
      <button>Learn more</button>
    </div>
  )
}

export default Card