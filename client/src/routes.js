import App from "./App"
import Home from "./pages/Home"
import ViewOne from "./pages/ViewOne"
import Signup from "./pages/Signup"
import Login from "./pages/Login"
// import Edit from "./pages/Edit"
// import ErrorPage from "./pages/ErrorPage"

const routes = [
    {
        path: "/",
        element: <App />,
        // errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                index: true,
                element: <Home />,
            },
            {
                path: "/crafts/:id",
                element: <ViewOne />,
            },
            {
                path: "/signup",
                element: <Signup />,
            },
            {
                path: "/login",
                element: <Login />,
            },
            {
                path: "/profile/:id",
                element: <ViewOne />,
            },
            // {
            //     path: "/profile/edit",
            //     element: <Edit />,
            // }
        ],
    },
];

export default routes;