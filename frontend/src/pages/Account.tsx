import {
  Card,
  CardContent,
  Container,
  Divider,
  Grid2 as Grid,
  Typography,
} from '@mui/material'

import NavBar from '../components/NavBar'
import AddCollectionCard from '../components/AddCollectionCard'
import CollectionCard from '../components/CollectionCard'

const Account = () => {
  return (
    <Container>
      <NavBar title='Account' isLoggedIn={false}/>
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
          <Grid
            container
            direction='row'
            spacing={3}
            sx={{
              justifyContent: 'flex-start',
              alignItems: 'center',
            }}
            columns={{ xs: 4, sm: 8, md: 12, lg: 12 }}
            // columnSpacing={2}
          >
            <Grid size={4}>
              <CollectionCard title='Reading' count={5}/>
            </Grid>
            <Grid size={4}>
              <CollectionCard title='Want to read' count={3}/>
            </Grid>
            <Grid size={4}>
              <CollectionCard title='Read' count={10}/>
            </Grid>
            <Grid size={4}>
              <AddCollectionCard />
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Container>
  )
}

export default Account
