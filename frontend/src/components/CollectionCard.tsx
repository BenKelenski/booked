import { Box, Card, CardContent, Typography } from '@mui/material'

interface Props {
  title: string
  count: number
}

const CollectionCard = ({ title, count }: Props) => {
  return (
    <Box>
      <Card sx={{ minWidth: 275, minHeight: 250 }}>
        <CardContent>
          <Typography variant='h5' color='primary' sx={{ float: 'left' }}>
            {title}
          </Typography>
          <Typography variant='h6' sx={{ float: 'right' }}>
            {count} books
          </Typography>
        </CardContent>
      </Card>
    </Box>
  )
}

export default CollectionCard
