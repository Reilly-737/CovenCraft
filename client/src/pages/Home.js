import { useEffect, useState } from "react";
import { useOutletContext } from "react-router-dom";
import Card from "../components/Card"

const Home = () => {
    const { setAlertMessage, handleSnackType } = useOutletContext()
    const [crafts, setCrafts] = useState([]);

    useEffect(() => {
        fetch("/crafts")
        .then(resp => resp.json())
            // if (resp.ok) {
            //     resp.json().then(setCrafts)
            // } else {
            //     resp.json().then(errorObj => {
            //         handleSnackType("error");
            //         setAlertMessage(errorObj.message);
            //     })
            // }
        // })
        .then(setCrafts)
        .catch(errorObj => {
            handleSnackType("error");
            setAlertMessage(errorObj.message);
        })
    }, [])

    const allCrafts = crafts?.map(craft => <Card key={craft.id} {...craft}/>)

    return (
        <div>
            <h2>Where magic meets creativity!</h2>
            <p>Join our enchanting workshops, crafted for local witches to brew a cauldron of artistic spells and conjure one-of-a-kind mystical crafts together.</p>
            <div className="container">
                {allCrafts}
            </div>
        </div>
    )
}

export default Home