import React, { useState } from "react";
import { useState } from "react";
import { useOutletContext } from "react-router-dom";
import styled from "styled-components";
import { useFormik } from "formik";
import * as yup from "yup";
import { useOutletContext } from "react-router-dom";

const Signup = () => {
  const { setAlertMessage, handleSnackType } = useOutletContext();
  const [snackbar, setSnackbar] = useState({
    // open: false,
    // message: "",
    // type: "success",
  });
function SignUp({ updateUser }) {
  const [signUp, setSignUp] = useState(true); // Set to true for sign-up only
  const { user, setAlertMessage, handleSnackType } = useOutletContext();
  const handleClick = () => setSignUp(true); // Always set to true for sign-up

  const signupSchema = yup.object().shape({
    username: yup.string().required("Please enter a witch name"),
    email: yup
      .string()
      .email("Must be a valid email")
      .required("Please enter an email"),
    password: yup
      .string()
      .required("Please enter a witchy password")
      .min(8, "Password is too short - should be 8 chars minimum.")
      .matches(/[a-zA-Z0-9]/, "Password can only contain letters and numbers."),
  });

  const url = signUp ? "/signup" : "/edit";

  const formik = useFormik({
    initialValues: {
      // Define your form fields here
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
    validationSchema: yup.object({
      // Define validation rules using yup
      username: yup.string().required("Username is required"),
      email: yup
        .string()
        .email("Invalid email address")
        .required("Email is required"),
      password: yup
        .string()
        .required("Password is required")
        .min(6, "Password must be at least 6 characters"),
      confirmPassword: yup
        .string()
        .oneOf([yup.ref("password"), null], "Passwords must match"),
    }),
    onSubmit: async (values) => {
      try {
        // Make a POST request to your Flask API endpoint
        const response = await fetch("/witch", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values),
        });

        // Check if the response is successful (you may need to adjust this based on your actual API response)
        if (response.ok) {
          setAlertMessage("Welcome to the Coven!");
          handleSnackType("success");
        } else {
          const data = await response.json();
          setAlertMessage(data.error || "An error occurred during signup.");
          handleSnackType("error");
        }
      } catch (error) {
        // Handle network errors or other exceptions
        setAlertMessage("An error occurred during signup.");
        handleSnackType("error");
      }
    validationSchema: signUp ? signupSchema : null,
    onSubmit: (values) => {
      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((res) => {
          if (res.ok) {
            res.json().then(updateUser);
          } else {
            res.json().then(errorObj => {
              handleSnackType("error")
              setAlertMessage(errorObj.message)
          });
          }
        })
        .catch(errorObj => {
          handleSnackType("error")
          setAlertMessage(errorObj.message)
      });
    },
  });

  return (
    <div>
      <h2>Sign Up</h2>
      <form onSubmit={formik.handleSubmit}>
        {/* Username Field */}
        <div>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            name="username"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.username}
          />
          {formik.touched.username && formik.errors.username && (
            <div className="error">{formik.errors.username}</div>
          )}
        </div>

        {/* Email Field */}
        <div>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.email}
          />
          {formik.touched.email && formik.errors.email && (
            <div className="error">{formik.errors.email}</div>
          )}
        </div>

        {/* Password Field */}
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.password}
          />
          {formik.touched.password && formik.errors.password && (
            <div className="error">{formik.errors.password}</div>
          )}
        </div>

        {/* Submit Button */}
        <div>
          <button type="submit">Sign Up</button>
        </div>
      </form>
    </div>
  );
};

export default Signup;
