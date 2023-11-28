import React, {useState, useEffect} from 'react';
import { Link, useNavigate } from "react-router-dom";
import Card from "../components/Card"


const Profile = () => {
  const navigate = useNavigate()
  const [user, setUser] = useState(null);
  const [savedCrafts, setSavedCrafts] = useState([]);

  // Placeholder data
  const initialSavedCrafts = [
    { id: 1, title: "Craft 1" },
    { id: 2, title: "Craft 2" },
  ];

  useEffect(() => {
    // Fetch user profile data 
    fetchProfile(); 
  }, []);

  // function for fetching user profile
  const fetchProfile = () => {
    // logic need to go here
    // setUser(result); // Set the user state with the fetched data
    setUser({
      name: "Ribbit Robbit",
      username: "frog_queen",
      bio: "Bow Down To The Frog Queen!",
    });
    setSavedCrafts(initialSavedCrafts);
  };

  // functions for saving, editing, and deleting crafts
  const saveCraft = (craft) => {
    // logic!
    setSavedCrafts((prevCrafts) => [...prevCrafts, craft]);
  };

  const editProfile = () => {
    // logic!
  };

  const deleteProfile = () => {
    // logic
    navigate("/"); // to go back home
  };

  const removeSavedCraft = (craftId) => {
    // logic
    setSavedCrafts((prevCrafts) =>
      prevCrafts.filter((craft) => craft.id !== craftId)
    );
  };

  return (
    <div>
      {user && (
        <>
          <h2>{user.name}'s Profile</h2>
          <p>Username: {user.username}</p>
          <p>Bio: {user.bio}</p>
          {/* logic */}
          <Link to="/edit-profile">Edit Profile</Link>
          <button onClick={deleteProfile}>Delete Profile</button>

          <h3>Saved Crafts</h3>
          {savedCrafts.map((craft) => (
            <Card
              key={craft.id}
              craft={craft}
              onSave={() => saveCraft(craft)}
              onRemove={() => removeSavedCraft(craft.id)}
              editable
            />
          ))}
        </>
      )}
    </div>
  );
};

export default Profile;