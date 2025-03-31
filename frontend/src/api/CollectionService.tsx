import axios from 'axios'

const client = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  timeout: 1000,
})

const getCollectionsByUserId = async (userId: number): Promise<any> => {
  return client
    .get(`/collections/user/${userId}`)
    .then((response) => {
      console.log('Collections fetched:', response.data)
      return response.data
    })
    .catch((error) => {
      console.error('Error fetching collections:', error)
      throw error
    })
}

export default getCollectionsByUserId