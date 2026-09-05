<template>
  <div class="flex min-h-screen flex-col bg-gray-50/50">

    <Navbar
      v-if="
        !isAdminRoute &&
        !isAdmin &&
        !route.meta.hideNavbar
      "
    />

    <main class="grow">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <Footer
      v-if="
        !isAdminRoute &&
        !isAdmin &&
        !route.meta.hideFooter
      "
    />

    <Toaster
      richColors
      position="top-right"
      closeButton
    />

  </div>
</template>


<script setup>
import {
  computed
} from "vue"

import {
  useRoute
} from "vue-router"

import {
  useAuthStore
} from "@/stores/auth"

import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"

import {
  Toaster
} from "vue-sonner"

import "vue-sonner/style.css"


const route = useRoute()

const authStore = useAuthStore()


const isAdminRoute = computed(() =>
  route.path.startsWith("/admin")
)


const isAdmin = computed(() =>
  authStore.isAuthenticated &&
  authStore.isAdmin
)
</script>


<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>