import { useEffect, useState } from "react";
import { useOutletContext, useNavigate, Link, useParams } from "react-router-dom";
import Card from "../components/Card";

const Profile = () => {
  const { id } = useParams()
  const { user, updateUser, setAlertMessage, handleSnackType } = useOutletContext()
  const [userInfo, setUserInfo] = useState({})
  const navigate = useNavigate();
  
  useEffect(() => {
    if (user) {
      if (user.id !== Number(id)) {
        navigate("/")
      }

      fetch(`/witches/${id}`)
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
          updateUser(null)
        } else {
          handleSnackType("error");
          setAlertMessage("Failed to delete profile.");
        }
      })
      .catch(error => {
        handleSnackType("error");
        setAlertMessage(error.message);
      })
  };

  const allCrafts = userInfo.crafts?.map(craft => <Card key={craft.id} {...craft}/>)

  return (
    <div>
      {user && (
        <>
          <div className="main">
            <h2>{userInfo.username}'s Profile</h2>
            <p>Username: {userInfo.username}</p>
            <p>Bio: {userInfo.bio}</p>

            <div className="buttons">
              <Link to="/profile/edit">
                <button>Edit Profile</button>
              </Link>
              <button onClick={deleteProfile}>Delete Profile</button>
            </div>
          </div>
        </>
      )}
      <div className="container">
        {allCrafts}
      </div>
    </div>
  );
};

export default Profile;
