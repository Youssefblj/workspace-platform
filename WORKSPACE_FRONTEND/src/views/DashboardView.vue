<script setup>
import {
  ref,
  onMounted,
  computed
} from "vue"

import { useRoute } from "vue-router"

import api from "@/services/api"


import DashboardHeader from "@/components/dashboard/DashboardHeader.vue"
import DashboardStats from "@/components/dashboard/DashboardStats.vue"
import DashboardSidebar from "@/components/dashboard/DashboardSidebar.vue"
import QuickActions from "@/components/dashboard/QuickActions.vue"
import UpcomingBooking from "@/components/dashboard/UpcomingBooking.vue"
import ReservationsSection from "@/components/dashboard/ReservationsSection.vue"
import RecentActivity from "@/components/dashboard/RecentActivity.vue"
import ProfileSection from "@/components/dashboard/ProfileSection.vue"
import SettingsSection from "@/components/dashboard/SettingsSection.vue"
import NotificationsSection from "@/components/dashboard/NotificationsSection.vue"
import BillingSection from "@/components/dashboard/billing/BillingSection.vue"


/* ==========================================================
   Router
========================================================== */

const route = useRoute()

const currentTab = computed(() => {
  return route.query.tab || "overview"
})


/* ==========================================================
   General State
========================================================== */

const loading = ref(true)

const bookings = ref([])
const favorites = ref([])
const notifications = ref([])
const payments = ref([])
const offices = ref([])


/* ==========================================================
   Booking Pagination
========================================================== */

const BOOKING_PAGE_SIZE = 6

const bookingPage = ref(1)
const bookingTotalPages = ref(1)
const bookingCount = ref(0)

const bookingPageLoading = ref(false)

const confirmedBookingCount = ref(0)

const favoriteCount = ref(0)
const paymentCount = ref(0)
const totalSpent = ref(0)

/* ==========================================================
   Load Bookings
========================================================== */

const loadBookings = async (page = 1) => {

  if (
    page < 1 ||
    page > bookingTotalPages.value
  ) {
    return
  }

  bookingPageLoading.value = true

  try {

    const response = await api.get(
      "bookings/my/",
      {
        params: {
          page
        }
      }
    )

    bookings.value =
      response.data.results ??
      response.data

    bookingCount.value =
      response.data.count ??
      bookings.value.length

    bookingPage.value = page

    bookingTotalPages.value = Math.max(
      1,
      Math.ceil(
        bookingCount.value /
        BOOKING_PAGE_SIZE
      )
    )

  } catch (error) {

    console.error(
      "Unable to load bookings:",
      error
    )

  } finally {

    bookingPageLoading.value = false

  }

}


/* ==========================================================
   Load Dashboard
========================================================== */

const loadDashboard = async () => {

  loading.value = true

  try {

    const [
      bookingsRes,
      confirmedBookingsRes,
      favoritesRes,
      notificationsRes,
      paymentsRes,
      officesRes
    ] = await Promise.all([

      /* All bookings */
      api.get(
        "bookings/my/",
        {
          params: {
            page: 1
          }
        }
      ),

      /* Confirmed bookings only */
      api.get(
        "bookings/my/",
        {
          params: {
            status: "confirmed",
            page: 1
          }
        }
      ),

      /* Favorites */
      api.get(
        "favorites/",
        {
          params: {
            page_size: 3
          }
        }
      ),

      /* Notifications */
      api.get(
        "notifications/",
        {
          params: {
            page_size: 5
          }
        }
      ),

      /* Payments */
      api.get(
        "payments/my/",
        {
          params: {
            page_size: 3
          }
        }
      ),

      /* Offices */
      api.get(
        "offices/",
        {
          params: {
            page_size: 100
          }
        }
      )

    ])


    /* --------------------------
       All Bookings
    -------------------------- */

    bookings.value =
      bookingsRes.data.results ??
      bookingsRes.data

    bookingCount.value =
      bookingsRes.data.count ??
      bookings.value.length

    bookingPage.value = 1

    bookingTotalPages.value = Math.max(
      1,
      Math.ceil(
        bookingCount.value /
        BOOKING_PAGE_SIZE
      )
    )


    /* --------------------------
       Confirmed Booking Count
    -------------------------- */

    confirmedBookingCount.value =
      confirmedBookingsRes.data.count ??
      confirmedBookingsRes.data.length ??
      0


    /* --------------------------
       Favorites
    -------------------------- */

    favorites.value =
      favoritesRes.data.results ??
      favoritesRes.data



      favoriteCount.value =
     favoritesRes.data.count ??
  favorites.value.length


    /* --------------------------
       Notifications
    -------------------------- */

    notifications.value =
      notificationsRes.data.results ??
      notificationsRes.data


    /* --------------------------
       Payments
    -------------------------- */

      payments.value =
      paymentsRes.data.results ??
      paymentsRes.data
      paymentCount.value =
      paymentsRes.data.count ??
      payments.value.length
    /* --------------------------
       Offices
    -------------------------- */

    offices.value =
      officesRes.data.results ??
      officesRes.data

  } catch (error) {

    console.error(
      "Unable to load dashboard:",
      error
    )

  } finally {

    loading.value = false

  }

}


/* ==========================================================
   Next Confirmed Booking
========================================================== */

const nextBooking = computed(() => {

  if (!bookings.value.length) {
    return null
  }

  const today = new Date()

  today.setHours(
    0,
    0,
    0,
    0
  )

  return bookings.value
    .filter(booking => {

      const startDate =
        new Date(
          `${booking.start_date}T00:00:00`
        )

      return (
        startDate >= today &&
        booking.status === "confirmed"
      )

    })
    .sort(
      (a, b) =>
        new Date(a.start_date) -
        new Date(b.start_date)
    )[0] || null

})


/* ==========================================================
   Mounted
========================================================== */

onMounted(() => {
  loadDashboard()
})
</script>


<template>

  <main class="min-h-screen bg-slate-50">

    <div class="mx-auto max-w-7xl px-6 py-8">


      <!-- Dashboard Header -->

      <DashboardHeader
        v-if="currentTab === 'overview'"
        :bookings="bookings"
        :booking-count="confirmedBookingCount"
        :favorites="favorites"
        :notifications="notifications"
        :payments="payments"
      />


      <div
        class="mt-8 grid gap-8 lg:grid-cols-[270px_1fr]"
      >

        <DashboardSidebar />


        <div class="space-y-8">


          <!-- Overview -->

          <template
            v-if="currentTab === 'overview'"
          >

<DashboardStats
  :bookings="bookings"
  :favorites="favorites"
  :payments="payments"
  :reservation-count="confirmedBookingCount"
  :favorite-count="favoriteCount"
  :payment-count="paymentCount"
/>

            <QuickActions />

            <UpcomingBooking
              :booking="nextBooking"
              :offices="offices"
            />

            <RecentActivity
              :bookings="bookings"
              :notifications="notifications"
            />

          </template>


          <!-- Reservations -->

          <ReservationsSection
            v-else-if="
              currentTab === 'reservations'
            "
            :bookings="bookings"
            :offices="offices"
            :current-page="bookingPage"
            :total-pages="bookingTotalPages"
            :total-bookings="bookingCount"
            :loading="bookingPageLoading"
            @page-change="loadBookings"
          />


          <!-- Billing -->

          <BillingSection
            v-else-if="
              currentTab === 'billing'
            "
            :payments="payments"
          />


          <!-- Notifications -->

          <NotificationsSection
            v-else-if="
              currentTab === 'notifications'
            "
          />


          <!-- Profile -->

          <ProfileSection
            v-else-if="
              currentTab === 'profile'
            "
          />


          <!-- Settings -->

          <SettingsSection
            v-else-if="
              currentTab === 'settings'
            "
          />

        </div>

      </div>

    </div>

  </main>

</template>