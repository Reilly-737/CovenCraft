import { useEffect, useState } from 'react'
import { useOutletContext, useParams } from 'react-router-dom'

const ViewOne = () => {
  const { setAlertMessage, handleSnackType } = useOutletContext()
  const { id } = useParams()
  const [craft, setCraft] = useState({})
  const { image, title, description, instructions, difficulty, materials, witches } = craft

  useEffect(() => {
    fetch(`/crafts/${id}`)
    .then(resp => resp.json())
    .then(setCraft)
    .catch(errorObj => {
        handleSnackType("error");
        setAlertMessage(errorObj.message);
    })
  }, [id])

  const materials_list = materials?.map(material => <li key={material["name"]}>{material["name"]}</li>)
  const witch_list = witches?.map(witch => <li key={witch["username"]}>{witch["username"]}</li>)

  return (
    <div className="one_craft">
      <img src={image} alt={title} />

      <div className='container'>
        <main className="craft_details">
          <h2>{title}</h2>
          <p className="subtle">{difficulty}</p>
          <p>{description}</p>
          <p>{instructions}</p>
          <ul>{materials_list}</ul>
          <button>Save craft</button>
        </main>
        <aside>
          <h3>Coven Crafters:</h3>
          <ul>{witch_list}</ul>
        </aside>
      </div>
    </div>
  )
}

export default ViewOne