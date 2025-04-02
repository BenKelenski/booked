import {
  Button,
  Card,
  Container,
  Divider,
  FormControl,
  Stack,
  TextField,
  Typography,
} from '@mui/material'
import { createFileRoute, useNavigate } from '@tanstack/react-router'
import {
  ColoredAppleIcon,
  ColoredFacebookIcon,
  ColoredGoogleIcon,
} from '../components/CustomIcons'
import { useState } from 'react'
import createNewUser from '../api/UserService'
import { CreateUserRequest } from '../common/types'

export const Route = createFileRoute('/signup')({
  component: SignUp,
})

function SignUp() {
  const navigate = useNavigate()

  const [nameError, setNameError] = useState(false)
  const [nameErrorMessage, setNameErrorMessage] = useState('')
  const [emailError, setEmailError] = useState(false)
  const [emailErrorMessage, setEmailErrorMessage] = useState('')
  const [passwordError, setPasswordError] = useState(false)
  const [passwordErrorMessage, setPasswordErrorMessage] = useState('')

  const validateInputs = (
    name: HTMLInputElement,
    email: HTMLInputElement,
    password: HTMLInputElement
  ) => {
    let isValid = true

    if (!name.value || name.value.length <= 4) {
      isValid = false
      setNameError(true)
      setNameErrorMessage('Name is required and must be at least 5 characters')
    }

    if (!email.value || !email.value.includes('@')) {
      isValid = false
      setEmailError(true)
      setEmailErrorMessage('Email is required and must be valid')
    }

    if (!password.value || password.value.length < 8) {
      isValid = false
      setPasswordError(true)
      setPasswordErrorMessage(
        'Password is required and must be at least 8 characters'
      )
    }

    return isValid
  }

  const handleSignUp = async () => {
    const name = document.getElementById('name') as HTMLInputElement
    const email = document.getElementById('email') as HTMLInputElement
    const password = document.getElementById('password') as HTMLInputElement
    if (validateInputs(name, email, password)) {
      let newUserData: CreateUserRequest ={
        name: name.value,
        password: password.value,
      }
      const response = await createNewUser(newUserData)
      console.log(response)
      localStorage.setItem('user', JSON.stringify(response))
      navigate({ to: '/account' })
    }
  }

  return (
    <Container maxWidth='sm' sx={{ height: '100%' }}>
      <Stack
        direction='row'
        spacing={2}
        sx={{
          paddingTop: 6,
          paddingBottom: 4,
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Typography color='primary' variant='h3'>
          booked
        </Typography>
      </Stack>
      <Stack
        direction='column'
        spacing={2}
        sx={{
          justifyContent: 'center',
          alignItems: 'flex-start',
        }}
      >
        <Card sx={{ width: '100%', padding: 2 }}>
          <Stack
            direction='column'
            spacing={2}
            sx={{
              justifyContent: 'center',
              alignItems: 'stretch',
            }}
          >
            <Typography color='primary' component='h1' variant='h4'>
              Sign Up
            </Typography>
            <FormControl>
              <Typography color='primary' variant='h6'>
                name
              </Typography>
              <TextField
                error={nameError}
                helperText={nameErrorMessage}
                id='name'
                type='text'
                name='name'
                placeholder='John Doe'
                autoFocus
                required
                fullWidth
                variant='outlined'
              />
            </FormControl>
            <FormControl>
              <Typography color='primary' variant='h6'>
                email
              </Typography>
              <TextField
                error={emailError}
                helperText={emailErrorMessage}
                id='email'
                type='email'
                name='email'
                placeholder='your@email.com'
                required
                fullWidth
                variant='outlined'
              />
            </FormControl>
            <FormControl>
              <Typography color='primary' variant='h6'>
                password
              </Typography>
              <TextField
                error={passwordError}
                helperText={passwordErrorMessage}
                id='password'
                type='password'
                name='password'
                placeholder='*********'
                required
                fullWidth
                variant='outlined'
              />
              <Typography color='primary' variant='subtitle1'>
                Minimum 8 characters
              </Typography>
            </FormControl>
            <Button
              type='submit'
              size='large'
              variant='contained'
              onClick={handleSignUp}
            >
              Submit
            </Button>
            <Divider orientation='horizontal' variant='fullWidth'>
              or
            </Divider>
            <Button
              fullWidth
              variant='outlined'
              onClick={() => alert('Sign in with Google')}
              startIcon={<ColoredGoogleIcon />}
            >
              Sign in with Google
            </Button>
            <Button
              fullWidth
              variant='outlined'
              onClick={() => alert('Sign in with Google')}
              startIcon={<ColoredFacebookIcon />}
            >
              Sign in with Facebook
            </Button>
            <Button
              fullWidth
              variant='outlined'
              onClick={() => alert('Sign in with Apple')}
              startIcon={<ColoredAppleIcon />}
            >
              Sign in with Apple
            </Button>
          </Stack>
        </Card>
      </Stack>
    </Container>
  )
}

export default SignUp
