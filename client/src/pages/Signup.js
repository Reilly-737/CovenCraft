import { useState } from "react";
import { useOutletContext } from "react-router-dom";
import styled from "styled-components";
import { useFormik } from "formik";
import * as yup from "yup";

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
      username: "",
      email: "",
      password: "",
    },
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
    <>
      <div>
        <h2>Join The Coven!</h2>
      </div>
      <Form onSubmit={formik.handleSubmit}>
        <label htmlFor="email">Email</label>
        <input
          type="text"
          name="email"
          value={formik.values.email}
          onChange={formik.handleChange}
        />
        {formik.errors.email ? (
          <div className="error-message show">{formik.errors.email}</div>
        ) : null}
        {signUp && (
          <>
            <label htmlFor="username">Username</label>
            <input
              type="text"
              name="username"
              value={formik.values.username}
              onChange={formik.handleChange}
            />
            {formik.errors.username ? (
              <div className="error-message show">{formik.errors.username}</div>
            ) : null}
          </>
        )}
        <label htmlFor="password">Password</label>
        <input
          type="password"
          name="password"
          value={formik.values.password}
          onChange={formik.handleChange}
        />
        {formik.errors.password ? (
          <div className="error-message show">{formik.errors.password}</div>
        ) : null}
        <input type="submit" value="Sign Up!" />
      </Form>
    </>
  );
}

export default SignUp;
