import { BrowserRouter, Route, Routes } from 'react-router'
import './App.css'
import Account from './pages/Account'

function App() {

  return (
    <BrowserRouter>
    <Routes>
      {/* <Route path="/" element={<Home />} /> */}
      <Route path="account" element={<Account />} />
    </Routes>
    </BrowserRouter>
  )
}

export default App
