// import

const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage />,
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
            {
                path: "/profile/edit",
                element: <Edit />,
            }
        ],
    },
];

export default routes;