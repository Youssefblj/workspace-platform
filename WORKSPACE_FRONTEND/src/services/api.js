import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/'

const api = axios.create({
  baseURL: API_URL,
  
})

// Request Interceptor: Inject JWT token if it exists
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Flag and queue to track token refreshing process
let isRefreshing = false
let failedQueue = []

const processQueue = (error, token = null) => {
  failedQueue.forEach((prom) => {
    if (error) {
      prom.reject(error)
    } else {
      prom.resolve(token)
    }
  })
  failedQueue = []
}

// Response Interceptor: Auto-refresh tokens on 401
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    // If 401 Unauthorized and request hasn't been retried yet
    if (error.response?.status === 401 && !originalRequest._retry) {
      // Avoid infinite loop if the failure is on the auth or refresh endpoint
      if (
        originalRequest.url.includes('login/') || 
        originalRequest.url.includes('token/refresh/') ||
        originalRequest.url.includes('register/')
      ) {
        return Promise.reject(error)
      }

      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        })
          .then((token) => {
            originalRequest.headers.Authorization = `Bearer ${token}`
            return api(originalRequest)
          })
          .catch((err) => Promise.reject(err))
      }

      originalRequest._retry = true
      isRefreshing = true

      const refreshToken = localStorage.getItem('refresh_token')
      if (!refreshToken) {
        isRefreshing = false
        clearAuthData()
        return Promise.reject(error)
      }

      try {
        const response = await axios.post(`${API_URL}token/refresh/`, {
          refresh: refreshToken,
        })

        const newAccessToken = response.data.access
        const newRefreshToken = response.data.refresh // present if rotation is active

        localStorage.setItem('access_token', newAccessToken)
        if (newRefreshToken) {
          localStorage.setItem('refresh_token', newRefreshToken)
        }

        api.defaults.headers.common['Authorization'] = `Bearer ${newAccessToken}`
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
        
        processQueue(null, newAccessToken)
        isRefreshing = false

        return api(originalRequest)
      } catch (refreshError) {
        processQueue(refreshError, null)
        isRefreshing = false
        clearAuthData()
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  }
)

function clearAuthData() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  localStorage.removeItem('user')
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new Event('auth-logout'))
  }
}

export default api
export { API_URL }
