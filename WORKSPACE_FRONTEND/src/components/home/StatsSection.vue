<template>
  <section class="relative overflow-hidden bg-[#23394e] py-24">
    <!-- Background pattern -->
    <div
      class="absolute inset-0 opacity-[0.07]"
      style="
        background-image: radial-gradient(circle, #ffffff 1px, transparent 1px);
        background-size: 34px 34px;
      "
    ></div>

    <div
      class="absolute -left-32 -top-32 h-80 w-80 rounded-full bg-[#f29200]/15 blur-3xl"
    ></div>

    <div
      class="absolute -bottom-32 -right-32 h-80 w-80 rounded-full bg-[#f29200]/10 blur-3xl"
    ></div>

    <div class="relative mx-auto max-w-7xl px-6">
      <!-- Header -->
      <div class="mx-auto mb-14 max-w-3xl text-center">
        <div
          class="mb-5 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm font-semibold text-[#f29200]"
        >
          <LayoutDashboard class="h-4 w-4" />
          Platform Overview
        </div>

        <h2
          class="text-4xl font-extrabold leading-tight text-white md:text-5xl"
        >
          A simpler way to
          <span class="text-[#f29200]">
            manage workspace bookings
          </span>
        </h2>

        <p class="mt-6 text-lg leading-8 text-gray-300">
          WorkSpace brings workspace discovery, availability, pricing and
          booking management together in one clear platform.
        </p>
      </div>

      <!-- Features -->
      <div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <article
          v-for="item in features"
          :key="item.title"
          class="group relative overflow-hidden rounded-2xl border border-white/10 bg-white/5 p-6 transition duration-300 hover:-translate-y-1 hover:border-[#f29200]/50 hover:bg-white/10"
        >
          <!-- Top accent -->
          <div
            class="absolute inset-x-0 top-0 h-[2px] origin-left scale-x-0 bg-[#f29200] transition-transform duration-300 group-hover:scale-x-100"
          ></div>

          <!-- Icon -->
          <div
            class="mb-6 flex h-12 w-12 items-center justify-center rounded-xl bg-[#f29200]/10 transition duration-300 group-hover:bg-[#f29200]"
          >
            <component
              :is="item.icon"
              class="h-6 w-6 text-[#f29200] transition duration-300 group-hover:text-white"
            />
          </div>

          <h3 class="text-lg font-bold text-white">
            {{ item.title }}
          </h3>

          <p class="mt-3 text-sm leading-6 text-gray-400">
            {{ item.description }}
          </p>

          <div
            class="mt-5 flex items-center gap-2 text-xs font-semibold uppercase tracking-wide text-gray-300"
          >
            <CheckCircle class="h-4 w-4 shrink-0 text-[#f29200]" />

            <span>
              {{ item.meta }}
            </span>
          </div>
        </article>
      </div>

      <!-- Bottom information -->
      <div
        class="mt-10 flex flex-col gap-6 rounded-2xl border border-white/10 bg-white/5 p-6 md:flex-row md:items-center md:justify-between"
      >
        <div>
          <p class="text-sm font-semibold text-[#f29200]">
            Designed for flexible work
          </p>

          <h3 class="mt-1 text-xl font-bold text-white">
            One platform for users and administrators
          </h3>

          <p class="mt-2 max-w-2xl text-sm leading-6 text-gray-400">
            Users can discover workspaces and manage reservations, while
            administrators can manage offices, users, bookings and
            availability from a dedicated dashboard.
          </p>
        </div>

        <RouterLink
          to="/browse-offices"
          class="inline-flex shrink-0 items-center justify-center gap-2 rounded-xl bg-[#f29200] px-5 py-3 text-sm font-semibold text-white transition duration-200 hover:opacity-90"
        >
          Explore Workspaces
          <ArrowRight class="h-4 w-4" />
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import {
  LayoutDashboard,
  Building2,
  CalendarCheck,
  CreditCard,
  Settings,
  CheckCircle,
  ArrowRight,
} from "lucide-vue-next";

const features = [
  {
    icon: Building2,
    title: "Multiple Workspace Types",
    description:
      "Explore offices, coworking spaces, meeting rooms and virtual office options in one place.",
    meta: "Flexible choices",
  },
  {
    icon: CalendarCheck,
    title: "Availability & Booking",
    description:
      "Check available dates, choose your booking period and avoid already reserved dates.",
    meta: "Date-based booking",
  },
  {
    icon: CreditCard,
    title: "Clear Pricing",
    description:
      "View workspace pricing and rental type before confirming your reservation.",
    meta: "Daily · Weekly · Monthly",
  },
  {
    icon: Settings,
    title: "Booking Management",
    description:
      "Users manage reservations while administrators control bookings and workspace availability.",
    meta: "User & admin tools",
  },
];
</script>