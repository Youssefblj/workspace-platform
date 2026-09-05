<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm"
  >

    <!-- Loading -->

    <div
      v-if="adminStore.loading && adminStore.bookings.length === 0"
      class="flex items-center justify-center gap-3 py-14"
    >
      <LoaderCircle
        class="h-5 w-5 animate-spin text-[#f29200]"
      />

      <span class="text-sm text-[#9f9f9f]">
        Loading bookings...
      </span>
    </div>

    <!-- Table -->

    <div v-else class="overflow-x-auto">

      <table class="min-w-full">

        <thead class="bg-[#23394e]">

          <tr>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase tracking-wide text-white">
              Customer
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase tracking-wide text-white">
              Workspace
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase tracking-wide text-white">
              Dates
            </th>

            <th class="px-5 py-4 text-right text-xs font-semibold uppercase tracking-wide text-white">
              Total
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase tracking-wide text-white">
              Status
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase tracking-wide text-white">
              Actions
            </th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="booking in adminStore.bookings"
            :key="booking.id"
            class="border-t border-gray-100 transition hover:bg-gray-50"
          >

            <!-- User -->

            <td class="px-5 py-4">

              <div class="flex items-center gap-3">

<div
  class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-xl bg-[#f29200]/10"
>
  <img
    v-if="booking.user?.profile_image"
    :src="booking.user.profile_image"
    :alt="booking.user?.username || 'User'"
    class="h-full w-full object-cover"
  />

  <User
    v-else
    class="h-4 w-4 text-[#f29200]"
  />
</div>

                <div>
                  <p class="text-sm font-semibold text-[#23394e]">
                    {{ booking.user?.username || "Unknown" }}
                  </p>

                  <p class="text-xs text-[#9f9f9f]">
                    {{ booking.user?.email || "-" }}
                  </p>
                </div>

              </div>

            </td>

            <!-- Office -->

            <td class="px-5 py-4">

              <div>
                <p class="text-sm font-semibold text-[#23394e]">
                  {{ booking.office?.title || "Unknown office" }}
                </p>

                <div
                  class="mt-1 flex items-center gap-1 text-xs text-[#9f9f9f]"
                >
                  <MapPin class="h-3.5 w-3.5" />

                  {{ booking.office?.city || "-" }}
                </div>
              </div>

            </td>

            <!-- Dates -->

            <td class="px-5 py-4">

              <div class="space-y-1 text-xs">

                <div class="flex items-center gap-2 text-[#23394e]">
                  <CalendarDays class="h-3.5 w-3.5 text-[#f29200]" />

                  {{ formatDate(booking.start_date) }}
                </div>

                <div class="pl-5 text-[#9f9f9f]">
                  to {{ formatDate(booking.end_date) }}
                </div>

              </div>

            </td>

            <!-- Price -->

            <td
              class="px-5 py-4 text-right text-sm font-bold text-[#23394e]"
            >
              {{ booking.total_price }} DH
            </td>

            <!-- Status -->

            <td class="px-5 py-4 text-center">

              <span
                class="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-xs font-semibold"
                :class="statusClass(booking.status)"
              >
                <component
                  :is="statusIcon(booking.status)"
                  class="h-3.5 w-3.5"
                />

                {{ formatStatus(booking.status) }}
              </span>

            </td>

            <!-- Actions -->

            <td class="px-5 py-4">

              <div class="flex items-center justify-center gap-2">

                <!-- Confirm -->

                <button
                  v-if="booking.status !== 'confirmed'"
                  @click="changeStatus(booking, 'confirmed')"
                  title="Confirm booking"
                  class="rounded-lg p-2 text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200]"
                >
                  <Check class="h-4 w-4" />
                </button>

                <!-- Pending -->

                <button
                  v-if="booking.status !== 'pending'"
                  @click="changeStatus(booking, 'pending')"
                  title="Set pending"
                  class="rounded-lg p-2 text-[#9f9f9f] transition hover:bg-gray-100 hover:text-[#23394e]"
                >
                  <Clock3 class="h-4 w-4" />
                </button>

                <!-- Cancel -->

                <button
                  v-if="booking.status !== 'cancelled'"
                  @click="changeStatus(booking, 'cancelled')"
                  title="Cancel booking"
                  class="rounded-lg p-2 text-red-500 transition hover:bg-red-50"
                >
                  <Ban class="h-4 w-4" />
                </button>

                <!-- Delete -->

                <button
                  @click="deleteBooking(booking)"
                  title="Delete booking"
                  class="rounded-lg p-2 text-red-500 transition hover:bg-red-50"
                >
                  <Trash2 class="h-4 w-4" />
                </button>

              </div>

            </td>

          </tr>

          <!-- Empty -->

          <tr v-if="adminStore.bookings.length === 0">

            <td colspan="6" class="py-14">

              <div
                class="flex flex-col items-center justify-center text-center"
              >
                <CalendarX
                  class="h-9 w-9 text-[#9f9f9f]"
                />

                <p class="mt-3 text-sm font-semibold text-[#23394e]">
                  No bookings found
                </p>

                <p class="mt-1 text-xs text-[#9f9f9f]">
                  Try another search term.
                </p>
              </div>

            </td>

          </tr>

        </tbody>

      </table>
<div
  v-if="adminStore.totalBookings > 0"
  class="flex flex-col gap-3 border-t border-gray-200 px-5 py-4 sm:flex-row sm:items-center sm:justify-between"
>

  <p class="text-sm text-[#9f9f9f]">

    Total

    <span class="font-semibold text-[#23394e]">
      {{ adminStore.totalBookings }}
    </span>

    bookings

  </p>

  <div class="flex items-center gap-2">

    <button
      @click="previousPage"
      :disabled="
        adminStore.bookingCurrentPage <= 1 ||
        adminStore.loading
      "
      class="flex items-center gap-1 rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
    >

      <ChevronLeft class="h-4 w-4" />

      Previous

    </button>

    <button
      v-for="page in visiblePages"
      :key="page"
      @click="goToPage(page)"
      :disabled="adminStore.loading"
      class="flex h-9 min-w-9 items-center justify-center rounded-lg px-2 text-sm font-medium transition"
      :class="
        page === adminStore.bookingCurrentPage
          ? 'bg-[#f29200] text-white'
          : 'border border-gray-200 text-[#23394e] hover:border-[#f29200]'
      "
    >
      {{ page }}
    </button>

    <button
      @click="nextPage"
      :disabled="
        adminStore.bookingCurrentPage >=
          adminStore.bookingTotalPages ||
        adminStore.loading
      "
      class="flex items-center gap-1 rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
    >

      Next

      <ChevronRight class="h-4 w-4" />

    </button>

  </div>

</div>

    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";
import Swal from "sweetalert2";

import {
  User,
  MapPin,
  CalendarDays,
  Check,
  CircleCheck,
  Clock3,
  Ban,
  CircleX,
  CalendarX,
  LoaderCircle,
  Trash2,
  ChevronLeft,
  ChevronRight
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();



const formatDate = (value) => {

  if (!value) return "-";

  return new Date(value).toLocaleDateString(
    undefined,
    {
      day: "2-digit",
      month: "short",
      year: "numeric"
    }
  );

};

const formatStatus = (status) => {

  if (!status) return "";

  return (
    status.charAt(0).toUpperCase() +
    status.slice(1)
  );

};

const statusClass = (status) => {

  switch (status) {

    case "confirmed":
      return "bg-green-50 text-green-700";

    case "cancelled":
      return "bg-red-50 text-red-600";

    default:
      return "bg-[#f29200]/10 text-[#f29200]";

  }

};

const statusIcon = (status) => {

  switch (status) {

    case "confirmed":
      return CircleCheck;

    case "cancelled":
      return CircleX;

    default:
      return Clock3;

  }

};

const changeStatus = async (
  booking,
  newStatus
) => {

  const labels = {
    confirmed: "confirm",
    pending: "set as pending",
    cancelled: "cancel"
  };

  const result = await Swal.fire({
    title: "Update booking?",
    text: `Do you want to ${labels[newStatus]} this booking?`,
    icon: "question",
    showCancelButton: true,
    confirmButtonText: "Continue",
    cancelButtonText: "Cancel",
    confirmButtonColor: "#f29200"
  });

  if (!result.isConfirmed) return;

  try {

    await adminStore.updateBookingStatus(
      booking.id,
      newStatus
    );

    Swal.fire({
      icon: "success",
      title: "Booking Updated",
      text: `Status changed to ${formatStatus(newStatus)}.`,
      timer: 1500,
      showConfirmButton: false
    });

  } catch (error) {

    Swal.fire({
      icon: "error",
      title: "Update Failed",
      text:
        error.response?.data?.error ||
        "Unable to update booking."
    });

  }

};
const deleteBooking = async (booking) => {

  const result = await Swal.fire({
    title: "Delete Booking?",
    text: `Delete booking #${booking.id} for ${booking.office?.title || "this office"}?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Delete",
    cancelButtonText: "Cancel",
    confirmButtonColor: "#f29200",
    cancelButtonColor: "#9f9f9f"
  });

  if (!result.isConfirmed) return;

  try {

    await adminStore.deleteBooking(
      booking.id
    );

    Swal.fire({
      icon: "success",
      title: "Booking Deleted",
      text: "The booking was deleted successfully.",
      timer: 1500,
      showConfirmButton: false
    });

  } catch (error) {

    Swal.fire({
      icon: "error",
      title: "Delete Failed",
      text:
        error.response?.data?.detail ||
        error.response?.data?.error ||
        "Unable to delete booking."
    });

  }

};

const goToPage = async (page) => {

  if (
    page < 1 ||
    page > adminStore.bookingTotalPages ||
    page === adminStore.bookingCurrentPage
  ) {
    return;
  }

  await adminStore.fetchBookings(page);

};

const previousPage = () => {

  goToPage(
    adminStore.bookingCurrentPage - 1
  );

};

const nextPage = () => {

  goToPage(
    adminStore.bookingCurrentPage + 1
  );

};

const visiblePages = computed(() => {

  const total = adminStore.bookingTotalPages;
  const current = adminStore.bookingCurrentPage;

  if (total <= 5) {
    return Array.from(
      { length: total },
      (_, index) => index + 1
    );
  }

  let start = Math.max(current - 2, 1);
  let end = Math.min(start + 4, total);

  if (end - start < 4) {
    start = Math.max(end - 4, 1);
  }

  return Array.from(
    { length: end - start + 1 },
    (_, index) => start + index
  );

});
</script>