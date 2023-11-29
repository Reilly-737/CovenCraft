import { useEffect, useState } from "react"
import { useOutletContext } from "react-router-dom"
import Card from "../components/Card"
// import SearchFilter from "../components/SearchFilter"

const Home = () => {
    const { setAlertMessage, handleSnackType } = useOutletContext()
    const [crafts, setCrafts] = useState([])
    const [searchTerm, setSearchTerm] = useState("")

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
            handleSnackType("error")
            setAlertMessage(errorObj.message)
        })
    }, [])

    const newSearch = (e) => setSearchTerm(e.target.value);

    const allCrafts = crafts?.filter(
        (craft) =>
        (craft.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        craft.description.toLowerCase().includes(searchTerm.toLowerCase())) || 
        (craft.instructions.toLowerCase().includes(searchTerm.toLowerCase()) || 
        craft.materials.toLowerCase().includes(searchTerm.toLowerCase()))
      )
      .map(craft => <Card key={craft.id} {...craft}/>)

    return (
        <div>
            <div>
                <h2>Where magic meets creativity!</h2>
                <p>Join our enchanting workshops, crafted for local witches to brew a cauldron of artistic spells and conjure one-of-a-kind mystical crafts together.</p>
            </div>
            {/* <SearchFilter searchTerm={searchTerm} newSearch={newSearch} /> */}
            
            <div className="container">
                {allCrafts}
            </div>
        </div>
    )
}

export default Home