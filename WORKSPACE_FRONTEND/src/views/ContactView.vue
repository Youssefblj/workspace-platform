<script setup>
import {
  MessageSquare,
  MapPin,
  Phone,
  Mail,
  Clock3,
  Send,
  Loader2,
  BadgeCheck,
  ShieldCheck,
  CircleCheck,
  CircleCheckBig
} from "lucide-vue-next"

import { reactive, ref, watch, onMounted } from "vue"
import api from "@/services/api"
import { VueTelInput } from "vue-tel-input"
import "vue-tel-input/vue-tel-input.css"
import { useSiteSettingsStore } from "@/stores/siteSettings"

// ======================================================
// STATE
// ======================================================

const loading = ref(false)
const success = ref(false)
const serverError = ref("")
const phoneData = ref(null)

const siteSettingsStore = useSiteSettingsStore()

onMounted(() => {
  siteSettingsStore.fetchSettings().catch(() => {})
})


const form = reactive({
  name: "",
  email: "",
  phone: "",
  category: "general",
  subject: "",
  message: ""
})

const fieldErrors = reactive({
  name: "",
  email: "",
  phone: "",
  subject: "",
  message: ""
})

// ======================================================
// HELPERS
// ======================================================

const clearErrors = () => {

  serverError.value = ""

  Object.keys(fieldErrors).forEach(key => {
    fieldErrors[key] = ""
  })

}

const resetForm = () => {

  form.name = ""
  form.email = ""
  form.phone = ""
  form.category = "general"
  form.subject = ""
  form.message = ""
  phoneData.value = null

}

// ======================================================
// VALIDATION
// ======================================================

const emailRegex =
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/

const nameRegex =
  /^[A-Za-zÀ-ÿ\s'-]+$/

const handlePhoneValidation = (data) => {
  phoneData.value = data

  if (!form.phone) {
    fieldErrors.phone = ""
    return
  }

  fieldErrors.phone =
    data.valid
      ? ""
      : "Please enter a valid phone number."
}

function validateField(field) {

  switch (field) {

    case "name":

      if (!form.name.trim()) {

        fieldErrors.name = "Full name is required."

      }

      else if (form.name.trim().length < 3) {

        fieldErrors.name =
          "Name must contain at least 3 characters."

      }

      else if (!nameRegex.test(form.name.trim())) {

        fieldErrors.name =
          "Name cannot contain numbers or special characters."

      }

      else {

        fieldErrors.name = ""

      }

      break

    case "email":

      if (!form.email.trim()) {

        fieldErrors.email =
          "Email address is required."

      }

      else if (!emailRegex.test(form.email.trim())) {

        fieldErrors.email =
          "Please enter a valid email address."

      }

      else {

        fieldErrors.email = ""

      }

      break

    case "phone":

      if (!form.phone) {

        fieldErrors.phone = ""

      }

      else if (phoneData.value?.valid === false) {

        fieldErrors.phone =
          "Please enter a valid phone number."

      }

      else {

        fieldErrors.phone = ""

      }

      break

    case "subject":

      if (!form.subject.trim()) {

        fieldErrors.subject =
          "Subject is required."

      }

      else if (form.subject.trim().length < 5) {

        fieldErrors.subject =
          "Subject must contain at least 5 characters."

      }

      else {

        fieldErrors.subject = ""

      }

      break

    case "message":

      if (!form.message.trim()) {

        fieldErrors.message =
          "Message is required."

      }

      else if (form.message.trim().length < 15) {

        fieldErrors.message =
          "Message must contain at least 15 characters."

      }

      else {

        fieldErrors.message = ""

      }

      break

  }

}

function validateForm() {

  validateField("name")
  validateField("email")
  validateField("phone")
  validateField("subject")
  validateField("message")

  return !Object.values(fieldErrors).some(Boolean)

}
// ======================================================
// REAL-TIME VALIDATION
// ======================================================

watch(
  () => form.name,
  (value) => {

    // Remove numbers and unsupported characters
    const cleaned = value.replace(/[^A-Za-zÀ-ÿ\s'-]/g, "")

    if (cleaned !== value) {
      form.name = cleaned
      return
    }

    if (fieldErrors.name) {
      validateField("name")
    }

  }
)

watch(
  () => form.email,
  () => {

    if (fieldErrors.email) {
      validateField("email")
    }

  }
)

watch(
  () => form.subject,
  () => {

    if (fieldErrors.subject) {
      validateField("subject")
    }

  }
)

watch(
  () => form.message,
  () => {

    if (fieldErrors.message) {
      validateField("message")
    }

  }
)

// ======================================================
// SUBMIT
// ======================================================

const submitContact = async () => {

  clearErrors()

  success.value = false

  if (!validateForm()) {
    return
  }

  // Clean values
  form.name = form.name.trim()
  form.email = form.email.trim().toLowerCase()

  if (form.phone) {
    form.phone =
      (phoneData.value?.number || form.phone)
        .replace(/[^\d+]/g, "")
        .replace(/(?!^)\+/g, "")
  }

  form.subject = form.subject.trim()
  form.message = form.message.trim()

  loading.value = true

  try {

    await api.post("/contact/create/", form)

    success.value = true

    // Remove all validation messages
    Object.keys(fieldErrors).forEach((key) => {
      fieldErrors[key] = ""
    })

    resetForm()

    window.scrollTo({
      top: 0,
      behavior: "smooth"
    })

  }

  catch (error) {

    if (error.response?.data) {

      const data = error.response.data

      Object.keys(data).forEach((key) => {

        fieldErrors[key] = Array.isArray(data[key])
          ? data[key][0]
          : data[key]

      })

    }

    else {

      serverError.value =
        "Something went wrong. Please try again later."

    }

  }

  finally {

    loading.value = false

  }

}
</script>

<template>
<main class="bg-[#F7F8FA] min-h-screen">

<!-- ================= HERO ================= -->

<section class="bg-white border-b border-[#E5E7EB]">

  <div class="max-w-6xl mx-auto px-6 py-16">

    <div class="max-w-3xl">

      <span
        class="inline-flex items-center gap-2 bg-orange-50 text-[#F9A825] px-4 py-2 rounded-full font-semibold text-sm">

        <MessageSquare class="w-4 h-4"/>

        Contact Us

      </span>

      <h1
        class="mt-6 text-4xl font-black text-[#1F2937] leading-tight">

        We'd Love to Hear From You

      </h1>

      <p
        class="mt-5 text-gray-600 leading-8 text-lg">

        Whether you have a question about bookings,
        pricing, partnerships, or technical support,
        our team is ready to help.

      </p>

    </div>

  </div>

</section>

<!-- ================= CONTACT INFO ================= -->

<section class="max-w-6xl mx-auto px-6 py-18">

<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

<!-- Card -->

<div
class="bg-white rounded-2xl border border-[#E5E7EB] p-6 hover:border-[#F9A825] transition">

<div
class="w-12 h-12 rounded-xl bg-orange-50 flex items-center justify-center">

<MapPin
class="w-6 h-6 text-[#F9A825]"/>

</div>

<h3
class="mt-5 font-bold text-[#1F2937]">

Office

</h3>

<p
  class="mt-2 text-gray-600 leading-7 text-sm"
>
  {{
    siteSettingsStore.settings.address ||
    "Address not available"
  }}
</p>

</div>

<!-- Card -->

<div
class="bg-white rounded-2xl border border-[#E5E7EB] p-6 hover:border-[#F9A825] transition">

<div
class="w-12 h-12 rounded-xl bg-orange-50 flex items-center justify-center">

<Phone
class="w-6 h-6 text-[#F9A825]"/>

</div>

<h3
class="mt-5 font-bold text-[#1F2937]">

Phone

</h3>

<a
  v-if="siteSettingsStore.settings.contact_phone"
  :href="`tel:${siteSettingsStore.settings.contact_phone}`"
  class="mt-2 block text-gray-600 transition hover:text-[#f29200]"
>
  {{ siteSettingsStore.settings.contact_phone }}
</a>

<p
  v-else
  class="mt-2 text-gray-600"
>
  Phone not available
</p>

</div>

<!-- Card -->

<div
class="bg-white rounded-2xl border border-[#E5E7EB] p-6 hover:border-[#F9A825] transition">

<div
class="w-12 h-12 rounded-xl bg-orange-50 flex items-center justify-center">

<Mail
class="w-6 h-6 text-[#F9A825]"/>

</div>

<h3
class="mt-5 font-bold text-[#1F2937]">

Email

</h3>

<a
  v-if="siteSettingsStore.settings.contact_email"
  :href="`mailto:${siteSettingsStore.settings.contact_email}`"
  class="mt-2 block break-all text-sm text-gray-600 transition hover:text-[#f29200]"
>
  {{ siteSettingsStore.settings.contact_email }}
</a>

<p
  v-else
  class="mt-2 break-all text-sm text-gray-600"
>
  Email not available
</p>

</div>

<!-- Card -->

<div
class="bg-white rounded-2xl border border-[#E5E7EB] p-6 hover:border-[#F9A825] transition">

<div
class="w-12 h-12 rounded-xl bg-orange-50 flex items-center justify-center">

<Clock3
class="w-6 h-6 text-[#F9A825]"/>

</div>

<h3
class="mt-5 font-bold text-[#1F2937]">

Working Hours

</h3>

<p
class="mt-2 text-gray-600 text-sm leading-7">

Monday – Friday

8:00 AM – 6:00 PM

</p>

</div>

</div>

</section>

<!-- ================= CONTACT FORM ================= -->

<section class="max-w-6xl mx-auto px-6 pb-10">

  <div
    class="grid lg:grid-cols-5 gap-6">

    <!-- Left -->

    <div
      class="lg:col-span-2">

      <span
        class="inline-flex items-center gap-2 bg-orange-50 text-[#F9A825] px-4 py-2 rounded-full text-sm font-semibold">

        <Send class="w-4 h-4"/>

        Send a Message

      </span>

      <h2
        class="mt-5 text-2xl font-black text-[#1F2937]">

        Tell us how we can help.

      </h2>

      <p
        class="mt-4 text-gray-600 leading-8">

        Fill out the form and our team will get back to you
        as soon as possible.

      </p>

      <div
        class="mt-8 space-y-4 text-gray-600">

        <div class="flex items-center gap-3">

          <BadgeCheck class="w-5 h-5 text-[#F9A825]" />

          <span>Response within 24 hours</span>

        </div>

        <div class="flex items-center gap-3">

          <ShieldCheck class="w-5 h-5 text-[#F9A825]" />

          <span>Your information is kept confidential</span>

        </div>

        <div class="flex items-center gap-3">

          <CircleCheck class="w-5 h-5 text-[#F9A825]" />

          <span>No spam. Professional support only.</span>

        </div>

      </div>

    </div>

    <!-- Right -->

    <div
      class="lg:col-span-3">
<!-- Success Message -->

  <div
    v-if="success"
    class="mb-8 rounded-2xl border border-green-200 bg-green-50 p-5">

    <div class="flex items-start gap-4">

      <CircleCheckBig
        class="w-7 h-7 text-green-600 shrink-0"/>

      <div>

        <h3 class="font-bold text-green-700">
          Message Sent Successfully
        </h3>

        <p class="mt-2 text-green-600 leading-7">
          Thank you for contacting us.
          Our team will review your request and reply as soon as possible.
        </p>

      </div>

    </div>

  </div>


  <div
  v-if="serverError"
  class="mb-6 rounded-2xl border border-red-200 bg-red-50 p-5">

  <h3
    class="font-semibold text-red-700">

    Unable to send your message

  </h3>

  <p
    class="mt-2 text-red-600">

    {{ serverError }}

  </p>

</div>

      <form
  @submit.prevent="submitContact"
  class="bg-white border border-[#E5E7EB] rounded-2xl p-6 space-y-4"
>

        <!-- Row -->

        <div class="grid md:grid-cols-2 gap-5">

          <!-- Name -->

          <div>

            <label
              class="block text-sm font-semibold text-[#1F2937] mb-2">

              Full Name *

            </label>

            <input
  v-model="form.name"
  type="text"
  placeholder="John Doe"
  :class="[
    'w-full rounded-lg px-3 py-2.5 text-sm outline-none transition-all',
    fieldErrors.name
      ? 'border border-red-500 focus:ring-2 focus:ring-red-200'
      : 'border border-[#E5E7EB] focus:ring-2 focus:ring-[#F9A825]'
  ]"
/>

<p
  v-if="fieldErrors.name"
  class="mt-2 text-sm text-red-500">

  {{ fieldErrors.name }}

</p>



          </div>

          <!-- Email -->

          <div>

            <label
              class="block text-sm font-semibold text-[#1F2937] mb-2">

              Email Address *

            </label>

            <input
  v-model="form.email"
  type="email"
  placeholder="john@example.com"
  :class="[
    'w-full rounded-lg px-3 py-2.5 text-sm outline-none transition-all',
    fieldErrors.email
      ? 'border border-red-500 focus:ring-2 focus:ring-red-200'
      : 'border border-[#E5E7EB] focus:ring-2 focus:ring-[#F9A825]'
  ]"
/>

<p
  v-if="fieldErrors.email"
  class="mt-2 text-sm text-red-500">

  {{ fieldErrors.email }}

</p>

          </div>

        </div>

        <!-- Row -->

        <div class="grid md:grid-cols-2 gap-5">

          <!-- Phone -->

          <div>

            <label
              class="block text-sm font-semibold text-[#1F2937] mb-2">

              Phone

            </label>

            <VueTelInput
              v-model="form.phone"
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
                'contact-phone-input',
                fieldErrors.phone ? 'phone-error' : ''
              ]"
            />

<p
  v-if="fieldErrors.phone"
  class="mt-2 text-sm text-red-500">

  {{ fieldErrors.phone }}

</p>

          </div>

          <!-- Category -->

          <div>

            <label
              class="block text-sm font-semibold text-[#1F2937] mb-2">

              Category

            </label>

            <select
              v-model="form.category"
              class="w-full rounded-lg border border-[#E5E7EB] px-3 py-2.5 focus:ring-2 focus:ring-[#F9A825] outline-none">

              <option value="general">General Inquiry</option>

              <option value="booking">Booking</option>

              <option value="payment">Payment</option>

              <option value="technical">Technical Support</option>

              <option value="complaint">Complaint</option>

              <option value="suggestion">Suggestion</option>

            </select>

          </div>

        </div>

        <!-- Subject -->

        <div>

          <label
            class="block text-sm font-semibold text-[#1F2937] mb-2">

            Subject *

          </label>

          <input
  v-model="form.subject"
  type="text"
  maxlength="255"
  placeholder="How can we help?"
  :class="[
    'w-full rounded-lg px-3 py-2.5 text-sm outline-none transition-all',
    fieldErrors.subject
      ? 'border border-red-500 focus:ring-2 focus:ring-red-200'
      : 'border border-[#E5E7EB] focus:ring-2 focus:ring-[#F9A825]'
  ]"
/>

<p
  v-if="fieldErrors.subject"
  class="mt-2 text-sm text-red-500">

  {{ fieldErrors.subject }}

</p>

        </div>

        <!-- Message -->

        <div>

  <div class="flex items-center justify-between mb-2">

    <label
      class="text-sm font-semibold text-[#1F2937]">

      Message *

    </label>

    <span
      :class="[
        'text-xs font-medium',
        form.message.length > 450
          ? 'text-red-500'
          : 'text-gray-400'
      ]">

      {{ form.message.length }}/500

    </span>

  </div>

  <textarea
    v-model="form.message"
    rows="4"
    maxlength="500"
    placeholder="Write your message here..."
    :class="[
      'w-full rounded-lg px-3 py-2.5 text-sm resize-none outline-none transition-all',
      fieldErrors.message
        ? 'border border-red-500 focus:ring-2 focus:ring-red-200'
        : 'border border-[#E5E7EB] focus:ring-2 focus:ring-[#F9A825]'
    ]"
  />

  <p
    v-if="fieldErrors.message"
    class="mt-2 text-sm text-red-500">

    {{ fieldErrors.message }}

  </p>

</div>

        <!-- Button -->

        <button
  type="submit"
  :disabled="loading"
  class="w-full h-11 rounded-lg bg-[#f29200] hover:opacity-90 transition-all duration-300 text-white text-sm font-semibold flex items-center justify-center gap-2 disabled:opacity-60 disabled:cursor-not-allowed">

  <Loader2
    v-if="loading"
    class="w-5 h-5 animate-spin" />

  <Send
    v-else
    class="w-5 h-5" />

  <span>

    {{ loading ? "Sending Message..." : "Send Message" }}

  </span>

</button>

      </form>

    </div>

  </div>

</section>
 </main>
</template>

<style>
.contact-phone-input {
  border: 1px solid #e5e7eb !important;
  border-radius: 0.5rem !important;
  min-height: 42px;
  background: white;
  transition: 0.2s;
}

.contact-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow: 0 0 0 2px rgba(242, 146, 0, 0.15);
}

.contact-phone-input.phone-error {
  border-color: #ef4444 !important;
}

.contact-phone-input .vti__input {
  font-size: 14px;
  color: #23394e;
  background: transparent;
}

.contact-phone-input .vti__dropdown {
  border-radius: 0.5rem 0 0 0.5rem;
}
</style>
