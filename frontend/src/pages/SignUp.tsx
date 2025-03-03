import {
  Card,
  Container,
  FormControl,
  FormLabel,
  Stack,
  TextField,
  Typography,
} from '@mui/material'
import Box from '@mui/material/Box'

const SignUp = () => {
  return (
    <Container maxWidth="sm">
      <Stack
        direction="column"
        spacing={2}
        sx={{
          justifyContent: 'center',
          alignItems: 'flex-start',
          paddingTop: 4,
        }}
      >
        <Card sx={{ width: '100%', padding: 2 }}>
          <Box>
            <Typography color="primary" variant="h6">
              Sign Up!
            </Typography>
            <FormControl>
              <FormLabel htmlFor="email">Email</FormLabel>
              <TextField
                id="email"
                type="email"
                name="email"
                placeholder="your@email.com"
                autoComplete="email"
                autoFocus
                required
                fullWidth
                variant="outlined"
              />
            </FormControl>
          </Box>
        </Card>
      </Stack>
    </Container>
  )
}

export default SignUp
