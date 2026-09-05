<template>
  <div
    class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
  >

    <div class="mb-5 flex items-center justify-between">

      <div>
        <h2 class="font-bold text-[#23394e]">
          Bookings Overview
        </h2>

        <p class="text-sm text-[#9f9f9f]">
          Current booking status summary.
        </p>
      </div>

      <CalendarDays
        class="h-5 w-5 text-[#f29200]"
      />

    </div>

    <div class="space-y-3">

      <div
        class="flex items-center justify-between rounded-xl bg-[#f29200]/10 px-4 py-3"
      >
        <div class="flex items-center gap-2">

          <Clock3
            class="h-4 w-4 text-[#f29200]"
          />

          <span class="text-sm text-[#23394e]">
            Pending
          </span>

        </div>

        <span class="font-bold text-[#23394e]">
          {{ dashboard.pending_bookings || 0 }}
        </span>
      </div>

      <div
        class="flex items-center justify-between rounded-xl bg-gray-50 px-4 py-3"
      >
        <div class="flex items-center gap-2">

          <CircleCheck
            class="h-4 w-4 text-[#23394e]"
          />

          <span class="text-sm text-[#23394e]">
            Confirmed
          </span>

        </div>

        <span class="font-bold text-[#23394e]">
          {{ dashboard.confirmed_bookings || 0 }}
        </span>
      </div>

      <div
        class="flex items-center justify-between rounded-xl bg-gray-50 px-4 py-3"
      >
        <div class="flex items-center gap-2">

          <CircleX
            class="h-4 w-4 text-[#9f9f9f]"
          />

          <span class="text-sm text-[#23394e]">
            Cancelled
          </span>

        </div>

        <span class="font-bold text-[#23394e]">
          {{ dashboard.cancelled_bookings || 0 }}
        </span>
      </div>

      <div
        class="mt-4 flex items-center justify-between border-t border-gray-200 pt-4"
      >
        <span class="text-sm text-[#9f9f9f]">
          Today
        </span>

        <span class="font-semibold text-[#f29200]">
          {{ dashboard.today_bookings || 0 }}
          bookings
        </span>
      </div>

    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";

import {
  CalendarDays,
  Clock3,
  CircleCheck,
  CircleX
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const dashboard = computed(() =>
  adminStore.dashboard || {}
);
</script>