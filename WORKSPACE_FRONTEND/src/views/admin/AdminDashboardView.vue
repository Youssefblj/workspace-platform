<template>
  <div class="space-y-6">

    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold text-[#23394e]">
          Dashboard
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Overview of users, offices, bookings and revenue.
        </p>
      </div>

<button
  type="button"
  @click="refreshDashboard"
  :disabled="refreshing"
  class="inline-flex items-center gap-2 rounded-lg border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
>
  <RefreshCw
    class="h-4 w-4"
    :class="{
      'animate-spin': refreshing
    }"
  />

  {{ refreshing ? "Refreshing..." : "Refresh" }}
</button>
    </div>

    <div
      v-if="adminStore.loading && !hasDashboardData"
      class="flex items-center justify-center py-16"
    >
      <LoaderCircle
        class="h-6 w-6 animate-spin text-[#f29200]"
      />
    </div>

    <div
      v-else-if="adminStore.error && !hasDashboardData"
      class="rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-600"
    >
      Unable to load dashboard data.
    </div>

    <template v-else>

      <DashboardStats />

      <div class="grid gap-6 xl:grid-cols-2">
        <UsersOverview />
        <OfficesOverview />
      </div>

      <div class="grid gap-6 xl:grid-cols-2">
        <BookingsOverview />
        <RevenueOverview />
      </div>
      <div class="grid gap-6 xl:grid-cols-2">
        <RecentBookings />
        <RecentPayments />
      </div>

    </template>

  </div>
</template>

<script setup>
import {
  computed,
  onMounted,
  ref
} from "vue";

import {
  RefreshCw,
  LoaderCircle
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";
import { toast } from "vue-sonner";
import DashboardStats from "@/components/admin/dashboard/DashboardStats.vue";
import UsersOverview from "@/components/admin/dashboard/UsersOverview.vue";
import OfficesOverview from "@/components/admin/dashboard/OfficesOverview.vue";
import BookingsOverview from "@/components/admin/dashboard/BookingsOverview.vue";
import RevenueOverview from "@/components/admin/dashboard/RevenueOverview.vue";
import RecentBookings from "@/components/admin/dashboard/RecentBookings.vue";
import RecentPayments from "@/components/admin/dashboard/RecentPayments.vue";
const adminStore = useAdminStore();
const refreshing = ref(false);
const hasDashboardData = computed(() => {
  return Object.keys(
    adminStore.dashboard || {}
  ).length > 0;
});

const refreshDashboard = async () => {
  if (refreshing.value) {
    return;
  }

  refreshing.value = true;

  try {
    await adminStore.fetchDashboard();

    toast.success(
      "Dashboard refreshed successfully."
    );
  } catch (error) {
    console.error(
      "Failed to refresh dashboard:",
      error
    );

    toast.error(
      "Unable to refresh dashboard."
    );
  } finally {
    refreshing.value = false;
  }
};

onMounted(() => {
  adminStore.fetchDashboard();
});
</script>