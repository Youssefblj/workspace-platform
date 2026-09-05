<template>
  <section class="relative overflow-hidden bg-white py-24">
    <!-- Background decoration -->
    <div
      class="absolute -top-20 -left-20 h-72 w-72 rounded-full bg-[#F9A825]/5 blur-3xl"
    ></div>

    <div
      class="absolute -bottom-20 -right-20 h-72 w-72 rounded-full bg-[#F9A825]/10 blur-3xl"
    ></div>

    <div class="relative mx-auto max-w-7xl px-6">
      <!-- Header -->
      <div class="mx-auto mb-16 max-w-3xl text-center">
        <div
          class="mb-5 inline-flex items-center gap-2 rounded-full bg-[#F9A825]/10 px-4 py-2 font-semibold text-[#F9A825]"
        >
          <ShieldCheck class="h-5 w-5" />
          Built for modern work
        </div>

        <h2
          class="text-4xl font-extrabold leading-tight text-[#1F2937] md:text-5xl"
        >
          Everything you need to find
          <span class="text-[#F9A825]">the right workspace</span>
        </h2>

        <p class="mt-6 text-lg leading-8 text-[#6B7280]">
          Discover flexible offices, compare options and book a workspace
          that fits your schedule, location and budget.
        </p>
      </div>

      <!-- Highlights -->
      <div class="mb-20 grid grid-cols-2 gap-5 lg:grid-cols-4">
        <div
          v-for="item in highlights"
          :key="item.title"
          class="group rounded-2xl border border-[#E5E7EB] bg-[#F7F8FA] p-6 text-center transition duration-300 hover:-translate-y-1 hover:border-[#F9A825] hover:bg-white hover:shadow-lg"
        >
          <div
            class="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-[#F9A825]/10 transition duration-300 group-hover:bg-[#F9A825]"
          >
            <component
              :is="item.icon"
              class="h-6 w-6 text-[#F9A825] transition duration-300 group-hover:text-white"
            />
          </div>

          <p class="text-lg font-bold text-[#1F2937]">
            {{ item.title }}
          </p>

          <p class="mt-2 text-sm leading-6 text-[#6B7280]">
            {{ item.label }}
          </p>
        </div>
      </div>

      <!-- Main feature cards -->
      <div class="grid gap-8 md:grid-cols-3">
        <div
          v-for="item in trustItems"
          :key="item.title"
          class="group rounded-3xl border border-[#E5E7EB] bg-white p-8 transition duration-300 hover:-translate-y-2 hover:shadow-xl"
        >
          <div
            class="mb-6 flex h-16 w-16 items-center justify-center rounded-2xl bg-[#F9A825]/10 transition duration-300 group-hover:bg-[#F9A825]"
          >
            <component
              :is="item.icon"
              class="h-8 w-8 text-[#F9A825] transition duration-300 group-hover:text-white"
            />
          </div>

          <h3 class="mb-3 text-2xl font-bold text-[#1F2937]">
            {{ item.title }}
          </h3>

          <p class="leading-8 text-[#6B7280]">
            {{ item.description }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import {
  ShieldCheck,
  Building2,
  CalendarCheck,
  BadgeCheck,
  WalletCards,
  Users,
  MapPin,
} from "lucide-vue-next";

const highlights = [
  {
    icon: Building2,
    title: "Flexible Spaces",
    label: "Offices, coworking spaces and meeting rooms.",
  },
  {
    icon: CalendarCheck,
    title: "Easy Booking",
    label: "Choose your workspace and booking dates in a few steps.",
  },
  {
    icon: MapPin,
    title: "Multiple Locations",
    label: "Explore available workspaces across different Moroccan cities.",
  },
  {
    icon: WalletCards,
    title: "Clear Pricing",
    label: "See pricing details before confirming your reservation.",
  },
];

const trustItems = [
  {
    icon: BadgeCheck,
    title: "Clear Listings",
    description:
      "Compare workspace information, amenities, location and pricing in one place before making your choice.",
  },
  {
    icon: Building2,
    title: "Flexible Rental Options",
    description:
      "Choose daily, weekly or monthly rental options depending on your schedule and workspace needs.",
  },
  {
    icon: Users,
    title: "Made for Professionals",
    description:
      "Designed for freelancers, startups, teams and businesses looking for a simpler way to find workspace.",
  },
];
</script>