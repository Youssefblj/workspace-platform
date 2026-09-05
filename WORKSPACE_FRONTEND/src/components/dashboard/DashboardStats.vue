<template>
  <section class="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">

    <div
      v-for="card in stats"
      :key="card.title"
      class="group relative overflow-hidden rounded-3xl border border-gray-100 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
    >

      <!-- Glow -->
      <div
        class="absolute -right-10 -top-10 h-28 w-28 rounded-full bg-amber-100 opacity-0 blur-3xl transition duration-500 group-hover:opacity-70"
      ></div>

      <div class="relative">

        <!-- Icon -->
        <div
          class="flex h-14 w-14 items-center justify-center rounded-2xl transition duration-300 group-hover:scale-110"
          :class="card.color"
        >
          <component
            :is="card.icon"
            class="h-7 w-7"
          />
        </div>

        <!-- Title -->
        <p class="mt-6 text-sm font-semibold text-gray-500">
          {{ card.title }}
        </p>

        <!-- Value -->
        <h3 class="mt-2 text-3xl font-black text-gray-900">
          {{ card.value }}
        </h3>

        <!-- Footer -->
        <div class="mt-5 flex items-center justify-between">

          <span
            class="inline-flex items-center rounded-full px-3 py-1 text-xs font-semibold"
            :class="card.badgeClass"
          >
            {{ card.change }}
          </span>

          <TrendingUp
            class="h-5 w-5 text-emerald-500 transition duration-300 group-hover:translate-x-1"
          />

        </div>

      </div>

    </div>

  </section>
</template>

<script setup>
import { computed } from "vue";

import {
  CalendarDays,
  Heart,
  CreditCard,
  DollarSign,
  TrendingUp
} from "lucide-vue-next";

const props = defineProps({
  bookings: {
    type: Array,
    default: () => []
  },

  favorites: {
    type: Array,
    default: () => []
  },

  payments: {
    type: Array,
    default: () => []
  },

  reservationCount: {
    type: Number,
    default: 0
  },

  favoriteCount: {
    type: Number,
    default: 0
  },

  paymentCount: {
    type: Number,
    default: 0
  }
})

const totalSpent = computed(() => {
  return props.payments.reduce((total, payment) => {
    return total + Number(payment.amount || 0);
  }, 0);
});

const stats = computed(() => [
  {
    title: "Reservations",
    value: props.reservationCount,
    icon: CalendarDays,
    color: "bg-blue-100 text-blue-600",
    change: `${props.reservationCount} Total`,
    badgeClass: "bg-blue-50 text-blue-600"
  },

  {
    title: "Favorites",
    value: props.favoriteCount,
    icon: Heart,
    color: "bg-red-100 text-red-500",
    change: `${props.favoriteCount} Saved`,
    badgeClass: "bg-red-50 text-red-500"
  },

  {
    title: "Payments",
    value: props.paymentCount,
    icon: CreditCard,
    color: "bg-emerald-100 text-emerald-600",
    change: `${props.payments.length} Completed`,
    badgeClass: "bg-emerald-50 text-emerald-600"
  },

  {
    title: "Total Spent",
    value: `$${totalSpent.value.toFixed(2)}`,
    icon: DollarSign,
    color: "bg-amber-100 text-amber-600",
    change: "Overall",
    badgeClass: "bg-amber-50 text-amber-600"
  }
]);
</script>