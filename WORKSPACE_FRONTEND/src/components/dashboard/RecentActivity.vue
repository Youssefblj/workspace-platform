<template>
  <section>

    <div class="mb-6">
      <h2 class="text-2xl font-bold text-gray-900">
        Recent Activity
      </h2>

      <p class="mt-1 text-gray-500">
        Latest activity on your account.
      </p>
    </div>

    <div
      class="rounded-3xl border border-gray-100 bg-white p-8 shadow-sm"
    >

      <div
        v-if="activities.length"
      >

        <div
          v-for="activity in activities"
          :key="activity.id"
          class="group flex gap-5 border-b border-gray-100 py-6 last:border-none"
        >

          <div
            class="flex h-14 w-14 items-center justify-center rounded-2xl transition duration-300"
            :class="activity.color"
          >
            <component
              :is="activity.icon"
              class="h-6 w-6"
            />
          </div>

          <div class="flex-1">

            <div
              class="flex flex-col gap-2 lg:flex-row lg:items-center lg:justify-between"
            >

              <div>

                <h3 class="text-lg font-bold text-gray-900">
                  {{ activity.title }}
                </h3>

                <p class="mt-1 text-gray-500">
                  {{ activity.description }}
                </p>

              </div>

              <span class="text-sm text-gray-400">
                {{ formatDate(activity.date) }}
              </span>

            </div>

          </div>

        </div>

      </div>

      <!-- Empty -->

      <div
        v-else
        class="py-12 text-center"
      >
        <Clock3 class="mx-auto h-12 w-12 text-gray-300"/>

        <h3 class="mt-4 text-lg font-semibold text-gray-700">
          No Recent Activity
        </h3>

        <p class="mt-2 text-gray-500">
          Your latest actions will appear here.
        </p>

      </div>

    </div>

  </section>
</template>

<script setup>
import { computed } from "vue";

import {
CheckCircle2,
CalendarPlus,
Clock3,
Bell,
AlertCircle
} from "lucide-vue-next";

const props = defineProps({

  bookings:{
    type:Array,
    default:()=>[]
  },

  notifications:{
    type:Array,
    default:()=>[]
  }

})

const bookingActivities = computed(()=>{

  return props.bookings.map(b=>({

    id:`booking-${b.id}`,

    title:
      b.status==="confirmed"
        ? "Booking Confirmed"
        : "Booking Pending",

    description:
      `Reservation from ${b.start_date} to ${b.end_date}`,

    date:b.created_at,

    icon:
      b.status==="confirmed"
        ? CheckCircle2
        : CalendarPlus,

    color:
      b.status==="confirmed"
        ? "bg-emerald-100 text-emerald-600"
        : "bg-amber-100 text-amber-600"

  }))

})

const notificationActivities = computed(()=>{

  return props.notifications.map(n=>({

    id:`notification-${n.id}`,

    title:n.title,

    description:n.message,

    date:n.created_at,

    icon:n.is_read
      ? Bell
      : AlertCircle,

    color:n.is_read
      ? "bg-blue-100 text-blue-600"
      : "bg-red-100 text-red-500"

  }))

})

const activities = computed(()=>{

  return [
    ...bookingActivities.value,
    ...notificationActivities.value
  ]

  .sort(
    (a,b)=>
      new Date(b.date)-new Date(a.date)
  )

  .slice(0,8)

})

const formatDate=(date)=>{

  return new Date(date).toLocaleDateString(
    undefined,
    {
      month:"short",
      day:"numeric"
    }
  )

}
</script>