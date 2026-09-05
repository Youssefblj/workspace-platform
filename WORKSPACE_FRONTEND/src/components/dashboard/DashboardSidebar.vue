<template>
  <aside
    class="sticky top-24 h-fit rounded-3xl border border-gray-100 bg-white p-4 shadow-sm"
  >
    <div class="mb-6 px-2">
      <h2 class="text-lg font-bold text-gray-900">
        Dashboard
      </h2>

      <p class="mt-1 text-sm text-gray-500">
        Manage your workspace account
      </p>
    </div>

    <nav class="space-y-2">

      <router-link
        v-for="item in items"
        :key="item.name"
        :to="item.to"
        class="group flex items-center gap-3 rounded-2xl px-4 py-3 transition-all duration-300"
        :class="[
          activeTab === item.tab
            ? 'bg-amber-500 text-white shadow-lg shadow-amber-300/40'
            : 'text-gray-600 hover:bg-amber-50 hover:text-amber-500'
        ]"
      >

        <component
          :is="item.icon"
          class="h-5 w-5"
        />

        <span class="font-semibold">
          {{ item.name }}
        </span>

      </router-link>

    </nav>
  </aside>
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";

import {
LayoutDashboard,
CalendarDays,
Heart,
CreditCard,
Bell,
User,
Settings
} from "lucide-vue-next";

const route = useRoute();

const activeTab = computed(() => route.query.tab || "overview");

const items = [

{
  name:"Overview",
  tab:"overview",
  to:{ path:"/dashboard", query:{ tab:"overview" } },
  icon:LayoutDashboard
},

{
  name:"Reservations",
  tab:"reservations",
  to:{ path:"/dashboard", query:{ tab:"reservations" } },
  icon:CalendarDays
},



{
  name:"Billing",
  tab:"billing",
  to:{ path:"/dashboard", query:{ tab:"billing" } },
  icon:CreditCard
},

{
  name:"Notifications",
  tab:"notifications",
  to:{ path:"/dashboard", query:{ tab:"notifications" } },
  icon:Bell
},

{
  name:"Profile",
  tab:"profile",
  to:{ path:"/dashboard", query:{ tab:"profile" } },
  icon:User
},

{
  name:"Settings",
  tab:"settings",
  to:{ path:"/dashboard", query:{ tab:"settings" } },
  icon:Settings
}

];
</script>