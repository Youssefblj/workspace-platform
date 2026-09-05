<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm"
  >
    <div
      class="flex items-center justify-between border-b border-gray-200 px-5 py-4"
    >
      <div>
        <h2 class="font-bold text-[#23394e]">
          Recent Bookings
        </h2>

        <p class="text-sm text-[#9f9f9f]">
          Latest workspace reservations.
        </p>
      </div>

      <CalendarDays class="h-5 w-5 text-[#f29200]" />
    </div>

    <div
      v-if="bookings.length === 0"
      class="py-10 text-center text-sm text-[#9f9f9f]"
    >
      No recent bookings.
    </div>

    <div v-else class="overflow-x-auto">
      <table class="min-w-full">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-5 py-3 text-left text-xs font-semibold text-[#9f9f9f]">
              Customer
            </th>

            <th class="px-5 py-3 text-left text-xs font-semibold text-[#9f9f9f]">
              Office
            </th>

            <th class="px-5 py-3 text-left text-xs font-semibold text-[#9f9f9f]">
              Status
            </th>

            <th class="px-5 py-3 text-right text-xs font-semibold text-[#9f9f9f]">
              Total
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="booking in bookings"
            :key="booking.id"
            class="border-t border-gray-100"
          >
            <td class="px-5 py-4">
              <p class="text-sm font-medium text-[#23394e]">
                {{ booking.user__username || "-" }}
              </p>
            </td>

            <td class="px-5 py-4">
              <p class="text-sm font-medium text-[#23394e]">
                {{ booking.office__title || "-" }}
              </p>

              <p class="text-xs text-[#9f9f9f]">
                {{ booking.office__city || "-" }}
              </p>
            </td>

            <td class="px-5 py-4">
              <span
                class="inline-flex rounded-full px-3 py-1 text-xs font-semibold"
                :class="statusClass(booking.status)"
              >
                {{ formatStatus(booking.status) }}
              </span>
            </td>

            <td class="px-5 py-4 text-right text-sm font-semibold text-[#23394e]">
              {{ formatMoney(booking.total_price) }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div
      class="border-t border-gray-200 px-5 py-3 text-right"
    >
      <RouterLink
        to="/admin/bookings"
        class="text-sm font-medium text-[#f29200] hover:underline"
      >
        View all bookings
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { CalendarDays } from "lucide-vue-next";
import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const bookings = computed(() =>
  adminStore.dashboard.recent_bookings || []
);

const formatMoney = (value) => {
  const amount = Number(value || 0);

  return `${amount.toLocaleString(undefined, {
    maximumFractionDigits: 2
  })} MAD`;
};

const formatStatus = (status) => {
  if (!status) return "-";

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
</script>