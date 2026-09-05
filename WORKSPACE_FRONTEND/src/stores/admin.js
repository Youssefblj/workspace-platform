import { defineStore } from "pinia";
import adminService from "@/services/admin";

export const useAdminStore = defineStore("admin", {
state: () => ({

  loading: false,
  error: null,
  adminProfile: null,

  dashboard: {},
  analytics: {},

  users: [],
  offices: [],
  bookings: [],
  payments: [],
  contacts: [],
  reviews: [],
  notifications: [],

  

  userSearch: "",
  officeSearch: "",
  bookingSearch: "",

  // Users pagination
  userCurrentPage: 1,
  userTotalPages: 1,
  totalUsers: 0,
  userPageSize: 10,

  // Offices pagination
  currentPage: 1,
  totalPages: 1,
  totalOffices: 0,
  officePageSize: 6,

  // Bookings pagination
  bookingCurrentPage: 1,
  bookingTotalPages: 1,
  totalBookings: 0,
  bookingPageSize: 6,

  bookingStatusFilter: "",

  // Payments
  paymentSearch: "",
  paymentStatusFilter: "",

  paymentCurrentPage: 1,
  paymentTotalPages: 1,
  totalPayments: 0,
  paymentPageSize: 6,

  // Contacts
  contactSearch: "",
  contactStatusFilter: "",
  contactCategoryFilter: "",

  contactCurrentPage: 1,
  contactTotalPages: 1,
  totalContacts: 0,
  contactPageSize: 6,

  // Reviews

  reviewSearch: "",
  reviewRatingFilter: "",

  reviewCurrentPage: 1,
  reviewTotalPages: 1,
  totalReviews: 0,
  reviewPageSize: 6,
  
  //notification

  notificationSearch: "",
  notificationReadFilter: "",

  notificationCurrentPage: 1,
  notificationTotalPages: 1,
  totalNotifications: 0,
  notificationPageSize: 6,
  
}),

  actions: {

    async fetchDashboard() {

      this.loading = true;
      this.error = null;

      try {

        const response =
          await adminService.getDashboard();

        this.dashboard = response.data;

      } catch (err) {

        this.error =
          err.response?.data || err.message;

      } finally {

        this.loading = false;

      }

    },

    async fetchAnalytics() {

  this.loading = true;
  this.error = null;

  try {

    const response =
      await adminService.getAnalytics();

    this.analytics =
      response.data;

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},


async createOffice(data) {

  this.loading = true;

  try {

    await adminService.createOffice(data);

    await this.fetchOffices();

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},


async updateOffice(id, data) {

  this.loading = true;

  try {

    await adminService.updateOffice(

      id,

      data

    );

    await this.fetchOffices();

  }

  catch(err){

    this.error =
      err.response?.data || err.message;

    throw err;

  }

  finally{

    this.loading = false;

  }

},


async deleteOffice(id) {

  this.loading = true;

  try {

    await adminService.deleteOffice(id);

    this.offices = this.offices.filter(

      office => office.id !== id

    );

  }

  catch (err) {

    this.error =

      err.response?.data || err.message;

    throw err;

  }

  finally {

    this.loading = false;

  }

},


//
async uploadOfficeImage(id, formData) {

  this.loading = true;

  try {

    await adminService.uploadOfficeImage(
      id,
      formData
    );

    await this.fetchOffices();

  }

  catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  }

  finally {

    this.loading = false;

  }

},

async setPrimaryOfficeImage(imageId) {

  this.loading = true;

  try {

    await adminService.setPrimaryOfficeImage(
      imageId
    );

    await this.fetchOffices();

  }

  catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  }

  finally {

    this.loading = false;

  }

},

async deleteOfficeImage(id) {

  try {

    await adminService.deleteOfficeImage(id);

    await this.fetchOffices();

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  }

},

async toggleOfficeActive(id) {

  try {

    const response =
      await adminService.toggleOfficeActive(id)

    const office =
      this.offices.find(
        office => office.id === id
      )

    if (office) {
      office.is_active =
        response.data.is_active
    }

    return {
      success: true,
      office,
      message:
        response.data.message
    }

  } catch (error) {

    return {
      success: false,
      error:
        error.response?.data?.error ||
        'Unable to update office status.'
    }

  }
},

async toggleOfficeAvailability(id) {

  try {

    const response =
      await adminService.toggleOfficeAvailability(id);

    const office =
      this.offices.find(
        office => office.id === id
      );

    if (office) {
      office.available =
        response.data.available;
    }

    return {
      success: true,
      office,
      message:
        response.data.message
    };

  } catch (error) {

    return {
      success: false,
      error:
        error.response?.data?.error ||
        "Unable to update office availability."
    };

  }

},

async updateBookingStatus(id, status) {
  this.loading = true;
  this.error = null;

  try {
    await adminService.updateBookingStatus(
      id,
      status
    );

    await this.fetchBookings(
      this.bookingCurrentPage
    );

  } catch (err) {
    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {
    this.loading = false;
  }
},



async deleteBooking(id) {
  this.loading = true;
  this.error = null;

  try {
    await adminService.deleteBooking(id);

    const shouldGoPrevious =
      this.bookings.length === 1 &&
      this.bookingCurrentPage > 1;

    const page = shouldGoPrevious
      ? this.bookingCurrentPage - 1
      : this.bookingCurrentPage;

    await this.fetchBookings(page);

  } catch (err) {
    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {
    this.loading = false;
  }
},

async createBooking(data) {
  this.loading = true;
  this.error = null;

  try {
    const response =
      await adminService.createBooking(
        data
      );

    return response.data;

  } catch (err) {
    this.error =
      err.response?.data ||
      err.message;

    throw err;

  } finally {
    this.loading = false;
  }
},


async fetchUsers(page = 1) {

  this.loading = true;
  this.error = null;

  try {

    const response =
      await adminService.getUsers({
        page
      });

    this.users =
      response.data.results ?? [];

    this.totalUsers =
      response.data.count ?? 0;

    this.userCurrentPage = page;

    this.userTotalPages = Math.max(
      1,
      Math.ceil(
        this.totalUsers /
        this.userPageSize
      )
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},



    async updateUser(id, data) {

  this.loading = true;

  try {

    await adminService.updateUser(id, data);

    // تحديث اللائحة بعد التعديل
    await this.fetchUsers();

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async toggleUser(id) {

  this.loading = true;

  try {

    await adminService.toggleUserActiveStatus(id);
    await this.fetchUsers();

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async deleteUser(id) {

  this.loading = true;

  try {

    await adminService.deleteUser(id);

    // حذف المستخدم مباشرة من الـ state
    this.users = this.users.filter(
      user => user.id !== id
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},



async fetchOffices(page = 1) {

  this.loading = true;
  this.error = null;

  try {

    const response =
      await adminService.getOffices(page);

    const data = response.data;

    this.offices =
      data.results || [];

    this.currentPage =
      page;

    this.totalOffices =
      data.count || 0;

    this.totalPages = Math.max(
      1,
      Math.ceil(
        this.totalOffices /
        this.officePageSize
      )
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

  } finally {

    this.loading = false;

  }

},


async fetchBookings(page = 1) {

  this.loading = true;
  this.error = null;

  try {

    const params = {
      page,
    };

    if (this.bookingSearch.trim()) {
      params.search = this.bookingSearch.trim();
    }

    if (this.bookingStatusFilter) {
      params.status = this.bookingStatusFilter;
    }

    const response =
      await adminService.getBookings(params);

    this.bookings =
      response.data.results ?? [];

    this.totalBookings =
      response.data.count ?? 0;

    this.bookingCurrentPage = page;

    this.bookingTotalPages = Math.max(
      1,
      Math.ceil(
        this.totalBookings /
        this.bookingPageSize
      )
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},


async fetchPayments(page = 1) {

  this.loading = true;
  this.error = null;

  try {

    const params = {
      page,
    };

    if (this.paymentSearch.trim()) {
      params.search =
        this.paymentSearch.trim();
    }

    if (this.paymentStatusFilter) {
      params.status =
        this.paymentStatusFilter;
    }

    const response =
      await adminService.getPayments(params);

    this.payments =
      response.data.results ?? [];

    this.totalPayments =
      response.data.count ?? 0;

    this.paymentCurrentPage = page;

    this.paymentTotalPages = Math.max(
      1,
      Math.ceil(
        this.totalPayments /
        this.paymentPageSize
      )
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async confirmCashPayment(id) {

  try {

    const response =
      await adminService.confirmCashPayment(
        id
      );

    const updatedPayment =
      response.data.payment;

    const index =
      this.payments.findIndex(
        payment => payment.id === id
      );

    if (index !== -1) {
      this.payments[index] = updatedPayment;
    }

    return {
      success: true,
      payment: updatedPayment
    };

  } catch (error) {

    return {
      success: false,
      error:
        error.response?.data?.error ||
        "Unable to confirm cash payment."
    };
  }
},



async fetchContacts(page = 1) {

  this.loading = true;
  this.error = null;

  try {

    const params = {
      page
    };

    if (this.contactSearch.trim()) {
      params.search =
        this.contactSearch.trim();
    }

    if (this.contactStatusFilter) {
      params.status =
        this.contactStatusFilter;
    }

    if (this.contactCategoryFilter) {
      params.category =
        this.contactCategoryFilter;
    }

    const response =
      await adminService.getContacts(params);

    this.contacts =
      response.data.results ?? [];

    this.totalContacts =
      response.data.count ?? 0;

    this.contactCurrentPage = page;

    this.contactTotalPages = Math.max(
      1,
      Math.ceil(
        this.totalContacts /
        this.contactPageSize
      )
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},
async updateContactStatus(id, status) {

  this.loading = true;
  this.error = null;

  try {

    await adminService.updateContact(
      id,
      { status }
    );

    await this.fetchContacts(
      this.contactCurrentPage
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},
async replyContact(id, reply) {

  this.loading = true;
  this.error = null;

  try {

    await adminService.replyContact(
      id,
      reply
    );

    await this.fetchContacts(
      this.contactCurrentPage
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},
async deleteContact(id) {

  this.loading = true;
  this.error = null;

  try {

    await adminService.deleteContact(id);

    const shouldGoPrevious =
      this.contacts.length === 1 &&
      this.contactCurrentPage > 1;

    const page = shouldGoPrevious
      ? this.contactCurrentPage - 1
      : this.contactCurrentPage;

    await this.fetchContacts(page);

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},
async fetchReviews(page = 1) {

  this.loading = true;
  this.error = null;

  try {

    const params = {
      page
    };

    if (this.reviewSearch.trim()) {
      params.search =
        this.reviewSearch.trim();
    }

    if (this.reviewRatingFilter) {
      params.rating =
        this.reviewRatingFilter;
    }

    const response =
      await adminService.getReviews(params);

    this.reviews =
      response.data.results ?? [];

    this.totalReviews =
      response.data.count ?? 0;

    this.reviewCurrentPage = page;

    this.reviewTotalPages = Math.max(
      1,
      Math.ceil(
        this.totalReviews /
        this.reviewPageSize
      )
    );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},
async deleteReview(id) {

  this.loading = true;
  this.error = null;

  try {

    await adminService.deleteReview(id);

    const shouldGoPrevious =
      this.reviews.length === 1 &&
      this.reviewCurrentPage > 1;

    const page = shouldGoPrevious
      ? this.reviewCurrentPage - 1
      : this.reviewCurrentPage;

    await this.fetchReviews(page);

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async fetchNotifications(page = 1) {

  this.loading = true;
  this.error = null;

  try {

    const params = {
      page
    };

    if (this.notificationSearch.trim()) {
      params.search =
        this.notificationSearch.trim();
    }

    if (this.notificationReadFilter !== "") {
      params.is_read =
        this.notificationReadFilter;
    }

    const response =
      await adminService.getNotifications(params);

    this.notifications =
      response.data.results ?? [];

    this.totalNotifications =
      response.data.count ?? 0;

    this.notificationCurrentPage =
      page;

    this.notificationTotalPages =
      Math.max(
        1,
        Math.ceil(
          this.totalNotifications /
          this.notificationPageSize
        )
      );

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async sendNotification(userId, message) {

  this.loading = true;
  this.error = null;

  try {

    await adminService.sendNotification({
      user: userId,
      message
    });

    await this.fetchNotifications(1);

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async deleteNotification(id) {

  this.loading = true;
  this.error = null;

  try {

    await adminService.deleteNotification(id);

    const shouldGoPrevious =
      this.notifications.length === 1 &&
      this.notificationCurrentPage > 1;

    const page =
      shouldGoPrevious
        ? this.notificationCurrentPage - 1
        : this.notificationCurrentPage;

    await this.fetchNotifications(page);

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async fetchAdminProfile() {

  this.loading = true;
  this.error = null;

  try {

    const response =
      await adminService.getProfile();

    this.adminProfile =
      response.data;

    return response.data;

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},

async updateAdminProfile(data) {

  this.loading = true;
  this.error = null;

  try {

    const response =
      await adminService.updateProfile(data);

    this.adminProfile =
      response.data;

    return response.data;

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},


async changeAdminPassword(data) {

  this.loading = true;
  this.error = null;

  try {

    const response =
      await adminService.changePassword(data);

    return response.data;

  } catch (err) {

    this.error =
      err.response?.data || err.message;

    throw err;

  } finally {

    this.loading = false;

  }

},




  } // close actions

  



}); // close defineStore