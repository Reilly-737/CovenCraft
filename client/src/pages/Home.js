import { useEffect, useState } from "react";

const Home = () => {
    const [crafts, setCrafts] = useState([]);

    useEffect(() => {
        fetch("/crafts")
        .then(resp => {
            if (resp.ok) {
                resp.json().then(setCrafts)
            } else {
                resp.json().then(errorObj => {
                    console.log(errorObj.message)
                    // handleError(errorObj.message)
                })
            }
        })
        // .catch(handleError)
    }, [])

    return (
        <div>Home</div>
    )
}

export default Home