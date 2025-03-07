import {
  Card,
  CardContent,
  Container,
  Divider,
  Grid2 as Grid,
  Typography,
} from '@mui/material'

import NavBar from '../components/NavBar'

const Account = () => {
  return (
    <Container>
      <NavBar title='Account' isLoggedIn={false} />
      <Grid
        container
        direction='column'
        spacing={2}
        sx={{
          marginTop: 8,
          justifyContent: 'center',
          alignItems: 'flex-start',
        }}
      >
        <Grid size={12}>
          <Typography variant='h4'>Collections</Typography>
          <Divider orientation='horizontal' variant='fullWidth' />
        </Grid>
        <Grid size={12}>
          <Grid container>
            <Grid size={4}>
              <Card>
                <CardContent>
                  <Typography
                    variant='h6'
                    color='primary'
                    sx={{ float: 'left' }}
                  >
                    Reading
                  </Typography>
                  <Typography sx={{ float: 'right' }}>5 books</Typography>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Container>
  )
}

export default Account
