<template>
  <nav class="sticky top-0 z-50 w-full border-b border-gray-100 bg-white/90 backdrop-blur-md transition-all duration-300">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="flex h-16 items-center justify-between">
        
        <!-- Brand Logo -->
        <div class="flex items-center">
          <router-link to="/" class="flex items-center gap-2 font-display text-xl font-bold text-gray-900 group">
            <div class="flex h-9 w-9 items-center justify-center rounded-xl bg-[#F59E0B] text-white transition-all duration-300 group-hover:bg-amber-500 shadow-lg shadow-amber-300/40">
              <Building class="h-5 w-5" />
            </div>
<span
  v-if="websiteName === 'WorkSpace'"
  class="tracking-tight"
>
  Work<span class="text-[#F59E0B]">Space</span>
</span>

<span
  v-else
  class="tracking-tight text-gray-900"
>
  {{ websiteName }}
</span>          </router-link>
        </div>

<div class="hidden md:flex items-center gap-8">

  <!-- Browse -->
<div
  class="relative"
  @mouseenter="showBrowseMenu=true"
  @mouseleave="showBrowseMenu=false"
>

  <button
    class="flex items-center gap-1 text-sm font-semibold text-gray-600 hover:text-[#F59E0B] transition"
  >
    Browse Offices

    <ChevronDown
      class="h-4 w-4 transition"
      :class="{ 'rotate-180': showBrowseMenu }"
    />
  </button>

    <transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0 translate-y-2"
    >

<div
v-if="showBrowseMenu"
class="absolute left-0 mt-5 w-80 rounded-3xl bg-white border border-gray-100 shadow-2xl overflow-hidden"
>

<div class="p-2">

<!-- All -->

<router-link
to="/browse-offices"
class="flex items-center gap-4 rounded-2xl p-4 hover:bg-amber-50 transition"
>

<div class="w-12 h-12 rounded-2xl bg-amber-100 flex items-center justify-center">

<Building class="w-6 h-6 text-[#F59E0B]" />

</div>

<div>

<div class="font-semibold">
All Workspaces
</div>

<div class="text-xs text-gray-500">
Browse every available workspace.
</div>

</div>

</router-link>

<!-- Offices -->

<router-link
to="/browse-offices"
class="flex items-center gap-4 rounded-2xl p-4 hover:bg-amber-50 transition"
>

<div class="w-12 h-12 rounded-2xl bg-amber-100 flex items-center justify-center">

<BriefcaseBusiness class="w-6 h-6 text-[#F59E0B]" />

</div>

<div>

<div class="font-semibold">
Private Offices
</div>

<div class="text-xs text-gray-500">
Dedicated offices for professionals.
</div>

</div>

</router-link>

<!-- Coworking -->

<router-link
to="/coworking-spaces"
class="flex items-center gap-4 rounded-2xl p-4 hover:bg-amber-50 transition"
>

<div class="w-12 h-12 rounded-2xl bg-amber-100 flex items-center justify-center">

<Users class="w-6 h-6 text-[#F59E0B]" />

</div>

<div>

<div class="font-semibold">
Coworking Spaces
</div>

<div class="text-xs text-gray-500">
Flexible desks in collaborative spaces.
</div>

</div>

</router-link>

<!-- Meeting -->

<router-link
to="/meeting-rooms"
class="flex items-center gap-4 rounded-2xl p-4 hover:bg-amber-50 transition"
>

<div class="w-12 h-12 rounded-2xl bg-amber-100 flex items-center justify-center">

<Presentation class="w-6 h-6 text-[#F59E0B]" />

</div>

<div>

<div class="font-semibold">
Meeting Rooms
</div>

<div class="text-xs text-gray-500">
Book rooms by the hour or day.
</div>

</div>

</router-link>

<!-- Virtual -->

<router-link
to="/virtual-offices"
class="flex items-center gap-4 rounded-2xl p-4 hover:bg-amber-50 transition"
>

<div class="w-12 h-12 rounded-2xl bg-amber-100 flex items-center justify-center">

<Globe class="w-6 h-6 text-[#F59E0B]" />

</div>

<div>

<div class="font-semibold">
Virtual Offices
</div>

<div class="text-xs text-gray-500">
Professional business addresses.
</div>

</div>

</router-link>

</div>

</div>

</transition>

</div>

  <template v-if="!authStore.isAuthenticated">
    <router-link
      to="/about"
      class="text-sm font-semibold text-gray-600 hover:text-[#F59E0B]"
    >
      About
    </router-link>

    <router-link
      to="/pricing"
      class="text-sm font-semibold text-gray-600 hover:text-[#F59E0B]"
    >
      Pricing
    </router-link>

    <router-link
      to="/contact"
      class="text-sm font-semibold text-gray-600 hover:text-[#F59E0B]"
    >
      Contact
    </router-link>
  </template>

<template v-else-if="!authStore.isAdmin">
    <router-link
      to="/favorites"
      class="text-sm font-semibold text-gray-600 hover:text-[#F59E0B]"
    >
      Favorites
    </router-link>

    <router-link
      to="/dashboard"
      class="text-sm font-semibold text-gray-600 hover:text-[#F59E0B]"
    >
      Dashboard
    </router-link>

  </template>

</div>

        <!-- User Controls / Auth (Desktop) -->
        <div class="hidden md:flex items-center gap-4">
          <template v-if="authStore.isAuthenticated">
            <!-- Notifications Bell -->
            <div class="relative">
              <button 
                @click="toggleNotifications" 
                class="relative rounded-xl p-2 text-gray-500 hover:bg-gray-50 hover:text-gray-900 transition-all duration-200"
              >
                <Bell class="h-5.5 w-5.5" />
                <span 
                  v-if="unreadCount > 0" 
                  class="absolute top-1.5 right-1.5 flex h-4 w-4 items-center justify-center rounded-full bg-red-500 text-[10px] font-bold text-white ring-2 ring-white animate-pulse"
                >
                  {{ unreadCount }}
                </span>
              </button>

              <!-- Notifications Dropdown -->
              <div 
                v-if="showNotifications" 
                class="absolute right-0 mt-3 w-80 rounded-2xl border border-gray-100 bg-white p-2 shadow-xl ring-1 ring-black/5 animate-in fade-in slide-in-from-top-2 duration-200"
              >
                <div class="flex items-center justify-between border-b border-gray-50 px-3 py-2">
                  <h3 class="font-display font-semibold text-gray-900 text-sm">Notifications</h3>
                  <button 
                    v-if="unreadCount > 0" 
                    @click="notificationStore.markAllAsRead()"
                    class="text-xs font-medium text-[#F59E0B] hover:text-amber-500 transition-colors duration-200"
                  >
                    Mark all read
                  </button>
                </div>
                <div class="max-h-60 overflow-y-auto py-1">
                  <div v-if="notifications.length === 0" class="py-6 text-center text-xs text-gray-400">
                    No new notifications
                  </div>
                  <div 
                    v-for="notification in notifications" 
                    :key="notification.id" 
                    :class="['px-3 py-2.5 rounded-xl text-xs hover:bg-amber-50 transition-colors duration-200 flex flex-col gap-0.5 border-b border-gray-50/50', !notification.is_read ? 'bg-amber-50' : '']"
                    @click="notificationStore.markAsRead(notification)"
                  >
                    <div class="flex justify-between items-start">
                      <span :class="['font-semibold', !notification.is_read ? 'text-gray-900' : 'text-gray-600']">{{ notification.title }}</span>
                      <span class="text-[10px] text-gray-400">{{ formatDate(notification.created_at) }}</span>
                    </div>
                    <p class="text-gray-500 line-clamp-2 mt-0.5">{{ notification.message }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Profile Menu Dropdown -->
            <div class="relative">
              <button 
                @click="toggleProfile" 
                class="flex items-center gap-2 rounded-xl p-1 pr-3 hover:bg-gray-50 transition-all duration-200"
              >
                <div class="flex h-8 w-8 items-center justify-center overflow-hidden rounded-full bg-amber-100 text-[#F59E0B] font-display font-semibold text-sm">
                  <img
                    v-if="authStore.user?.profile_image"
                    :src="authStore.user.profile_image"
                    alt="Profile"
                    class="h-full w-full object-cover"
                  />

                  <span v-else>
                    {{ userInitials }}
                  </span>
                </div>
                <div class="text-left">
                  <div class="text-xs font-semibold text-gray-900 line-clamp-1 leading-none">{{ authStore.user?.username }}</div>
                  <div class="text-[10px] text-gray-400 leading-none mt-0.5">{{ authStore.user?.email }}</div>
                </div>
                <ChevronDown class="h-4 w-4 text-gray-400 transition-transform duration-200" :class="{'rotate-180': showProfileMenu}" />
              </button>

              <div 
                v-if="showProfileMenu" 
                class="absolute right-0 mt-3 w-48 rounded-2xl border border-gray-100 bg-white p-1.5 shadow-xl ring-1 ring-black/5 animate-in fade-in slide-in-from-top-2 duration-200"
              >
                <router-link
                v-if="!authStore.isAdmin"
  :to="{ path: '/dashboard', query: { tab: 'profile' } }"
  class="flex items-center gap-2 rounded-xl px-3 py-2 text-sm text-gray-700 hover:bg-gray-50"
  @click="showProfileMenu=false"
>
  <User class="h-4 w-4"/>
  My Account
</router-link>





<router-link
  v-if="!authStore.isAdmin"
  :to="{ path: '/dashboard', query: { tab: 'settings' } }"
  class="flex items-center gap-2 rounded-xl px-3 py-2 text-sm text-gray-700 hover:bg-gray-50"
  @click="showProfileMenu=false"
>
  <Settings class="h-4 w-4"/>
  Settings
</router-link>



<hr class="my-2">

<button
  @click="handleLogout"
  class="flex w-full items-center gap-2 rounded-xl px-3 py-2 text-left text-sm text-red-600 hover:bg-red-50"
>
  <LogOut class="h-4 w-4"/>
  Logout
</button>
              </div>
            </div>
          </template>

          <template v-else>
            <router-link to="/login" class="text-sm font-semibold text-gray-700 hover:text-[#F59E0B] transition-colors duration-200">
              Sign In
            </router-link>
            <router-link to="/register" class="rounded-xl bg-[#F59E0B] px-4 py-2 text-sm font-semibold text-white transition-all duration-300 hover:bg-amber-500 shadow-md shadow-amber-300/40">
              Get Started
            </router-link>
          </template>
        </div>

        <!-- Burger Icon (Mobile) -->
        <div class="flex items-center md:hidden">
          <button 
            @click="toggleMobileMenu" 
            class="rounded-xl p-2 text-gray-500 hover:bg-gray-50 hover:text-gray-900 transition-colors duration-200"
          >
            <Menu v-if="!showMobileMenu" class="h-6 w-6" />
            <X v-else class="h-6 w-6" />
          </button>
        </div>

      </div>
    </div>

<!-- Mobile Navigation Menu -->
<div
  v-if="showMobileMenu"
  class="md:hidden border-t border-gray-100 bg-white px-4 py-4 space-y-2 animate-in slide-in-from-top duration-300"
>
  <!-- Browse Offices -->
 <!-- Browse Offices -->

<div class="rounded-xl border border-gray-100 overflow-hidden">

  <button
    @click="showBrowseMobile = !showBrowseMobile"
    class="flex w-full items-center justify-between px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50"
  >
    <span>Browse Offices</span>

    <ChevronDown
      class="h-5 w-5 transition"
      :class="{ 'rotate-180': showBrowseMobile }"
    />
  </button>

  <transition
    enter-active-class="transition-all duration-300"
    enter-from-class="max-h-0 opacity-0"
    enter-to-class="max-h-96 opacity-100"
    leave-active-class="transition-all duration-300"
    leave-from-class="max-h-96 opacity-100"
    leave-to-class="max-h-0 opacity-0"
  >

    <div
      v-if="showBrowseMobile"
      class="border-t border-gray-100 bg-gray-50"
    >

      <router-link
        to="/browse-offices"
        class="flex items-center gap-3 px-5 py-3 hover:bg-white"
        @click="showMobileMenu=false"
      >
        <Building class="w-5 h-5 text-[#F59E0B]" />
        All Workspaces
      </router-link>

      <router-link
        to="/browse-offices"
        class="flex items-center gap-3 px-5 py-3 hover:bg-white"
        @click="showMobileMenu=false"
      >
        <BriefcaseBusiness class="w-5 h-5 text-[#F59E0B]" />
        Private Offices
      </router-link>

      <router-link
        to="/coworking-spaces"
        class="flex items-center gap-3 px-5 py-3 hover:bg-white"
        @click="showMobileMenu=false"
      >
        <Users class="w-5 h-5 text-[#F59E0B]" />
        Coworking Spaces
      </router-link>

      <router-link
        to="/meeting-rooms"
        class="flex items-center gap-3 px-5 py-3 hover:bg-white"
        @click="showMobileMenu=false"
      >
        <Presentation class="w-5 h-5 text-[#F59E0B]" />
        Meeting Rooms
      </router-link>

      <router-link
        to="/virtual-offices"
        class="flex items-center gap-3 px-5 py-3 hover:bg-white"
        @click="showMobileMenu=false"
      >
        <Globe class="w-5 h-5 text-[#F59E0B]" />
        Virtual Offices
      </router-link>

    </div>

  </transition>

</div>

  <template v-if="authStore.isAuthenticated && !authStore.isAdmin">

    <router-link
      to="/favorites"
      class="block rounded-xl px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50 hover:text-[#F59E0B]"
      @click="showMobileMenu = false"
    >
      Favorites
    </router-link>

    <router-link
      to="/dashboard"
      class="block rounded-xl px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50 hover:text-[#F59E0B]"
      @click="showMobileMenu = false"
    >
      Dashboard
    </router-link>

    <router-link
      :to="{ path: '/dashboard', query: { tab: 'profile' } }"
      class="block rounded-xl px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50 hover:text-[#F59E0B]"
      @click="showMobileMenu = false"
    >
      My Account

    </router-link>

    <router-link
      :to="{ path: '/dashboard', query: { tab: 'settings' } }"
      class="block rounded-xl px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50 hover:text-[#F59E0B]"
      @click="showMobileMenu = false"
    >
      Settings
    </router-link>

    <router-link
      v-if="authStore.isAdmin"
      to="/admin"
      class="block rounded-xl px-3 py-3 font-semibold text-[#F59E0B] hover:bg-amber-50"
      @click="showMobileMenu = false"
    >
      Admin Panel
    </router-link>

    <hr class="my-2 border-gray-100">

    <button
      @click="handleLogout"
      class="flex w-full items-center gap-2 rounded-xl px-3 py-3 font-semibold text-red-600 hover:bg-red-50"
    >
      <LogOut class="h-5 w-5"/>
      Logout
    </button>

  </template>

  <template v-else>

    <router-link
      to="/about"
      class="block rounded-xl px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50 hover:text-[#F59E0B]"
      @click="showMobileMenu = false"
    >
      About
    </router-link>

    <router-link
      to="/pricing"
      class="block rounded-xl px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50 hover:text-[#F59E0B]"
      @click="showMobileMenu = false"
    >
      Pricing
    </router-link>

    <router-link
      to="/contact"
      class="block rounded-xl px-3 py-3 font-semibold text-gray-700 hover:bg-amber-50 hover:text-[#F59E0B]"
      @click="showMobileMenu = false"
    >
      Contact
    </router-link>

    <hr class="my-2 border-gray-100">

    <router-link
      to="/login"
      class="block rounded-xl px-3 py-3 text-center font-semibold text-gray-700 hover:bg-gray-50"
      @click="showMobileMenu = false"
    >
      Sign In
    </router-link>

    <router-link
      to="/register"
      class="block rounded-xl bg-[#F59E0B] px-3 py-3 text-center font-semibold text-white hover:bg-amber-500 transition"
      @click="showMobileMenu = false"
    >
      Get Started
    </router-link>

  </template>

</div>
  </nav>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted,watch } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { useNotificationStore } from "@/stores/notification";
import api from "@/services/api";
import { useSiteSettingsStore } from "@/stores/siteSettings";
import {
  Building,
  Bell,
  User,
  LogOut,
  LayoutDashboard,
  Menu,
  X,
  ChevronDown,
  BellOff,
  Settings,
  Heart,
  BriefcaseBusiness,
  Shield,
  Users,
  Presentation,
  Globe
} from "lucide-vue-next";

const router = useRouter();
const authStore = useAuthStore();
const notificationStore = useNotificationStore();
const siteSettingsStore = useSiteSettingsStore();
const showProfileMenu = ref(false);
const showNotifications = ref(false);
const showMobileMenu = ref(false);
const showBrowseMenu = ref(false);
const showBrowseMobile = ref(false);

let pollInterval = null;
const stopNotificationPolling = () => {

  if (pollInterval) {
    clearInterval(pollInterval);
    pollInterval = null;
  }

};

const startNotificationPolling = async () => {

  stopNotificationPolling();

  if (!authStore.isAuthenticated) {
    return;
  }

  await notificationStore.fetchNotifications();

  pollInterval = setInterval(() => {

    if (authStore.isAuthenticated) {
      notificationStore.fetchNotifications();
    }

  }, 30000);

};



const userInitials = computed(() => {
  if (!authStore.user?.username) return "U";
  return authStore.user.username.slice(0, 2).toUpperCase();
});

const refreshNavbarUser = async () => {
  try {
    const { data } = await api.get("profile/");

    authStore.user = {
      ...authStore.user,
      ...data
    };

    localStorage.setItem(
      "user",
      JSON.stringify(authStore.user)
    );
  } catch (error) {
    console.error(
      "Failed to refresh navbar user:",
      error
    );
  }
};

const notifications = computed(() => notificationStore.notifications);

const unreadCount = computed(() => notificationStore.unreadCount);

const toggleProfile = () => {

  showProfileMenu.value = !showProfileMenu.value;

  showNotifications.value = false;

};

const toggleNotifications = async () => {

  if (!authStore.isAuthenticated) {
    return;
  }

  showNotifications.value =
    !showNotifications.value;

  showProfileMenu.value = false;

  if (showNotifications.value) {
    await notificationStore.fetchNotifications();
  }

};

const toggleMobileMenu = () => {

  showMobileMenu.value = !showMobileMenu.value;

};

const handleLogout = () => {

  stopNotificationPolling();

  showProfileMenu.value = false;
  showNotifications.value = false;
  showMobileMenu.value = false;

  authStore.logout();

  router.push({
    name: "login"
  });

};

const formatDate = (dateStr) => {

  if (!dateStr) return "";

  const date = new Date(dateStr);

  return date.toLocaleDateString(undefined, {
    month: "short",
    day: "numeric"
  });

};

const closeMenus = (e) => {

  if (!e.target.closest(".relative")) {

    showProfileMenu.value = false;

    showNotifications.value = false;

  }

};

const websiteName = computed(() =>
  siteSettingsStore.settings.website_name || "WorkSpace"
);

onMounted(() => {

  siteSettingsStore.fetchSettings().catch(() => {});


  document.addEventListener(
    "click",
    closeMenus
  );

  window.addEventListener(
    "user-profile-updated",
    refreshNavbarUser
  );

  startNotificationPolling();

});

onUnmounted(() => {

  
  document.removeEventListener(
    "click",
    closeMenus
  );

  window.removeEventListener(
    "user-profile-updated",
    refreshNavbarUser
  );

  stopNotificationPolling();

});


watch(
  () => authStore.isAuthenticated,

  (isAuthenticated) => {

    if (isAuthenticated) {

      startNotificationPolling();

    } else {

      stopNotificationPolling();

      showNotifications.value = false;

    }

  }
);
</script>









<style scoped>
.notifications-scroll::-webkit-scrollbar {
  width: 6px;
}

.notifications-scroll::-webkit-scrollbar-track {
  background: transparent;
}

.notifications-scroll::-webkit-scrollbar-thumb {
  background: #FCD34D;
  border-radius: 999px;
}

.notifications-scroll::-webkit-scrollbar-thumb:hover {
  background: #F59E0B;
}

.notifications-scroll {
  scrollbar-width: thin;
  scrollbar-color: #FCD34D transparent;
}

</style>
