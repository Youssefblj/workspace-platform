<template>
  <section>

    <!-- Header -->
    <div class="mb-6 flex flex-wrap items-end justify-between gap-4">

      <div>
        <h2 class="text-2xl font-bold text-[#23394e]">
          My Reservations
        </h2>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          View and manage all your workspace bookings.
        </p>
      </div>


      <div
        v-if="totalBookings > 0"
        class="rounded-xl border border-gray-200 bg-white px-4 py-2 text-xs font-semibold text-[#9f9f9f]"
      >
        {{ totalBookings }}
        {{ totalBookings === 1 ? "reservation" : "reservations" }}
      </div>

    </div>


    <!-- Loading -->
    <div
      v-if="loading"
      class="flex items-center justify-center rounded-2xl border border-gray-100 bg-white py-16"
    >
      <div class="flex items-center gap-3 text-sm font-semibold text-[#9f9f9f]">

        <Loader2
          class="h-5 w-5 animate-spin text-[#f29200]"
        />

        Loading reservations...

      </div>
    </div>


    <!-- Reservations -->
    <div
      v-else-if="reservations.length"
      class="space-y-6"
    >

      <div
        v-for="reservation in reservations"
        :key="reservation.id"
        class="group overflow-hidden rounded-3xl border border-gray-100 bg-white shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg"
      >

        <div class="grid lg:grid-cols-[260px_1fr]">

          <!-- Image -->
          <div class="min-h-[220px] overflow-hidden bg-gray-100">

            <img
              :src="getOfficeImage(reservation.office)"
              :alt="reservation.office.title"
              class="h-full w-full object-cover transition duration-700 group-hover:scale-105"
            />

          </div>


          <!-- Content -->
          <div class="p-7">

            <div
              class="flex flex-wrap items-start justify-between gap-4"
            >

              <div>

                <h3
                  class="text-xl font-bold text-[#23394e] sm:text-2xl"
                >
                  {{ reservation.office.title }}
                </h3>


                <div
                  class="mt-4 flex flex-wrap gap-x-6 gap-y-3 text-sm text-[#9f9f9f]"
                >

                  <div class="flex items-center gap-2">

                    <MapPin
                      class="h-4 w-4 text-[#f29200]"
                    />

                    {{ reservation.office.city }}

                  </div>


                  <div class="flex items-center gap-2">

                    <CalendarDays
                      class="h-4 w-4 text-[#f29200]"
                    />

                    {{ formatDate(reservation.start_date) }}

                  </div>


                  <div class="flex items-center gap-2">

                    <Users
                      class="h-4 w-4 text-[#f29200]"
                    />

                    {{ reservation.office.capacity }}
                    People

                  </div>

                </div>

              </div>


              <!-- Status -->
              <span
                class="rounded-full px-4 py-2 text-xs font-bold"
                :class="statusClass(reservation.status)"
              >
                {{ statusLabel(reservation.status) }}
              </span>

            </div>


            <div
              class="mt-8 flex flex-wrap items-center justify-between gap-5"
            >

              <!-- Price -->
              <div>

                <p class="text-sm text-[#9f9f9f]">
                  Total Price
                </p>

                <h4
                  class="mt-1 text-2xl font-black text-[#23394e] sm:text-3xl"
                >
                  {{ reservation.total_price }} MAD
                </h4>

              </div>


              <!-- Actions -->
              <div class="flex flex-wrap gap-3">

                <button
  type="button"
  @click="openBookingDetails(reservation)"
  class="inline-flex items-center gap-2 rounded-xl border border-gray-200 px-5 py-3 text-sm font-semibold text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200]"
>
  <Eye class="h-4 w-4" />
  Details
</button>


                <!-- Pending -->
                <router-link
                  v-if="reservation.status === 'pending'"
                  :to="{
                    path: `/office/${reservation.office.id}`,
                    query: {
                      resume_payment: 'true',
                      booking_id: reservation.id
                    }
                  }"
                  class="inline-flex items-center gap-2 rounded-xl bg-[#f29200] px-5 py-3 text-sm font-semibold text-white transition hover:bg-[#d97706]"
                >
                  <CreditCard class="h-4 w-4" />

                  Complete Payment
                </router-link>


                <!-- Confirmed -->
                <router-link
                  v-else-if="reservation.status === 'confirmed'"
                  :to="`/office/${reservation.office.id}`"
                  class="inline-flex items-center gap-2 rounded-xl bg-[#23394e] px-5 py-3 text-sm font-semibold text-white transition hover:opacity-90"
                >
                  <Building2 class="h-4 w-4" />

                  View Office
                </router-link>


                <!-- Cancelled -->
                <router-link
                  v-else
                  :to="`/office/${reservation.office.id}`"
                  class="inline-flex items-center gap-2 rounded-xl bg-gray-100 px-5 py-3 text-sm font-semibold text-gray-600 transition hover:bg-gray-200"
                >
                  <Building2 class="h-4 w-4" />

                  View Office
                </router-link>

              </div>

            </div>

          </div>

        </div>

      </div>


      <!-- ==================================================
           Pagination
      =================================================== -->

      <div
        v-if="totalPages > 1"
        class="flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-100 bg-white px-4 py-4 shadow-sm"
      >

        <!-- Info -->
        <p class="text-xs font-medium text-[#9f9f9f]">
          Page
          <span class="font-bold text-[#23394e]">
            {{ currentPage }}
          </span>
          of
          <span class="font-bold text-[#23394e]">
            {{ totalPages }}
          </span>
        </p>


        <div class="flex items-center gap-2">

          <!-- Previous -->
          <button
            type="button"
            :disabled="currentPage <= 1 || loading"
            @click="changePage(currentPage - 1)"
            class="flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200 bg-white text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
          >
            <ChevronLeft class="h-4 w-4" />
          </button>


          <!-- Page Numbers -->
          <button
            v-for="page in visiblePages"
            :key="page"
            type="button"
            :disabled="loading"
            @click="changePage(page)"
            :class="[
              'flex h-9 min-w-9 items-center justify-center rounded-lg px-3 text-xs font-bold transition',

              page === currentPage
                ? 'bg-[#f29200] text-white shadow-sm'
                : 'border border-gray-200 bg-white text-[#23394e] hover:border-[#f29200] hover:text-[#f29200]'
            ]"
          >
            {{ page }}
          </button>


          <!-- Next -->
          <button
            type="button"
            :disabled="currentPage >= totalPages || loading"
            @click="changePage(currentPage + 1)"
            class="flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200 bg-white text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
          >
            <ChevronRight class="h-4 w-4" />
          </button>

        </div>

      </div>

    </div>


    <!-- Empty -->
    <div
      v-else
      class="rounded-3xl border border-dashed border-gray-200 bg-white py-16 text-center"
    >

      <CalendarDays
        class="mx-auto h-12 w-12 text-gray-300"
      />

      <h3
        class="mt-4 text-xl font-bold text-[#23394e]"
      >
        No Reservations Yet
      </h3>

      <p class="mt-2 text-sm text-[#9f9f9f]">
        Start exploring workspaces and make your first booking.
      </p>


      <router-link
        to="/browse-offices"
        class="mt-6 inline-flex items-center gap-2 rounded-xl bg-[#f29200] px-6 py-3 text-sm font-semibold text-white transition hover:bg-[#d97706]"
      >
        <Search class="h-4 w-4" />

        Browse Offices
      </router-link>

    </div>
    

    <ReservationDetailsModal
  :show="showDetailsModal"
  :booking="selectedBooking"
  @close="closeBookingDetails"
/>
  </section>
</template>


<script setup>
import { computed, ref } from "vue"

import ReservationDetailsModal from "@/components/dashboard/reservation/ReservationDetailsModal.vue"

import {
  MapPin,
  CalendarDays,
  Users,
  CreditCard,
  Building2,
  Eye,
  ChevronLeft,
  ChevronRight,
  Loader2,
  Search
} from "lucide-vue-next"

const selectedBooking = ref(null)
const showDetailsModal = ref(false)

const openBookingDetails = (booking) => {
  console.log("CAPACITY:", booking.office?.capacity)
  console.log("OFFICE KEYS:", Object.keys(booking.office))
  console.log(
    "OFFICE DATA:",
    JSON.parse(JSON.stringify(booking.office))
  )

  selectedBooking.value = booking
  showDetailsModal.value = true
}

const closeBookingDetails = () => {
  showDetailsModal.value = false
  selectedBooking.value = null
}
/* ==========================================================
   Props
========================================================== */

const props = defineProps({

  bookings: {
    type: Array,
    default: () => []
  },

  offices: {
    type: Array,
    default: () => []
  },

  currentPage: {
    type: Number,
    default: 1
  },

  totalPages: {
    type: Number,
    default: 1
  },

  totalBookings: {
    type: Number,
    default: 0
  },

  loading: {
    type: Boolean,
    default: false
  }

})


/* ==========================================================
   Emits
========================================================== */

const emit = defineEmits([
  "page-change"
])


/* ==========================================================
   Reservations
========================================================== */

const reservations = computed(() => {

  return props.bookings
    .map(booking => {

      const office =
        props.offices.find(
          office =>
            office.id === booking.office
        )

      return {
        ...booking,
        office
      }

    })
    .filter(
      reservation =>
        reservation.office
    )

})


/* ==========================================================
   Visible Pagination Pages
========================================================== */

const visiblePages = computed(() => {

  const total = props.totalPages
  const current = props.currentPage

  if (total <= 5) {

    return Array.from(
      {
        length: total
      },
      (_, index) =>
        index + 1
    )

  }


  let start =
    Math.max(
      1,
      current - 2
    )

  let end =
    Math.min(
      total,
      start + 4
    )


  if (end - start < 4) {

    start =
      Math.max(
        1,
        end - 4
      )

  }


  return Array.from(
    {
      length:
        end - start + 1
    },
    (_, index) =>
      start + index
  )

})


/* ==========================================================
   Change Page
========================================================== */

const changePage = page => {

  if (
    page < 1 ||
    page > props.totalPages ||
    page === props.currentPage ||
    props.loading
  ) {
    return
  }

  emit(
    "page-change",
    page
  )

}


/* ==========================================================
   Office Image
========================================================== */

const getOfficeImage = office => {

  const image =
    office?.images?.[0]?.image

  if (!image) {

    return (
      "data:image/svg+xml;utf8," +
      '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400">' +
      '<rect width="100%" height="100%" fill="%23f3f4f6"/>' +
      '<text x="50%" y="50%" text-anchor="middle" fill="%239f9f9f" font-size="20">No image</text>' +
      "</svg>"
    )

  }

  if (image.startsWith("http")) {
    return image
  }

  return `http://127.0.0.1:8000${image}`

}


/* ==========================================================
   Date
========================================================== */

const formatDate = date => {

  if (!date) {
    return "—"
  }

  return new Date(
    `${date}T00:00:00`
  ).toLocaleDateString(
    undefined,
    {
      year: "numeric",
      month: "short",
      day: "numeric"
    }
  )

}


/* ==========================================================
   Status
========================================================== */

const statusClass = status => {

  switch (
    status?.toLowerCase()
  ) {

    case "confirmed":

      return (
        "bg-emerald-100 " +
        "text-emerald-700"
      )


    case "pending":

      return (
        "bg-[#f29200]/10 " +
        "text-[#f29200]"
      )


    case "cancelled":

      return (
        "bg-red-100 " +
        "text-red-700"
      )


    default:

      return (
        "bg-gray-100 " +
        "text-gray-600"
      )

  }

}


const statusLabel = status => {

  switch (
    status?.toLowerCase()
  ) {

    case "confirmed":
      return "Confirmed"

    case "pending":
      return "Pending Payment"

    case "cancelled":
      return "Cancelled"

    default:
      return status || "Unknown"

  }

}



</script>