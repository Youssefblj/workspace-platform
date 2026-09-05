<template>
  <div
    v-if="show && booking"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-sm"
    @click.self="emit('close')"
  >
    <div
      class="w-full max-w-2xl overflow-hidden rounded-2xl bg-white shadow-2xl"
    >

      <!-- Header -->
      <div
        class="flex items-center justify-between border-b border-gray-100 px-6 py-5"
      >
        <div class="flex items-center gap-3">

          <div
            class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#f29200]/10"
          >
            <CalendarDays class="h-5 w-5 text-[#f29200]" />
          </div>

          <div>
            <h2 class="text-lg font-bold text-[#23394e]">
              Reservation Details
            </h2>

            <p class="mt-0.5 text-sm text-[#9f9f9f]">
              Booking #{{ booking.id }}
            </p>
          </div>

        </div>

        <button
          type="button"
          @click="emit('close')"
          class="rounded-lg p-2 text-[#9f9f9f] transition hover:bg-gray-100 hover:text-[#23394e]"
        >
          <X class="h-5 w-5" />
        </button>
      </div>


      <!-- Content -->
      <div class="grid gap-4 p-6 sm:grid-cols-2">

        <!-- Office -->
        <div
          class="rounded-xl border border-gray-100 bg-gray-50 p-4"
        >
          <div class="flex items-center gap-2 text-sm text-[#9f9f9f]">
            <Building2 class="h-4 w-4 text-[#f29200]" />
            Office
          </div>

          <p class="mt-2 font-semibold text-[#23394e]">
            {{ booking.office_title || booking.office?.title || '-' }}
          </p>
        </div>


        <!-- City -->
        <div
          class="rounded-xl border border-gray-100 bg-gray-50 p-4"
        >
          <div class="flex items-center gap-2 text-sm text-[#9f9f9f]">
            <MapPin class="h-4 w-4 text-[#f29200]" />
            City
          </div>

          <p class="mt-2 font-semibold text-[#23394e]">
            {{ booking.office_city || booking.office?.city || '-' }}
          </p>
        </div>


        <!-- Booking dates -->
        <div
          class="rounded-xl border border-gray-100 bg-gray-50 p-4"
        >
          <div class="flex items-center gap-2 text-sm text-[#9f9f9f]">
            <Calendar class="h-4 w-4 text-[#f29200]" />
            Booking dates
          </div>

          <div class="mt-2 space-y-1 font-medium text-[#23394e]">
            <p>{{ formatDate(booking.start_date) }}</p>
            <p>{{ formatDate(booking.end_date) }}</p>
          </div>
        </div>


        <!-- Duration -->
        <div
          class="rounded-xl border border-gray-100 bg-gray-50 p-4"
        >
          <div class="flex items-center gap-2 text-sm text-[#9f9f9f]">
            <Clock3 class="h-4 w-4 text-[#f29200]" />
            Duration
          </div>

          <span
            class="mt-2 inline-flex rounded-lg bg-[#23394e]/5 px-2.5 py-1 text-sm font-semibold text-[#23394e]"
          >
            {{ duration }} {{ duration === 1 ? 'Day' : 'Days' }}
          </span>
        </div>


        <!-- Capacity -->
<div
  class="rounded-xl border border-gray-100 bg-gray-50 p-4"
>
  <div
    class="flex items-center gap-2 text-sm text-[#9f9f9f]"
  >
    <Users class="h-4 w-4 text-[#f29200]" />
    Capacity
  </div>

  <p class="mt-2 font-semibold text-[#23394e]">
    {{ booking.office?.capacity ?? "-" }} People
  </p>
</div>


        <!-- Status -->
        <div
          class="rounded-xl border border-gray-100 bg-gray-50 p-4"
        >
          <p class="text-sm text-[#9f9f9f]">
            Status
          </p>

          <span
            class="mt-2 inline-flex rounded-full px-3 py-1 text-sm font-semibold"
            :class="statusClasses"
          >
            {{ formatStatus(booking.status) }}
          </span>
        </div>

      </div>


      <!-- Total -->
      <div class="px-6 pb-6">
        <div
          class="flex items-end justify-between rounded-xl bg-gray-50 p-5"
        >

          <div>
            <p class="text-xs font-semibold uppercase tracking-wide text-[#9f9f9f]">
              Total
            </p>

            <p class="mt-1 text-3xl font-black text-[#23394e]">
              {{ booking.total_price }} MAD
            </p>
          </div>

          <div class="text-right">
            <p class="text-xs text-[#9f9f9f]">
              Created
            </p>

            <p class="mt-1 text-sm font-medium text-[#9f9f9f]">
              {{ formatDate(booking.created_at) }}
            </p>
          </div>

        </div>
      </div>


      <!-- Footer -->
      <div
        class="flex justify-end border-t border-gray-100 px-6 py-4"
      >
        <button
          type="button"
          @click="emit('close')"
          class="rounded-lg border border-gray-200 px-5 py-2.5 text-sm font-medium text-[#23394e] transition hover:bg-gray-50"
        >
          Close
        </button>
      </div>

    </div>
  </div>
</template>


<script setup>
import { computed } from 'vue'

import {
  X,
  CalendarDays,
  Building2,
  MapPin,
  Calendar,
  Clock3,
  Users
} from 'lucide-vue-next'


const props = defineProps({
  show: Boolean,

  booking: {
    type: Object,
    default: null
  }
})


const emit = defineEmits([
  'close'
])


const duration = computed(() => {

  if (
    !props.booking?.start_date ||
    !props.booking?.end_date
  ) {
    return 0
  }

  const start = new Date(
    props.booking.start_date
  )

  const end = new Date(
    props.booking.end_date
  )

  return (
    Math.floor(
      (end - start) /
      (1000 * 60 * 60 * 24)
    ) + 1
  )
})


const statusClasses = computed(() => {

  if (props.booking?.status === 'confirmed') {
    return 'bg-emerald-100 text-emerald-700'
  }

  if (props.booking?.status === 'cancelled') {
    return 'bg-red-100 text-red-600'
  }

  return 'bg-[#f29200]/10 text-[#f29200]'
})


const formatDate = (value) => {

  if (!value) {
    return '-'
  }

  return new Date(value).toLocaleDateString(
    undefined,
    {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    }
  )
}


const formatStatus = (value) => {

  if (!value) {
    return '-'
  }

  return value
    .replaceAll('_', ' ')
    .replace(
      /\b\w/g,
      char => char.toUpperCase()
    )
}
</script>