
import Landingpage from "./pages/landingpage"
import Productpage from "./pages/productpage"
// import Navbar from "./components/navbar"


function App() {
 

  return (
    <div className="max-sm:p-6 max-w-screen-xl flex flex-col  items-center justify-between mx-auto">
    <Landingpage/>
    <Productpage/>
    </div>
  )
}

export default App