<script setup>
import { ref, computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth"
import api from "@/services/api"
import { VueTelInput } from "vue-tel-input"
import "vue-tel-input/vue-tel-input.css"
import { useSiteSettingsStore } from "@/stores/siteSettings"
import {
  Search,
  Building2,
  Calendar,
  CalendarDays,
  ChevronLeft,
  ChevronRight,
  CircleCheckBig,
  ArrowRight,
  ArrowLeft,
  MessageCircle,
  Globe2,
  ExternalLink
} from "lucide-vue-next"

const router = useRouter()
const authStore = useAuthStore()
const siteSettingsStore = useSiteSettingsStore()
// Current Wizard Step
const currentStep = ref(1)

// Search
const searchQuery = ref("")
const offices = ref([])

// Selected Office
const selectedOffice = ref(null)

// Booking Dates
const booking = ref({
  start_date: "",
  end_date: ""
})

const contactForm = ref({
  full_name: "",
  phone: "",
  note: ""
})

const contactErrors = ref({
  full_name: "",
  phone: ""
})

const phoneData = ref(null)

const handlePhoneValidation = (data) => {
  phoneData.value = data

  if (!contactForm.value.phone) {
    contactErrors.value.phone = ""
    return
  }

  contactErrors.value.phone = data.valid
    ? ""
    : "Enter a valid phone number."
}

const reservedDateRanges = ref([])
const activeDateField = ref(null)
const todayStr = new Date().toISOString().split("T")[0]
const calendarMonth = ref(new Date(
  new Date().getFullYear(),
  new Date().getMonth(),
  1
))
const calendarWeekdays = [
  "Su",
  "Mo",
  "Tu",
  "We",
  "Th",
  "Fr",
  "Sa"
]

const createDateFromKey = (dateKey) => {
  const [year, month, day] = dateKey.split("-").map(Number)

  return new Date(year, month - 1, day)
}

const getDateKey = (date) => {
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, "0")
  const day = String(date.getDate()).padStart(2, "0")

  return `${year}-${month}-${day}`
}

const calendarMonthLabel = computed(() =>
  calendarMonth.value.toLocaleDateString(undefined, {
    month: "long",
    year: "numeric"
  })
)

const calendarDays = computed(() => {
  const year = calendarMonth.value.getFullYear()
  const month = calendarMonth.value.getMonth()
  const firstWeekday = new Date(year, month, 1).getDay()
  const daysInMonth = new Date(year, month + 1, 0).getDate()
  const leadingDays = Array.from(
    { length: firstWeekday },
    () => null
  )
  const monthDays = Array.from(
    { length: daysInMonth },
    (_, index) => {
      const date = new Date(year, month, index + 1)

      return {
        date,
        day: index + 1,
        key: getDateKey(date)
      }
    }
  )

  return [...leadingDays, ...monthDays]
})

const formatBookingDate = (dateKey) =>
  createDateFromKey(dateKey).toLocaleDateString(undefined, {
    month: "short",
    day: "numeric",
    year: "numeric"
  })

const isReservedDate = (dateKey) =>
  reservedDateRanges.value.some((range) =>
    range.start_date &&
    range.end_date &&
    dateKey >= range.start_date &&
    dateKey <= range.end_date
  )

const hasReservedDateInRange = (startDate, endDate) =>
  reservedDateRanges.value.some((range) =>
    range.start_date &&
    range.end_date &&
    range.start_date <= endDate &&
    range.end_date >= startDate
  )

const isCalendarDateSelected = (day) =>
  day.key === booking.value.start_date ||
  day.key === booking.value.end_date

const isCalendarDateInSelectedRange = (day) =>
  booking.value.start_date &&
  booking.value.end_date &&
  day.key > booking.value.start_date &&
  day.key < booking.value.end_date

const isCalendarDateDisabled = (day) => {
  if (!day || day.key < todayStr || isReservedDate(day.key)) {
    return true
  }

  if (activeDateField.value === "end" && booking.value.start_date) {
    return (
      day.key < booking.value.start_date ||
      hasReservedDateInRange(
        booking.value.start_date,
        day.key
      )
    )
  }

  return false
}

const calendarDayClasses = (day) => {
  const baseClasses = "flex h-8 w-full items-center justify-center rounded-lg text-xs font-semibold transition focus:outline-none focus:ring-2 focus:ring-[#f29200]/20"

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
  activeDateField.value =
    activeDateField.value === field
      ? null
      : field

  if (!activeDateField.value) {
    return
  }

  const selectedDate =
    booking.value[
      activeDateField.value === "start"
        ? "start_date"
        : "end_date"
    ] || todayStr
  const date = createDateFromKey(selectedDate)

  calendarMonth.value = new Date(
    date.getFullYear(),
    date.getMonth(),
    1
  )
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

  if (activeDateField.value === "start") {
    booking.value.start_date = day.key

    if (
      booking.value.end_date &&
      (
        booking.value.end_date < day.key ||
        hasReservedDateInRange(
          day.key,
          booking.value.end_date
        )
      )
    ) {
      booking.value.end_date = ""
    }

    activeDateField.value = "end"
  }

  else if (activeDateField.value === "end") {
    booking.value.end_date = day.key
    activeDateField.value = null
  }
}

const loadReservedDates = async (office) => {
  if (!office?.id) {
    reservedDateRanges.value = []
    return
  }

  try {
    const response = await api.get(
      `bookings/office/${office.id}/reserved-dates/`
    )
    const reservedDates = response.data

    if (selectedOffice.value?.id !== office.id) {
      return
    }

    reservedDateRanges.value = Array.isArray(reservedDates)
      ? reservedDates
      : reservedDates?.results ?? []
  }

  catch (error) {
    reservedDateRanges.value = []

    console.error(
      "Failed to load reserved office dates",
      error
    )
  }
}

// Loading State
const loading = ref(false)
const bookingSuccess = ref(false)

// Error Message
const errorMessage = ref("")

// Progress Percentage
const progress = computed(() => {
  

  switch(currentStep.value){

    case 1:
      return 25

    case 2:
      return 50

    case 3:
      return 75

    case 4:
      return 100

    default:
      return 0
  }


})
// Search Offices From API

const searchOffices = async () => {

  loading.value = true
  errorMessage.value = ""

  try{

    const response = await api.get("offices/",{

      params:{
        search: searchQuery.value
      }

    })

    offices.value = response.data.results || response.data

    if(offices.value.length === 0){

      errorMessage.value =
      "No offices found. Try another search."

    }

  }

  catch(error){

    console.error(error)

    errorMessage.value =
    "Unable to load offices."

  }

  finally{

    loading.value = false

  }

}
const selectOffice = async (office) => {

  selectedOffice.value = office
  booking.value.start_date = ""
  booking.value.end_date = ""
  reservedDateRanges.value = []
  activeDateField.value = null
  calendarMonth.value = new Date(
    new Date().getFullYear(),
    new Date().getMonth(),
    1
  )

  await loadReservedDates(office)

  currentStep.value = 2

}
const officeImage = (office) => {

  if (office.images && office.images.length > 0) {

    const img = office.images[0].image

    return img.startsWith("http")
      ? img
      : `http://127.0.0.1:8000${img}`

  }

  return "https://placehold.co/600x400/F7F8FA/9CA3AF?text=Workspace"

  
}
const estimatedPrice = computed(() => {

  if (
    !selectedOffice.value ||
    !booking.value.start_date ||
    !booking.value.end_date
  ) {
    return 0
  }

  const start = new Date(booking.value.start_date)
  const end = new Date(booking.value.end_date)

  const days =
    Math.ceil((end - start) / (1000 * 60 * 60 * 24)) + 1

  if (days <= 0) return 0

  return days * Number(selectedOffice.value.price)

})
const goBack = () => {

  currentStep.value = 1

}
const bookingDuration = computed(() => {

  if (
    !booking.value.start_date ||
    !booking.value.end_date
  ) return 0

  const start = new Date(booking.value.start_date)
  const end = new Date(booking.value.end_date)

  return Math.ceil(
    (end - start) / (1000 * 60 * 60 * 24)
  ) + 1

})

const steps = [

  {
    number:1,
    title:"Search"
  },

  {
    number:2,
    title:"Workspace"
  },

  {
    number:3,
    title:"Contact"
  },

  {
    number:4,
    title:"Complete"
  }

]

const continueToSummary = () => {

  if (
    !booking.value.start_date ||
    !booking.value.end_date
  ) {

    errorMessage.value =
      "Please select booking dates."

    return

  }

  errorMessage.value = ""

  currentStep.value = 3

}

const validateContactForm = () => {
  contactErrors.value.full_name = ""
  contactErrors.value.phone = ""

  let valid = true

  if (contactForm.value.full_name.trim().length < 3) {
    contactErrors.value.full_name =
      "Please enter your full name."
    valid = false
  }

  if (!contactForm.value.phone) {
    contactErrors.value.phone =
      "Phone number is required."
    valid = false
  }
  else if (!phoneData.value?.valid) {
    contactErrors.value.phone =
      "Enter a valid phone number."
    valid = false
  }

  return valid
}

const websiteName = computed(() =>
  siteSettingsStore.settings.website_name || "WorkSpace"
)

const websiteUrl = computed(() =>
  siteSettingsStore.settings.website_url ||
  window.location.origin
)

const whatsappNumber = computed(() =>
  (
    siteSettingsStore.settings.whatsapp_number || ""
  ).replace(/[^\d]/g, "")
)

const cashWhatsAppUrl = computed(() => {

  if (!whatsappNumber.value) {
    return "#"
  }

  const message = `
Hello ${websiteName.value},

I need help with my cash booking request.

Workspace: ${selectedOffice.value?.title || ""}
Dates: ${booking.value.start_date || ""} to ${booking.value.end_date || ""}
Amount: ${estimatedPrice.value} MAD
  `.trim()

  return `https://wa.me/${whatsappNumber.value}?text=${encodeURIComponent(message)}`
})

const createBooking = async () => {

  if (!authStore.isAuthenticated) {

    router.push("/login")

    return

  }

  if (loading.value) {
    return
  }

  errorMessage.value = ""

  if (!validateContactForm()) {
    return
  }

  const normalizedPhone =
    (
      phoneData.value?.number ||
      contactForm.value.phone
    )
      .replace(/[^\d+]/g, "")
      .replace(/(?!^)\+/g, "")

  loading.value = true

  try {

    const bookingResponse = await api.post("bookings/create/", {

      office: selectedOffice.value.id,

      start_date: booking.value.start_date,

      end_date: booking.value.end_date

    })

    const bookingId = bookingResponse.data.id

    try {
      await api.post(
        `payments/${bookingId}/cash/`,
        {
          full_name: contactForm.value.full_name.trim(),
          phone: normalizedPhone,
          note: contactForm.value.note.trim()
        }
      )
    }
    catch (error) {
      const paymentErrors = error.response?.data || {}

      if (paymentErrors.full_name) {
        contactErrors.value.full_name = Array.isArray(
          paymentErrors.full_name
        )
          ? paymentErrors.full_name[0]
          : paymentErrors.full_name
      }

      if (paymentErrors.phone) {
        contactErrors.value.phone = Array.isArray(
          paymentErrors.phone
        )
          ? paymentErrors.phone[0]
          : paymentErrors.phone
      }

      if (!paymentErrors.full_name && !paymentErrors.phone) {
        errorMessage.value =
          paymentErrors.error ||
          "Unable to submit your cash booking request."
      }

      return
    }

    bookingSuccess.value = true

    currentStep.value = 4

  }

  catch (error) {

    console.error(error)

    if (error.response?.data) {

      const data = error.response.data

      if (typeof data === "string") {

        errorMessage.value = data

      }

      else if (data.detail) {

        errorMessage.value = data.detail

      }

      else if (data.non_field_errors) {

        errorMessage.value =
          data.non_field_errors[0]

      }

      else {

        errorMessage.value =
          JSON.stringify(data)

      }

    }

    else {

      errorMessage.value =
        "Unable to create booking."

    }

  }

  finally {

    loading.value = false

  }

}
const goToDashboard = () => {

  router.push("/dashboard")

}

const browseOffices = () => {

  router.push("/")

}
onMounted(() => {
  siteSettingsStore.fetchSettings().catch(() => {})
})


</script>
<template>

<main class="min-h-screen bg-[#F7F8FA]">

  <!-- Hero -->

  <section
    class="pt-12 pb-8 md:pt-16 md:pb-10">

    <div class="max-w-5xl mx-auto px-4 sm:px-6">

      <span
        class="inline-flex items-center gap-2
        bg-[#f29200]/10
        text-[#f29200]
        px-3 py-1.5
        rounded-full
        text-sm font-semibold">

        Booking Guide

      </span>

      <h1
        class="mt-5
        text-3xl md:text-4xl
        font-black
        text-[#23394e]
        leading-tight">

        Book Your Workspace

        <br>

        In Just A Few Steps

      </h1>

      <p
        class="mt-4
        max-w-xl
        text-base
        leading-7
        text-[#9f9f9f]">

        Experience the complete booking process using
        real data from our platform.

      </p>

    </div>

  </section>

 <!-- Progress Tracker -->

<section class="pb-12 md:pb-14">

  <div class="max-w-5xl mx-auto px-4 sm:px-6">

    <div
      class="bg-white
      rounded-2xl
      border
      border-[#E5E7EB]
      shadow-sm
      p-5 sm:p-6">

      <!-- Steps -->

      <div
        class="flex
        items-center
        justify-between">

        <template
          v-for="(step,index) in steps"
          :key="step.number">

          <!-- Circle -->

          <div
            class="flex
            flex-col
            items-center
            flex-1">

            <div

              class="w-10
              h-10
              rounded-full
              flex
              items-center
              justify-center
              text-sm font-bold
              transition-all
              duration-500"

              :class="

              currentStep>=step.number

              ?

              'bg-[#f29200] text-white scale-105'

              :

              'bg-[#F7F8FA] text-[#9f9f9f]'

              ">

              {{ step.number }}

            </div>

            <span
              class="mt-2
              text-xs sm:text-sm
              font-semibold
              text-center">

              {{ step.title }}

            </span>

          </div>

          <!-- Line -->

          <div

            v-if="index<steps.length-1"

            class="flex-1 h-1 rounded-full mx-2 sm:mx-3 transition-all duration-500"

            :class="

            currentStep>step.number

            ?

            'bg-[#f29200]'

            :

            'bg-[#E5E7EB]'

            ">

          </div>

        </template>

      </div>

    </div>

  </div>

</section>


  <!-- STEP 1 -->
<Transition
name="wizard"
mode="out-in">


<section class="pb-14 md:pb-16">

  <div class="max-w-5xl mx-auto px-4 sm:px-6">

    <Transition
      enter-active-class="transition duration-500"
      enter-from-class="opacity-0 translate-y-10"
      enter-to-class="opacity-100 translate-y-0">

      <div
        v-if="currentStep===1"
        class="bg-white rounded-2xl border border-[#E5E7EB] p-5 sm:p-7">

        <h2
          class="text-2xl font-black text-[#23394e] sm:text-3xl">

          Step 1

        </h2>

        <p
          class="mt-2 text-sm text-[#9f9f9f]">

          Search for a workspace.

        </p>

        <!-- Search -->

        <div
          class="mt-6 flex flex-col gap-3 sm:flex-row">

          <input

            v-model="searchQuery"

            @keyup.enter="searchOffices"

            type="text"

            placeholder="Search city or office..."

            class="flex-1
            border
            border-[#E5E7EB]
            rounded-xl
            h-11
            px-4
            py-3
            outline-none
            focus:border-[#f29200]"/>

          <button

            @click="searchOffices"

            class="bg-[#f29200]
            hover:bg-[#f29200]/90
            transition
            text-white
            rounded-xl
            px-5 py-2.5">

            Search

          </button>

        </div>

        <!-- Loading -->

        <div
          v-if="loading"
          class="mt-5 text-sm text-[#9f9f9f]">

          Loading offices...

        </div>

        <!-- Error -->

        <div
          v-if="errorMessage"
          class="mt-5
          bg-red-50
          text-red-600
          rounded-xl
          p-4">

          {{ errorMessage }}

        </div>
        <!-- Results -->

<div
  v-if="offices.length"
  class="grid lg:grid-cols-3 gap-5 mt-8">

  <div

    v-for="office in offices"

    :key="office.id"

    class="bg-[#F7F8FA]
    rounded-2xl
    overflow-hidden
    border
    border-[#E5E7EB]
    hover:shadow-xl
    hover:-translate-y-1
    transition
    duration-300">

    <!-- Image -->

    <img

      :src="officeImage(office)"

      class="h-44 w-full object-cover"/>

    <!-- Content -->

    <div class="p-5">

      <div
        class="flex justify-between items-start">

        <div>

          <h3
            class="text-lg
            font-bold
            text-[#23394e]">

            {{ office.title }}

          </h3>

          <p
            class="mt-1
            text-sm text-[#9f9f9f]">

            {{ office.city }}

          </p>

        </div>

        <span
          class="bg-[#f29200]/10
          text-[#f29200]
          px-3 py-1.5
          rounded-full
          text-sm
          font-semibold">

          {{ office.rent_type }}

        </span>

      </div>

      <!-- Price -->

      <div
        class="mt-5">

        <span
          class="text-2xl
          font-black
          text-[#23394e]">

          {{ office.price }}

        </span>

        <span
          class="text-sm text-[#9f9f9f]">

          MAD

        </span>

      </div>

      <!-- Button -->

      <button

        @click="selectOffice(office)"

        class="mt-5
        w-full
        bg-[#f29200]
        hover:bg-[#f29200]/90
        transition
        text-white
        rounded-xl
        py-2.5
        font-semibold">

        Select Workspace

      </button>

    </div>

  </div>

</div>


      </div>

    </Transition>

  </div>

</section>
       </Transition>



<Transition
name="wizard"
mode="out-in">
<!-- STEP 2 -->

<section
  v-if="currentStep===2"
  class="pb-14 md:pb-16">

  <div class="max-w-4xl mx-auto px-4 sm:px-6">

    <div
      class="bg-white
      rounded-2xl
      border
      border-[#E5E7EB]
      p-5 sm:p-7">

      <h2
        class="text-2xl sm:text-3xl
        font-black
        text-[#23394e]">

        Step 2

      </h2>

      <p
        class="mt-2
        text-sm text-[#9f9f9f]">

        Choose your booking dates.

      </p>

      <!-- Office -->

      <div
        class="mt-6
        flex
        gap-4
        items-center
        bg-[#F7F8FA]
        rounded-2xl
        p-4">

        <img

          :src="officeImage(selectedOffice)"

          class="w-28
          h-20
          rounded-xl
          object-cover"/>

        <div>

          <h3
            class="text-xl
            font-bold
            text-[#23394e]">

            {{ selectedOffice.title }}

          </h3>

          <p class="mt-1 text-sm text-[#9f9f9f]">

            {{ selectedOffice.city }}

          </p>

          <p
            class="mt-2
            text-[#f29200]
            font-bold">

            {{ selectedOffice.price }} MAD

          </p>

        </div>

      </div>

      <!-- Dates -->

      <div
        class="grid
        md:grid-cols-2
        gap-5
        mt-6">

        <div>

          <label
            class="text-sm font-semibold text-[#23394e]">

            Check-in

          </label>

          <button
            type="button"
            :aria-expanded="activeDateField === 'start'"
            @click="openDatePicker('start')"
            :class="[
              'mt-2 flex h-11 w-full items-center justify-between rounded-xl border px-4 text-left text-sm transition focus:outline-none focus:ring-2 focus:ring-[#f29200]/20',
              activeDateField === 'start'
                ? 'border-[#f29200] bg-[#f29200]/5 text-[#23394e]'
                : 'border-[#E5E7EB] text-[#23394e] hover:border-[#f29200]/60'
            ]"
          >
            <span :class="booking.start_date ? 'font-medium' : 'text-[#9f9f9f]'">
              {{ booking.start_date ? formatBookingDate(booking.start_date) : 'Select date' }}
            </span>
            <Calendar class="h-4 w-4 shrink-0 text-[#f29200]" />
          </button>

        </div>

        <div>

          <label
            class="text-sm font-semibold text-[#23394e]">

            Check-out

          </label>

          <button
            type="button"
            :aria-expanded="activeDateField === 'end'"
            @click="openDatePicker('end')"
            :class="[
              'mt-2 flex h-11 w-full items-center justify-between rounded-xl border px-4 text-left text-sm transition focus:outline-none focus:ring-2 focus:ring-[#f29200]/20',
              activeDateField === 'end'
                ? 'border-[#f29200] bg-[#f29200]/5 text-[#23394e]'
                : 'border-[#E5E7EB] text-[#23394e] hover:border-[#f29200]/60'
            ]"
          >
            <span :class="booking.end_date ? 'font-medium' : 'text-[#9f9f9f]'">
              {{ booking.end_date ? formatBookingDate(booking.end_date) : 'Select date' }}
            </span>
            <Calendar class="h-4 w-4 shrink-0 text-[#f29200]" />
          </button>

        </div>

      </div>

      <div
        v-if="activeDateField"
        class="mt-5 rounded-2xl border border-[#E5E7EB] bg-white p-3 shadow-sm"
      >
        <div class="mb-3 flex items-center justify-between gap-3">
          <div>
            <p class="text-sm font-bold text-[#23394e]">
              {{ calendarMonthLabel }}
            </p>

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

          <template
            v-for="(day, index) in calendarDays"
            :key="day ? day.key : `empty-${index}`"
          >
            <span
              v-if="!day"
              aria-hidden="true"
              class="h-8 w-full"
            />

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

        <div class="mt-3 flex flex-wrap items-center gap-x-3 gap-y-1.5 border-t border-[#E5E7EB] pt-3 text-[10px] font-medium text-[#9f9f9f]">
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

      <!-- Price -->

      <div
        class="mt-8
        bg-[#f29200]/10
        rounded-2xl
        p-5">

        <p
          class="text-sm text-[#9f9f9f]">

          Estimated Total

        </p>

        <h2
          class="mt-2
          text-3xl
          font-black
          text-[#f29200]">

          {{ estimatedPrice }}

          MAD

        </h2>

      </div>

      <!-- Buttons -->

      <div
        class="mt-7
        flex
        justify-between gap-3">

        <button

          @click="goBack"

          class="border
          border-[#E5E7EB]
          px-5
          py-2.5
          rounded-xl">

          ← Back

        </button>

        <button

          @click="continueToSummary"

          class="bg-[#f29200]
          hover:bg-[#f29200]/90
          transition
          text-white
          px-5
          py-2.5
          rounded-xl">

          Continue →

        </button>

      </div>

    </div>

  </div>

</section>
</Transition>

<Transition
name="wizard"
mode="out-in">
<!-- STEP 3 -->

<section
  v-if="currentStep===3"
  class="pb-14 md:pb-16">

  <div class="max-w-4xl mx-auto px-4 sm:px-6">

    <div
      class="bg-white
      rounded-2xl
      border
      border-[#E5E7EB]
      p-5 sm:p-7">

      <h2
        class="text-2xl sm:text-3xl
        font-black
        text-[#23394e]">

        Complete Your Booking

      </h2>

      <p
        class="mt-2
        text-sm text-[#9f9f9f]">

        Enter your contact information to submit your cash booking request.

      </p>

      <!-- Reservation Summary -->

      <div
        class="mt-6
        grid
        sm:grid-cols-2
        gap-3
        rounded-2xl
        border
        border-[#E5E7EB]
        bg-[#F7F8FA]
        p-4">

        <div>

          <p class="text-sm text-[#9f9f9f]">
            Workspace
          </p>

          <h3
            class="mt-1 truncate text-sm
            font-bold text-[#23394e]">

            {{ selectedOffice.title }}

          </h3>

        </div>

        <div>

          <p class="text-sm text-[#9f9f9f]">

            City

          </p>

          <h3
            class="mt-1 truncate text-sm
            font-bold text-[#23394e]">

            {{ selectedOffice.city }}

          </h3>

        </div>

        <div>

          <p class="text-sm text-[#9f9f9f]">

            Booking Dates

          </p>

          <h3
            class="mt-1 text-sm
            font-bold text-[#23394e]">

            {{ booking.start_date }}

            →

            {{ booking.end_date }}

          </h3>

        </div>

        <div>

          <p class="text-sm text-[#9f9f9f]">

            Duration

          </p>

          <h3
            class="mt-1 text-sm
            font-bold text-[#23394e]">

            {{ bookingDuration }}

            Days

          </h3>

        </div>

      </div>

      <!-- Amount -->

      <div
        class="mt-5 flex flex-col gap-3 rounded-2xl border border-[#f29200]/20 bg-[#f29200]/10 p-4 sm:flex-row sm:items-center sm:justify-between"
      >
        <div>
          <p class="text-xs font-semibold text-[#9f9f9f]">
            Amount due
          </p>

          <p class="mt-1 text-sm font-bold text-[#23394e]">
            {{ selectedOffice.title }}
          </p>
        </div>

        <p class="text-2xl font-black text-[#f29200]">
          {{ estimatedPrice }}
          <span class="text-sm font-bold">MAD</span>
        </p>
      </div>

      <!-- Contact Form -->

      <div class="mt-6 space-y-4">
        <div>
          <label
            class="mb-1 block text-[11px] font-bold uppercase tracking-wider text-[#9f9f9f]"
          >
            Full Name
          </label>

          <input
            v-model.trim="contactForm.full_name"
            type="text"
            placeholder="Your full name"
            :class="[
              'block h-11 w-full rounded-xl border px-3.5 text-sm text-[#23394e] outline-none transition focus:ring-2 focus:ring-[#f29200]/10',
              contactErrors.full_name
                ? 'border-red-400 focus:border-red-500'
                : 'border-[#E5E7EB] focus:border-[#f29200]'
            ]"
          />

          <p
            v-if="contactErrors.full_name"
            class="mt-1 text-xs text-red-500"
          >
            {{ contactErrors.full_name }}
          </p>
        </div>

        <div>
          <label
            class="mb-1 block text-[11px] font-bold uppercase tracking-wider text-[#9f9f9f]"
          >
            Phone Number
          </label>

          <VueTelInput
            v-model="contactForm.phone"
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
              maxlength: 20
            }"
            @validate="handlePhoneValidation"
            :class="[
              'booking-guide-phone-input',
              contactErrors.phone ? 'phone-error' : ''
            ]"
          />

          <p
            v-if="contactErrors.phone"
            class="mt-1 text-xs text-red-500"
          >
            {{ contactErrors.phone }}
          </p>
        </div>

        <div>
          <label
            class="mb-1 block text-[11px] font-bold uppercase tracking-wider text-[#9f9f9f]"
          >
            Note
          </label>

          <textarea
            v-model.trim="contactForm.note"
            rows="3"
            maxlength="250"
            placeholder="Optional message..."
            class="block w-full resize-none rounded-xl border border-[#E5E7EB] px-3.5 py-3 text-sm text-[#23394e] outline-none transition focus:border-[#f29200] focus:ring-2 focus:ring-[#f29200]/10"
          ></textarea>
        </div>
      </div>

      <!-- Support Information -->

      <div
        class="mt-5 rounded-xl border border-[#E5E7EB] bg-[#F7F8FA] p-4"
      >
        <p class="text-xs font-bold text-[#23394e]">
          Need help with your booking?
        </p>

        <div class="mt-3 grid gap-2 sm:grid-cols-2">
          <a
  v-if="whatsappNumber"
  :href="cashWhatsAppUrl"
  target="_blank"
  rel="noopener noreferrer"
  class="flex items-center justify-between rounded-lg bg-white px-3 py-2.5 text-xs font-semibold text-[#23394e] transition hover:text-[#f29200]"
>
  <span class="flex items-center gap-2">
    <MessageCircle class="h-4 w-4 text-[#f29200]" />
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
      </div>

      <!-- Error -->

      <div
        v-if="errorMessage"
        class="mt-5 rounded-xl bg-red-50 p-3 text-sm text-red-600"
        aria-live="polite"
      >

        {{ errorMessage }}

      </div>

      <!-- Buttons -->

      <div
        class="mt-6 flex flex-col-reverse gap-3 sm:flex-row sm:items-center sm:justify-between"
      >

        <button
          type="button"
          @click="currentStep = 2"
          class="inline-flex h-11 items-center justify-center gap-2 rounded-xl border border-[#E5E7EB] px-5 text-sm font-semibold text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200]"
        >
          <ArrowLeft class="h-4 w-4" />
          Back

        </button>

        <button
          type="button"
          @click="createBooking"
          :disabled="loading"
          class="inline-flex h-11 items-center justify-center gap-2 rounded-xl bg-[#f29200] px-5 text-sm font-bold text-white transition hover:bg-[#f29200]/90 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {{ loading ? "Confirming..." : "Confirm Cash" }}
          <ArrowRight class="h-4 w-4" />

        </button>

      </div>

    </div>

  </div>

</section>
</Transition>

<Transition
name="wizard"
mode="out-in">
<!-- STEP 4 -->

<section
  v-if="currentStep===4"
  class="pb-14 md:pb-16">

  <div class="max-w-3xl mx-auto px-4 sm:px-6">

    <div
      class="bg-white
      rounded-2xl
      border
      border-[#E5E7EB]
      shadow-xl
      overflow-hidden">

      <!-- Top -->

      <div
        class="bg-[#23394e]
        text-center
        py-10
        px-5 sm:px-7">

        <div
          class="w-16
          h-16
          rounded-full
          bg-[#f29200]
          flex
          items-center
          justify-center
          mx-auto">

          <CircleCheckBig
            class="text-white"
            :size="32"/>

        </div>

        <h2
          class="mt-4
          text-3xl
          font-black
          text-white">

          Booking Request Submitted

        </h2>

        <p
          class="mt-3
          text-base
          text-gray-300
          max-w-lg
          mx-auto">

          Your booking request was created successfully and is waiting for
          administrator confirmation.

        </p>

      </div>

      <!-- Body -->

      <div class="p-5 sm:p-7">

        <div
          class="space-y-4">

          <div
            class="flex items-center gap-3">

            <CircleCheckBig
              class="text-green-500"
              :size="20"/>

            <span>
              Booking request submitted
            </span>

          </div>

          <div
            class="flex items-center gap-3">

            <CircleCheckBig
              class="text-green-500"
              :size="20"/>

            <span>
              Cash payment request received
            </span>

          </div>

          <div
            class="flex items-center gap-3">

            <CircleCheckBig
              class="text-green-500"
              :size="20"/>

            <span>
              Waiting for administrator confirmation
            </span>

          </div>

        </div>

        <!-- Selected Office -->

        <div
          class="mt-8
          bg-[#F7F8FA]
          rounded-2xl
          p-5">

          <h3
            class="text-xl
            font-bold
            text-[#23394e]">

            Reservation Summary

          </h3>

          <div
            class="grid
            md:grid-cols-2
            gap-5
            mt-5">

            <div>

              <p class="text-sm text-[#9f9f9f]">
                Workspace
              </p>

              <h4
                class="font-bold
                text-lg
                mt-1 text-[#23394e]">

                {{ selectedOffice.title }}

              </h4>

            </div>

            <div>

              <p class="text-sm text-[#9f9f9f]">
                City
              </p>

              <h4
                class="font-bold
                text-lg
                mt-1 text-[#23394e]">

                {{ selectedOffice.city }}

              </h4>

            </div>

            <div>

              <p class="text-sm text-[#9f9f9f]">
                Start Date
              </p>

              <h4
                class="font-semibold
                mt-1 text-[#23394e]">

                {{ booking.start_date }}

              </h4>

            </div>

            <div>

              <p class="text-sm text-[#9f9f9f]">
                End Date
              </p>

              <h4
                class="font-semibold
                mt-1 text-[#23394e]">

                {{ booking.end_date }}

              </h4>

            </div>

          </div>

        </div>

        <!-- Buttons -->

        <div
          class="mt-8
          grid
          md:grid-cols-2
          gap-3">

          <button

            @click="goToDashboard"

            class="bg-[#f29200]
            hover:bg-[#f29200]/90
            transition
            text-white
            rounded-xl
            py-3
            font-bold">

            View My Bookings

          </button>

          <button

            @click="browseOffices"

            class="border
            border-[#E5E7EB]
            hover:border-[#f29200]
            hover:text-[#f29200]
            transition
            rounded-xl
            py-3
            font-semibold">

            Browse More Offices

          </button>

        </div>

      </div>

    </div>

  </div>

</section>
</Transition>


</main>

</template>
<style scoped>

/* ===== Wizard Transition ===== */

.wizard-enter-active,
.wizard-leave-active{

    transition:
        opacity .45s ease,
        transform .45s ease;

}

.wizard-enter-from{

    opacity:0;

    transform:translateX(70px);

}

.wizard-leave-to{

    opacity:0;

    transform:translateX(-70px);

}

.booking-guide-phone-input {
  border: 1px solid #e5e7eb !important;
  border-radius: 0.75rem !important;
  min-height: 46px;
  background: white;
  transition: 0.2s;
}

.booking-guide-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow: 0 0 0 3px rgba(242, 146, 0, 0.1);
}

.booking-guide-phone-input.phone-error {
  border-color: #ef4444 !important;
}

.booking-guide-phone-input.phone-error:focus-within {
  border-color: #ef4444 !important;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.08);
}

.booking-guide-phone-input :deep(.vti__input) {
  font-size: 14px;
  color: #23394e;
  background: transparent;
}

.booking-guide-phone-input :deep(.vti__dropdown) {
  border-radius: 0.75rem 0 0 0.75rem;
}

</style>
