<template>
  <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
    <div v-if="loading" class="flex flex-col items-center justify-center py-20 gap-4">
      <svg class="h-10 w-10 animate-spin text-[#f29200]" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
      <span class="text-sm font-medium text-gray-500">Loading office details...</span>
    </div>

    <div v-else-if="!office" class="text-center py-20 bg-white/50 border border-gray-100 rounded-3xl">
      <Building class="mx-auto h-12 w-12 text-gray-300" />
      <h3 class="mt-4 font-display font-bold text-gray-900 text-lg">Office not found</h3>
      <router-link to="/" class="mt-4 inline-block rounded-xl bg-[#f29200] px-4 py-2 text-xs font-semibold text-white">
        Back to browse
      </router-link>
    </div>

    <template v-else>
      <div class="mb-5">
        <router-link to="/" class="inline-flex items-center gap-2 text-sm font-semibold text-gray-700 hover:text-[#f29200]">
          <ArrowLeft class="h-4 w-4" />
          <span>Back to workspaces</span>
        </router-link>
      </div>

      <div class="grid grid-cols-1 gap-8 lg:grid-cols-[minmax(0,1fr)_360px]">
        <div class="space-y-7">
          <div class="space-y-3">
            <div
              class="group relative aspect-[16/7.45] min-h-[320px] overflow-hidden rounded-[22px] bg-gray-100 shadow-sm ring-1 ring-gray-200"
            >
              <img
                :src="activeImage"
                :alt="office.title"
                class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
              />

              <div class="absolute left-5 top-5 flex items-center gap-2 rounded-xl bg-white px-4 py-3 shadow-sm">
                <Star class="h-4 w-4 fill-amber-400 text-amber-400" />
                <span class="text-sm font-extrabold text-gray-900">{{ office.average_rating }}</span>
                <span class="text-xs font-semibold text-gray-400">({{ reviews.length }} reviews)</span>
              </div>

              <div
                class="absolute right-5 top-5 flex items-center gap-2 rounded-xl px-4 py-3 shadow-sm"
                :class="office.available ? 'bg-emerald-50 text-emerald-600' : 'bg-gray-100 text-gray-500'"
              >
                <span class="h-2 w-2 rounded-full" :class="office.available ? 'bg-emerald-500' : 'bg-gray-400'"></span>
                <span class="text-xs font-bold">{{ office.available ? 'Available' : 'Booked' }}</span>
              </div>

              <div class="absolute inset-0 bg-gradient-to-t from-black/45 via-transparent to-transparent"></div>

              <div class="absolute bottom-5 left-5 flex flex-wrap gap-2">
                <div class="flex items-center gap-2 rounded-xl bg-gray-900/75 px-4 py-3 text-xs font-bold text-white backdrop-blur-md">
                  <MapPin class="h-4 w-4" />
                  <span>{{ office.city }}</span>
                </div>
                <div class="flex items-center gap-2 rounded-xl bg-gray-900/75 px-4 py-3 text-xs font-bold text-white backdrop-blur-md">
                  <Users class="h-4 w-4" />
                  <span>Up to {{ office.capacity }} people</span>
                </div>
              </div>
            </div>

            <div v-if="office.images && office.images.length > 1" class="flex gap-3 overflow-x-auto pb-1">
              <button
                v-for="(img, idx) in office.images"
                :key="img.id"
                @click="activeIndex = idx"
                :class="['h-[62px] w-[116px] shrink-0 overflow-hidden rounded-xl border-2 bg-gray-50 transition-all', activeIndex === idx ? 'border-[#f29200] shadow-sm' : 'border-transparent']"
              >
                <img :src="getAbsoluteImageUrl(img.image)" :alt="office.title" class="h-full w-full object-cover" />
              </button>
            </div>
          </div>

          <div>
            <div class="flex flex-wrap items-start justify-between gap-4">
              <h1 class="font-display text-2xl font-black leading-tight text-gray-950 sm:text-3xl">
                {{ office.title }}
              </h1>
              <div class="flex shrink-0 items-center gap-3">
                <button
  type="button"
  @click="toggleFavorite"
  :disabled="favoriteLoading"
  :class="[
    'flex items-center gap-2 rounded-xl border px-4 py-3 text-xs font-semibold shadow-sm transition disabled:cursor-not-allowed disabled:opacity-60',

    isFavorite
      ? 'border-[#f29200]/30 bg-[#f29200]/10 text-[#f29200]'
      : 'border-gray-200 bg-white text-[#23394e] hover:border-[#f29200] hover:text-[#f29200]'
  ]"
>

  <Loader2
    v-if="favoriteLoading"
    class="h-4 w-4 animate-spin"
  />

  <Heart
    v-else
    :class="[
      'h-4 w-4 transition',
      isFavorite
        ? 'fill-[#f29200] text-[#f29200]'
        : ''
    ]"
  />

  {{
    favoriteLoading
      ? 'Saving...'
      : isFavorite
        ? 'Saved'
        : 'Add to favorites'
  }}

</button>
<button
  type="button"
  @click="shareOffice"
  class="flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-3 text-xs font-semibold text-[#23394e] shadow-sm transition hover:border-[#f29200] hover:text-[#f29200]"
>
  <Check
    v-if="linkCopied"
    class="h-4 w-4 text-emerald-500"
  />

  <Share2
    v-else
    class="h-4 w-4"
  />

  {{ linkCopied ? "Link copied" : "Share" }}
</button>
              </div>
            </div>

            <p class="mt-2 flex items-center gap-2 text-sm font-medium text-gray-500">
              <MapPin class="h-4 w-4 text-[#f29200]" />
              <span>{{ office.address }}, {{ office.city }}</span>
            </p>

            <div class="mt-5 flex flex-wrap items-center gap-x-6 gap-y-3 text-xs font-semibold text-gray-500">
              <span
                v-for="amenity in amenitiesList.filter(a => a.active).slice(0, 4)"
                :key="amenity.label"
                class="flex items-center gap-2"
              >
                <component :is="amenity.icon" class="h-4 w-4 text-gray-400" />
                {{ amenity.label }}
              </span>
              <span
                class="rounded-lg bg-gray-100 px-3 py-1.5 text-[11px] font-bold text-gray-500"
              >
                +3 more
              </span>
            </div>
          </div>

          <div class="border-t border-gray-100 pt-5">
            <h3 class="font-display text-lg font-bold text-gray-950">About this workspace</h3>
            <p class="mt-2 max-w-3xl whitespace-pre-line text-sm leading-relaxed text-gray-600">
              {{ office.description }}
            </p>

            <div class="mt-4 grid grid-cols-2 gap-3 sm:grid-cols-3 xl:grid-cols-6">
              <div
                v-for="amenity in amenitiesList"
                :key="amenity.label"
                :class="['flex min-h-[58px] items-center justify-center gap-2 rounded-xl border px-3 py-3 text-center text-xs font-semibold transition-all', amenity.active ? 'border-gray-200 bg-white text-gray-700 shadow-sm' : 'border-gray-100 bg-gray-50/60 text-gray-400 opacity-70']"
              >
                <component :is="amenity.icon" class="h-5 w-5 shrink-0" :class="amenity.active ? 'text-[#f29200]' : 'text-gray-300'" />
                <span>{{ amenity.label }}</span>
              </div>
              <div class="flex min-h-[58px] items-center justify-center gap-2 rounded-xl border border-gray-200 bg-white px-3 py-3 text-center text-xs font-semibold text-gray-700 shadow-sm">
                <CreditCard class="h-5 w-5 shrink-0 text-[#f29200]" />
                <span>Printer & Scanner</span>
              </div>
              <div class="flex min-h-[58px] items-center justify-center gap-2 rounded-xl border border-gray-200 bg-white px-3 py-3 text-center text-xs font-semibold text-gray-700 shadow-sm">
                <Flame class="h-5 w-5 shrink-0 text-[#f29200]" />
                <span>24/7 Access</span>
              </div>
            </div>
          </div>

          <div class="rounded-2xl border border-gray-100 bg-white p-5 shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <h3 class="flex items-center gap-2 font-display text-lg font-bold text-gray-950">
                <Star class="h-5 w-5 fill-amber-400 text-amber-400" />
                Reviews ({{ reviews.length }})
              </h3>
              <button
                v-if="authStore.isAuthenticated && !showReviewForm"
                @click="showReviewForm = true"
                class="flex items-center gap-1.5 text-xs font-semibold text-[#f29200] hover:text-[#d97706]"
              >
                <Pencil class="h-3.5 w-3.5" />
                Write a review
              </button>
            </div>

            <!-- Review write form -->
            <div
              v-if="showReviewForm"
              class="mb-6 p-5 border border-[#f29200] rounded-3xl bg-white shadow-sm space-y-4 animate-in slide-in-from-top-3 duration-300"
            >
              <h4 class="font-display font-bold text-sm text-gray-900">Share your experience</h4>

              <!-- Stars selector -->
              <div>
                <label class="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-1">Rating</label>
                <div class="flex gap-1.5">
                  <button
                    v-for="star in 5"
                    :key="star"
                    type="button"
                    @click="newReview.rating = star"
                    class="p-0.5"
                  >
                    <Star
                      :class="['h-6 w-6 transition-all', star <= newReview.rating ? 'fill-amber-400 text-amber-400' : 'text-gray-300']"
                    />
                  </button>
                </div>
              </div>

              <!-- Comment textarea -->
              <div>
                <label for="comment" class="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-1">Comment</label>
                <textarea
                  id="comment"
                  v-model="newReview.comment"
                  rows="3"
                  required
                  placeholder="Tell us about the environment, internet speed, comfort..."
                  class="block w-full rounded-xl border border-gray-200 px-3 py-2 text-xs focus:border-[#f29200] focus:outline-none"
                ></textarea>
              </div>

              <div class="flex gap-2 justify-end">
                <button
                  type="button"
                  @click="showReviewForm = false"
                  class="rounded-xl border border-gray-200 px-4 py-2 text-xs font-semibold text-gray-700 hover:bg-gray-50"
                >
                  Cancel
                </button>
                <button
                  type="button"
                  @click="submitReview"
                  :disabled="submitReviewLoading"
                  class="rounded-xl bg-[#f29200] px-4 py-2 text-xs font-semibold text-white hover:bg-[#d97706] disabled:opacity-50"
                >
                  Post Review
                </button>
              </div>
            </div>

            <!-- Review items list -->
            <div v-if="reviews.length === 0" class="py-10 text-center text-xs text-gray-400">
              No reviews for this office yet. Be the first to leave one!
            </div>
            <div v-else class="space-y-4">
              <div
                v-for="review in reviews"
                :key="review.id"
                class="border border-gray-100 rounded-3xl p-5 bg-white shadow-sm flex flex-col gap-2"
              >
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-2">
                    <div class="flex h-7 w-7 items-center justify-center rounded-lg bg-gray-100 text-xs font-semibold text-gray-600">
                      {{ review.user_username ? review.user_username.slice(0, 2).toUpperCase() : 'U' }}
                    </div>
                    <span class="text-xs font-semibold text-gray-800">{{ review.user_username || 'Anonymous User' }}</span>
                  </div>
                  <span class="text-[10px] text-gray-400">{{ formatDate(review.created_at) }}</span>
                </div>
                <div class="flex gap-0.5">
                  <Star
                    v-for="star in 5"
                    :key="star"
                    :class="['h-3.5 w-3.5', star <= review.rating ? 'fill-amber-400 text-amber-400' : 'text-gray-200']"
                  />
                </div>
                <p class="text-xs text-gray-500 leading-relaxed mt-1">
                  {{ review.comment }}
                </p>
              </div>
            </div>
          </div>

        </div>

        <div>
          <div class="sticky top-24 space-y-4">

            <div class="space-y-7 rounded-[26px] border border-gray-100 bg-white p-8 shadow-xl shadow-gray-200/60">

              <div>
                <span class="text-xs font-bold uppercase text-gray-400">Rate</span>
                <div class="flex items-baseline gap-1 mt-1">
                  <span class="font-display text-3xl font-black text-gray-950">{{ office.price }} DH</span>
                  <span class="text-xs font-medium text-gray-500">/ {{ office.rent_type }}</span>
                </div>
                <span class="mt-3 flex w-max items-center gap-1 rounded-lg bg-gray-100 px-2.5 py-1 text-[11px] font-semibold text-gray-500">
                  <UserCircle class="h-3.5 w-3.5" />
                  Holds up to {{ office.capacity }} people
                </span>
              </div>

              <form @submit.prevent="handleBookingSubmit" class="space-y-4">

                <span class="block text-xs font-bold uppercase tracking-wider text-gray-400">Select Dates</span>

                <div class="grid gap-3 sm:grid-cols-2">
                  <div>
                    <label for="start_date" class="mb-1 block text-xs font-semibold text-gray-600">Check-in</label>
                    <button
                      id="start_date"
                      type="button"
                      :aria-expanded="activeDateField === 'start'"
                      @click="openDatePicker('start')"
                      :class="[
                        'flex w-full items-center justify-between rounded-xl border px-3.5 py-3.5 text-left text-sm transition focus:outline-none focus:ring-2 focus:ring-[#f29200]/20',
                        activeDateField === 'start'
                          ? 'border-[#f29200] bg-[#f29200]/5 text-[#23394e]'
                          : 'border-gray-200 text-[#23394e] hover:border-[#f29200]/60'
                      ]"
                    >
                      <span :class="bookingDates.start ? 'font-medium' : 'text-[#9f9f9f]'">
                        {{ bookingDates.start ? formatBookingDate(bookingDates.start) : 'Select date' }}
                      </span>
                      <Calendar class="h-4 w-4 shrink-0 text-[#f29200]" />
                    </button>
                  </div>

                  <div>
                    <label for="end_date" class="mb-1 block text-xs font-semibold text-gray-600">Check-out</label>
                    <button
                      id="end_date"
                      type="button"
                      :aria-expanded="activeDateField === 'end'"
                      @click="openDatePicker('end')"
                      :class="[
                        'flex w-full items-center justify-between rounded-xl border px-3.5 py-3.5 text-left text-sm transition focus:outline-none focus:ring-2 focus:ring-[#f29200]/20',
                        activeDateField === 'end'
                          ? 'border-[#f29200] bg-[#f29200]/5 text-[#23394e]'
                          : 'border-gray-200 text-[#23394e] hover:border-[#f29200]/60'
                      ]"
                    >
                      <span :class="bookingDates.end ? 'font-medium' : 'text-[#9f9f9f]'">
                        {{ bookingDates.end ? formatBookingDate(bookingDates.end) : 'Select date' }}
                      </span>
                      <Calendar class="h-4 w-4 shrink-0 text-[#f29200]" />
                    </button>
                  </div>
                </div>

                <div
                  v-if="activeDateField"
                  class="rounded-2xl border border-gray-200 bg-white p-3 shadow-sm"
                >
                  <div class="mb-3 flex items-center justify-between gap-3">
                    <div>
                      <p class="text-sm font-bold text-[#23394e]">{{ calendarMonthLabel }}</p>
                      <p class="text-[11px] font-medium text-[#9f9f9f]">
                        Select {{ activeDateField === 'start' ? 'check-in' : 'check-out' }} date
                      </p>
                    </div>

                    <div class="flex items-center gap-1">
                      <button
                        type="button"
                        title="Previous month"
                        aria-label="Previous month"
                        @click="changeCalendarMonth(-1)"
                        class="flex h-8 w-8 items-center justify-center rounded-lg text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200] focus:outline-none focus:ring-2 focus:ring-[#f29200]/20"
                      >
                        <ChevronLeft class="h-4 w-4" />
                      </button>
                      <button
                        type="button"
                        title="Next month"
                        aria-label="Next month"
                        @click="changeCalendarMonth(1)"
                        class="flex h-8 w-8 items-center justify-center rounded-lg text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200] focus:outline-none focus:ring-2 focus:ring-[#f29200]/20"
                      >
                        <ChevronRight class="h-4 w-4" />
                      </button>
                    </div>
                  </div>

                  <div class="grid grid-cols-7 gap-1 text-center">
                    <span
                      v-for="weekday in calendarWeekdays"
                      :key="weekday"
                      class="py-1 text-[10px] font-bold uppercase text-[#9f9f9f]"
                    >
                      {{ weekday }}
                    </span>

                    <template v-for="(day, index) in calendarDays" :key="day ? day.key : `empty-${index}`">
                      <span v-if="!day" aria-hidden="true" class="h-8 w-full" />
                      <button
                        v-else
                        type="button"
                        :disabled="isCalendarDateDisabled(day)"
                        :aria-pressed="isCalendarDateSelected(day)"
                        :aria-label="formatBookingDate(day.key)"
                        @click="selectCalendarDate(day)"
                        :class="calendarDayClasses(day)"
                      >
                        {{ day.day }}
                      </button>
                    </template>
                  </div>

                  <div class="mt-3 flex flex-wrap items-center gap-x-3 gap-y-1.5 border-t border-gray-100 pt-3 text-[10px] font-medium text-[#9f9f9f]">
                    <span class="flex items-center gap-1.5">
                      <i class="h-2.5 w-2.5 rounded-full border border-gray-300 bg-white" />
                      Available
                    </span>
                    <span class="flex items-center gap-1.5">
                      <i class="h-2.5 w-2.5 rounded-full bg-[#f29200]" />
                      Selected
                    </span>
                    <span class="flex items-center gap-1.5">
                      <i class="h-2.5 w-2.5 rounded-full bg-red-200" />
                      Reserved
                    </span>
                  </div>
                </div>

                <div v-if="bookingError" class="rounded-xl bg-red-50 p-3.5 text-xs text-red-600 border border-red-100">
                  {{ bookingError }}
                </div>

                <div v-if="estimatedPrice > 0" class="space-y-4 rounded-2xl border border-[#f29200]/10 bg-[#f29200]/5 p-4 text-xs">
                  <div class="flex justify-between font-semibold text-gray-700">
                    <span>Duration</span>
                    <span>{{ durationDays }} {{ durationDays === 1 ? 'day' : 'days' }}</span>
                  </div>
                  <div class="flex justify-between font-semibold text-gray-700">
                    <span>Base rate</span>
                    <span>{{ office.price }} DH &times; {{ durationDays }} {{ durationDays === 1 ? 'day' : 'days' }}</span>
                  </div>
                  <hr class="border-dashed border-[#f29200]/20" />
                  <div class="flex justify-between text-sm font-bold text-gray-950">
                    <span>Total price</span>
                    <span class="text-lg text-[#f29200]">{{ estimatedPrice }} DH</span>
                  </div>
                </div>

                <button
                  type="submit"
                  :disabled="!office.available || bookingSubmitLoading || !bookingDates.start || !bookingDates.end"
                  class="flex w-full items-center justify-center rounded-xl bg-[#f29200] px-4 py-4 text-sm font-bold text-white shadow-lg shadow-[#f29200]/15 transition-all hover:bg-[#d97706] disabled:cursor-not-allowed disabled:opacity-50"
                >
                  <template v-if="bookingSubmitLoading">Processing...</template>
                  <template v-else-if="!office.available">Space Booked</template>
                  <template v-else>Book Workspace</template>
                </button>

                <p class="flex items-center justify-center gap-1.5 text-[11px] font-medium text-gray-400">
                  <ShieldCheck class="h-3.5 w-3.5" />
                  Secure booking &middot; No hidden fees
                </p>

              </form>
            </div>

            <div class="grid grid-cols-3 gap-2 rounded-2xl border border-gray-100 bg-white p-4 shadow-lg shadow-gray-200/50">
              <div class="flex flex-col items-center gap-1.5 text-center">
                <CheckCircle2 class="h-4 w-4 text-emerald-500" />
                <span class="text-[10px] font-semibold text-gray-600 leading-tight">Instant<br />Confirmation</span>
              </div>
              <div class="flex flex-col items-center gap-1.5 text-center">
                <CreditCard class="h-4 w-4 text-emerald-500" />
                <span class="text-[10px] font-semibold text-gray-600 leading-tight">Secure<br />Payment</span>
              </div>
              <div class="flex flex-col items-center gap-1.5 text-center">
                <CheckCircle2 class="h-4 w-4 text-emerald-500" />
                <span class="text-[10px] font-semibold text-gray-600 leading-tight">Best Price<br />Guaranteed</span>
              </div>
            </div>

          </div>
        </div>

      </div>


<!-- ======================================================
     CASH PAYMENT
======================================================= -->

<div
  v-if="showCashModal"
  class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm"
>
  <div
    class="w-full max-w-md rounded-2xl border border-gray-100 bg-white p-6 shadow-2xl"
  >

    <!-- Header -->

    <div class="flex items-start justify-between gap-4">

      <div class="flex items-center gap-3">

        <div
          class="flex h-11 w-11 items-center justify-center rounded-xl bg-[#f29200]/10"
        >
          <Banknote class="h-5 w-5 text-[#f29200]" />
        </div>

        <div>
          <h3 class="text-lg font-bold text-[#23394e]">
            Cash Payment
          </h3>

          <p class="mt-0.5 text-xs text-[#9f9f9f]">
            Pay when you arrive at the workspace.
          </p>
        </div>

      </div>

      <button
        type="button"
        @click="closeCashModal"
        class="rounded-lg p-2 text-[#9f9f9f] transition hover:bg-gray-100"
      >
        <X class="h-4 w-4" />
      </button>

    </div>


    <!-- Amount -->

    <div
      class="mt-5 flex items-center justify-between rounded-xl border border-[#f29200]/20 bg-[#f29200]/5 p-4"
    >

      <div>
        <p class="text-xs text-[#9f9f9f]">
          Amount due
        </p>

        <p class="mt-1 text-sm font-semibold text-[#23394e]">
          {{ office.title }}
        </p>
      </div>

      <p class="text-xl font-black text-[#f29200]">
        {{ estimatedPrice }} DH
      </p>

    </div>


    <!-- Contact Form -->

    <div class="mt-5 space-y-4">

      <div>

        <label
          class="mb-1 block text-[11px] font-bold uppercase tracking-wider text-[#9f9f9f]"
        >
          Full Name
        </label>

        <input
          v-model.trim="cashForm.full_name"
          type="text"
          placeholder="Your full name"
          class="block w-full rounded-xl border border-gray-200 px-3.5 py-3 text-sm text-[#23394e] outline-none transition focus:border-[#f29200]"
        />

        <p
          v-if="cashErrors.full_name"
          class="mt-1 text-xs text-red-500"
        >
          {{ cashErrors.full_name }}
        </p>

      </div>


      <div>

        <label
          class="mb-1 block text-[11px] font-bold uppercase tracking-wider text-[#9f9f9f]"
        >
          Phone Number
        </label>

<VueTelInput
  v-model="cashForm.phone"
  mode="international"
  :auto-format="true"
  :valid-characters-only="true"
  :preferred-countries="['MA', 'FR', 'ES', 'US', 'GB']"
  :dropdown-options="{
    showDialCodeInList: true,
    showFlags: true,
    showSearchBox: true
  }"
  :input-options="{
    placeholder: 'Phone Number',
    autocomplete: 'tel',
    maxlength: 16
  }"
  @validate="handleCashPhoneValidation"
  :class="[
    'cash-phone-input',
    cashErrors.phone ? 'phone-error' : ''
  ]"
/>

<p
  v-if="cashErrors.phone"
  class="mt-1 text-xs text-red-500"
>
  {{ cashErrors.phone }}
</p>



      </div>


      <div>

        <label
          class="mb-1 block text-[11px] font-bold uppercase tracking-wider text-[#9f9f9f]"
        >
          Note
        </label>

        <textarea
          v-model.trim="cashForm.note"
          rows="2"
          maxlength="250"
          placeholder="Optional message..."
          class="block w-full resize-none rounded-xl border border-gray-200 px-3.5 py-3 text-sm text-[#23394e] outline-none transition focus:border-[#f29200]"
        ></textarea>

      </div>

    </div>


    <!-- Support Information -->

<div class="mt-3 space-y-2">

  <a
    v-if="whatsappNumber"
    :href="cashWhatsAppUrl"
    target="_blank"
    rel="noopener noreferrer"
    class="flex items-center justify-between rounded-lg bg-white px-3 py-2.5 text-xs font-semibold text-[#23394e] transition hover:text-[#f29200]"
  >
    <span class="flex items-center gap-2">
      <MessageCircle class="h-4 w-4 text-emerald-500" />
      Contact us on WhatsApp
    </span>

    <ExternalLink class="h-3.5 w-3.5" />
  </a>

  <a
    :href="websiteUrl"
    target="_blank"
    rel="noopener noreferrer"
    class="flex items-center justify-between rounded-lg bg-white px-3 py-2.5 text-xs font-semibold text-[#23394e] transition hover:text-[#f29200]"
  >
    <span class="flex items-center gap-2">
      <Globe2 class="h-4 w-4 text-[#f29200]" />
      {{ websiteName }} Website
    </span>

    <ExternalLink class="h-3.5 w-3.5" />
  </a>

</div>
    <div
      v-if="paymentError"
      class="mt-4 rounded-xl border border-red-100 bg-red-50 p-3 text-xs text-red-600"
    >
      {{ paymentError }}
    </div>


    <!-- Buttons -->

    <div class="mt-5 flex gap-3">

      <button
        type="button"
        @click="closeCashModal"
        :disabled="paymentLoading"
        class="h-11 flex-1 rounded-xl border border-gray-200 text-sm font-semibold text-[#23394e] transition hover:bg-gray-50"
      >
        cancel
      </button>

      <button
        type="button"
        @click="confirmCashPayment"
        :disabled="paymentLoading"
        class="flex h-11 flex-1 items-center justify-center gap-2 rounded-xl bg-[#f29200] text-sm font-bold text-white transition hover:bg-[#d97706] disabled:opacity-50"
      >

        <Loader2
          v-if="paymentLoading"
          class="h-4 w-4 animate-spin"
        />

        {{
          paymentLoading
            ? 'Confirming...'
            : 'Confirm Cash'
        }}

      </button>

    </div>

  </div>
</div>
    </template>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted} from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useFavoriteStore } from '@/stores/favoriteStore'
import api from '@/services/api'
import { toast } from 'vue-sonner'
import { VueTelInput } from "vue-tel-input"
import "vue-tel-input/vue-tel-input.css"
import {
  Building,
  MapPin,
  Star,
  Wifi,
  Car,
  Users,
  Wind,
  UserCircle,
  ArrowLeft,
  ArrowRight,
  ShieldCheck,
  Flame,
  Volume2,
  Heart,
  Share2,
  Pencil,
  Calendar,
  CheckCircle2,
  CreditCard,
  Loader2,
  Check,
  Banknote,
  ChevronRight,
  X,
  MessageCircle,
   Globe2,
   Mail,
   ExternalLink,
  
} from 'lucide-vue-next'
import { useSiteSettingsStore } from '@/stores/siteSettings'
/* ==========================================================
   Router & Store
========================================================== */

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const favoriteStore = useFavoriteStore()
const siteSettingsStore = useSiteSettingsStore()
/* ==========================================================
   General States
========================================================== */

const loading = ref(true)

const office = ref(null)

const reviews = ref([])
const favoriteLoading = ref(false)
const linkCopied = ref(false);
const cashPhoneData = ref(null)

const handleCashPhoneValidation = (data) => {
  cashPhoneData.value = data

  if (!cashForm.phone) {
    cashErrors.phone = ""
    return
  }

  cashErrors.phone = data.valid
    ? ""
    : "Enter a valid phone number."
}


const isFavorite = computed(() => {

  if (!office.value) {
    return false
  }

  return favoriteStore.isFavorite(
    office.value.id
  )
})

/* ==========================================================
   Image Gallery
========================================================== */

const activeIndex = ref(0)

const activeImage = computed(() => {

  if (
    office.value?.images &&
    office.value.images.length > 0
  ) {

    return getAbsoluteImageUrl(
      office.value.images[activeIndex.value].image
    )

  }

  return 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="%23cccccc" stroke-width="1.5"><rect x="2" y="2" width="20" height="20" rx="2"/><line x1="6" y1="6" x2="18" y2="6"/><line x1="6" y1="12" x2="18" y2="12"/><line x1="6" y1="18" x2="18" y2="18"/></svg>'

})

/* ==========================================================
   Amenities
========================================================== */

const amenitiesList = computed(() => {

  if (!office.value) return []

  return [

    {
      label: 'Free High-speed Wifi',
      icon: Wifi,
      active: office.value.wifi
    },

    {
      label: 'Dedicated Parking Slot',
      icon: Car,
      active: office.value.parking
    },

    {
      label: 'Meeting Rooms Equipped',
      icon: Users,
      active: office.value.meeting_room
    },

    {
      label: 'Air Conditioning System',
      icon: Wind,
      active: office.value.air_conditioning
    }

  ]

})

/* ==========================================================
   Review States
========================================================== */

const showReviewForm = ref(false)

const submitReviewLoading = ref(false)

const newReview = reactive({

  rating: 5,

  comment: ''

})

/* ==========================================================
   Booking States
========================================================== */

const todayStr = new Date().toISOString().split('T')[0]

const bookingDates = reactive({

  start: '',

  end: ''

})

const reservedDateRanges = ref([])

const activeDateField = ref(null)

const calendarMonth = ref(new Date(
  new Date().getFullYear(),
  new Date().getMonth(),
  1
))

const calendarWeekdays = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

const createDateFromKey = (dateKey) => {
  const [year, month, day] = dateKey.split('-').map(Number)

  return new Date(year, month - 1, day)
}

const getDateKey = (date) => {
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')

  return `${year}-${month}-${day}`
}

const calendarMonthLabel = computed(() =>
  calendarMonth.value.toLocaleDateString(undefined, {
    month: 'long',
    year: 'numeric'
  })
)

const calendarDays = computed(() => {
  const year = calendarMonth.value.getFullYear()
  const month = calendarMonth.value.getMonth()
  const firstWeekday = new Date(year, month, 1).getDay()
  const daysInMonth = new Date(year, month + 1, 0).getDate()
  const leadingDays = Array.from({ length: firstWeekday }, () => null)
  const monthDays = Array.from({ length: daysInMonth }, (_, index) => {
    const date = new Date(year, month, index + 1)

    return {
      date,
      day: index + 1,
      key: getDateKey(date)
    }
  })

  return [...leadingDays, ...monthDays]
})

const formatBookingDate = (dateKey) =>
  createDateFromKey(dateKey).toLocaleDateString(undefined, {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })

const isReservedDate = (dateKey) =>
  reservedDateRanges.value.some(range =>
    range.start_date &&
    range.end_date &&
    dateKey >= range.start_date &&
    dateKey <= range.end_date
  )

const hasReservedDateInRange = (startDate, endDate) =>
  reservedDateRanges.value.some(range =>
    range.start_date &&
    range.end_date &&
    range.start_date <= endDate &&
    range.end_date >= startDate
  )

const isCalendarDateSelected = (day) =>
  day.key === bookingDates.start || day.key === bookingDates.end

const isCalendarDateInSelectedRange = (day) =>
  bookingDates.start &&
  bookingDates.end &&
  day.key > bookingDates.start &&
  day.key < bookingDates.end

const isCalendarDateDisabled = (day) => {
  if (!day || day.key < todayStr || isReservedDate(day.key)) {
    return true
  }

  if (activeDateField.value === 'end' && bookingDates.start) {
    return (
      day.key < bookingDates.start ||
      hasReservedDateInRange(bookingDates.start, day.key)
    )
  }

  return false
}

const calendarDayClasses = (day) => {
  const baseClasses = 'flex h-8 w-full items-center justify-center rounded-lg text-xs font-semibold transition focus:outline-none focus:ring-2 focus:ring-[#f29200]/20'

  if (isCalendarDateSelected(day)) {
    return `${baseClasses} bg-[#f29200] text-white shadow-sm`
  }

  if (isReservedDate(day.key)) {
    return `${baseClasses} cursor-not-allowed bg-red-50 text-red-300 line-through`
  }

  if (isCalendarDateDisabled(day)) {
    return `${baseClasses} cursor-not-allowed text-gray-300`
  }

  if (isCalendarDateInSelectedRange(day)) {
    return `${baseClasses} bg-[#f29200]/10 text-[#f29200]`
  }

  return `${baseClasses} text-[#23394e] hover:bg-[#f29200]/10 hover:text-[#f29200]`
}

const openDatePicker = (field) => {
  activeDateField.value = activeDateField.value === field ? null : field

  if (!activeDateField.value) {
    return
  }

  const selectedDate = bookingDates[field] || todayStr
  const date = createDateFromKey(selectedDate)

  calendarMonth.value = new Date(date.getFullYear(), date.getMonth(), 1)
}

const changeCalendarMonth = (monthOffset) => {
  calendarMonth.value = new Date(
    calendarMonth.value.getFullYear(),
    calendarMonth.value.getMonth() + monthOffset,
    1
  )
}

const selectCalendarDate = (day) => {
  if (isCalendarDateDisabled(day)) {
    return
  }

  if (activeDateField.value === 'start') {
    bookingDates.start = day.key

    if (
      bookingDates.end &&
      (
        bookingDates.end < day.key ||
        hasReservedDateInRange(day.key, bookingDates.end)
      )
    ) {
      bookingDates.end = ''
    }

    activeDateField.value = 'end'
  }

  else if (activeDateField.value === 'end') {
    bookingDates.end = day.key
    activeDateField.value = null
  }

  calculatePrice()
}

const durationDays = ref(0)

const estimatedPrice = ref(0)

const bookingSubmitLoading = ref(false)

const bookingError = ref('')

/* ==========================================================
   Payment States
========================================================== */
const showCashModal = ref(false)

const createdBookingId = ref(null)

const paymentLoading = ref(false)

const paymentError = ref('')



const cashForm = reactive({
  full_name: '',
  phone: '',
  note: ''
})

const cashErrors = reactive({
  full_name: '',
  phone: ''
})

const closeCashModal = () => {
  showCashModal.value = false
  paymentError.value = ''

  cashErrors.full_name = ''
  cashErrors.phone = ''
  cashPhoneData.value = null
}


const websiteName = computed(() =>
  siteSettingsStore.settings.website_name || 'WorkSpace'
)

const websiteUrl = computed(() =>
  siteSettingsStore.settings.website_url ||
  window.location.origin
)

const whatsappNumber = computed(() =>
  (
    siteSettingsStore.settings.whatsapp_number || ''
  ).replace(/[^\d]/g, '')
)

///watsap///
const cashWhatsAppUrl = computed(() => {
  if (!whatsappNumber.value) {
    return '#'
  }

  const message = `
Hello ${websiteName.value},

I want to confirm a cash booking.

Workspace: ${office.value?.title || ''}
Booking ID: ${createdBookingId.value || ''}
Amount: ${estimatedPrice.value} MAD

Name: ${cashForm.full_name}
Phone: ${cashForm.phone}
Note: ${cashForm.note || 'No note'}
  `.trim()

  return `https://wa.me/${whatsappNumber.value}?text=${encodeURIComponent(message)}`
})


//cash payment confirmation//

const confirmCashPayment = async () => {

  cashErrors.full_name = ''
  cashErrors.phone = ''

  let valid = true


  if (cashForm.full_name.trim().length < 3) {

    cashErrors.full_name =
      'Please enter your full name.'

    valid = false
  }


if (!cashForm.phone) {
  cashErrors.phone =
    "Phone number is required."

  valid = false

} else if (!cashPhoneData.value?.valid) {
  cashErrors.phone =
    "Enter a valid phone number."

  valid = false
}


  if (!valid) {
    return
  }

const normalizedCashPhone =
  (
    cashPhoneData.value?.number ||
    cashForm.phone
  )
    .replace(/[^\d+]/g, "")
    .replace(/(?!^)\+/g, "")


  paymentLoading.value = true
  paymentError.value = ''


  try {

    await api.post(
      `payments/${createdBookingId.value}/cash/`,
      {
        full_name: cashForm.full_name,
        phone: normalizedCashPhone,
        note: cashForm.note
      }
    )
    toast.success('Cash payment request sent successfully.', {
  description: 'Your booking is waiting for admin confirmation.'
})


    showCashModal.value = false


    router.push({
      name: 'dashboard',
      query: {
        booking_success: 'true',
        payment_method: 'cash',
        contact_sent: 'true'
      }
    })


  } catch (error) {

    const errors =
      error.response?.data || {}


    if (errors.full_name) {

      cashErrors.full_name =
        Array.isArray(errors.full_name)
          ? errors.full_name[0]
          : errors.full_name
    }


    if (errors.phone) {

      cashErrors.phone =
        Array.isArray(errors.phone)
          ? errors.phone[0]
          : errors.phone
    }


    paymentError.value =
      errors.error ||
      'Unable to submit cash payment request.'


  } finally {

    paymentLoading.value = false
  }


}



/* ==========================================================
   Helpers
========================================================== */

const getAbsoluteImageUrl = (url) => {

  return url.startsWith('http')

    ? url

    : `http://127.0.0.1:8000${url}`

}

const formatDate = (dateStr) => {

  if (!dateStr) return ''

  return new Date(dateStr).toLocaleDateString(
    undefined,
    {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    }
  )

}



const toggleFavorite = async () => {

  if (!office.value) {
    return
  }

  if (!authStore.isAuthenticated) {

    router.push({
      name: 'login',
      query: {
        redirect: route.fullPath
      }
    })

    return
  }

  favoriteLoading.value = true

  try {

    await favoriteStore.toggleFavorite(
      office.value.id
    )

  } catch (error) {

    console.error(
      'Failed to update favorite',
      error
    )

  } finally {

    favoriteLoading.value = false

  }
}


/// share///
const shareOffice = async () => {

  if (!office.value) {
    return;
  }

  const shareData = {
    title: office.value.title,

    text:
  `Check out ${office.value.title} in ${office.value.city} on ${websiteName.value}.`,

    url: window.location.href
  };


  try {

    // Mobile / supported browsers
    if (navigator.share) {

      await navigator.share(
        shareData
      );

      return;
    }


    // Desktop fallback
    await navigator.clipboard.writeText(
      window.location.href
    );
   
    showCopiedMessage();

  } catch (error) {

    // User closed native share dialog
    if (
      error?.name === "AbortError"
    ) {
      return;
    }

    // Clipboard fallback
    try {

      await navigator.clipboard.writeText(
        window.location.href
      );

      showCopiedMessage();

    } catch (clipboardError) {

      console.error(
        "Unable to share office",
        clipboardError
      );
    }

  }
};

let copiedTimer = null;

const showCopiedMessage = () => {

  linkCopied.value = true;

  if (copiedTimer) {
    clearTimeout(copiedTimer);
  }

  copiedTimer = setTimeout(() => {

    linkCopied.value = false;

  }, 2000);
};


///////=========///////////////

const resumePendingPayment = () => {

  const shouldResume =
    route.query.resume_payment === 'true'

  const bookingId =
    Number(route.query.booking_id)


  if (
    !shouldResume ||
    !Number.isInteger(bookingId) ||
    bookingId <= 0
  ) {
    return
  }


  createdBookingId.value = bookingId
  paymentError.value = ''
  showCashModal.value = true
}
/* ==========================================================
   Fetch Office Details
========================================================== */

const fetchOfficeDetail = async () => {

  loading.value = true

  try {

    const id = route.params.id

    const officeResponse = await api.get(`offices/${id}/`)

    office.value = officeResponse.data

    try {
      const reservedDatesResponse = await api.get(
        `bookings/office/${id}/reserved-dates/`
      )

      const reservedDates = reservedDatesResponse.data

      reservedDateRanges.value = Array.isArray(reservedDates)
        ? reservedDates
        : reservedDates?.results ?? []
    }

    catch (error) {
      reservedDateRanges.value = []

      console.error(
        'Failed to load reserved office dates',
        error
      )
    }

    const reviewResponse = await api.get(
      `reviews/office/${id}/`
    )

    const data = reviewResponse.data

    reviews.value = Array.isArray(data)

      ? data

      : data?.results ?? []

  }

  catch (error) {

    console.error(
      'Failed to load office details',
      error
    )

  }

  finally {

    loading.value = false

  }

}

/* ==========================================================
   Submit Review
========================================================== */

const submitReview = async () => {

  submitReviewLoading.value = true

  try {

    const response = await api.post(

      'reviews/create/',

      {

        office: office.value.id,

        rating: newReview.rating,

        comment: newReview.comment

      }

    )

    reviews.value.unshift({

      ...response.data,

      user_username: authStore.user?.username

    })

    newReview.rating = 5

    newReview.comment = ''

    showReviewForm.value = false

  }

  catch (error) {

    console.error(
      'Failed to submit review',
      error
    )

  }

  finally {

    submitReviewLoading.value = false

  }

}

/* ==========================================================
   Calculate Booking Price
========================================================== */

const calculatePrice = () => {

  if (

    !bookingDates.start ||

    !bookingDates.end

  ) {

    durationDays.value = 0

    estimatedPrice.value = 0

    return

  }

  const start = new Date(bookingDates.start)

  const end = new Date(bookingDates.end)

  if (end < start) {

    durationDays.value = 0

    estimatedPrice.value = 0

    return

  }

  const duration =

    Math.ceil(

      Math.abs(end - start)

      / 86400000

    ) + 1

  durationDays.value = duration

  const price = Number(office.value.price)

  switch (office.value.rent_type) {

    case 'daily':

      estimatedPrice.value =

        price * duration

      break

    case 'weekly':

      estimatedPrice.value =

        Number(

          (

            price *

            Math.max(1, duration / 7)

          ).toFixed(2)

        )

      break

    default:

      estimatedPrice.value =

        Number(

          (

            price *

            Math.max(1, duration / 30)

          ).toFixed(2)

        )

  }

}

/* ==========================================================
   Create Booking
========================================================== */

const handleBookingSubmit = async () => {

  if (!authStore.isAuthenticated) {

    router.push({

      name: 'login',

      query: {

        redirect: route.fullPath

      }

    })

    return

  }

  bookingError.value = ''

  bookingSubmitLoading.value = true

  try {

    const response = await api.post(

      'bookings/create/',

      {

        office: office.value.id,

        start_date: bookingDates.start,

        end_date: bookingDates.end

      }

    )

    createdBookingId.value = response.data.id

    paymentError.value = ''
    showCashModal.value = true
  }

  catch (error) {

    const details = error.response?.data

    if (

      typeof details === 'object' &&

      details.non_field_errors

    ) {

      bookingError.value =

        details.non_field_errors.join(', ')

    }

    else if (typeof details === 'object') {

      bookingError.value =

        Object.entries(details)

          .map(

            ([key, value]) =>

              `${key}: ${value}`

          )

          .join(' ')

    }

    else {

      bookingError.value =

        error.response?.data?.error ||

        'Unable to create booking.'

    }

  }

  finally {

    bookingSubmitLoading.value = false

  }

}

/* ==========================================================
   Initial Load
========================================================== */

onMounted(async () => {

  siteSettingsStore.fetchSettings().catch(() => {})


  await fetchOfficeDetail()

  if (authStore.isAuthenticated) {
    await favoriteStore.fetchFavorites()
  }

  resumePendingPayment()
})
</script>

<style>
.cash-phone-input {
  border: 1px solid #e5e7eb !important;
  border-radius: 0.75rem !important;
  min-height: 48px;
  background: white;
  transition: 0.2s;
}

.cash-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow: 0 0 0 3px rgba(242, 146, 0, 0.1);
}

.cash-phone-input.phone-error {
  border-color: #ef4444 !important;
}

.cash-phone-input .vti__input {
  font-size: 14px;
  color: #23394e;
  background: transparent;
}

.cash-phone-input .vti__dropdown {
  border-radius: 0.75rem 0 0 0.75rem;
}</style>