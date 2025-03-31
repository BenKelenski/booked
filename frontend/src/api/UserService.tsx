import axios from 'axios'
import { User } from '../common/types'

const client = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  timeout: 1000,
})

const createNewUser = async (user_data: any): Promise<User> => {
  return client
    .post('/users', user_data)
    .then((response) => {
      console.log('User created:', response.data)
      return response.data
    })
    .catch((error) => {
      console.error('Error creating user:', error)
      throw error
    })
}

export default createNewUser