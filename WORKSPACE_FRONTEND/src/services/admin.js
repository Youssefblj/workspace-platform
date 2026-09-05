import api from "./api";

export default {

  /*
  ==========================
          Dashboard
  ==========================
  */

  getDashboard() {
    return api.get("dashboard/");
  },

  getAnalytics() {
    return api.get("analytics/");
  },

  /*
  ==========================
            Users
  ==========================
  */

  getUsers(params = {}) {
  return api.get(
    "admin/users/",
    {
      params
    }
  );
  },

  updateUser(id, data) {
    return api.put(`admin/users/${id}/update/`, data);
  },
  toggleUserActiveStatus(id, data) {
    return api.patch(`admin/users/${id}/toggle-active/`);
  },

  deleteUser(id) {
    return api.delete(`admin/users/${id}/delete/`);
  },

  /*
  ==========================
           Offices
  ==========================
  */

  getOffices(page = 1) {
  return api.get("offices/admin/", {
    params: {
      page
    }
  });
},

  createOffice(data) {
    return api.post("offices/create/", data);
  },

  updateOffice(id, data) {
    return api.put(`offices/${id}/update/`, data);
  },

  deleteOffice(id) {
    return api.delete(`offices/${id}/delete/`);
  },

  uploadOfficeImage(id, formData) {
    return api.post(
      `offices/${id}/upload-image/`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }
    );
  },

 setPrimaryOfficeImage(imageId) {

  return api.patch(
    `offices/images/${imageId}/set-primary/`
  );

},

deleteOfficeImage(id) {
  return api.delete(`offices/images/${id}/delete/`);
},


toggleOfficeActive(id) {
  return api.patch(
    `offices/admin/${id}/toggle-active/`
  )
},

toggleOfficeAvailability(id) {
  return api.patch(
    `offices/admin/${id}/toggle-availability/`
  );
},
/*
==========================
        Bookings
==========================
*/

getBookings(params = {}) {
  return api.get("bookings/admin/", {
    params
  });
},

getBooking(id) {
  return api.get(
    `bookings/admin/${id}/`
  );
},

updateBookingStatus(id, status) {
  return api.patch(
    `bookings/admin/${id}/status/`,
    {
      status
    }
  );
},
deleteBooking(id) {
  return api.delete(
    `bookings/admin/${id}/delete/`
  );
},

createBooking(data) {
  return api.post(
    "bookings/admin/create/",
    data
  );
},

/*
==========================
        Payments
==========================
*/

getPayments(params = {}) {
  return api.get("payments/admin/", {
    params
  });
},

getPayment(id) {
  return api.get(
    `payments/admin/${id}/`
  );
},


confirmCashPayment(id) {
  return api.post(
    `payments/admin/${id}/confirm-cash/`,
    {}
  );
},
/*
==========================
        Contacts
==========================
*/

getContacts(params = {}) {
  return api.get("contact/", {
    params
  });
},


getContact(id) {
  return api.get(
    `contact/${id}/`
  );
},

updateContact(id, data) {
  return api.patch(
    `contact/${id}/update/`,
    data
  );
},

replyContact(id, adminReply) {
  return api.post(
    `contact/${id}/reply/`,
    {
      admin_reply: adminReply
    }
  );
},

deleteContact(id) {
  return api.delete(
    `contact/${id}/delete/`
  );
},
/*
==========================
        Reviews
==========================
*/

getReviews(params = {}) {
  return api.get("reviews/admin/", {
    params
  });
},

getReview(id) {
  return api.get(
    `reviews/admin/${id}/`
  );
},

deleteReview(id) {
  return api.delete(
    `reviews/admin/${id}/delete/`
  );
},

/*
==========================
      Notifications
==========================
*/

getNotifications(params = {}) {
  return api.get("notifications/admin/", {
    params
  });
},

getNotification(id) {
  return api.get(
    `notifications/admin/${id}/`
  );
},

sendNotification(data) {
  return api.post(
    "notifications/admin/send/",
    data
  );
},

deleteNotification(id) {
  return api.delete(
    `notifications/admin/${id}/delete/`
  );
},

/*
==========================
        Settings
==========================
*/

getProfile() {
  return api.get("profile/");
},

updateProfile(data) {
  return api.patch(
    "profile/update/",
    data
  );
},

changePassword(data) {
  return api.post(
    "profile/change-password/",
    data
  );
},

};