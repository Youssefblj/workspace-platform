<template>
  <section v-if="booking">
    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="text-2xl font-bold text-gray-900">
          Upcoming Booking
        </h2>

        <p class="mt-1 text-gray-500">
          Your next scheduled workspace reservation.
        </p>
      </div>

      <router-link
        to="/dashboard?tab=reservations"
        class="text-sm font-semibold text-amber-500 transition hover:text-amber-600"
      >
        View All
      </router-link>
    </div>

    <div
      class="group overflow-hidden rounded-3xl border border-gray-100 bg-white shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
    >
      <div class="grid lg:grid-cols-[360px_1fr]">

        <!-- Image -->

        <div class="overflow-hidden">
          <img
            :src="officeImage"
            :alt="office.title"
            class="h-full w-full object-cover transition duration-700 group-hover:scale-110"
          />
        </div>

        <!-- Content -->

        <div class="flex flex-col justify-between p-8">

          <div>

            <span
              class="inline-flex items-center rounded-full px-3 py-1 text-xs font-semibold"
              :class="statusClass"
            >
              {{ booking.status }}
            </span>

            <h3 class="mt-5 text-3xl font-bold text-gray-900">
              {{ office.title }}
            </h3>

            <div class="mt-6 grid gap-5 sm:grid-cols-2">

              <div class="flex items-center gap-3">
                <MapPin class="h-5 w-5 text-amber-500" />
                <span>{{ office.city }}</span>
              </div>

              <div class="flex items-center gap-3">
                <CalendarDays class="h-5 w-5 text-amber-500" />
                <span>{{ booking.start_date }}</span>
              </div>

              <div class="flex items-center gap-3">
                <CalendarCheck class="h-5 w-5 text-amber-500" />
                <span>{{ booking.end_date }}</span>
              </div>

              <div class="flex items-center gap-3">
                <Users class="h-5 w-5 text-amber-500" />
                <span>{{ office.capacity }} People</span>
              </div>

            </div>

          </div>

          <!-- Amenities -->

          <div class="mt-8 flex flex-wrap gap-3">

            <span
              v-if="office.wifi"
              class="inline-flex items-center gap-2 rounded-xl bg-slate-100 px-4 py-2 text-sm"
            >
              <Wifi class="h-4 w-4 text-amber-500" />
              WiFi
            </span>

            <span
              v-if="office.parking"
              class="inline-flex items-center gap-2 rounded-xl bg-slate-100 px-4 py-2 text-sm"
            >
              <Car class="h-4 w-4 text-amber-500" />
              Parking
            </span>

            <span
              v-if="office.meeting_room"
              class="inline-flex items-center gap-2 rounded-xl bg-slate-100 px-4 py-2 text-sm"
            >
              <Building2 class="h-4 w-4 text-amber-500" />
              Meeting Room
            </span>

            <span
              v-if="office.air_conditioning"
              class="inline-flex items-center gap-2 rounded-xl bg-slate-100 px-4 py-2 text-sm"
            >
              <Snowflake class="h-4 w-4 text-amber-500" />
              AC
            </span>

          </div>

          <!-- Footer -->

          <div class="mt-8 flex items-center justify-between">

            <div>
              <p class="text-sm text-gray-500">
                Total Price
              </p>

              <p class="text-2xl font-bold text-amber-500">
                {{ booking.total_price }} MAD
              </p>
            </div>

            <router-link
              :to="`/office/${office.id}`"
              class="inline-flex items-center gap-2 rounded-2xl bg-amber-500 px-6 py-3 font-semibold text-white transition hover:bg-amber-600"
            >
              View Office

              <ArrowRight class="h-5 w-5"/>
            </router-link>

          </div>

        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from "vue";

import {
  MapPin,
  CalendarDays,
  CalendarCheck,
  Users,
  Wifi,
  Car,
  Building2,
  Snowflake,
  ArrowRight
} from "lucide-vue-next";

const props = defineProps({
  booking: {
    type: Object,
    default: null
  },

  offices: {
    type: Array,
    default: () => []
  }
});

const office = computed(() => {
  return props.offices.find(
    o => o.id === props.booking.office
  ) || {};
});

const officeImage = computed(() => {
  const image = office.value?.images?.[0]?.image

  if (!image) {
    return (
      "data:image/svg+xml;utf8," +
      '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600">' +
      '<rect width="100%" height="100%" fill="%23f3f4f6"/>' +
      '<text x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" fill="%239f9f9f" font-size="24">No image</text>' +
      "</svg>"
    )
  }

  if (
    image.startsWith("http://") ||
    image.startsWith("https://")
  ) {
    return image
  }

  return `http://127.0.0.1:8000${image}`
})

const statusClass = computed(() => {
  switch (props.booking.status) {
    case "confirmed":
      return "bg-emerald-100 text-emerald-700";

    case "pending":
      return "bg-amber-100 text-amber-700";

    case "cancelled":
      return "bg-red-100 text-red-700";

    default:
      return "bg-slate-100 text-slate-700";
  }
});
</script>