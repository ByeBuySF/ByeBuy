import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider, } from "react-router-dom";

import App from './App.tsx'
import ErrorPage from './routes/ErrorPage/ErrorPage.tsx';

import LandingPage from './routes/LandingPage/LandingPage';
import Register from './routes/Register/Register';
import Login from './routes/Login/Login';
import Upload from './routes/Upload/Upload';
import Results from './routes/Results/Results';


import './index.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "home/",
        element: <LandingPage />,
      },
      {
        path: "register/",
        element: <Register />,
      },
      {
        path: "login/",
        element: <Login />,
      },
      {
        path: "upload/",
        element: <Upload />,
      },
      {
        path: "results/",
        element: <Results />,
      },
    ],
  },
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
