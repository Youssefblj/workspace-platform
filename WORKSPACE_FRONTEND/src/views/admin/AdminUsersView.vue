<template>
  <div class="space-y-6">

    <UsersStats />

    <UsersToolbar />

    <UsersTable />
    

  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useAdminStore } from "@/stores/admin";

import UsersStats from "@/components/admin/users/UsersStats.vue";
import UsersToolbar from "@/components/admin/users/UsersToolbar.vue";
import UsersTable from "@/components/admin/users/UsersTable.vue";

const adminStore = useAdminStore();

onMounted(() => {
  adminStore.fetchUsers();
});
</script>