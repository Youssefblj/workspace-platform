<template>
  <div
    class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
  >

    <div class="mb-5 flex items-center justify-between">

      <div>
        <h2 class="font-bold text-[#23394e]">
          Users Overview
        </h2>

        <p class="text-sm text-[#9f9f9f]">
          Current user account status.
        </p>
      </div>

      <Users class="h-5 w-5 text-[#f29200]" />

    </div>

    <div class="space-y-4">

      <div>

        <div
          class="mb-2 flex items-center justify-between text-sm"
        >
          <span class="text-[#23394e]">
            Active Users
          </span>

          <span class="font-semibold text-[#23394e]">
            {{ dashboard.active_users || 0 }}
          </span>
        </div>

        <div class="h-2 overflow-hidden rounded-full bg-gray-100">

          <div
            class="h-full rounded-full bg-[#f29200]"
            :style="{
              width: `${activePercentage}%`
            }"
          />

        </div>

      </div>

      <div
        class="flex items-center justify-between rounded-xl bg-gray-50 px-4 py-3"
      >
        <span class="text-sm text-[#9f9f9f]">
          Inactive Users
        </span>

        <span class="font-semibold text-[#23394e]">
          {{ dashboard.inactive_users || 0 }}
        </span>
      </div>

      <div
        class="flex items-center justify-between rounded-xl bg-gray-50 px-4 py-3"
      >
        <span class="text-sm text-[#9f9f9f]">
          Total Users
        </span>

        <span class="font-semibold text-[#23394e]">
          {{ dashboard.total_users || 0 }}
        </span>
      </div>

    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";
import { Users } from "lucide-vue-next";
import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const dashboard = computed(() =>
  adminStore.dashboard || {}
);

const activePercentage = computed(() => {

  const total =
    Number(dashboard.value.total_users || 0);

  const active =
    Number(dashboard.value.active_users || 0);

  if (!total) return 0;

  return Math.min(
    100,
    Math.round((active / total) * 100)
  );

});
</script>