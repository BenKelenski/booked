import * as React from 'react'
import {
  Box,
  Button,
  Card,
  Container,
  Divider,
  FormControl,
  IconButton,
  Stack,
  TextField,
  Typography,
} from '@mui/material'
import {
  AppleIcon,
  ColoredAppleIcon,
  ColoredFacebookIcon,
  ColoredGoogleIcon,
  FacebookIcon,
  GoogleIcon,
} from '../components/CustomIcons'

const SignUp = () => {
  const [nameError, setNameError] = React.useState(false)
  const [nameErrorMessage, setNameErrorMessage] = React.useState('')
  const [emailError, setEmailError] = React.useState(false)
  const [emailErrorMessage, setEmailErrorMessage] = React.useState('')
  const [passwordError, setPasswordError] = React.useState(false)
  const [passwordErrorMessage, setPasswordErrorMessage] = React.useState('')

  const validateInputs = () => {
    const name = document.getElementById('name') as HTMLInputElement
    const email = document.getElementById('email') as HTMLInputElement
    const password = document.getElementById('password') as HTMLInputElement

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
  }

  return (
    <Container maxWidth='sm'>
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
              onClick={validateInputs}
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
