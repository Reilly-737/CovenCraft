import { useEffect, useState } from "react";
import Card from "../components/Card"

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

    const allCrafts = crafts.map(craft => <Card key={craft.id} {...craft}/>)

    return (
        <div>
            <h2>Where magic meets creativity!</h2>
            <p>Join our enchanting workshops, crafted for local witches to brew a cauldron of artistic spells and conjure one-of-a-kind mystical crafts together.</p>
            <div>
                {allCrafts}
            </div>
        </div>
    )
}

export default Home