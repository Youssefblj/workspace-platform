<template>
  <div
    class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
  >

    <div class="mb-5 flex items-center justify-between">

      <div>
        <h2 class="font-bold text-[#23394e]">
          Offices Overview
        </h2>

        <p class="text-sm text-[#9f9f9f]">
          Workspace availability status.
        </p>
      </div>

      <Building2
        class="h-5 w-5 text-[#f29200]"
      />

    </div>

    <div class="grid gap-4 sm:grid-cols-2">

      <div
        class="rounded-xl border border-gray-200 p-4"
      >
        <p class="text-sm text-[#9f9f9f]">
          Available
        </p>

        <p class="mt-2 text-2xl font-bold text-[#23394e]">
          {{ dashboard.available_offices || 0 }}
        </p>
      </div>

      <div
        class="rounded-xl border border-gray-200 p-4"
      >
        <p class="text-sm text-[#9f9f9f]">
          Unavailable
        </p>

        <p class="mt-2 text-2xl font-bold text-[#23394e]">
          {{ dashboard.unavailable_offices || 0 }}
        </p>
      </div>

    </div>

    <div class="mt-4">

      <div
        class="mb-2 flex items-center justify-between text-sm"
      >
        <span class="text-[#9f9f9f]">
          Availability
        </span>

        <span class="font-semibold text-[#23394e]">
          {{ availabilityPercentage }}%
        </span>
      </div>

      <div class="h-2 overflow-hidden rounded-full bg-gray-100">

        <div
          class="h-full rounded-full bg-[#f29200]"
          :style="{
            width: `${availabilityPercentage}%`
          }"
        />

      </div>

    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";
import { Building2 } from "lucide-vue-next";
import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const dashboard = computed(() =>
  adminStore.dashboard || {}
);

const availabilityPercentage = computed(() => {

  const total =
    Number(dashboard.value.total_offices || 0);

  const available =
    Number(dashboard.value.available_offices || 0);

  if (!total) return 0;

  return Math.min(
    100,
    Math.round(
      (available / total) * 100
    )
  );

});
</script>