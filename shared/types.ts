// Shared TypeScript types for frontend and backend communication

export interface User {
  id: string;
  username: string;
  role: string;
}

export interface Class {
  id: string;
  name: string;
  description?: string;
  subject?: string;
  grade_level?: string;
  students_count: number;
  created_by: string;
  created_at: string;
  updated_at: string;
}

export interface ClassCreate {
  name: string;
  description?: string;
  subject?: string;
  grade_level?: string;
}

export interface ClassUpdate {
  name?: string;
  description?: string;
  subject?: string;
  grade_level?: string;
}

export interface AuthToken {
  access_token: string;
  token_type: string;
}

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  message?: string;
}