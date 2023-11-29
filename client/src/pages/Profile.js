import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";

const Profile = () => {
  const navigate = useNavigate();
  const { id: userId } = useParams(); // Using useParams to get userId from the route
  const [user, setUser] = useState(null);
  const [savedCrafts, setSavedCrafts] = useState([]);
  const [bio, setBio] = useState("");

  useEffect(() => {
    fetchProfile();
    fetchSavedCrafts();
  }, [userId]);

  const fetchProfile = () => {
    if (!userId) {
      return;
    }

    fetch(`/witches/${userId}`)
      .then((response) => response.json())
      .then((result) => setUser(result))
      .catch((error) => console.error("Error fetching user profile:", error));
  };

  const fetchSavedCrafts = () => {
    if (!userId) {
      return;
    }

    fetch(`/witches/${userId}/listSavedCrafts`)
      .then((response) => response.json())
      .then((result) => setSavedCrafts(result))
      .catch((error) => console.error("Error fetching saved crafts:", error));
  };

  const deleteProfile = () => {
    if (!userId) {
      return;
    }

    fetch(`/witches/${userId}`, { method: "DELETE" })
      .then((response) => {
        if (response.ok) {
          navigate("/");
        } else {
          console.error("Failed to delete profile");
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
        } else {
          console.error("Sorry! Failed to update bio");
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
        navigate("/login");
      } else {
        console.error("Logout failed");
      }
    } catch (error) {
      console.error("Error during logout:", error);
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

          <h3>Saved Crafts</h3>
          {savedCrafts.map((craft) => (
            <div key={craft.id}>
              <p>{craft.title}</p>
            </div>
          ))}
        </>
      )}
    </div>
  );
};

export default Profile;
