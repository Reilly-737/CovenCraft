import React from 'react'

const Home = () => {
    const [crafts, setCrafts] = useState([]);

    useEffect(() => {
        fetch("/crafts")
        .then(resp => {
            if (resp.ok) {
                resp.json().then(setCrafts)
            } else {
                response.json().then(errorObj => handleError(errorObj.message))
            }
        })
        .catch(handleError)
    }, [])

    return (
        <div>Home</div>
    )
}

export default Home