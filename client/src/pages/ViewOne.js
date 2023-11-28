import { useEffect, useState } from 'react'
import { useOutletContext, useParams } from 'react-router-dom'

const ViewOne = () => {
  const { setAlertMessage, handleSnackType } = useOutletContext()
  const { id } = useParams()
  const [craft, setCraft] = useState({})
  const { image, title, description, instructions, difficulty, materials } = craft

  useEffect(() => {
    fetch(`/crafts/${id}`)
    .then(resp => resp.json())
    .then(setCraft)
    .catch(errorObj => {
        handleSnackType("error");
        setAlertMessage(errorObj.message);
    })
  }, [id])

  const materials_list = materials?.map(material => <li>{material["name"]}</li>)

  return (
    <div className="one_craft">
      <main>
        <h2>{title}</h2>
        <p>{difficulty}</p>
        <img src={image} alt={title} />
        <p>{description}</p>
        <p>{instructions}</p>
        <ul>{materials_list}</ul>
      </main>
      <aside>

      </aside>
    </div>
  )
}

export default ViewOne