<template>
  <div class="space-y-6">

    <!-- Header -->

    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold text-[#23394e]">
          Analytics
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Track platform performance and booking activity.
        </p>
      </div>

<button
  type="button"
  @click="refreshAnalytics"
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

    <!-- Loading -->

    <div
      v-if="adminStore.loading && !adminStore.analytics.dashboard"
      class="flex items-center justify-center py-16"
    >
      <LoaderCircle
        class="h-6 w-6 animate-spin text-[#f29200]"
      />
    </div>

    <template v-else>

      <!-- KPI Cards -->

      <div
        class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4"
      >

        <div
          v-for="card in cards"
          :key="card.label"
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div
            class="mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
          >
            <component
              :is="card.icon"
              class="h-5 w-5 text-[#f29200]"
            />
          </div>

          <p class="text-sm text-[#9f9f9f]">
            {{ card.label }}
          </p>

          <p class="mt-2 text-2xl font-bold text-[#23394e]">
            {{ card.value }}
          </p>
        </div>

      </div>

      <!-- Highlights -->

      <div class="grid gap-4 md:grid-cols-3">

        <div
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div class="flex items-center gap-3">

            <div
              class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
            >
              <Building2
                class="h-5 w-5 text-[#f29200]"
              />
            </div>

            <div>
              <p class="text-xs text-[#9f9f9f]">
                Most Booked Office
              </p>

              <p class="mt-1 font-semibold text-[#23394e]">
                {{
                  adminStore.analytics.most_booked_office
                    ?.office__title || "No data"
                }}
              </p>

              <p class="text-xs text-[#9f9f9f]">
                {{
                  adminStore.analytics.most_booked_office
                    ?.total || 0
                }}
                bookings
              </p>
            </div>

          </div>
        </div>

        <div
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div class="flex items-center gap-3">

            <div
              class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
            >
              <MapPin
                class="h-5 w-5 text-[#f29200]"
              />
            </div>

            <div>
              <p class="text-xs text-[#9f9f9f]">
                Most Popular City
              </p>

              <p class="mt-1 font-semibold text-[#23394e]">
                {{
                  adminStore.analytics.most_popular_city
                    ?.office__city || "No data"
                }}
              </p>

              <p class="text-xs text-[#9f9f9f]">
                {{
                  adminStore.analytics.most_popular_city
                    ?.total || 0
                }}
                bookings
              </p>
            </div>

          </div>
        </div>

        <div
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div class="flex items-center gap-3">

            <div
              class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
            >
              <ReceiptText
                class="h-5 w-5 text-[#f29200]"
              />
            </div>

            <div>
              <p class="text-xs text-[#9f9f9f]">
                Average Booking Price
              </p>

              <p class="mt-1 font-semibold text-[#23394e]">
                {{ formatMoney(
                  adminStore.analytics.average_booking_price
                ) }}
              </p>
            </div>

          </div>
        </div>

      </div>

      <!-- Main Charts -->

      <div class="grid gap-6 xl:grid-cols-2">

        <div
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div class="mb-5">
            <h2 class="font-bold text-[#23394e]">
              Revenue Per Month
            </h2>

            <p class="text-sm text-[#9f9f9f]">
              Paid revenue across the year.
            </p>
          </div>

          <div class="h-[320px]">
            <canvas ref="revenueChartCanvas"></canvas>
          </div>
        </div>

        <div
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div class="mb-5">
            <h2 class="font-bold text-[#23394e]">
              Bookings Per Month
            </h2>

            <p class="text-sm text-[#9f9f9f]">
              Number of bookings created each month.
            </p>
          </div>

          <div class="h-[320px]">
            <canvas ref="bookingsChartCanvas"></canvas>
          </div>
        </div>

      </div>

      <!-- Secondary Charts -->

      <div class="grid gap-6 xl:grid-cols-2">

        <div
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div class="mb-5">
            <h2 class="font-bold text-[#23394e]">
              Revenue Per City
            </h2>

            <p class="text-sm text-[#9f9f9f]">
              Booking revenue grouped by office city.
            </p>
          </div>

          <div class="h-[320px]">
            <canvas ref="cityChartCanvas"></canvas>
          </div>
        </div>

        <div
          class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
        >
          <div class="mb-5">
            <h2 class="font-bold text-[#23394e]">
              Booking Status
            </h2>

            <p class="text-sm text-[#9f9f9f]">
              Current booking status distribution.
            </p>
          </div>

          <div
            class="mx-auto h-[320px] max-w-[380px]"
          >
            <canvas ref="statusChartCanvas"></canvas>
          </div>
        </div>

      </div>

    </template>

  </div>
</template>

<script setup>
import {
  ref,
  computed,
  onMounted,
  onBeforeUnmount,
  nextTick
} from "vue";

import {
  Users,
  Building2,
  CalendarDays,
  Banknote,
  MapPin,
  ReceiptText,
  RefreshCw,
  LoaderCircle
} from "lucide-vue-next";

import Chart from "chart.js/auto";

import { useAdminStore } from "@/stores/admin";
import { toast } from "vue-sonner";
const adminStore = useAdminStore();

const revenueChartCanvas = ref(null);
const bookingsChartCanvas = ref(null);
const cityChartCanvas = ref(null);
const statusChartCanvas = ref(null);
const refreshing = ref(false);
let revenueChart = null;
let bookingsChart = null;
let cityChart = null;
let statusChart = null;

const monthNames = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec"
];

const cards = computed(() => [
  {
    label: "Total Users",
    value:
      adminStore.analytics.dashboard
        ?.total_users || 0,
    icon: Users
  },
  {
    label: "Total Offices",
    value:
      adminStore.analytics.dashboard
        ?.total_offices || 0,
    icon: Building2
  },
  {
    label: "Total Bookings",
    value:
      adminStore.analytics.dashboard
        ?.total_bookings || 0,
    icon: CalendarDays
  },
  {
    label: "Total Revenue",
    value: formatMoney(
      adminStore.analytics.dashboard
        ?.total_revenue
    ),
    icon: Banknote
  }
]);

const formatMoney = (value) => {

  const amount =
    Number(value || 0);

  return `${amount.toLocaleString()} MAD`;

};

const destroyCharts = () => {

  revenueChart?.destroy();
  bookingsChart?.destroy();
  cityChart?.destroy();
  statusChart?.destroy();

  revenueChart = null;
  bookingsChart = null;
  cityChart = null;
  statusChart = null;

};

const renderCharts = async () => {

  await nextTick();

  destroyCharts();

  /*
  =========================
      Revenue per month
  =========================
  */

  const revenueMap = {};

  for (
    const item of
    adminStore.analytics.revenue_per_month || []
  ) {
    revenueMap[item.month] =
      Number(item.revenue || 0);
  }

  if (revenueChartCanvas.value) {

    revenueChart = new Chart(
      revenueChartCanvas.value,
      {
        type: "bar",

        data: {
          labels: monthNames,

          datasets: [
            {
              label: "Revenue",
              data: monthNames.map(
                (_, index) =>
                  revenueMap[index + 1] || 0
              ),

              backgroundColor:
                "rgba(242, 146, 0, 0.75)",

              borderColor:
                "#f29200",

              borderWidth: 1,

              borderRadius: 6
            }
          ]
        },

        options: {
          responsive: true,
          maintainAspectRatio: false,

          plugins: {
            legend: {
              display: false
            }
          },

          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      }
    );

  }

  /*
  =========================
      Bookings per month
  =========================
  */

  const bookingsMap = {};

  for (
    const item of
    adminStore.analytics.bookings_per_month || []
  ) {
    bookingsMap[item.month] =
      Number(item.total || 0);
  }

  if (bookingsChartCanvas.value) {

    bookingsChart = new Chart(
      bookingsChartCanvas.value,
      {
        type: "line",

        data: {
          labels: monthNames,

          datasets: [
            {
              label: "Bookings",

              data: monthNames.map(
                (_, index) =>
                  bookingsMap[index + 1] || 0
              ),

              borderColor:
                "#23394e",

              backgroundColor:
                "rgba(35, 57, 78, 0.12)",

              fill: true,

              tension: 0.35,

              pointBackgroundColor:
                "#f29200",

              pointBorderColor:
                "#f29200"
            }
          ]
        },

        options: {
          responsive: true,
          maintainAspectRatio: false,

          plugins: {
            legend: {
              display: false
            }
          },

          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                precision: 0
              }
            }
          }
        }
      }
    );

  }

  /*
  =========================
        Revenue city
  =========================
  */

  const cityData =
    adminStore.analytics.revenue_per_city || [];

  if (cityChartCanvas.value) {

    cityChart = new Chart(
      cityChartCanvas.value,
      {
        type: "bar",

        data: {
          labels: cityData.map(
            item => item.booking__office__city
          ),

          datasets: [
            {
              label: "Revenue",

              data: cityData.map(
                item =>
                  Number(item.revenue || 0)
              ),

              backgroundColor:
                "rgba(35, 57, 78, 0.8)",

              borderColor:
                "#23394e",

              borderWidth: 1,

              borderRadius: 6
            }
          ]
        },

        options: {
          responsive: true,
          maintainAspectRatio: false,

          indexAxis: "y",

          plugins: {
            legend: {
              display: false
            }
          },

          scales: {
            x: {
              beginAtZero: true
            }
          }
        }
      }
    );

  }

  /*
  =========================
        Booking status
  =========================
  */

  const status =
    adminStore.analytics.booking_status || {};

  if (statusChartCanvas.value) {

    statusChart = new Chart(
      statusChartCanvas.value,
      {
        type: "doughnut",

        data: {
          labels: [
            "Pending",
            "Confirmed",
            "Cancelled"
          ],

          datasets: [
            {
              data: [
                status.pending || 0,
                status.confirmed || 0,
                status.cancelled || 0
              ],

              backgroundColor: [
                "#f29200",
                "#23394e",
                "#9f9f9f"
              ],

              borderWidth: 0
            }
          ]
        },

        options: {
          responsive: true,
          maintainAspectRatio: false,

          cutout: "68%",

          plugins: {
            legend: {
              position: "bottom",

              labels: {
                boxWidth: 12,
                padding: 18
              }
            }
          }
        }
      }
    );

  }

};

const loadAnalytics = async () => {

  await adminStore.fetchAnalytics();

  await renderCharts();

};

const refreshAnalytics = async () => {
  if (refreshing.value) {
    return;
  }

  refreshing.value = true;

  try {
    await loadAnalytics();

    toast.success(
      "Analytics refreshed successfully."
    );
  } catch (error) {
    console.error(
      "Failed to refresh analytics:",
      error
    );

    toast.error(
      "Unable to refresh analytics."
    );
  } finally {
    refreshing.value = false;
  }
};

onMounted(() => {

  loadAnalytics();

});

onBeforeUnmount(() => {

  destroyCharts();

});
</script>