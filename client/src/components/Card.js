import React from 'react'

const Card = ({ image, title, description, difficulty }) => {
  return (
    <div className="card">
      <img src={image} alt={title} />
      <div className="details">
        <h2>{title}</h2>
        <div className="hidden">
          <p>{description}</p>
          <p>{difficulty}</p>
          <button>Learn more</button>
        </div>
      </div>
    </div>
  )
}

export default Card