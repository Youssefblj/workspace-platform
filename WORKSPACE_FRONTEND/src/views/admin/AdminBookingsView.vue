<template>
  <div class="space-y-6">

    <!-- Header -->
    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold text-[#23394e]">
          Bookings Management
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Review and manage workspace reservations.
        </p>
      </div>

      <div class="flex items-center gap-2">

        <!-- Refresh -->
        <button
          type="button"
          @click="refreshBookings"
          :disabled="refreshing"
          class="inline-flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
        >
          <RefreshCw
            class="h-4 w-4"
            :class="{
              'animate-spin': refreshing
            }"
          />

          {{ refreshing ? "Refreshing..." : "Refresh" }}
        </button>

        <!-- Create Booking -->
        <button
          type="button"
          @click="openCreateBooking"
          class="inline-flex items-center gap-2 rounded-xl bg-[#f29200] px-4 py-2 text-sm font-medium text-white transition hover:opacity-90"
        >
          <Plus class="h-4 w-4" />

          Create Booking
        </button>

      </div>
    </div>

    <!-- Filters -->
    <div
      class="flex flex-col gap-3 rounded-xl border border-gray-200 bg-white p-4 sm:flex-row sm:items-center"
    >

      <!-- Search -->
      <div class="relative flex-1">

        <Search
          class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9f9f9f]"
        />

        <input
          v-model="adminStore.bookingSearch"
          type="text"
          placeholder="Search user, office or city..."
          class="w-full rounded-lg border border-gray-200 py-2 pl-10 pr-4 text-sm text-[#23394e] outline-none transition focus:border-[#f29200]"
        />

      </div>

      <!-- Status -->
      <select
        v-model="adminStore.bookingStatusFilter"
        class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
      >
        <option value="">
          All Statuses
        </option>

        <option value="pending">
          Pending
        </option>

        <option value="confirmed">
          Confirmed
        </option>

        <option value="cancelled">
          Cancelled
        </option>
      </select>

      <!-- Reset -->
      <button
        v-if="
          adminStore.bookingSearch ||
          adminStore.bookingStatusFilter
        "
        type="button"
        @click="resetFilters"
        class="inline-flex items-center gap-2 rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#9f9f9f] transition hover:border-[#f29200] hover:text-[#f29200]"
      >
        <X class="h-4 w-4" />

        Reset
      </button>

    </div>

    <!-- Table -->
    <BookingsTable />

    <!-- Create Booking Modal -->
    <CreateBookingModal
      :show="showCreateBookingModal"
      @close="closeCreateBooking"
      @created="handleBookingCreated"
    />

  </div>
</template>

<script setup>
import {
  onMounted,
  onBeforeUnmount,
  watch,
  ref
} from "vue";

import {
  Search,
  RefreshCw,
  X,
  Plus
} from "lucide-vue-next";

import { toast } from "vue-sonner";

import { useAdminStore } from "@/stores/admin";

import BookingsTable from "@/components/admin/bookings/BookingsTable.vue";
import CreateBookingModal from "@/components/admin/bookings/CreateBookingModal.vue";

const adminStore = useAdminStore();

const refreshing = ref(false);

const showCreateBookingModal = ref(false);

let searchTimeout = null;

/*
|--------------------------------------------------------------------------
| Refresh
|--------------------------------------------------------------------------
*/

const refreshBookings = async () => {
  if (refreshing.value) {
    return;
  }

  refreshing.value = true;

  try {
    adminStore.bookingSearch = "";
    adminStore.bookingStatusFilter = "";

    clearTimeout(searchTimeout);

    await adminStore.fetchBookings(1);

    toast.success(
      "Bookings refreshed successfully."
    );

  } catch (error) {

    console.error(
      "Failed to refresh bookings:",
      error
    );

    toast.error(
      "Unable to refresh bookings."
    );

  } finally {
    refreshing.value = false;
  }
};

/*
|--------------------------------------------------------------------------
| Filters
|--------------------------------------------------------------------------
*/

const resetFilters = () => {
  adminStore.bookingSearch = "";
  adminStore.bookingStatusFilter = "";
};

/*
|--------------------------------------------------------------------------
| Create Booking Modal
|--------------------------------------------------------------------------
*/

const openCreateBooking = () => {
  showCreateBookingModal.value = true;
};

const closeCreateBooking = () => {
  showCreateBookingModal.value = false;
};

const handleBookingCreated = async () => {
  showCreateBookingModal.value = false;

  adminStore.bookingSearch = "";
  adminStore.bookingStatusFilter = "";

  clearTimeout(searchTimeout);

  try {
    await adminStore.fetchBookings(1);

    toast.success(
      "Booking created successfully."
    );

  } catch (error) {

    console.error(
      "Failed to refresh bookings after creation:",
      error
    );
  }
};

/*
|--------------------------------------------------------------------------
| Search Watch
|--------------------------------------------------------------------------
*/

watch(
  () => adminStore.bookingSearch,
  () => {

    clearTimeout(searchTimeout);

    searchTimeout = setTimeout(() => {
      adminStore.fetchBookings(1);
    }, 400);

  }
);

/*
|--------------------------------------------------------------------------
| Status Watch
|--------------------------------------------------------------------------
*/

watch(
  () => adminStore.bookingStatusFilter,
  () => {
    adminStore.fetchBookings(1);
  }
);

/*
|--------------------------------------------------------------------------
| Lifecycle
|--------------------------------------------------------------------------
*/

onMounted(() => {
  adminStore.fetchBookings(1);
});

onBeforeUnmount(() => {
  clearTimeout(searchTimeout);
});
</script>