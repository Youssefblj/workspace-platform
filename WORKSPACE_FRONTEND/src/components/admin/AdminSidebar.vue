<template>
  <aside
    class="group flex h-screen w-72 flex-col border-r border-gray-200 bg-white transition-all duration-300"
  >
    <!-- Logo -->

    <div
      class="flex h-20 items-center gap-3 border-b border-gray-100 px-6"
    >
      <div
        class="flex h-12 w-12 items-center justify-center rounded-2xl bg-[#F59E0B] shadow-lg shadow-amber-300/40"
      >
        <ShieldCheck class="h-6 w-6 text-white" />
      </div>

      <div>
        <h2
          class="font-display text-lg font-black tracking-tight text-gray-900"
        >
          Workspace
        </h2>

        <p
          class="text-xs font-medium text-gray-400"
        >
          Admin Panel
        </p>
      </div>
    </div>

    <!-- Menu -->

    <div class="flex-1 overflow-y-auto px-4 py-6">

      <p
        class="mb-3 px-3 text-[11px] font-bold uppercase tracking-[0.2em] text-gray-400"
      >
        Management
      </p>

      <nav class="space-y-2">

        <RouterLink
          v-for="item in menu"
          :key="item.name"
          :to="item.to"
          class="group flex items-center gap-3 rounded-2xl px-4 py-3 text-sm font-semibold transition-all duration-300"
          :class="isActive(item.to)
            ? 'bg-amber-50 text-[#F59E0B] shadow-sm'
            : 'text-gray-600 hover:bg-gray-50 hover:text-[#F59E0B]'"
        >

          <component
            :is="item.icon"
            class="h-5 w-5 transition duration-300 group-hover:scale-110"
          />

          {{ item.name }}

        </RouterLink>

      </nav>

    </div>

    <!-- Bottom -->

    <div
      class="border-t border-gray-100 p-4"
    >

      <button
        @click="logout"
        class="flex w-full items-center gap-3 rounded-2xl px-4 py-3 text-sm font-semibold text-red-500 transition hover:bg-red-50"
      >

        <LogOut class="h-5 w-5"/>

        Logout

      </button>

    </div>

  </aside>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router"

import { useAuthStore } from "@/stores/auth"

import {

LayoutDashboard,

Users,

Building2,

CalendarDays,
CreditCard,

BarChart3,

Settings,

LogOut,
MessageSquare,

ShieldCheck,
Star ,
Bell ,
Globe2



} from "lucide-vue-next"

const router = useRouter()

const route = useRoute()

const auth = useAuthStore()

const menu = [

{
name:"Dashboard",
to:"/admin",
icon:LayoutDashboard
},

{
name:"Users",
to:"/admin/users",
icon:Users
},

{
name:"Offices",
to:"/admin/offices",
icon:Building2
},

{
name:"Bookings",
to:"/admin/bookings",
icon:CalendarDays
},
{
  name: "Payments",
  to: "/admin/payments",
  icon: CreditCard
},
{
  name: "Messages",
  to: "/admin/contacts",
  icon: MessageSquare
},
{
  name: "Reviews",
  to: "/admin/reviews",
  icon: Star
},
{
  name: "Notifications",
  to: "/admin/notifications",
  icon: Bell
},

{
name:"Analytics",
to:"/admin/analytics",
icon:BarChart3
},
{
  name: "Website Settings",
  to: "/admin/site-settings",
  icon: Globe2,
},

{
name:"Settings",
to:"/admin/settings",
icon:Settings
}

]

const isActive = (path)=>{

if(path==="/admin"){

return route.path==="/admin"

}

return route.path.startsWith(path)

}

const logout=()=>{

auth.logout()

router.replace("/login")

}
</script>