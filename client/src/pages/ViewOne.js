import { useEffect, useState } from 'react'
import { useOutletContext, useParams } from 'react-router-dom'

const ViewOne = () => {
  const { user, setAlertMessage, handleSnackType } = useOutletContext()
  const { id } = useParams()
  const [craft, setCraft] = useState({})
  const { image, title, description, instructions, difficulty, materials, witches } = craft

  useEffect(() => {
    fetch(`/crafts/${id}`)
    .then(resp => resp.json())
    .then(setCraft)
    .catch(errorObj => {
        handleSnackType("error")
        setAlertMessage(errorObj.message)
    })
  }, [id])

  const handleSaveCraft = () =>{
    fetch('/witch_crafts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ craft_id: id }),
    })
      .then((resp) => resp.json())
      .then(data => {
        handleSnackType("success")
        setAlertMessage("Craft added!")
      })
      .catch(errorObj => {
        handleSnackType("error");
        setAlertMessage(errorObj.message)
      })
  }

  const handleDeleteCraft = (id) =>{
    fetch(`/witch_crafts/${id}`, {
      method: 'DELETE',
    })
      .then((resp) => resp.json())
      .then(data => {
        handleSnackType("success")
        setAlertMessage("Craft removed!")
      })
      .catch(errorObj => {
        handleSnackType("error")
        setAlertMessage(errorObj.message)
      })
  }

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
          { user ? (
            <button onClick={() => handleDeleteCraft(id)}>Remove craft</button> ) : (
            <button onClick={handleSaveCraft}>Save craft</button>
          )}
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