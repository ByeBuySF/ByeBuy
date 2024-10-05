import { Outlet } from "react-router-dom";

import Header from './routes/Header/Header';
import Footer from './routes/Footer/Footer';

import './App.css'

function App() {

  return (
    <>
      <Header />

      <Outlet />

      <Footer/>
    </>
  )
}

export default App
