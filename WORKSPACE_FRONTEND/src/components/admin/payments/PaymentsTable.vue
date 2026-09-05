<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm"
  >

    <!-- Loading -->

    <div
      v-if="
        adminStore.loading &&
        adminStore.payments.length === 0
      "
      class="flex items-center justify-center gap-3 py-14"
    >
      <LoaderCircle
        class="h-5 w-5 animate-spin text-[#f29200]"
      />

      <span class="text-sm text-[#9f9f9f]">
        Loading payments...
      </span>
    </div>

    <!-- Table -->

    <div v-else class="overflow-x-auto">

      <table class="min-w-full">

        <thead class="bg-[#23394e]">

          <tr>

            <th
              class="px-5 py-4 text-left text-xs font-semibold uppercase text-white"
            >
              Invoice
            </th>

            <th
              class="px-5 py-4 text-left text-xs font-semibold uppercase text-white"
            >
              Customer
            </th>

            <th
              class="px-5 py-4 text-left text-xs font-semibold uppercase text-white"
            >
              Office
            </th>

            <th
              class="px-5 py-4 text-right text-xs font-semibold uppercase text-white"
            >
              Amount
            </th>

            <th
              class="px-5 py-4 text-center text-xs font-semibold uppercase text-white"
            >
              Status
            </th>

            <th
              class="px-5 py-4 text-left text-xs font-semibold uppercase text-white"
            >
              Transaction
            </th>

            <th
              class="px-5 py-4 text-left text-xs font-semibold uppercase text-white"
            >
              Date
            </th>

            <th
              class="px-5 py-4 text-center text-xs font-semibold uppercase text-white"
            >
              Actions
            </th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="payment in adminStore.payments"
            :key="payment.id"
            class="border-t border-gray-100 transition hover:bg-gray-50"
          >

            <!-- Invoice -->

            <td class="px-5 py-4">

              <p
                class="text-sm font-semibold text-[#23394e]"
              >
                {{ payment.invoice_number }}
              </p>

            </td>

            <!-- Customer -->

            <td class="px-5 py-4">

              <div class="flex items-center gap-3">

                <div
  class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-xl bg-[#f29200]/10"
>
  <img
    v-if="payment.user_profile_image"
    :src="payment.user_profile_image"
    :alt="payment.username || 'User'"
    class="h-full w-full object-cover"
  />

  <User
    v-else
    class="h-4 w-4 text-[#f29200]"
  />
</div>

                <div>

                  <p
                    class="text-sm font-semibold text-[#23394e]"
                  >
                    {{ payment.username || "Unknown" }}
                  </p>

                  <p
                    class="text-xs text-[#9f9f9f]"
                  >
                    {{ payment.user_email || "-" }}
                  </p>

                </div>

              </div>

            </td>

            <!-- Office -->

            <td class="px-5 py-4">

              <div>

                <p
                  class="text-sm font-semibold text-[#23394e]"
                >
                  {{ payment.office_title || "-" }}
                </p>

                <div
                  class="mt-1 flex items-center gap-1 text-xs text-[#9f9f9f]"
                >
                  <MapPin class="h-3.5 w-3.5" />

                  {{ payment.office_city || "-" }}
                </div>

              </div>

            </td>

            <!-- Amount -->

            <td class="px-5 py-4 text-right">

              <span
                class="text-sm font-bold text-[#23394e]"
              >
                {{ payment.amount }}
                {{ payment.currency }}
              </span>

            </td>

            <!-- Status -->

            <td class="px-5 py-4 text-center">

              <span
                class="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-xs font-semibold"
                :class="statusClass(payment.status)"
              >
                <component
                  :is="statusIcon(payment.status)"
                  class="h-3.5 w-3.5"
                />

                {{ formatStatus(payment.status) }}
              </span>

            </td>

            <!-- Transaction -->

            <td class="px-5 py-4">

              <div>

                <p
                  class="max-w-[160px] truncate text-sm text-[#23394e]"
                  :title="payment.transaction_id"
                >
                  {{ payment.transaction_id || "-" }}
                </p>

                <p
                  class="mt-1 text-xs text-[#9f9f9f]"
                >
                  {{
                    formatPaymentMethod(
                      payment.payment_method
                    )
                  }}
                </p>

              </div>

            </td>

            <!-- Date -->

            <td class="px-5 py-4">

              <div
                class="flex items-center gap-2 text-sm text-[#23394e]"
              >
                <CalendarDays
                  class="h-4 w-4 text-[#f29200]"
                />

                {{
                  formatDate(
                    payment.paid_at ||
                    payment.created_at
                  )
                }}
              </div>

            </td>

            <!-- Actions -->

<!-- Actions -->

<td class="px-5 py-4">

  <div
    class="flex items-center justify-center gap-1"
  >

    <!-- View -->

    <button
      type="button"
      @click="emit('view', payment)"
      title="View payment details"
      class="rounded-lg p-2 text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200]"
    >
      <Eye class="h-4 w-4" />
    </button>


    <!-- Confirm Cash -->

    <button
      v-if="
        payment.payment_method === 'cash' &&
        payment.status === 'pending'
      "
      type="button"
      @click="emit('confirm-cash', payment)"
      :disabled="
        props.confirmingPaymentId === payment.id
      "
      title="Confirm cash payment"
      class="inline-flex items-center gap-1.5 rounded-lg bg-emerald-50 px-2.5 py-2 text-xs font-semibold text-emerald-700 transition hover:bg-emerald-100 disabled:cursor-not-allowed disabled:opacity-50"
    >

      <LoaderCircle
        v-if="
          props.confirmingPaymentId === payment.id
        "
        class="h-4 w-4 animate-spin"
      />

      <BadgeCheck
        v-else
        class="h-4 w-4"
      />

      <span class="hidden xl:inline">
        Confirm
      </span>

    </button>

  </div>

</td>

          </tr>

          <!-- Empty State -->

          <tr
            v-if="adminStore.payments.length === 0"
          >

            <td
              colspan="8"
              class="py-14"
            >

              <div
                class="flex flex-col items-center text-center"
              >

                <CreditCard
                  class="h-9 w-9 text-[#9f9f9f]"
                />

                <p
                  class="mt-3 text-sm font-semibold text-[#23394e]"
                >
                  No payments found
                </p>

                <p
                  class="mt-1 text-xs text-[#9f9f9f]"
                >
                  Try another search or status filter.
                </p>

              </div>

            </td>

          </tr>

        </tbody>

      </table>

      <!-- Pagination -->

      <div
        v-if="adminStore.totalPayments > 0"
        class="flex flex-col gap-3 border-t border-gray-200 px-5 py-4 sm:flex-row sm:items-center sm:justify-between"
      >

        <p class="text-sm text-[#9f9f9f]">

          Total

          <span
            class="font-semibold text-[#23394e]"
          >
            {{ adminStore.totalPayments }}
          </span>

          payments

        </p>

        <div class="flex items-center gap-2">

          <button
            @click="previousPage"
            :disabled="
              adminStore.paymentCurrentPage <= 1 ||
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
              page === adminStore.paymentCurrentPage
                ? 'bg-[#f29200] text-white'
                : 'border border-gray-200 text-[#23394e] hover:border-[#f29200]'
            "
          >
            {{ page }}
          </button>

          <button
            @click="nextPage"
            :disabled="
              adminStore.paymentCurrentPage >=
                adminStore.paymentTotalPages ||
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

import {
  User,
  MapPin,
  CalendarDays,
  CreditCard,
  CircleCheck,
  CircleX,
  Clock3,
  LoaderCircle,
  ChevronLeft,
  ChevronRight,
  Eye,
  BadgeCheck
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

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

const statusIcon = (status) => {
  switch (status) {
    case "paid":
      return CircleCheck;

    case "failed":
      return CircleX;

    default:
      return Clock3;
  }
};

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
const props = defineProps({

  confirmingPaymentId: {
    type: Number,
    default: null
  }

});

const formatPaymentMethod = (value) => {
  if (!value) return "-";

  return value
    .replaceAll("_", " ")
    .replace(/\b\w/g, char =>
      char.toUpperCase()
    );
};

const visiblePages = computed(() => {

  const total =
    adminStore.paymentTotalPages;

  const current =
    adminStore.paymentCurrentPage;

  if (total <= 5) {
    return Array.from(
      { length: total },
      (_, index) => index + 1
    );
  }

  let start = Math.max(
    current - 2,
    1
  );

  let end = Math.min(
    start + 4,
    total
  );

  if (end - start < 4) {
    start = Math.max(
      end - 4,
      1
    );
  }

  return Array.from(
    { length: end - start + 1 },
    (_, index) => start + index
  );
});

const goToPage = async (page) => {

  if (
    page < 1 ||
    page > adminStore.paymentTotalPages ||
    page === adminStore.paymentCurrentPage
  ) {
    return;
  }

  await adminStore.fetchPayments(page);
};

const previousPage = () => {
  goToPage(
    adminStore.paymentCurrentPage - 1
  );
};

const nextPage = () => {
  goToPage(
    adminStore.paymentCurrentPage + 1
  );
};
const emit = defineEmits([
  "view",
  "confirm-cash"
]);
</script>