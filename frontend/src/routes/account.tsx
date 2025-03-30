import { createFileRoute } from '@tanstack/react-router'
import { useEffect, useState } from 'react'
import { User } from '../common/types'
import { Box, Container, Divider, Grid2 as Grid, Modal, TextField, Typography } from '@mui/material'
import NavBar from '../components/NavBar'
import CollectionCard from '../components/CollectionCard'
import AddCollectionCard from '../components/AddCollectionCard'

export const Route = createFileRoute('/account')({
  component: Account,
})

const modalStyle = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};


function Account() {
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false)
  const [user, setUser] = useState<User | null>(null)

  useEffect(() => {
    const userData = localStorage.getItem('user')
    console.log('User data:', userData)
    if (userData) {
      let parsedUserData: User = JSON.parse(userData)
      console.log('Parsed user:', parsedUserData)
      setUser(parsedUserData)
    } else {
      console.error('Error loading user data')
    }
  }, [])

  const openCreateModal = () => {
    setIsCreateModalOpen(true)
  }

  return (
    <Container>
      <Modal
        open={isCreateModalOpen}
        onClose={() => setIsCreateModalOpen(false)}
        aria-labelledby='create-collection-modal'
        aria-describedby='create-collection-modal'
      >
        <Box sx={modalStyle}>
          <Typography variant='h6' component='h2'>
            Enter collection name
          </Typography>
          <TextField id="collection-name-input" label="New Collection" variant="standard" />
        </Box>
      </Modal>
      <NavBar title='Account' isLoggedIn={user?.is_active} username={user?.name} />
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
          >
            <Grid size={4}>
              <CollectionCard title='Reading' count={5} />
            </Grid>
            <Grid size={4}>
              <CollectionCard title='Want to read' count={3} />
            </Grid>
            <Grid size={4}>
              <CollectionCard title='Read' count={10} />
            </Grid>
            <Grid size={4}>
              <AddCollectionCard openCreateModal={openCreateModal}/>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Container>
  )
}

export default Account