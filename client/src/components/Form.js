import React from 'react'
import { useState, useEffect } from "react";
import { object, string, number } from "yup";
import { useOutletContext, useNavigate } from "react-router-dom";
import PasswordStrengthBar from "react-password-strength-bar";
import bcrypt from "bcryptjs";

const URL = "http://localhost:3005/witches/<int:id>"; 

const initialValue = {
  username: "",
  email: "",
  password: "",
  bio: "",
};

const formSchema = object().shape({
  username: string().required("Username is required"),
  email: string().email("Invalid email address").required("Email is required"),
  password: string()
    .min(4, "Password must be at least 8 characters long")
    .required("Password is required"),
  bio: string().required("Bio is required"),
});

const Form = ({ edit }) => {
  const navigate = useNavigate();
  const { setAlertMessage, handleSnackType, user } = useOutletContext();
  const [formData, setFormData] = useState(initialValue);
  const [readyToSubmit, setReadyToSubmit] = useState(false);

  useEffect(() => {
    if (user) {
      setFormData({
        username: user.username || "",
        email: user.email || "",
        password: "", 
        bio: user.bio || "",
      });
    }
  }, [user]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    let newForm = { ...formData, [name]: value };
    setFormData(newForm);

    formSchema
      .validate(newForm)
      .then(() => {
        setReadyToSubmit(true);
      })
      .catch(() => {
        setReadyToSubmit(false);
      });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const url = `${URL}/${user?.id || ""}`;
    const method = user ? "PATCH" : "POST";

    try {
      const validData = await formSchema.validate(formData);
      const hash = !edit
        ? await new Promise((resolve, reject) => {
            bcrypt.hash(validData.password, 10, (err, hash) => {
              if (err) {
                reject(err);
              } else {
                resolve(hash);
              }
            });
          })
        : validData.password;

      const processedForm = { ...validData, password: hash };

      fetch(url, {
        method,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(processedForm),
      })
        .then((resp) => resp.json())
        .then((userData) => {
          updateState(userData)
          navigate("/witches")
        })
        .catch((err) => {
          showErrorToUser(err.message)
        });
    } catch (err) {
      showValidationErrorsToUser(err.message);
    }
  };

  return (
    <div>
      <div className="form-div">
        <form onSubmit={handleSubmit}>
          <label htmlFor="username" className="col-3">
            Username:
            <input
              type="text"
              name="username"
              id="username"
              value={formData.username}
              onChange={handleChange}
            />
          </label>
          <label htmlFor="email" className="col-3">
            Email:
            <input
              type="text"
              name="email"
              id="email"
              value={formData.email}
              onChange={handleChange}
            />
          </label>
          <label htmlFor="bio" className="col-6">
            Bio:
            <textarea
              name="bio"
              id="bio"
              value={formData.bio}
              onChange={handleChange}
            />
          </label>
          {!edit && (
            <label htmlFor="password" className="col-6">
              Password:
              <input
                type="password"
                name="password"
                id="password"
                value={formData.password}
                onChange={handleChange}
              />
              <PasswordStrengthBar
                style={{ width: "30%" }}
                password={formData.password}
              />
            </label>
          )}

          {readyToSubmit ? (
            <input
              type="submit"
              value="Submit"
              className="btn-large bg-yellow larger-text"
            />
          ) : (
            <input
              type="submit"
              value="Submit"
              disabled
              className="btn-large bg-yellow larger-text"
            />
          )}
        </form>
      </div>
    </div>
  );
};

export default Form;

