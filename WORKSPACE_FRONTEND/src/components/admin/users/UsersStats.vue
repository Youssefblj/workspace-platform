<template>
  <div class="grid grid-cols-1 gap-4 md:grid-cols-3">

    <div
      class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
    >
      <div class="flex items-center justify-between">

        <div>
          <p class="text-sm text-[#9f9f9f]">
            Total Users
          </p>

          <h2 class="mt-2 text-2xl font-bold text-[#23394e]">
            {{ totalUsers }}
          </h2>
        </div>

        <div
          class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
        >
          <Users class="h-5 w-5 text-[#f29200]" />
        </div>

      </div>
    </div>

    <div
      class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
    >
      <div class="flex items-center justify-between">

        <div>
          <p class="text-sm text-[#9f9f9f]">
            Active Users
          </p>

          <h2 class="mt-2 text-2xl font-bold text-[#23394e]">
            {{ activeUsers }}
          </h2>
        </div>

        <div
          class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
        >
          <UserCheck class="h-5 w-5 text-[#f29200]" />
        </div>

      </div>
    </div>

    <div
      class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
    >
      <div class="flex items-center justify-between">

        <div>
          <p class="text-sm text-[#9f9f9f]">
            Administrators
          </p>

          <h2 class="mt-2 text-2xl font-bold text-[#23394e]">
            {{ admins }}
          </h2>
        </div>

        <div
          class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
        >
          <ShieldCheck class="h-5 w-5 text-[#f29200]" />
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";
import {
  Users,
  UserCheck,
  ShieldCheck
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const totalUsers = computed(() =>
  adminStore.users.length
);

const activeUsers = computed(() =>
  adminStore.users.filter(
    user => user.is_active
  ).length
);

const admins = computed(() =>
  adminStore.users.filter(
    user => user.is_staff
  ).length
);
</script>