import { defineStore } from "pinia"
import api from "@/services/api"

export const useSiteSettingsStore = defineStore(
  "siteSettings",
  {
    state: () => ({
      settings: {
        website_name: "WorkSpace",
        website_url: "",
        contact_email: "",
        contact_phone: "",
        whatsapp_number: "",
        address: "",
        instagram_url: "",
        facebook_url: "",
        linkedin_url: "",
        twitter_url: "",

      },

      loading: false,
      error: "",
      loaded: false,
    }),

    actions: {
      async fetchSettings() {
        if (this.loaded) {
          return this.settings
        }

        this.loading = true
        this.error = ""

        try {
          const response = await api.get(
            "site-settings/"
          )

          this.settings = {
            ...this.settings,
            ...response.data,
          }

          this.loaded = true

          return this.settings
        } catch (error) {
          console.error(
            "Failed to load site settings:",
            error
          )

          this.error =
            "Unable to load website settings."

          throw error
        } finally {
          this.loading = false
        }
      },

      async updateSettings(payload) {
        this.loading = true
        this.error = ""

        try {
          const response = await api.patch(
            "site-settings/admin/",
            payload
          )

          this.settings = {
            ...this.settings,
            ...response.data,
          }

          this.loaded = true

          return response.data
        } catch (error) {
          console.error(
            "Failed to update site settings:",
            error
          )

          this.error =
            "Unable to update website settings."

          throw error
        } finally {
          this.loading = false
        }
      },

      resetSettings() {
        this.loaded = false
        this.error = ""
      },
    },
  }
)