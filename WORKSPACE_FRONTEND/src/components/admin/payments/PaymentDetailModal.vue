<template>
  <div
    v-if="show"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4"
    @click.self="emit('close')"
  >

    <div
      class="max-h-[85vh] w-full max-w-2xl overflow-y-auto rounded-2xl bg-white shadow-xl"
    >

      <!-- Header -->

      <div
        class="flex items-center justify-between border-b border-gray-200 px-6 py-4"
      >

        <div>
          <h2 class="text-lg font-bold text-[#23394e]">
            Payment Details
          </h2>

          <p class="mt-1 text-sm text-[#9f9f9f]">
            {{ payment?.invoice_number || "-" }}
          </p>
        </div>

        <button
          @click="emit('close')"
          class="rounded-lg p-2 text-[#9f9f9f] transition hover:bg-gray-100 hover:text-[#23394e]"
        >
          <X class="h-5 w-5" />
        </button>

      </div>

      <div
        v-if="payment"
        class="space-y-6 p-6"
      >

        <!-- Status + amount -->

        <div
          class="grid gap-4 sm:grid-cols-2"
        >

          <div
            class="rounded-xl border border-gray-200 p-4"
          >
            <p class="text-xs text-[#9f9f9f]">
              Amount
            </p>

            <p class="mt-2 text-xl font-bold text-[#23394e]">
              {{ payment.amount }}
              {{ payment.currency }}
            </p>
          </div>

          <div
            class="rounded-xl border border-gray-200 p-4"
          >
            <p class="text-xs text-[#9f9f9f]">
              Status
            </p>

            <div class="mt-2">

              <span
                class="inline-flex items-center gap-2 rounded-full px-3 py-1 text-sm font-semibold"
                :class="statusClass(payment.status)"
              >

                <component
                  :is="statusIcon(payment.status)"
                  class="h-4 w-4"
                />

                {{ formatStatus(payment.status) }}

              </span>

            </div>
          </div>

        </div>

        <!-- Customer -->

        <section>
          <h3
            class="mb-3 text-sm font-semibold text-[#23394e]"
          >
            Customer
          </h3>

          <div
            class="rounded-xl border border-gray-200 p-4"
          >

            <div class="flex items-center gap-3">

              <div
                class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
              >
                <User class="h-5 w-5 text-[#f29200]" />
              </div>

              <div>

                <p class="font-semibold text-[#23394e]">
                  {{ payment.username || "Unknown" }}
                </p>

                <p class="text-sm text-[#9f9f9f]">
                  {{ payment.user_email || "-" }}
                </p>

              </div>

            </div>

          </div>
        </section>

        <!-- Office -->

        <section>

          <h3
            class="mb-3 text-sm font-semibold text-[#23394e]"
          >
            Workspace
          </h3>

          <div
            class="rounded-xl border border-gray-200 p-4"
          >

            <div class="flex gap-4">

              <img
                v-if="payment.office_image"
                :src="payment.office_image"
                :alt="payment.office_title"
                class="h-16 w-20 rounded-lg object-cover"
              />

              <div
                v-else
                class="flex h-16 w-20 items-center justify-center rounded-lg bg-gray-100"
              >
                <Building2
                  class="h-6 w-6 text-[#9f9f9f]"
                />
              </div>

              <div>

                <p class="font-semibold text-[#23394e]">
                  {{ payment.office_title || "-" }}
                </p>

                <div
                  class="mt-1 flex items-center gap-1 text-sm text-[#9f9f9f]"
                >
                  <MapPin class="h-4 w-4" />

                  {{ payment.office_city || "-" }}
                </div>

              </div>

            </div>

          </div>

        </section>

        <!-- Booking -->

        <section>

          <h3
            class="mb-3 text-sm font-semibold text-[#23394e]"
          >
            Booking Information
          </h3>

          <div
            class="grid gap-4 rounded-xl border border-gray-200 p-4 sm:grid-cols-3"
          >

            <div>

              <p class="text-xs text-[#9f9f9f]">
                Start Date
              </p>

              <p class="mt-1 text-sm font-medium text-[#23394e]">
                {{ formatDate(payment.start_date) }}
              </p>

            </div>

            <div>

              <p class="text-xs text-[#9f9f9f]">
                End Date
              </p>

              <p class="mt-1 text-sm font-medium text-[#23394e]">
                {{ formatDate(payment.end_date) }}
              </p>

            </div>

            <div>

              <p class="text-xs text-[#9f9f9f]">
                Duration
              </p>

              <p class="mt-1 text-sm font-medium text-[#23394e]">
                {{ payment.duration ?? 0 }} days
              </p>

            </div>

          </div>

        </section>

        <!-- Transaction -->

        <section>

          <h3
            class="mb-3 text-sm font-semibold text-[#23394e]"
          >
            Transaction
          </h3>

          <div
            class="space-y-4 rounded-xl border border-gray-200 p-4"
          >

            <div
              class="flex flex-col justify-between gap-1 sm:flex-row"
            >
              <span class="text-sm text-[#9f9f9f]">
                Transaction ID
              </span>

              <span
                class="break-all text-sm font-medium text-[#23394e]"
              >
                {{ payment.transaction_id || "-" }}
              </span>
            </div>

            <div
              class="flex justify-between gap-4"
            >
              <span class="text-sm text-[#9f9f9f]">
                Method
              </span>

              <span class="text-sm font-medium text-[#23394e]">
                {{ formatPaymentMethod(payment.payment_method) }}
              </span>
            </div>

            <div
              class="flex justify-between gap-4"
            >
              <span class="text-sm text-[#9f9f9f]">
                Paid At
              </span>

              <span class="text-sm font-medium text-[#23394e]">
                {{ formatDateTime(payment.paid_at) }}
              </span>
            </div>

            <div
              class="flex justify-between gap-4"
            >
              <span class="text-sm text-[#9f9f9f]">
                Created At
              </span>

              <span class="text-sm font-medium text-[#23394e]">
                {{ formatDateTime(payment.created_at) }}
              </span>
            </div>

          </div>

        </section>

      </div>

      <!-- Footer -->

<div
  class="flex items-center justify-between gap-3 border-t border-gray-200 px-6 py-4"
>

  <div>

    <button
      v-if="
        payment?.payment_method === 'cash' &&
        payment?.status === 'pending'
      "
      type="button"
      @click="emit('confirm-cash', payment)"
      :disabled="confirming"
      class="inline-flex items-center gap-2 rounded-lg bg-emerald-600 px-4 py-2 text-sm font-semibold text-white transition hover:bg-emerald-700 disabled:cursor-not-allowed disabled:opacity-50"
    >

      <LoaderCircle
        v-if="confirming"
        class="h-4 w-4 animate-spin"
      />

      <BadgeCheck
        v-else
        class="h-4 w-4"
      />

      {{
        confirming
          ? "Confirming..."
          : "Confirm Cash Payment"
      }}

    </button>

  </div>


  <button
    type="button"
    @click="emit('close')"
    class="rounded-lg bg-[#23394e] px-5 py-2 text-sm font-medium text-white transition hover:opacity-90"
  >
    Close
  </button>

</div>

    </div>

  </div>
</template>

<script setup>
import {
  X,
  User,
  Building2,
  MapPin,
  CircleCheck,
  CircleX,
  Clock3,
  BadgeCheck,
  LoaderCircle
} from "lucide-vue-next";

defineProps({
  show: {
    type: Boolean,
    default: false
  },

  payment: {
    type: Object,
    default: null
  },
  confirming: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits([
  "close",
  "confirm-cash"
]);

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

const formatDateTime = (value) => {
  if (!value) return "-";

  return new Date(value).toLocaleString(
    undefined,
    {
      day: "2-digit",
      month: "short",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit"
    }
  );
};

const formatPaymentMethod = (value) => {
  if (!value) return "-";

  return value
    .replaceAll("_", " ")
    .replace(/\b\w/g, char =>
      char.toUpperCase()
    );
};
</script>