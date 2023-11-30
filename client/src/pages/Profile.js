import React, { useEffect, useState, useContext } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useOutletContext } from "react-router-dom";

const Profile = () => {
  const navigate = useNavigate();
  const { id: userId } = useParams();
  const [user, setUser] = useState(null);
  const [bio, setBio] = useState("");
  const { setSnackMessage, setSnackType, setSnackOpen } = useOutletContext(); // Use your actual context functions

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
          setSnackMessage("Witch's profile vanished into mist.🦇");
          setSnackType("success");
          setSnackOpen(true);
          navigate("/");
        } else {
          console.error("Failed to delete profile");
          setSnackMessage("Failed to delete profile.");
          setSnackType("error");
          setSnackOpen(true);
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
          setSnackMessage("Bio updated successfully.🕷️");
          setSnackType("success");
          setSnackOpen(true);
        } else {
          console.error("Sorry! Failed to update bio");
          setSnackMessage("Failed to update bio.");
          setSnackType("error");
          setSnackOpen(true);
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
        setSnackMessage("Witch logged out.🌙");
        setSnackType("success");
        setSnackOpen(true);
        navigate("/login");
      } else {
        console.error("Logout failed");
        setSnackMessage("Logout failed.");
        setSnackType("error");
        setSnackOpen(true);
      }
    } catch (error) {
      console.error("Error during logout:", error);
      setSnackMessage("An error occurred during logout.");
      setSnackType("error");
      setSnackOpen(true);
    }
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
        </>
      )}
    </div>
  );
};

export default Profile;
