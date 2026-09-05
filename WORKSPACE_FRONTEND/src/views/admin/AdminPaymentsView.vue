<template>
  <div class="space-y-6">

    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold text-[#23394e]">
          Payments Management
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Review all customer payments and transactions.
        </p>
      </div>

<button
  type="button"
  @click="refreshPayments"
  :disabled="refreshing"
  class="inline-flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
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
      class="flex flex-col gap-3 rounded-xl border border-gray-200 bg-white p-4 sm:flex-row sm:items-center"
    >

      <div class="relative flex-1">

        <Search
          class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9f9f9f]"
        />

        <input
          v-model="adminStore.paymentSearch"
          type="text"
          placeholder="Search user, office or transaction..."
          class="w-full rounded-lg border border-gray-200 py-2 pl-10 pr-4 text-sm text-[#23394e] outline-none transition focus:border-[#f29200]"
        />

      </div>

      <select
        v-model="adminStore.paymentStatusFilter"
        class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
      >
        <option value="">
          All Statuses
        </option>

        <option value="paid">
          Paid
        </option>

        <option value="pending">
          Pending
        </option>

        <option value="failed">
          Failed
        </option>
      </select>

      <button
        v-if="
          adminStore.paymentSearch ||
          adminStore.paymentStatusFilter
        "
        @click="resetFilters"
        class="inline-flex items-center gap-2 rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#9f9f9f] transition hover:border-[#f29200] hover:text-[#f29200]"
      >
        <X class="h-4 w-4" />
        Reset
      </button>

    </div>

      <PaymentsTable
  :confirming-payment-id="confirmingPaymentId"
  @view="openPaymentDetails"
  @confirm-cash="confirmCashPayment"
   />
     <PaymentDetailModal
  :show="showPaymentModal"
  :payment="selectedPayment"
  :confirming="confirmingPaymentId === selectedPayment?.id"
  @close="closePaymentDetails"
  @confirm-cash="confirmCashPayment"
/>

  </div>
</template>

<script setup>
import {ref,
  onMounted,
  onBeforeUnmount,
  watch
} from "vue";
import Swal from "sweetalert2";

import {
  Search,
  RefreshCw,
  X
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";
import PaymentsTable from "@/components/admin/payments/PaymentsTable.vue";
import PaymentDetailModal from "@/components/admin/payments/PaymentDetailModal.vue";
import { toast } from "vue-sonner";
const adminStore = useAdminStore();
const showPaymentModal = ref(false);
const selectedPayment = ref(null);
const confirmingPaymentId = ref(null);
const refreshing = ref(false);
let searchTimeout = null;

const openPaymentDetails = (payment) => {
  selectedPayment.value = payment;
  showPaymentModal.value = true;
};

const closePaymentDetails = () => {
  showPaymentModal.value = false;
  selectedPayment.value = null;
};

const refreshPayments = async () => {
  if (refreshing.value) return;

  refreshing.value = true;

  try {
    adminStore.paymentSearch = "";
    adminStore.paymentStatusFilter = "";

    clearTimeout(searchTimeout);

    await adminStore.fetchPayments(1);

    toast.success(
      "Payments refreshed successfully."
    );

  } catch (error) {

    console.error(
      "Failed to refresh payments:",
      error
    );

    toast.error(
      "Unable to refresh payments."
    );

  } finally {
    refreshing.value = false;
  }
};

const confirmCashPayment = async (payment) => {

  if (
    !payment ||
    payment.payment_method !== "cash" ||
    payment.status !== "pending"
  ) {
    return;
  }


  const result = await Swal.fire({
    title: "Confirm cash payment?",

    html: `
      <div style="text-align:left;font-size:14px;line-height:1.8">
        <p>
          <strong>Customer:</strong>
          ${payment.username || "-"}
        </p>

        <p>
          <strong>Workspace:</strong>
          ${payment.office_title || "-"}
        </p>

        <p>
          <strong>Amount:</strong>
          ${payment.amount} ${payment.currency}
        </p>
      </div>
    `,

    icon: "question",

    showCancelButton: true,

    confirmButtonText: "Confirm Payment",
    cancelButtonText: "Cancel",

    confirmButtonColor: "#f29200",
    cancelButtonColor: "#23394e",

    reverseButtons: true
  });


  if (!result.isConfirmed) {
    return;
  }


  confirmingPaymentId.value =
    payment.id;


  try {

    const result =
      await adminStore.confirmCashPayment(
        payment.id
      );


    if (!result.success) {

      await Swal.fire({
        title: "Unable to confirm payment",

        text:
          result.error ||
          "Something went wrong. Please try again.",

        icon: "error",

        confirmButtonText: "Close",

        confirmButtonColor: "#23394e"
      });

      return;
    }


    const updatedPayment =
      result.payment;


    // Update modal if open
    if (
      selectedPayment.value?.id ===
      payment.id
    ) {

      selectedPayment.value =
        updatedPayment;

    }


    await Swal.fire({
      title: "Payment Confirmed",

      text:
        "The cash payment has been confirmed successfully.",

      icon: "success",

      confirmButtonText: "Done",

      confirmButtonColor: "#f29200"
    });


  } catch (error) {

    console.error(
      "Confirm cash payment error:",
      error
    );


    await Swal.fire({
      title: "Unable to confirm payment",

      text:
        error.response?.data?.error ||
        error.message ||
        "Something went wrong. Please try again.",

      icon: "error",

      confirmButtonText: "Close",

      confirmButtonColor: "#23394e"
    });


  } finally {

    confirmingPaymentId.value =
      null;

  }

};

const resetFilters = () => {
  adminStore.paymentSearch = "";
  adminStore.paymentStatusFilter = "";
};

watch(
  () => adminStore.paymentSearch,
  () => {
    clearTimeout(searchTimeout);

    searchTimeout = setTimeout(() => {
      adminStore.fetchPayments(1);
    }, 400);
  }
);

watch(
  () => adminStore.paymentStatusFilter,
  () => {
    adminStore.fetchPayments(1);
  }
);

onMounted(() => {
  adminStore.fetchPayments(1);
});

onBeforeUnmount(() => {
  clearTimeout(searchTimeout);
});
</script>