import { useEffect, useState } from "react";
import { useOutletContext } from "react-router-dom";
import FormComp from "../components/Form";

const Edit = () => {
  const { user, setAlertMessage, handleSnackType } = useOutletContext()
  const [userInfo, setUserInfo] = useState({})

  useEffect(() => {
    if (user) {
      fetch(`/witches/${user.id}`)
      .then(resp => {
        if (resp.ok) {
          resp.json().then(setUserInfo)
        } else {
          resp.json().then(err => {
            handleSnackType("error")
            setAlertMessage(err.message)
          })
        }
      })
      .catch(err => {
        handleSnackType("error")
        setAlertMessage(err.message)
      })
    }
  }, [user])

  return (

    <div className="main">
      <h2>Edit Profile</h2>
      <div>
        <FormComp userInfo={userInfo} />
      </div>
    </div>
  )
}

export default Edit