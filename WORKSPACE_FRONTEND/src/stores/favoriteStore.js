// src/stores/favoriteStore.js

import { defineStore } from "pinia";
import favoriteService from "@/services/favoriteService";

export const useFavoriteStore = defineStore(
  "favorites",
  {
    state: () => ({
      favorites: [],
      loading: false,
      error: null
    }),

    getters: {
      favoriteCount: (state) =>
        state.favorites.length,

      favoriteOfficeIds: (state) =>
        state.favorites.map(
          (favorite) => favorite.office
        )
    },

    actions: {
      async fetchFavorites() {
        this.loading = true;
        this.error = null;

        try {
          const response =
            await favoriteService.getFavorites();

          this.favorites =
            response.data.results ??
            response.data ??
            [];

          return true;

        } catch (err) {
          this.error =
            err.response?.data ||
            "Unable to load favorites.";

          return false;

        } finally {
          this.loading = false;
        }
      },

      async addFavorite(officeId) {
        this.error = null;

        try {
          const response =
            await favoriteService.addFavorite(
              officeId
            );

          this.favorites.unshift(
            response.data
          );

          return response.data;

        } catch (err) {
          this.error =
            err.response?.data ||
            "Unable to add favorite.";

          return null;
        }
      },

      async removeFavorite(favoriteId) {
        this.error = null;

        try {
          await favoriteService.deleteFavorite(
            favoriteId
          );

          this.favorites =
            this.favorites.filter(
              (favorite) =>
                favorite.id !== favoriteId
            );

          return true;

        } catch (err) {
          this.error =
            err.response?.data ||
            "Unable to remove favorite.";

          return false;
        }
      },

      getFavoriteByOffice(officeId) {
        return this.favorites.find(
          (favorite) =>
            Number(favorite.office) ===
            Number(officeId)
        );
      },

      isFavorite(officeId) {
        return Boolean(
          this.getFavoriteByOffice(officeId)
        );
      },

      async toggleFavorite(officeId) {
        const favorite =
          this.getFavoriteByOffice(officeId);

        if (favorite) {
          return await this.removeFavorite(
            favorite.id
          );
        }

        return await this.addFavorite(
          officeId
        );
      },

      clearFavorites() {
        this.favorites = [];
        this.error = null;
      }
    }
  }
);