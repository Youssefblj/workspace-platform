<script setup>
import {
  computed,
  onMounted,
  ref,
  watch
} from "vue"

import { useNotificationStore } from "@/stores/notification"

import {
  Bell,
  BellRing,
  CheckCircle2,
  CalendarClock,
  CheckCheck,
  ChevronLeft,
  ChevronRight
} from "lucide-vue-next"


const notificationStore = useNotificationStore()


/* ==========================================================
   Store Data
========================================================== */

const notifications = computed(() =>
  notificationStore.notifications
)

const unreadCount = computed(() =>
  notificationStore.unreadCount
)

const loading = computed(() =>
  notificationStore.loading
)

/* ==========================================================
   Stats
========================================================== */

const totalCount = computed(() =>
  notificationStore.totalNotifications
)


const todayCount = computed(() => {

  const today =
    new Date().toDateString()

  return notifications.value.filter(
    notification =>
      new Date(
        notification.created_at
      ).toDateString() === today
  ).length

})


/* ==========================================================
   Filters
========================================================== */

const filter = ref("all")


const filteredNotifications = computed(() => {

  if (filter.value === "unread") {

    return notifications.value.filter(
      notification =>
        !notification.is_read
    )
  }

  if (filter.value === "read") {

    return notifications.value.filter(
      notification =>
        notification.is_read
    )
  }

  return notifications.value
})


/* ==========================================================
   Pagination
========================================================== */

const currentPage = computed(() =>
  notificationStore.currentPage
)

const totalPages = computed(() =>
  notificationStore.totalPages
)



const visiblePages = computed(() => {

  const total =
    totalPages.value

  const current =
    currentPage.value


  if (total <= 5) {

    return Array.from(
      { length: total },
      (_, index) =>
        index + 1
    )

  }


  let start =
    Math.max(
      1,
      current - 2
    )

  let end =
    Math.min(
      total,
      start + 4
    )


  if (end - start < 4) {

    start =
      Math.max(
        1,
        end - 4
      )

  }


  return Array.from(
    {
      length:
        end - start + 1
    },
    (_, index) =>
      start + index
  )

})


const changePage = async page => {

  if (
    page < 1 ||
    page > totalPages.value ||
    page === currentPage.value ||
    loading.value
  ) {
    return
  }

  await notificationStore
    .fetchNotifications(page)

  window.scrollTo({
    top: 0,
    behavior: "smooth"
  })
}


/* Reset pagination after filter change */

watch(
  filter,
  () => {
    currentPage.value = 1
  }
)


/* If notifications change and current page
   becomes invalid */




/* ==========================================================
   Mounted
========================================================== */

onMounted(async () => {

  await notificationStore
    .fetchNotifications(1)

})
</script>


<template>

  <section class="mx-auto max-w-4xl space-y-5">

    <!-- ==================================================
         Header
    =================================================== -->

    <div
      class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
    >

      <div>

        <h2
          class="text-3xl font-black text-[#23394E]"
        >
          Notifications
        </h2>

        <p
          class="mt-2 text-[#9f9f9f]"
        >
          Stay updated with your latest account activity.
        </p>

      </div>


      <button
        type="button"
        @click="notificationStore.markAllAsRead()"
        class="inline-flex items-center gap-2 rounded-2xl bg-[#F29200] px-5 py-3 font-semibold text-white transition hover:bg-[#d98200]"
      >

        <CheckCheck class="h-5 w-5" />

        Mark all as read

      </button>

    </div>


    <!-- ==================================================
         Stats
    =================================================== -->

    <div
      class="mt-8 grid gap-6 md:grid-cols-3"
    >

      <!-- Unread -->

      <div
        class="rounded-3xl border border-amber-100 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg"
      >

        <div
          class="flex items-center justify-between"
        >

          <div>

            <p class="text-sm text-gray-500">
              Unread
            </p>

            <h3
              class="mt-2 text-4xl font-black text-[#23394E]"
            >
              {{ unreadCount }}
            </h3>

          </div>


          <div
            class="flex h-14 w-14 items-center justify-center rounded-2xl bg-amber-100"
          >

            <BellRing
              class="h-7 w-7 text-[#F29200]"
            />

          </div>

        </div>

      </div>


      <!-- Today -->

      <div
        class="rounded-3xl border border-gray-100 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg"
      >

        <div
          class="flex items-center justify-between"
        >

          <div>

            <p class="text-sm text-gray-500">
              Today
            </p>

            <h3
              class="mt-2 text-4xl font-black text-[#23394E]"
            >
              {{ todayCount }}
            </h3>

          </div>


          <div
            class="flex h-14 w-14 items-center justify-center rounded-2xl bg-[#23394e]/10"
          >

            <CalendarClock
              class="h-7 w-7 text-[#23394e]"
            />

          </div>

        </div>

      </div>


      <!-- Total -->

      <div
        class="rounded-3xl border border-emerald-100 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg"
      >

        <div
          class="flex items-center justify-between"
        >

          <div>

            <p class="text-sm text-gray-500">
              Total
            </p>

            <h3
              class="mt-2 text-4xl font-black text-[#23394E]"
            >
              {{ totalCount }}
            </h3>

          </div>


          <div
            class="flex h-14 w-14 items-center justify-center rounded-2xl bg-emerald-100"
          >

            <Bell
              class="h-7 w-7 text-emerald-600"
            />

          </div>

        </div>

      </div>

    </div>


    <!-- ==================================================
         Filters
    =================================================== -->

    <div
      class="mt-8 flex flex-wrap gap-3"
    >

      <button
        type="button"
        @click="filter = 'all'"
        :class="[
          'rounded-2xl px-5 py-2 text-sm font-semibold transition',

          filter === 'all'
            ? 'bg-[#F29200] text-white'
            : 'border border-gray-200 bg-white text-gray-600 hover:border-[#F29200]'
        ]"
      >
        All ({{ totalCount }})
      </button>


      <button
        type="button"
        @click="filter = 'unread'"
        :class="[
          'rounded-2xl px-5 py-2 text-sm font-semibold transition',

          filter === 'unread'
            ? 'bg-[#F29200] text-white'
            : 'border border-gray-200 bg-white text-gray-600 hover:border-[#F29200]'
        ]"
      >
        Unread ({{ unreadCount }})
      </button>


      <button
        type="button"
        @click="filter = 'read'"
        :class="[
          'rounded-2xl px-5 py-2 text-sm font-semibold transition',

          filter === 'read'
            ? 'bg-[#F29200] text-white'
            : 'border border-gray-200 bg-white text-gray-600 hover:border-[#F29200]'
        ]"
      >
        Read ({{ totalCount - unreadCount }})
      </button>

    </div>


    <!-- ==================================================
         Notifications List
    =================================================== -->

    <div class="mt-8">

      <!-- Loading -->

      <div
        v-if="loading"
        class="space-y-5"
      >

        <div
          v-for="i in 6"
          :key="i"
          class="animate-pulse rounded-3xl border border-gray-100 bg-white p-6"
        >

          <div
            class="flex items-center gap-4"
          >

            <div
              class="h-14 w-14 rounded-2xl bg-gray-200"
            ></div>

            <div
              class="flex-1 space-y-3"
            >

              <div
                class="h-5 w-52 rounded bg-gray-200"
              ></div>

              <div
                class="h-4 w-full rounded bg-gray-100"
              ></div>

              <div
                class="h-4 w-32 rounded bg-gray-100"
              ></div>

            </div>

          </div>

        </div>

      </div>


      <!-- Empty -->

      <div
        v-else-if="
          filteredNotifications.length === 0
        "
        class="rounded-3xl border border-dashed border-gray-200 bg-white p-16 text-center"
      >

        <div
          class="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-slate-100"
        >

          <Bell
            class="h-10 w-10 text-gray-400"
          />

        </div>


        <h3
          class="mt-6 text-2xl font-bold text-[#23394E]"
        >
          No Notifications
        </h3>


        <p
          class="mt-2 text-[#9f9f9f]"
        >
          You're all caught up.
        </p>

      </div>


      <!-- Cards -->

      <div
        v-else
        class="space-y-5"
      >

        <div
v-for="notification in filteredNotifications"
          :key="notification.id"
          class="group rounded-3xl border bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
          :class="
            notification.is_read
              ? 'border-gray-100'
              : 'border-[#F29200] ring-2 ring-amber-100'
          "
        >

          <div
            class="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between"
          >

            <!-- Left -->

            <div class="flex gap-5">

              <div
                class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl"
                :class="
                  notification.is_read
                    ? 'bg-slate-100'
                    : 'bg-amber-100'
                "
              >

                <Bell
                  class="h-7 w-7"
                  :class="
                    notification.is_read
                      ? 'text-slate-500'
                      : 'text-[#F29200]'
                  "
                />

              </div>


              <div>

                <div
                  class="flex flex-wrap items-center gap-3"
                >

                  <h3
                    class="text-xl font-bold text-[#23394E]"
                  >
                    {{ notification.title }}
                  </h3>


                  <span
                    v-if="!notification.is_read"
                    class="rounded-full bg-[#F29200] px-3 py-1 text-xs font-semibold text-white"
                  >
                    NEW
                  </span>

                </div>


                <p
                  class="mt-2 text-gray-500"
                >
                  {{ notification.message }}
                </p>


                <p
                  class="mt-4 text-sm text-gray-400"
                >
                  {{
                    new Date(
                      notification.created_at
                    ).toLocaleString()
                  }}
                </p>

              </div>

            </div>


            <!-- Right -->

            <div
              class="flex items-center gap-3"
            >

              <button
                v-if="!notification.is_read"
                type="button"
                @click="
                  notificationStore
                    .markAsRead(notification)
                "
                class="rounded-2xl bg-[#F29200] px-5 py-3 text-sm font-semibold text-white transition hover:bg-[#dc8500]"
              >
                Mark as read
              </button>


              <div
                v-else
                class="flex items-center gap-2 rounded-2xl bg-emerald-100 px-4 py-3 text-sm font-semibold text-emerald-600"
              >

                <CheckCircle2
                  class="h-5 w-5"
                />

                Read

              </div>

            </div>

          </div>

        </div>


        <!-- ==============================================
             Pagination
        =============================================== -->

        <div
          v-if="totalPages > 1"
          class="flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-gray-100 bg-white px-4 py-4 shadow-sm"
        >

          <!-- Page Information -->

          <p
            class="text-xs font-medium text-[#9f9f9f]"
          >
            Page

            <span
              class="font-bold text-[#23394e]"
            >
              {{ currentPage }}
            </span>

            of

            <span
              class="font-bold text-[#23394e]"
            >
              {{ totalPages }}
            </span>
          </p>


          <div
            class="flex items-center gap-2"
          >

            <!-- Previous -->

            <button
              type="button"
              :disabled="currentPage <= 1"
              @click="
                changePage(
                  currentPage - 1
                )
              "
              class="flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200 bg-white text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
            >

              <ChevronLeft
                class="h-4 w-4"
              />

            </button>


            <!-- Pages -->

            <button
              v-for="page in visiblePages"
              :key="page"
              type="button"
              @click="changePage(page)"
              :class="[
                'flex h-9 min-w-9 items-center justify-center rounded-lg px-3 text-xs font-bold transition',

                page === currentPage
                  ? 'bg-[#f29200] text-white shadow-sm'
                  : 'border border-gray-200 bg-white text-[#23394e] hover:border-[#f29200] hover:text-[#f29200]'
              ]"
            >
              {{ page }}
            </button>


            <!-- Next -->

            <button
              type="button"
              :disabled="
                currentPage >= totalPages
              "
              @click="
                changePage(
                  currentPage + 1
                )
              "
              class="flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200 bg-white text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-40"
            >

              <ChevronRight
                class="h-4 w-4"
              />

            </button>

          </div>

        </div>

      </div>

    </div>

  </section>

</template>
