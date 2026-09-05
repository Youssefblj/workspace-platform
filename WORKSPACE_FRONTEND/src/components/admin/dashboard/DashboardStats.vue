<template>
  <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">

    <div
      v-for="card in cards"
      :key="card.label"
      class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
    >

      <div class="flex items-start justify-between">

        <div>

          <p class="text-sm text-[#9f9f9f]">
            {{ card.label }}
          </p>

          <p class="mt-2 text-2xl font-bold text-[#23394e]">
            {{ card.value }}
          </p>

        </div>

        <div
          class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
        >
          <component
            :is="card.icon"
            class="h-5 w-5 text-[#f29200]"
          />
        </div>

      </div>

      <p class="mt-4 text-xs text-[#9f9f9f]">
        {{ card.description }}
      </p>

    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";

import {
  Users,
  Building2,
  CalendarDays,
  Banknote
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const formatMoney = (value) => {

  const amount = Number(value || 0);

  return `${amount.toLocaleString(undefined, {
    maximumFractionDigits: 2
  })} MAD`;

};

const cards = computed(() => [

  {
    label: "Total Users",
    value:
      adminStore.dashboard.total_users || 0,
    description:
      `${adminStore.dashboard.active_users || 0} active users`,
    icon: Users
  },

  {
    label: "Total Offices",
    value:
      adminStore.dashboard.total_offices || 0,
    description:
      `${adminStore.dashboard.available_offices || 0} available offices`,
    icon: Building2
  },

  {
    label: "Total Bookings",
    value:
      adminStore.dashboard.total_bookings || 0,
    description:
      `${adminStore.dashboard.today_bookings || 0} bookings today`,
    icon: CalendarDays
  },

  {
    label: "Total Revenue",
    value:
      formatMoney(
        adminStore.dashboard.total_revenue
      ),
    description:
      `${formatMoney(adminStore.dashboard.this_month_revenue)} this month`,
    icon: Banknote
  }

]);
</script>