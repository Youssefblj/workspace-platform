// src/services/favoriteService.js

import api from "@/services/api";

const favoriteService = {
  getFavorites() {
    return api.get("favorites/");
  },

  addFavorite(officeId) {
    return api.post("favorites/create/", {
      office: officeId
    });
  },

  deleteFavorite(favoriteId) {
    return api.delete(
      `favorites/delete/${favoriteId}/`
    );
  }
};

export default favoriteService;