<template>
  <section
    class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-amber-500 via-orange-500 to-amber-400 p-8 shadow-xl"
  >
    <!-- Background Effects -->
    <div
      class="absolute -right-20 -top-20 h-72 w-72 rounded-full bg-white/10 blur-3xl"
    ></div>

    <div
      class="absolute -bottom-20 -left-20 h-72 w-72 rounded-full bg-white/10 blur-3xl"
    ></div>

    <div
      class="relative flex flex-col gap-10 lg:flex-row lg:items-center lg:justify-between"
    >
      <!-- Left -->

      <div class="max-w-2xl">

        <div
          class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-4 py-2 backdrop-blur-md"
        >
          <LayoutDashboard class="h-4 w-4 text-white" />

          <span class="text-sm font-medium text-white">
            Dashboard Overview
          </span>
        </div>

        <h1
          class="mt-6 text-4xl font-black tracking-tight text-white lg:text-5xl"
        >
          {{ greeting }},

          <span class="text-amber-100">
            {{ userName }}
          </span>
        </h1>

        <p class="mt-3 text-sm text-amber-100">
          {{ today }}
        </p>

        <p
          class="mt-6 max-w-xl text-lg leading-8 text-amber-50/90"
        >
          Manage your reservations, favorite offices, notifications and
          account activity from one place.
        </p>

        <div class="mt-8 flex gap-4">

          <router-link
            to="/browse-offices"
            class="group inline-flex items-center gap-2 rounded-2xl bg-white px-6 py-3 font-semibold text-amber-600 shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl"
          >
            Browse Offices

            <ArrowRight
              class="h-5 w-5 transition group-hover:translate-x-1"
            />

          </router-link>

        </div>

      </div>

      <!-- Stats -->

      <div
        class="grid w-full max-w-md grid-cols-2 gap-4"
      >

        <!-- Bookings -->

        <div
          class="rounded-2xl border border-white/15 bg-white/10 p-5 backdrop-blur-xl transition duration-300 hover:bg-white/20"
        >
          <CalendarDays class="h-7 w-7 text-white"/>

          <p class="mt-4 text-3xl font-bold text-white">
            {{ activeBookings }}
          </p>

          <span class="text-sm text-amber-100">
            Reservations
          </span>
        </div>

        <!-- Favorites -->

        <div
          class="rounded-2xl border border-white/15 bg-white/10 p-5 backdrop-blur-xl transition duration-300 hover:bg-white/20"
        >
          <Heart class="h-7 w-7 text-white"/>

          <p class="mt-4 text-3xl font-bold text-white">
            {{ favoriteCount }}
          </p>

          <span class="text-sm text-amber-100">
            Favorites
          </span>
        </div>

        <!-- Notifications -->

        <div
          class="rounded-2xl border border-white/15 bg-white/10 p-5 backdrop-blur-xl transition duration-300 hover:bg-white/20"
        >
          <Bell class="h-7 w-7 text-white"/>

          <p class="mt-4 text-3xl font-bold text-white">
            {{ unreadNotifications }}
          </p>

          <span class="text-sm text-amber-100">
            Unread
          </span>
        </div>

        <!-- Payments -->

        <div
          class="rounded-2xl border border-white/15 bg-white/10 p-5 backdrop-blur-xl transition duration-300 hover:bg-white/20"
        >
          <CreditCard class="h-7 w-7 text-white"/>

          <p class="mt-4 text-3xl font-bold text-white">
            {{ payments.length }}
          </p>

          <span class="text-sm text-amber-100">
            Payments
          </span>
        </div>

      </div>

    </div>
  </section>
</template>

<script setup>
import { computed } from "vue";
import { useAuthStore } from "@/stores/auth";

import {
  LayoutDashboard,
  CalendarDays,
  Heart,
  Bell,
  CreditCard,
  ArrowRight
} from "lucide-vue-next";

const authStore = useAuthStore();

const props = defineProps({
  bookings: {
    type: Array,
    default: () => []
  },

  bookingCount: {
    type: Number,
    default: 0
  },

  favorites: {
    type: Array,
    default: () => []
  },

  notifications: {
    type: Array,
    default: () => []
  },

  payments: {
    type: Array,
    default: () => []
  }
});

const userName = computed(() =>
  authStore.user?.username || "User"
);

const greeting = computed(() => {
  const hour = new Date().getHours();

  if (hour < 12) return "Good Morning";

  if (hour < 18) return "Good Afternoon";

  return "Good Evening";
});

const today = computed(() =>
  new Date().toLocaleDateString(undefined, {
    weekday: "long",
    month: "long",
    day: "numeric",
    year: "numeric"
  })
);

const activeBookings = computed(() =>
  props.bookingCount
);

const favoriteCount = computed(() =>
  props.favorites.length
);

const unreadNotifications = computed(() =>
  props.notifications.filter(
    notification => !notification.is_read
  ).length
);
</script>