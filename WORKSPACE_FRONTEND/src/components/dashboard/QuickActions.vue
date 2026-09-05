<template>
  <section>

    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="text-2xl font-bold text-[#23394e]">
          Quick Actions
        </h2>

        <p class="mt-1 text-[#9f9f9f]">
          Access your most used features.
        </p>
      </div>
    </div>


    <div class="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">

      <router-link
        v-for="action in actions"
        :key="action.title"
        :to="action.to"
        class="group relative overflow-hidden rounded-2xl border border-gray-100 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg"
      >

        <!-- Soft hover background -->
        <div
          class="absolute -right-12 -top-12 h-32 w-32 rounded-full opacity-0 blur-3xl transition duration-500 group-hover:opacity-60"
          :class="action.glow"
        ></div>


        <div class="relative">

          <!-- Icon -->
          <div
            class="flex h-14 w-14 items-center justify-center rounded-xl transition-all duration-300 group-hover:scale-105"
            :class="action.iconBox"
          >
            <component
              :is="action.icon"
              class="h-7 w-7"
              :class="action.iconColor"
            />
          </div>


          <!-- Title -->
          <h3
            class="mt-5 text-lg font-bold text-[#23394e]"
          >
            {{ action.title }}
          </h3>


          <!-- Description -->
          <p
            class="mt-2 min-h-[72px] text-sm leading-6 text-[#6b7280]"
          >
            {{ action.description }}
          </p>


          <!-- Action -->
          <div
            class="mt-5 flex items-center gap-2 text-sm font-semibold transition"
            :class="action.actionColor"
          >
            {{ action.label }}

            <ArrowRight
              class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
            />
          </div>

        </div>

      </router-link>

    </div>

  </section>
</template>


<script setup>
import {
  Search,
  Heart,
  CreditCard,
  Settings,
  ArrowRight
} from "lucide-vue-next"


const actions = [

  {
    title: "Browse Offices",
    description:
      "Discover premium workspaces available across Morocco.",
    label: "Explore Offices",
    to: "/browse-offices",
    icon: Search,

    iconBox:
      "bg-[#f29200]/10",

    iconColor:
      "text-[#f29200]",

    actionColor:
      "text-[#f29200]",

    glow:
      "bg-[#f29200]/20"
  },


  {
    title: "Favorites",
    description:
      "Manage all your saved workspaces in one place.",
    label: "View Favorites",
    to: "/favorites",
    icon: Heart,

    iconBox:
      "bg-rose-50",

    iconColor:
      "text-rose-500",

    actionColor:
      "text-rose-500",

    glow:
      "bg-rose-100"
  },


  {
    title: "Billing",
    description:
      "View invoices, payments and booking history.",
    label: "View Billing",
    to: "/dashboard?tab=billing",
    icon: CreditCard,

    iconBox:
      "bg-emerald-50",

    iconColor:
      "text-emerald-600",

    actionColor:
      "text-emerald-600",

    glow:
      "bg-emerald-100"
  },


  {
    title: "Settings",
    description:
      "Update your profile and account preferences.",
    label: "Manage Settings",
    to: "/dashboard?tab=settings",
    icon: Settings,

    iconBox:
      "bg-[#23394e]/10",

    iconColor:
      "text-[#23394e]",

    actionColor:
      "text-[#23394e]",

    glow:
      "bg-[#23394e]/15"
  }

]
</script>