<script setup>
import {
  ref,
  computed,
  watch
} from "vue";

import BillingStats from "./BillingStats.vue";
import BillingToolbar from "./BillingToolbar.vue";
import InvoicesTable from "./InvoicesTable.vue";


const props = defineProps({
  payments: {
    type: Array,
    default: () => []
  }
});


const search = ref("");
const status = ref("all");


/* ==========================================================
   Filtering
========================================================== */

const filteredPayments = computed(() => {

  return props.payments.filter(payment => {

    const searchValue =
      search.value.trim().toLowerCase();

    const matchesSearch =
      !searchValue ||
      payment.office_title
        ?.toLowerCase()
        .includes(searchValue) ||
      payment.invoice_number
        ?.toLowerCase()
        .includes(searchValue);

    const matchesStatus =
      status.value === "all" ||
      payment.status === status.value;

    return (
      matchesSearch &&
      matchesStatus
    );

  });

});


/* ==========================================================
   Pagination
========================================================== */

const PAGE_SIZE = 6;

const currentPage = ref(1);


const totalPages = computed(() => {

  return Math.max(
    1,
    Math.ceil(
      filteredPayments.value.length /
      PAGE_SIZE
    )
  );

});


const paginatedPayments = computed(() => {

  const start =
    (currentPage.value - 1) *
    PAGE_SIZE;

  const end =
    start + PAGE_SIZE;

  return filteredPayments.value.slice(
    start,
    end
  );

});


const visiblePages = computed(() => {

  const total =
    totalPages.value;

  const current =
    currentPage.value;


  if (total <= 5) {

    return Array.from(
      {
        length: total
      },
      (_, index) =>
        index + 1
    );

  }


  let start =
    Math.max(
      1,
      current - 2
    );

  let end =
    Math.min(
      total,
      start + 4
    );


  if (end - start < 4) {

    start =
      Math.max(
        1,
        end - 4
      );

  }


  return Array.from(
    {
      length:
        end - start + 1
    },
    (_, index) =>
      start + index
  );

});


const changePage = page => {

  if (
    page < 1 ||
    page > totalPages.value ||
    page === currentPage.value
  ) {
    return;
  }

  currentPage.value = page;

};


/* Reset page when search/status changes */

watch(
  [search, status],
  () => {
    currentPage.value = 1;
  }
);


/* Keep page valid when payments change */

watch(
  totalPages,
  newTotal => {

    if (
      currentPage.value >
      newTotal
    ) {
      currentPage.value =
        newTotal;
    }

  }
);


/* ==========================================================
   CSV Export
========================================================== */

const exportCSV = () => {

  const rows = [
    [
      "Invoice",
      "Office",
      "City",
      "Amount",
      "Status",
      "Date"
    ],

    ...filteredPayments.value.map(
      payment => [

        payment.invoice_number,

        payment.office_title,

        payment.office_city,

        payment.amount,

        payment.status,

        payment.created_at

      ]
    )
  ];


  const csv = rows
    .map(row => row.join(","))
    .join("\n");


  const blob = new Blob(
    [csv],
    {
      type: "text/csv"
    }
  );


  const url =
    URL.createObjectURL(blob);


  const a =
    document.createElement("a");


  a.href = url;

  a.download =
    "payments.csv";

  a.click();


  URL.revokeObjectURL(url);

};
</script>


<template>

  <div class="space-y-5">

    <!-- Stats use ALL filtered payments -->
    <BillingStats
      :payments="filteredPayments"
    />


    <BillingToolbar
      v-model:search="search"
      v-model:status="status"
      @export="exportCSV"
    />


    <!-- Table gets only current page -->
    <InvoicesTable
      :payments="paginatedPayments"
    />


    <!-- Pagination -->
    <div
      v-if="
        filteredPayments.length > 0 &&
        totalPages > 1
      "
      class="flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-100 bg-white px-4 py-4 shadow-sm"
    >

      <p
        class="text-xs font-medium text-[#9f9f9f]"
      >
        Page

        <span
          class="font-bold text-[#23394e]"
        >
          {{ currentPage }}
        </span>

        of

        <span
          class="font-bold text-[#23394e]"
        >
          {{ totalPages }}
        </span>
      </p>


      <div class="flex items-center gap-2">

        <!-- Previous -->
        <button
          type="button"
          :disabled="currentPage <= 1"
          @click="
            changePage(
              currentPage - 1
            )
          "
          class="flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200 bg-white text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
        >
          <span>
            ‹
          </span>
        </button>


        <!-- Pages -->
        <button
          v-for="page in visiblePages"
          :key="page"
          type="button"
          @click="changePage(page)"
          :class="[
            'flex h-9 min-w-9 items-center justify-center rounded-lg px-3 text-xs font-bold transition',

            page === currentPage
              ? 'bg-[#f29200] text-white shadow-sm'
              : 'border border-gray-200 bg-white text-[#23394e] hover:border-[#f29200] hover:text-[#f29200]'
          ]"
        >
          {{ page }}
        </button>


        <!-- Next -->
        <button
          type="button"
          :disabled="
            currentPage >= totalPages
          "
          @click="
            changePage(
              currentPage + 1
            )
          "
          class="flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200 bg-white text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
        >
          <span>
            ›
          </span>
        </button>

      </div>

    </div>

  </div>

</template>