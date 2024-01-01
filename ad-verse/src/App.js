import Landingpage from "./pages/landingpage"
import Productpage from "./pages/productpage"
// import Navbar from "./components/navbar"
import './index.css';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

function App() {
 

  return (
    <div className="max-sm:p-6 max-w-screen-xl flex flex-col  items-center justify-between mx-auto bg-amber-400">
    <div className="max-w-md w-full space-y-8">
     <BrowserRouter>
        <Routes>
            <Route path="/" element={<Landingpage/>} />
            <Route path="/product" element={<Productpage/>} />
        </Routes>
      </BrowserRouter>
    </div>
    </div>
  )
}

export default App