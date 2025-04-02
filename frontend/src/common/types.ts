export interface CreateUserRequest {
  name: string,
  password: string,
}

export interface CreateCollectionRequest {
  name: string
  description?: string
  is_private?: boolean
  user_id: number
}

export interface User {
  id: number
  name: string
  // email: string
  is_active: boolean
  is_admin: boolean
}

export interface Collection {
  id: number
  name: string
  description: string
  is_private: boolean
  user_id: number
  created_at: string
  books: Book[]
}

export interface Book {
  id: number
  title: string
  author: string
  collection_id: number
  collected_ts: string
}