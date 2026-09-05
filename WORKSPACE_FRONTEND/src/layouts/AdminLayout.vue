<template>
  <div class="flex h-screen bg-gray-100">

    <!-- Sidebar -->
    <AdminSidebar />

    <!-- Main Area -->
    <div class="flex flex-1 flex-col overflow-hidden">

      <!-- Top Navbar -->
      <AdminNavbar />

      <!-- Page Content -->
      <main class="flex-1 overflow-y-auto p-6">
        <router-view />
      </main>

    </div>

  </div>
</template>

<script setup>
import AdminNavbar from "@/components/admin/AdminNavbar.vue";
import AdminSidebar from "@/components/admin/AdminSidebar.vue";
</script>