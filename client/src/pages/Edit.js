import { useOutletContext } from "react-router-dom";
import Form from "../components/Form";

const Edit = () => {
  const { user, setAlertMessage, handleSnackType } = useOutletContext()

  return (
    <div className="main">
      <h2>Edit Profile</h2>
      <div>
        <Form user={user} />
      </div>
    </div>
  )
}

export default Edit