<script setup>
import {
  Building2,
  CalendarDays,
  Clock3,
  CreditCard,
  Download,
  Eye,
  MapPin,
  WalletCards,
  X,
} from "lucide-vue-next";
import { ref } from "vue";

import { jsPDF } from "jspdf";
const props = defineProps({
  payments: {
    type: Array,
    default: () => [],
  },
});

const formatDate = (date) =>
  new Date(date).toLocaleDateString("en-US", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });

const formatPaymentMethod = (method) => {
  const methods = {
    card: "Card",
    cash: "Cash",
    paypal: "PayPal",
  };

  return methods[method] || method;
};

const imageUrl = (url) => {
  if (!url) return "";

  if (url.startsWith("http")) return url;

  return `http://127.0.0.1:8000${url}`;
};

const selectedInvoice = ref(null);
const showInvoice = ref(false);

const openInvoice = (payment) => {
  selectedInvoice.value = payment;
  showInvoice.value = true;
};

const closeInvoice = () => {
  showInvoice.value = false;
};
const downloadInvoice = (payment) => {
  const pdf = new jsPDF({
    orientation: "portrait",
    unit: "mm",
    format: "a4",
  });

  const dark = [40, 40, 40];
  const gray = [120, 120, 120];

  const logo = new Image();
  logo.src = "/wlogo.png";

  logo.onload = () => {
    // ==========================
    // HEADER
    // ==========================

    pdf.addImage(logo, "PNG", 15, 10, 18, 18);

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(20);
    pdf.setTextColor(...dark);
    pdf.text("Workspace", 40, 18);

    pdf.setFont("helvetica", "normal");
    pdf.setFontSize(11);
    pdf.text("Workspace Reservation Invoice", 40, 25);

    pdf.setLineWidth(0.4);
    pdf.setDrawColor(180);
    pdf.line(15, 33, 195, 33);

    // ==========================
    // TITLE
    // ==========================

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(18);
    pdf.text("INVOICE", 15, 45);

    // Invoice Number (right side)

    pdf.setFontSize(11);

    pdf.text("Invoice #", 145, 18);
    pdf.setFont("helvetica", "normal");
    pdf.text(payment.invoice_number, 195, 18, { align: "right" });

    // ==========================
    // INFORMATION
    // ==========================

    let y = 58;

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(10);

    pdf.text("Status", 15, y);
    pdf.text("Date", 15, y + 8);
    pdf.text("Payment", 15, y + 16);

    pdf.setFont("helvetica", "normal");

    pdf.text(payment.status.toUpperCase(), 55, y);

    pdf.text(formatDate(payment.created_at), 55, y + 8);

    pdf.text(payment.payment_method.toUpperCase(), 55, y + 16);

    // ==========================
    // WORKSPACE
    // ==========================

    y = 92;

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(12);

    pdf.text("WORKSPACE", 15, y);

    pdf.line(15, y + 2, 195, y + 2);

    pdf.setFont("helvetica", "normal");
    pdf.setFontSize(10);

    pdf.text(payment.office_title, 20, y + 12);

    pdf.text(payment.office_city, 20, y + 20);

    // ==========================
    // BOOKING DETAILS
    // ==========================

    y = 130;

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(12);

    pdf.text("BOOKING DETAILS", 15, y);

    pdf.line(15, y + 2, 195, y + 2);

    pdf.setFont("helvetica", "normal");
    pdf.setFontSize(10);

    pdf.text("Start Date", 20, y + 12);
    pdf.text(payment.start_date, 65, y + 12);

    pdf.text("End Date", 20, y + 20);
    pdf.text(payment.end_date, 65, y + 20);

    pdf.text("Duration", 20, y + 28);
    pdf.text(`${payment.duration} Days`, 65, y + 28);

    // ==========================
    // PAYMENT SUMMARY
    // ==========================

    y = 180;

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(12);

    pdf.text("PAYMENT SUMMARY", 15, y);

    pdf.line(15, y + 2, 195, y + 2);

    pdf.setFont("helvetica", "normal");
    pdf.setFontSize(10);

    pdf.text("Amount", 20, y + 15);

    pdf.text(
      `${payment.amount} ${payment.currency}`,
      190,
      y + 15,
      { align: "right" }
    );

    pdf.line(15, y + 20, 195, y + 20);

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(14);

    pdf.text("TOTAL", 140, y + 32);

    pdf.text(
      `${payment.amount} ${payment.currency}`,
      190,
      y + 32,
      { align: "right" }
    );

    // ==========================
    // FOOTER
    // ==========================

    pdf.setDrawColor(180);
    pdf.line(15, 270, 195, 270);

    pdf.setFont("helvetica", "normal");
    pdf.setFontSize(9);
    pdf.setTextColor(...gray);

    pdf.text("Thank you for choosing Workspace.", 15, 278);

    pdf.text(
      "Generated automatically by Workspace Platform",
      15,
      284
    );

    pdf.save(`${payment.invoice_number}.pdf`);
  };
};
</script>

<template>
  <div class="overflow-hidden rounded-2xl border border-gray-100 bg-white shadow-sm">

    <!-- Header -->
    <div class="border-b border-gray-100 px-5 py-4 sm:px-6">

      <h2 class="text-lg font-bold text-[#23394E]">
        Payment History
      </h2>

      <p class="mt-1 text-sm text-[#9F9F9F]">
        All invoices generated from your workspace bookings.
      </p>

    </div>

    <!-- Empty -->
    <div
      v-if="payments.length === 0"
      class="flex flex-col items-center justify-center px-4 py-14 text-center"
    >
      <Download class="mb-3 h-10 w-10 text-[#9F9F9F]/50" />

      <h3 class="text-base font-bold text-[#23394E]">
        No invoices yet
      </h3>

      <p class="mt-1 text-sm text-[#9F9F9F]">
        Your payment history will appear here.
      </p>
    </div>

    <!-- Table -->
    <div v-else class="overflow-x-auto">

      <table class="min-w-[820px] w-full">

        <thead class="bg-gray-50">

          <tr>

            <th class="px-5 py-3 text-left text-[11px] font-bold uppercase tracking-wide text-[#9F9F9F] sm:px-6">
              Workspace
            </th>

            <th class="px-5 py-3 text-left text-[11px] font-bold uppercase tracking-wide text-[#9F9F9F]">
              Invoice
            </th>

            <th class="px-5 py-3 text-left text-[11px] font-bold uppercase tracking-wide text-[#9F9F9F]">
              Booking
            </th>

            <th class="px-5 py-3 text-left text-[11px] font-bold uppercase tracking-wide text-[#9F9F9F]">
              Amount
            </th>

            <th class="px-5 py-3 text-left text-[11px] font-bold uppercase tracking-wide text-[#9F9F9F]">
              Status
            </th>

            <th class="px-5 py-3 text-center text-[11px] font-bold uppercase tracking-wide text-[#9F9F9F]">
              Actions
            </th>

          </tr>

        </thead>

        <tbody class="divide-y divide-gray-100">

          <tr
            v-for="payment in payments"
            :key="payment.id"
            class="align-middle transition duration-200 hover:bg-[#F29200]/5"
          >

            <!-- Workspace -->
            <td class="px-5 py-4 sm:px-6">

              <div class="flex min-w-0 items-center gap-3">

                <img
                  :src="imageUrl(payment.office_image)"
                  class="h-12 w-12 shrink-0 rounded-xl object-cover shadow-sm"
                >

                <div class="min-w-0">

                  <h4 class="max-w-[190px] truncate text-sm font-bold text-[#23394E]">
                    {{ payment.office_title }}
                  </h4>

                  <div class="mt-1 flex items-center gap-1 text-xs text-[#9F9F9F]">

                    <MapPin class="h-3.5 w-3.5 shrink-0 text-[#F29200]" />

                    {{ payment.office_city }}

                  </div>

                </div>

              </div>

            </td>

            <!-- Invoice -->
            <td class="px-5 py-4">

              <span
                class="inline-flex rounded-lg bg-[#F29200]/10 px-2.5 py-1 text-xs font-bold text-[#F29200]"
              >
                {{ payment.invoice_number }}
              </span>

            </td>

            <!-- Booking -->
            <td class="px-5 py-4">

              <div class="space-y-1.5">

                <div class="flex items-center gap-1.5 whitespace-nowrap text-xs font-medium text-[#23394E]">

                  <CalendarDays class="h-3.5 w-3.5 text-[#F29200]" />

                  {{ formatDate(payment.start_date) }}

                  →

                  {{ formatDate(payment.end_date) }}

                </div>

                <div
                  class="inline-flex rounded-lg bg-gray-100 px-2 py-0.5 text-[11px] font-semibold text-[#9F9F9F]"
                >
                  {{ payment.duration }}
                  {{ payment.duration > 1 ? "Days" : "Day" }}
                </div>

              </div>

            </td>

            <!-- Amount -->
            <td class="px-5 py-4">

              <div>

                <div class="text-lg font-black text-[#23394E]">
                  {{ payment.amount }}
                </div>

                <div class="text-xs font-medium text-[#9F9F9F]">
                  {{ payment.currency }}
                </div>

              </div>

            </td>

            <!-- Status -->
            <td class="px-5 py-4">

              <span
                :class="payment.status === 'paid' ? 'bg-green-100 text-green-700' : payment.status === 'failed' ? 'bg-red-100 text-red-700' : 'bg-[#F29200]/10 text-[#F29200]'"
                class="inline-flex rounded-full px-2.5 py-1 text-xs font-bold capitalize"
              >
                {{ payment.status }}
              </span>

            </td>

            <!-- Actions -->
            <td class="px-5 py-4">

              <div class="flex justify-center gap-2">

<button
@click="openInvoice(payment)"
title="View invoice"
aria-label="View invoice"
class="flex h-8 w-8 items-center justify-center rounded-lg border border-gray-200 text-[#23394E] transition duration-200 hover:border-[#F29200] hover:bg-[#F29200]/10 hover:text-[#F29200]"
>
<Eye class="h-4 w-4"/>
</button>

                <button
@click="openInvoice(payment)"
title="Open invoice download"
aria-label="Open invoice download"
class="flex h-8 w-8 items-center justify-center rounded-lg border border-gray-200 text-[#23394E] transition duration-200 hover:border-[#F29200] hover:bg-[#F29200]/10 hover:text-[#F29200]"
>
<Download class="h-4 w-4"/>
</button>

              </div>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>

  <Teleport to="body">
    <div
      v-if="showInvoice"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4 backdrop-blur-sm"
    >
      <div class="flex max-h-[90vh] w-full max-w-xl flex-col overflow-hidden rounded-2xl border border-gray-100 bg-white shadow-2xl">
        <div class="flex items-start justify-between gap-4 border-b border-gray-100 px-5 py-4 sm:px-6">
          <div class="flex min-w-0 items-center gap-3">
            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-[#F29200]/10">
              <WalletCards class="h-5 w-5 text-[#F29200]" />
            </div>

            <div class="min-w-0">
              <h2 class="text-lg font-bold text-[#23394E]">
                Invoice
              </h2>
              <p class="mt-0.5 truncate text-sm text-[#9F9F9F]">
                {{ selectedInvoice.invoice_number }}
              </p>
            </div>
          </div>

          <button
            type="button"
            title="Close invoice"
            aria-label="Close invoice"
            @click="closeInvoice"
            class="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg text-[#9F9F9F] transition duration-200 hover:bg-gray-100 hover:text-[#23394E] focus:outline-none focus:ring-4 focus:ring-[#F29200]/10"
          >
            <X class="h-4 w-4" />
          </button>
        </div>

        <div class="min-h-0 overflow-y-auto p-5 sm:p-6">
          <div class="grid gap-3 sm:grid-cols-2">
            <div class="rounded-xl border border-gray-100 bg-gray-50 p-3">
              <div class="flex items-center gap-2 text-xs font-medium text-[#9F9F9F]">
                <Building2 class="h-3.5 w-3.5 text-[#F29200]" />
                Office
              </div>
              <p class="mt-1.5 truncate text-sm font-semibold text-[#23394E]">
                {{ selectedInvoice.office_title }}
              </p>
            </div>

            <div class="rounded-xl border border-gray-100 bg-gray-50 p-3">
              <div class="flex items-center gap-2 text-xs font-medium text-[#9F9F9F]">
                <MapPin class="h-3.5 w-3.5 text-[#F29200]" />
                City
              </div>
              <p class="mt-1.5 truncate text-sm font-semibold text-[#23394E]">
                {{ selectedInvoice.office_city }}
              </p>
            </div>

            <div class="rounded-xl border border-gray-100 bg-gray-50 p-3">
              <div class="flex items-center gap-2 text-xs font-medium text-[#9F9F9F]">
                <CalendarDays class="h-3.5 w-3.5 text-[#F29200]" />
                Booking dates
              </div>
              <div class="mt-1.5 space-y-0.5 text-sm font-semibold text-[#23394E]">
                <p>{{ formatDate(selectedInvoice.start_date) }}</p>
                <p>{{ formatDate(selectedInvoice.end_date) }}</p>
              </div>
            </div>

            <div class="rounded-xl border border-gray-100 bg-gray-50 p-3">
              <div class="flex items-center gap-2 text-xs font-medium text-[#9F9F9F]">
                <Clock3 class="h-3.5 w-3.5 text-[#F29200]" />
                Duration
              </div>
              <span class="mt-1.5 inline-flex rounded-lg bg-[#23394E]/5 px-2 py-1 text-xs font-semibold text-[#23394E]">
                {{ selectedInvoice.duration }} {{ selectedInvoice.duration > 1 ? "Days" : "Day" }}
              </span>
            </div>

            <div class="rounded-xl border border-gray-100 bg-gray-50 p-3">
              <div class="flex items-center gap-2 text-xs font-medium text-[#9F9F9F]">
                <CreditCard class="h-3.5 w-3.5 text-[#F29200]" />
                Payment method
              </div>
              <p class="mt-1.5 text-sm font-semibold text-[#23394E]">
                {{ formatPaymentMethod(selectedInvoice.payment_method) }}
              </p>
            </div>

            <div class="rounded-xl border border-gray-100 bg-gray-50 p-3">
              <p class="text-xs font-medium text-[#9F9F9F]">
                Status
              </p>
              <span
                :class="selectedInvoice.status === 'paid' ? 'bg-green-100 text-green-700' : selectedInvoice.status === 'failed' ? 'bg-red-100 text-red-700' : 'bg-[#F29200]/10 text-[#F29200]'"
                class="mt-1.5 inline-flex rounded-full px-2.5 py-1 text-xs font-bold capitalize"
              >
                {{ selectedInvoice.status }}
              </span>
            </div>
          </div>

          <div class="mt-4 flex items-end justify-between gap-4 rounded-xl bg-[#23394E]/5 px-4 py-3.5">
            <div>
              <p class="text-xs font-semibold uppercase tracking-wide text-[#9F9F9F]">
                Total
              </p>
              <p class="mt-1 text-2xl font-black text-[#23394E]">
                {{ selectedInvoice.amount }}
                <span class="text-sm font-semibold text-[#9F9F9F]">{{ selectedInvoice.currency }}</span>
              </p>
            </div>

            <span class="text-xs font-medium text-[#9F9F9F]">
              {{ formatDate(selectedInvoice.created_at) }}
            </span>
          </div>
        </div>

        <div class="flex flex-col-reverse gap-3 border-t border-gray-100 bg-gray-50/60 px-5 py-4 sm:flex-row sm:justify-end sm:px-6">
          <button
            type="button"
            @click="closeInvoice"
            class="h-10 rounded-lg border border-gray-200 bg-white px-4 text-sm font-semibold text-[#23394E] transition duration-200 hover:bg-gray-50 focus:outline-none focus:ring-4 focus:ring-[#23394E]/10"
          >
            Close
          </button>

          <button
            type="button"
            @click="downloadInvoice(selectedInvoice)"
            class="inline-flex h-10 items-center justify-center gap-2 rounded-lg bg-[#F29200] px-4 text-sm font-semibold text-white shadow-sm transition duration-200 hover:-translate-y-0.5 hover:bg-[#F29200]/90 hover:shadow-md focus:outline-none focus:ring-4 focus:ring-[#F29200]/20"
          >
            <Download class="h-4 w-4" />
            Download PDF
          </button>
        </div>
      </div>
    </div>
  </Teleport>
</template>
