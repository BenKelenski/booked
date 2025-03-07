import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import Button from '@mui/material/Button'
import IconButton from '@mui/material/IconButton'
import MenuIcon from '@mui/icons-material/Menu'

interface Props {
  title: string
  isLoggedIn: boolean
  username?: string
}

const NavBar = ({ title, isLoggedIn, username }: Props) => {
  return (
    <Box sx={{ flexGrow: 1, marginTop: 2 }}>
      <AppBar position='static' sx={{ borderRadius: 2 }}>
        <Toolbar>
          <IconButton
            size='large'
            edge='start'
            color='primary'
            aria-label='menu'
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant='h6' component='div' sx={{ flexGrow: 1 }} color='primary'>
            {title}
          </Typography>
          <Button color='primary'>{isLoggedIn ? username : 'Login'}</Button>
        </Toolbar>
      </AppBar>
    </Box>
  )
}

export default NavBar
