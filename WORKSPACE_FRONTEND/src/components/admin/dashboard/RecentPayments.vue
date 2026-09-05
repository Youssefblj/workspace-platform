<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm"
  >
    <div
      class="flex items-center justify-between border-b border-gray-200 px-5 py-4"
    >
      <div>
        <h2 class="font-bold text-[#23394e]">
          Recent Payments
        </h2>

        <p class="text-sm text-[#9f9f9f]">
          Latest payment activity.
        </p>
      </div>

      <CreditCard class="h-5 w-5 text-[#f29200]" />
    </div>

    <div
      v-if="payments.length === 0"
      class="py-10 text-center text-sm text-[#9f9f9f]"
    >
      No recent payments.
    </div>

    <div v-else class="divide-y divide-gray-100">

      <div
        v-for="payment in payments"
        :key="payment.id"
        class="flex items-center justify-between gap-4 px-5 py-4"
      >
        <div class="min-w-0">

          <p class="truncate text-sm font-semibold text-[#23394e]">
            {{ payment.user__username || "-" }}
          </p>

          <p class="truncate text-xs text-[#9f9f9f]">
            {{ payment.booking__office__title || "-" }}
          </p>

          <p
            v-if="payment.transaction_id"
            class="mt-1 truncate text-xs text-[#9f9f9f]"
          >
            {{ payment.transaction_id }}
          </p>

        </div>

        <div class="shrink-0 text-right">

          <p class="text-sm font-bold text-[#23394e]">
            {{ formatMoney(
              payment.amount,
              payment.currency
            ) }}
          </p>

          <span
            class="mt-1 inline-flex rounded-full px-2.5 py-1 text-xs font-semibold"
            :class="statusClass(payment.status)"
          >
            {{ formatStatus(payment.status) }}
          </span>

        </div>
      </div>

    </div>

    <div
      class="border-t border-gray-200 px-5 py-3 text-right"
    >
      <RouterLink
        to="/admin/payments"
        class="text-sm font-medium text-[#f29200] hover:underline"
      >
        View all payments
      </RouterLink>
    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";
import { CreditCard } from "lucide-vue-next";
import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const payments = computed(() =>
  adminStore.dashboard.recent_payments || []
);

const formatMoney = (value, currency = "MAD") => {
  const amount = Number(value || 0);

  return `${amount.toLocaleString(undefined, {
    maximumFractionDigits: 2
  })} ${currency || "MAD"}`;
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
    case "paid":
      return "bg-green-50 text-green-700";

    case "failed":
      return "bg-red-50 text-red-600";

    default:
      return "bg-[#f29200]/10 text-[#f29200]";
  }
};
</script>