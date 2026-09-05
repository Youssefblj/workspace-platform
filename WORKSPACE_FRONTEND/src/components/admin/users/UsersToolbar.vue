<template>
  <div
    class="flex flex-col gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm md:flex-row md:items-center md:justify-between"
  >
    <div>
      <h2 class="text-lg font-bold text-[#23394e]">
        Users
      </h2>

      <p class="text-sm text-[#9f9f9f]">
        {{ adminStore.totalUsers }} users available
      </p>
    </div>

    <div
      class="flex flex-col gap-3 sm:flex-row sm:items-center"
    >
      <div class="relative">
        <Search
          class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9f9f9f]"
        />

        <input
          v-model="search"
          type="text"
          placeholder="Search user..."
          class="w-64 rounded-lg border border-gray-200 py-2 pl-10 pr-4 text-sm text-[#23394e] outline-none transition focus:border-[#f29200]"
        />
      </div>

      <button
        type="button"
        @click="refreshUsers"
        :disabled="refreshing"
        class="flex items-center gap-2 rounded-lg border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
      >
        <RefreshCw
          class="h-4 w-4"
          :class="{
            'animate-spin': refreshing
          }"
        />

        Refresh
      </button>
    </div>
  </div>
</template>

<script setup>
import {
  computed,
  ref
} from "vue";

import {
  Search,
  RefreshCw
} from "lucide-vue-next";
import { toast } from "vue-sonner";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const refreshing = ref(false);

const search = computed({
  get() {
    return adminStore.userSearch || "";
  },

  set(value) {
    adminStore.userSearch = value;
  }
});

const refreshUsers = async () => {

  if (refreshing.value) {
    return;
  }

  refreshing.value = true;

  try {

    adminStore.userSearch = "";

    await adminStore.fetchUsers(1);

    toast.success(
      "Users refreshed successfully."
    );

  } catch (error) {

    console.error(
      "Failed to refresh users:",
      error
    );

    toast.error(
      "Unable to refresh users."
    );

  } finally {

    refreshing.value = false;

  }

};
</script>