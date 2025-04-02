import axios from 'axios'
import { CreateCollectionRequest } from '../common/types'

const client = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  timeout: 1000,
})

export const createNewCollection = async (
  collectionData: CreateCollectionRequest
): Promise<any> => {
  return client
    .post('/collections', collectionData)
    .then((response) => {
      console.log('Collection created:', response.data)
      return response.data
    })
    .catch((error) => {
      console.error('Error creating collection:', error)
      throw error
    })
}

export const getCollectionsByUserId = async (userId: number): Promise<any> => {
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
