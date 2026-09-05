import { defineStore } from 'pinia'
import api from '@/services/api'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('access_token') || null,
    refreshToken: localStorage.getItem('refresh_token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    loading: false,
    error: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.accessToken,
    isAdmin: (state) => !!(state.user && state.user.is_staff),
  },

  actions: {
    async login(username, password) {
      this.loading = true
      this.error = null
      try {
        const response = await api.post('login/', { username, password })
        const { access, refresh } = response.data
        
        this.accessToken = access
        this.refreshToken = refresh
        
        localStorage.setItem('access_token', access)
        localStorage.setItem('refresh_token', refresh)
        
        // Fetch user profile immediately
        await this.fetchProfile()
        
        return true
      } catch (err) {
        this.error = err.response?.data?.detail || err.response?.data?.error || 'Login failed'
        this.logout()
        throw err
      } finally {
        this.loading = false
      }
    },

    async register(username, email, phone, password) {
      this.loading = true
      this.error = null
      try {
        await api.post('register/', {
          username,
          email,
          phone,
          password
        })
        return true
      } catch (err) {
        this.error = err.response?.data || 'Registration failed'
        throw err
      } finally {
        this.loading = false
      }
    },

    async fetchProfile() {
      try {
        const response = await api.get('profile/')
        console.log("PROFILE:", response.data)

        this.user = response.data
        localStorage.setItem('user', JSON.stringify(response.data))
      } catch (err) {
        this.error = err.response?.data?.detail || 'Failed to fetch profile'
        throw err
      }
    },

    async updateProfile(profileData) {
      this.loading = true
      try {
        const response = await api.put('profile/update/', profileData)
        this.user = response.data
        localStorage.setItem('user', JSON.stringify(response.data))
        return true
      } catch (err) {
        this.error = err.response?.data || 'Failed to update profile'
        throw err
      } finally {
        this.loading = false
      }
    },

    async changePassword(old_password, new_password) {
      this.loading = true
      try {
        await api.post('change-password/', { old_password, new_password })
        return true
      } catch (err) {
        this.error = err.response?.data || 'Failed to change password'
        throw err
      } finally {
        this.loading = false
      }
    },

    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.user = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
    }
  }
})
