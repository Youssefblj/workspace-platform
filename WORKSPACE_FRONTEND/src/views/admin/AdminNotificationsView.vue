<template>
  <div class="space-y-6">

    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold text-[#23394e]">
          Notifications Management
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Review notifications and send messages to users.
        </p>
      </div>

      <div class="flex items-center gap-2">

<button
  type="button"
  @click="refreshNotifications"
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

        <button
          @click="openSendModal"
          class="inline-flex items-center gap-2 rounded-lg bg-[#f29200] px-4 py-2 text-sm font-medium text-white transition hover:opacity-90"
        >
          <Send class="h-4 w-4" />

          Send Notification
        </button>

      </div>
    </div>

    <!-- Filters -->

    <div
      class="flex flex-col gap-3 rounded-xl border border-gray-200 bg-white p-4 sm:flex-row sm:items-center"
    >

      <div class="relative flex-1">

        <Search
          class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9f9f9f]"
        />

        <input
          v-model="adminStore.notificationSearch"
          type="text"
          placeholder="Search user or message..."
          class="w-full rounded-lg border border-gray-200 py-2 pl-10 pr-4 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
        />

      </div>

      <select
        v-model="adminStore.notificationReadFilter"
        class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
      >

        <option value="">
          All Notifications
        </option>

        <option value="false">
          Unread
        </option>

        <option value="true">
          Read
        </option>

      </select>

      <button
        v-if="
          adminStore.notificationSearch ||
          adminStore.notificationReadFilter !== ''
        "
        @click="resetFilters"
        class="inline-flex items-center gap-2 rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#9f9f9f] transition hover:border-[#f29200] hover:text-[#f29200]"
      >
        <X class="h-4 w-4" />

        Reset
      </button>

    </div>

    <NotificationsTable
      @view="openDetails"
    />

    <NotificationDetailModal
      :show="showDetailModal"
      :notification="selectedNotification"
      @close="closeDetails"
    />

    <SendNotificationModal
      :show="showSendModal"
      @close="closeSendModal"
    />

  </div>
</template>

<script setup>
import {
  ref,
  watch,
  onMounted,
  onBeforeUnmount
} from "vue";

import {
  Search,
  RefreshCw,
  Send,
  X
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

import NotificationsTable from "@/components/admin/notifications/NotificationsTable.vue";
import NotificationDetailModal from "@/components/admin/notifications/NotificationDetailModal.vue";
import SendNotificationModal from "@/components/admin/notifications/SendNotificationModal.vue";
import { toast } from "vue-sonner";
const adminStore = useAdminStore();

const showDetailModal = ref(false);
const showSendModal = ref(false);
const refreshing = ref(false);
const selectedNotification = ref(null);

let searchTimeout = null;

const refreshNotifications = async () => {

  if (refreshing.value) {
    return;
  }

  refreshing.value = true;

  try {

    adminStore.notificationSearch = "";
    adminStore.notificationReadFilter = "";

    clearTimeout(searchTimeout);

    await adminStore.fetchNotifications(1);

    toast.success(
      "Notifications refreshed successfully."
    );

  } catch (error) {

    console.error(
      "Failed to refresh notifications:",
      error
    );

    toast.error(
      "Unable to refresh notifications."
    );

  } finally {

    refreshing.value = false;

  }

};

const resetFilters = () => {
  adminStore.notificationSearch = "";
  adminStore.notificationReadFilter = "";
};

const openDetails = (notification) => {
  selectedNotification.value = notification;
  showDetailModal.value = true;
};

const closeDetails = () => {
  showDetailModal.value = false;
  selectedNotification.value = null;
};

const openSendModal = () => {
  showSendModal.value = true;
};

const closeSendModal = () => {
  showSendModal.value = false;
};

watch(
  () => adminStore.notificationSearch,
  () => {
    clearTimeout(searchTimeout);

    searchTimeout = setTimeout(() => {
      adminStore.fetchNotifications(1);
    }, 400);
  }
);

watch(
  () => adminStore.notificationReadFilter,
  () => {
    adminStore.fetchNotifications(1);
  }
);

onMounted(() => {
  adminStore.fetchNotifications(1);
});

onBeforeUnmount(() => {
  clearTimeout(searchTimeout);
});
</script>