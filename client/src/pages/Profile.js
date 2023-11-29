import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
//import Snackbar from "@material-ui/core/Snackbar";
//import MuiAlert from "@material-ui/lab/Alert";

const Profile = () => {
  const navigate = useNavigate();
  const { id: userId } = useParams(); // Using useParams to get userId from the route
  const [user, setUser] = useState(null);
  const [bio, setBio] = useState("");
  //const [savedCrafts, setSavedCrafts] = useState([]);
  //const [snackOpen, setSnackOpen] = useState(false);
  //const [snackMessage, setSnackMessage] = useState("");
  //const [snackType, setSnackType] = useState("success");

  useEffect(() => {
    fetchProfile();
  }, [userId]);

  const fetchProfile = () => {
    if (!userId) {
      return;
    }

    fetch(`/witches/${userId}`)
      .then((response) => response.json())
      .then((result) => {
        setUser(result);
        setSavedCrafts(result.savedCrafts);
      })
      .catch((error) => console.error("Error fetching user profile:", error));
  };

  const deleteProfile = () => {
    if (!userId) {
      return;
    }

    fetch(`/witches/${userId}`, { method: "DELETE" })
      .then((response) => {
        if (response.ok) {
          
          //setSnackMessage("Witch's profile vanished into mist.🦇");
          //setSnackType("success");
          //setSnackOpen(true);

          navigate("/");
        } else {
          console.error("Failed to delete profile");
         
          //setSnackMessage("Failed to delete profile.");
          //setSnackType("error");
          //setSnackOpen(true);
        }
      })
      .catch((error) => console.error("Error deleting profile:", error));
  };

  const updateBio = () => {
    if (!userId) {
      return;
    }

    fetch(`/witches/${userId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ bio }),
    })
      .then((response) => {
        if (response.ok) {
          fetchProfile();
          //setSnackMessage("Bio updated successfully.🕷️");
         // setSnackType("success");
         // setSnackOpen(true);
        } else {
          console.error("Sorry! Failed to update bio");
         // setSnackMessage("Failed to update bio.");
        //  setSnackType("error");
         // setSnackOpen(true);
        }
      })
      .catch((error) => console.error("Error updating bio:", error));
  };

  const handleLogout = async () => {
    try {
      const response = await fetch("/logout", {
        method: "DELETE",
      });

      if (response.ok) {
        
       // setSnackMessage("Witch logged out.🌙");
       // setSnackType("success");
       // setSnackOpen(true);

        navigate("/login");
      } else {
        console.error("Logout failed");
        //setSnackMessage("Logout failed.");
        //setSnackType("error");
        //setSnackOpen(true);
      }
    } catch (error) {
      console.error("Error during logout:", error);
     // setSnackMessage("An error occurred during logout.");
     // setSnackType("error");
     // setSnackOpen(true);
    }
  };

  const handleSnackClose = () => {
    setSnackOpen(false);
  };

  return (
    <div>
      {user && (
        <>
          <h2>{user.name}'s Profile</h2>
          <p>Username: {user.username}</p>
          <p>Bio: {user.bio}</p>
          <textarea
            value={bio}
            onChange={(e) => setBio(e.target.value)}
            placeholder="Enter your bio"
          />
          <button onClick={updateBio}>Update Bio</button>
          <button onClick={deleteProfile}>Delete Profile</button>
          <button onClick={handleLogout}>Logout</button>

          <h3>Saved Crafts</h3>
          {savedCrafts.map((craft) => (
            <div key={craft.id}>
              <p>{craft.title}</p>
            </div>
          ))}

          {/* Snackbar for success or error messages 
          <Snackbar
            open={snackOpen}
            autoHideDuration={6000}
            onClose={handleSnackClose}
          >
            <MuiAlert
              elevation={6}
              variant="filled"
              onClose={handleSnackClose}
              severity={snackType}
            >
              {snackMessage}
            </MuiAlert>
          </Snackbar>*/}
        </>
      )}
    </div>
  );
};

export default Profile;
