<template>
  <div
    class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
  >

    <div class="mb-5 flex items-center justify-between">

      <div>
        <h2 class="font-bold text-[#23394e]">
          Revenue Overview
        </h2>

        <p class="text-sm text-[#9f9f9f]">
          Revenue from successful payments.
        </p>
      </div>

      <Banknote
        class="h-5 w-5 text-[#f29200]"
      />

    </div>

    <div class="space-y-4">

      <div
        class="rounded-xl bg-[#23394e] p-5 text-white"
      >
        <p class="text-sm text-white/70">
          Total Revenue
        </p>

        <p class="mt-2 text-2xl font-bold">
          {{ formatMoney(
            dashboard.total_revenue
          ) }}
        </p>
      </div>

      <div class="grid gap-4 sm:grid-cols-2">

        <div
          class="rounded-xl border border-gray-200 p-4"
        >
          <p class="text-xs text-[#9f9f9f]">
            Today
          </p>

          <p class="mt-2 font-bold text-[#23394e]">
            {{ formatMoney(
              dashboard.today_revenue
            ) }}
          </p>
        </div>

        <div
          class="rounded-xl border border-gray-200 p-4"
        >
          <p class="text-xs text-[#9f9f9f]">
            This Month
          </p>

          <p class="mt-2 font-bold text-[#23394e]">
            {{ formatMoney(
              dashboard.this_month_revenue
            ) }}
          </p>
        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";
import { Banknote } from "lucide-vue-next";
import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const dashboard = computed(() =>
  adminStore.dashboard || {}
);

const formatMoney = (value) => {

  const amount = Number(value || 0);

  return `${amount.toLocaleString(undefined, {
    maximumFractionDigits: 2
  })} MAD`;

};
</script>