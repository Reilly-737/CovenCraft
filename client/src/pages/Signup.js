import React, { useState } from "react";
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
