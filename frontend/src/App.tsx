import { BrowserRouter, Route, Routes } from 'react-router'
import Account from './pages/Account'
import SignUp from './pages/SignUp'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#8A4FFF',
    },
  },
})

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Account />} />
          <Route path='signup' element={<SignUp />} />
          <Route path='account' element={<Account />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  )
}
