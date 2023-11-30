import { useOutletContext } from "react-router-dom";
import Form from "../components/Form";

const Signup = () => {
  const { setAlertMessage, handleSnackType } = useOutletContext()

  return (
    <div className="main">
      <h2>Create Profile</h2>
      <div>
        <Form />
      </div>
    </div>
  )
}

export default Signup