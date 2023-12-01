import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const FormComp = ({ userInfo }) => {

  return (
    <Formik
      initialValues={{ 
        username: '' && userInfo.username, 
        email: '' && userInfo.email, 
        bio: '' && userInfo.bio, 
        password: '' }
      }
      validationSchema={Yup.object({
        username: Yup.string()
          .min(3, 'Must be at least 3 characters')
          .required('Required'),
        email: Yup.string().email('Invalid email address').required('Required'),
        bio: Yup.string()
          .min(50, 'Must be at least 50 characters')
          .required('Required'),
        password: Yup.string()
          .min(8, 'Must be at least 8 characters')
          .required('Required'),
      })}
      onSubmit={(values, { setSubmitting }) => {
        setTimeout(() => {
          alert(JSON.stringify(values, null, 2));
          setSubmitting(false);
        }, 400);
      }}
    >
      <Form>
        <label htmlFor="username">Username</label>
        <Field name="username" type="text" className="block" />
        <ErrorMessage name="username" className="block" />

        <label htmlFor="email">Email Address</label>
        <Field name="email" type="email" className="block" />
        <ErrorMessage name="email" className="block" />

        <label htmlFor="bio">Bio</label>
        <Field name="bio" type="textarea" className="block textarea" />
        <ErrorMessage name="bio" className="block" />

        <label htmlFor="password">Password</label>
        <Field name="password" type="text" className="block" />
        <ErrorMessage name="password" className="block" />

        <button type="submit">Submit</button>
      </Form>
    </Formik>
  );
};

export default FormComp