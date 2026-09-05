<template>
  <header
    class="flex min-h-20 items-center justify-between border-b border-gray-200 bg-white px-6"
  >

    <!-- Left -->

    <div class="min-w-0">

      <h1
        class="truncate text-xl font-bold text-[#23394e]"
      >
        {{ pageTitle }}
      </h1>

      <p class="mt-1 text-xs text-[#9f9f9f]">
        Welcome back,
        <span class="font-medium text-[#23394e]">
          {{ auth.user?.username || "Admin" }}
        </span>
      </p>

    </div>

    <!-- Right -->

    <div class="flex items-center gap-3">

      <!-- Notifications -->

      <RouterLink
        to="/admin/notifications"
        class="relative flex h-10 w-10 items-center justify-center rounded-xl border border-gray-200 bg-white text-[#23394e] transition hover:border-[#f29200] hover:bg-[#f29200]/5 hover:text-[#f29200]"
      >
        <Bell class="h-5 w-5" />

        <span
          v-if="unreadCount > 0"
          class="absolute -right-1 -top-1 flex h-5 min-w-5 items-center justify-center rounded-full bg-[#f29200] px-1 text-[10px] font-bold text-white"
        >
          {{ unreadCount > 9 ? "9+" : unreadCount }}
        </span>
      </RouterLink>

      <!-- Profile -->

      <RouterLink
        to="/admin/settings"
        class="flex items-center gap-3 rounded-xl border border-gray-200 bg-white px-2.5 py-2 transition hover:border-[#f29200]"
      >

        <div
  class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-lg bg-[#f29200]/10 text-sm font-bold text-[#f29200]"
>
  <img
    v-if="auth.user?.profile_image"
    :src="auth.user.profile_image"
    alt="Admin profile"
    class="h-full w-full object-cover"
  />

  <span v-else>
    {{ initials }}
  </span>
</div>

        <div class="hidden text-left lg:block">

          <p
            class="max-w-32 truncate text-sm font-semibold text-[#23394e]"
          >
            {{ auth.user?.username || "Admin" }}
          </p>

          <p class="text-xs text-[#9f9f9f]">
            Administrator
          </p>

        </div>

        <ChevronDown
          class="hidden h-4 w-4 text-[#9f9f9f] lg:block"
        />

      </RouterLink>

    </div>

  </header>
</template>

<script setup>
import {
  computed,
  onMounted
} from "vue";

import {
  Bell,
  ChevronDown
} from "lucide-vue-next";

import {
  useRoute
} from "vue-router";

import { useAuthStore } from "@/stores/auth";
import { useAdminStore } from "@/stores/admin";

const route = useRoute();

const auth = useAuthStore();
const adminStore = useAdminStore();

const pageTitles = {
  "/admin": "Dashboard",
  "/admin/users": "Users",
  "/admin/offices": "Offices",
  "/admin/bookings": "Bookings",
  "/admin/payments": "Payments",
  "/admin/contacts": "Messages",
  "/admin/reviews": "Reviews",
  "/admin/notifications": "Notifications",
  "/admin/analytics": "Analytics",
  "/admin/settings": "Settings"
};

const pageTitle = computed(() => {
  return (
    pageTitles[route.path] ||
    route.meta?.title ||
    "Admin Panel"
  );
});

const initials = computed(() => {

  const username =
    auth.user?.username || "Admin";

  return username
    .slice(0, 2)
    .toUpperCase();

});

const unreadCount = computed(() => {

  return adminStore.notifications.filter(
    notification => !notification.is_read
  ).length;

});

onMounted(() => {

  if (
    adminStore.notifications.length === 0
  ) {
    adminStore.fetchNotifications(1);
  }

});
</script>