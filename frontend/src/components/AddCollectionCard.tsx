import { Add } from '@mui/icons-material'
import {
  Box,
  Card,
  CardActions,
  CardContent,
  IconButton,
  Typography,
} from '@mui/material'

interface Props {
  openCreateModal: () => void
}

const AddCollectionCard = ({openCreateModal}: Props) => {
  const handleCreateCollection = () => {
    openCreateModal()
  }

  return (
    <Box>
      <Card variant='outlined' sx={{ minWidth: 275, minHeight: 250 }}>
        <CardContent sx={{ textAlign: 'center' }}>
          <Typography
            variant='h6'
            color='primary'
            sx={{ paddingTop: 2, paddingBottom: 2 }}
          >
            Create new collection
          </Typography>
          <CardActions
            sx={{
              justifyContent: 'center',
              alignItems: 'center',
              height: '100%',
            }}
          >
            <IconButton
              onClick={handleCreateCollection}
              aria-label='Create new collection'
              color='primary'
              sx={{ p: 0, height: '100%' }}
            >
              <Add sx={{ fontSize: 72 }} />
            </IconButton>
          </CardActions>
        </CardContent>
      </Card>
    </Box>
  )
}

export default AddCollectionCard
