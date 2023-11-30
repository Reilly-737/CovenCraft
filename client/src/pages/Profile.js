import { useEffect, useState } from "react";
import { useOutletContext, useNavigate, Link } from "react-router-dom";
import Card from "../components/Card";

const Profile = () => {
  // const { id: userId } = useParams();
  // const [user, setUser] = useState(null);
  // const [bio, setBio] = useState("");
  const { user, setAlertMessage, handleSnackType } = useOutletContext()
  const [userInfo, setUserInfo] = useState({})
  const navigate = useNavigate();
  
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

  const deleteProfile = () => {
    if (!user) {
      return;
    }

    fetch(`/witches/${user.id}`, { method: "DELETE" })
      .then((response) => {
        if (response.ok) {
          handleSnackType("success");
          setAlertMessage("Witch's profile vanished into mist.🦇");
          navigate("/");
        } else {
          console.error("Failed to delete profile");
          handleSnackType("error");
          setAlertMessage("Failed to delete profile.");
        }
      })
      .catch((error) => console.error("Error deleting profile:", error));
  };

  const allCrafts = userInfo.crafts?.map(craft => <Card key={craft.id} {...craft}/>)

  return (
    <>
      {user && (
        <>
          <div className="main">
            <h2>{userInfo.username}'s Profile</h2>
            <p>Username: {userInfo.username}</p>
            <p>Bio: {userInfo.bio}</p>
          </div>
          <div className="main">
            <Link to="/edit">
              <button>Edit Profile</button>
            </Link>
            <button onClick={deleteProfile}>Delete Profile</button>
          </div>
        </>
      )}
      <div className="container">
        {allCrafts}
      </div>
    </>
  );
};

export default Profile;
