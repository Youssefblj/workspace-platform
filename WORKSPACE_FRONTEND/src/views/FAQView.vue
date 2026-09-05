<script setup>
const contactSupport = () => {

  router.push("/contact")

}
import { ref, computed } from "vue"

import {
  Search,
  HelpCircle,
  CalendarDays,
  CreditCard,
  Building2,
  ShieldCheck,
  User,
  ChevronDown,
  MessageCircle
} from "lucide-vue-next"
import { useRouter } from "vue-router"

const router = useRouter()

const searchQuery = ref("")
const activeCategory = ref("All")
const categories = [

  {
    name: "All",
    icon: HelpCircle
  },

  {
    name: "Booking",
    icon: CalendarDays
  },

  {
    name: "Payments",
    icon: CreditCard
  },

  {
    name: "Offices",
    icon: Building2
  },

  {
    name: "Privacy",
    icon: ShieldCheck
  },

  {
    name: "Account",
    icon: User
  }

]

const openQuestion = ref(null)

const faqs = [

  // BOOKING

  {
    id: 1,
    category: "Booking",
    question: "How do I book a workspace?",
    answer:
      "Search for an available workspace, choose your preferred dates, review your booking summary, and confirm your reservation."
  },

  {
    id: 2,
    category: "Booking",
    question: "Can I cancel my booking?",
    answer:
      "Yes. You can cancel eligible bookings from your dashboard according to our cancellation policy."
  },

  {
    id: 3,
    category: "Booking",
    question: "Can I modify my reservation?",
    answer:
      "Yes. Depending on availability, you can update your booking dates from your account."
  },

  // PAYMENTS

  {
    id: 4,
    category: "Payments",
    question: "Which payment methods are accepted?",
    answer:
      "We currently support secure online payment methods available on our platform."
  },

  {
    id: 5,
    category: "Payments",
    question: "Will I receive an invoice?",
    answer:
      "Yes. An invoice is generated after your booking is confirmed."
  },

  {
    id: 6,
    category: "Payments",
    question: "When will I be charged?",
    answer:
      "Your payment is processed once your reservation is successfully confirmed."
  },

  // OFFICES

  {
    id: 7,
    category: "Offices",
    question: "Can I visit an office before booking?",
    answer:
      "Some offices allow visits before booking. Please contact the office owner for availability."
  },

  {
    id: 8,
    category: "Offices",
    question: "Are offices fully furnished?",
    answer:
      "Most listed offices include furniture and essential amenities. Details are available on each office page."
  },

  {
    id: 9,
    category: "Offices",
    question: "Do offices include internet?",
    answer:
      "Most workspaces provide high-speed internet. Check the office amenities before booking."
  },

  // PRIVACY

  {
    id: 10,
    category: "Privacy",
    question: "Is my personal information secure?",
    answer:
      "Yes. Your personal information is protected using industry-standard security practices."
  },

  {
    id: 11,
    category: "Privacy",
    question: "How is my payment information protected?",
    answer:
      "Sensitive payment information is processed through secure payment providers."
  },

  // ACCOUNT

  {
    id: 12,
    category: "Account",
    question: "How do I reset my password?",
    answer:
      "Use the 'Forgot Password' option on the login page to receive a password reset link."
  },

  {
    id: 13,
    category: "Account",
    question: "Can I delete my account?",
    answer:
      "Yes. You can request account deletion by contacting our support team."
  }

]
const filteredFaqs = computed(() => {

  return faqs.filter(faq => {

    const matchCategory =

      activeCategory.value === "All"

      ||

      faq.category === activeCategory.value

    const matchSearch =

      faq.question
      .toLowerCase()
      .includes(searchQuery.value.toLowerCase())

    return matchCategory && matchSearch

  })

})
</script>


<template>

<main class="bg-[#F7F8FA] min-h-screen">

  <!-- Hero -->

  <section class="pt-20 pb-12">

    <div class="max-w-6xl mx-auto px-6 text-center">

      <div
        class="inline-flex items-center gap-2
        bg-[#F9A825]/10
        text-[#F9A825]
        px-4 py-2
        rounded-full
        font-medium">

        <HelpCircle :size="18"/>

        Help Center

      </div>

      <h1
        class="mt-6
        text-4xl
        font-bold
        text-[#1F2937]">

        Frequently Asked Questions

      </h1>

      <p
        class="mt-4
        text-gray-600
        max-w-2xl
        mx-auto
        leading-7">

        Find quick answers about bookings, payments,
        offices, privacy, and your account.

      </p>

    </div>

  </section>

  <!-- Search -->

  <section class="pb-12">

    <div class="max-w-3xl mx-auto px-6">

      <div class="relative">

        <Search
          class="absolute left-5 top-1/2
          -translate-y-1/2
          text-gray-400"
          :size="20"/>

        <input

          v-model="searchQuery"

          type="text"

          placeholder="Search a question..."

          class="w-full
          bg-white
          border
          border-[#E5E7EB]
          rounded-2xl
          py-4
          pl-14
          pr-5
          outline-none
          focus:border-[#F9A825]
          transition"/>

      </div>

    </div>

  </section>

  <!-- Categories -->

<section class="pb-14">

  <div class="max-w-6xl mx-auto px-6">

    <div
      class="flex
      flex-wrap
      justify-center
      gap-4">

      <button

        v-for="category in categories"

        :key="category.name"

        @click="activeCategory = category.name"

        class="flex
        items-center
        gap-2
        px-5
        py-3
        rounded-full
        border
        transition-all
        duration-300
        font-medium"

        :class="

          activeCategory === category.name

          ?

          'bg-[#F9A825] text-white border-[#F9A825] shadow-md'

          :

          'bg-white text-[#374151] border-[#E5E7EB] hover:border-[#F9A825] hover:text-[#F9A825]'

        ">

        <component

          :is="category.icon"

          :size="18"/>

        {{ category.name }}

      </button>

    </div>

  </div>

</section>
<!-- FAQ List -->

<section class="pb-20">

  <div class="max-w-4xl mx-auto px-6">

    <div
      v-for="faq in filteredFaqs"
      :key="faq.id"
      class="mb-4">

      <div

        @click="openQuestion =
        openQuestion === faq.id
        ? null
        : faq.id"

        class="bg-white
        border
        border-[#E5E7EB]
        rounded-2xl
        cursor-pointer
        transition
        hover:border-[#F9A825]">

        <!-- Header -->

        <div
          class="flex
          justify-between
          items-center
          p-6">

          <h3
            class="text-lg
            font-semibold
            text-[#1F2937]">

            {{ faq.question }}

          </h3>

          <ChevronDown

            :size="22"

            class="transition-transform duration-300"

            :class="{

              'rotate-180':
              openQuestion===faq.id

            }"/>

        </div>

        <!-- Body -->

        <Transition name="faq">

          <div

            v-if="openQuestion===faq.id"

            class="px-6
            pb-6
            text-gray-600
            leading-7">

            {{ faq.answer }}

          </div>

        </Transition>

      </div>

    </div>

  </div>

</section>
<!-- Contact Support -->

<section class="pb-24">

  <div class="max-w-5xl mx-auto px-6">

    <div
      class="bg-[#1F2937]
      rounded-3xl
      overflow-hidden">

      <div
        class="px-10
        py-14
        text-center">

        <div
          class="w-16
          h-16
          mx-auto
          rounded-full
          bg-[#F9A825]/20
          flex
          items-center
          justify-center">

          <MessageCircle

            :size="30"

            class="text-[#F9A825]" />

        </div>

        <h2
          class="mt-6
          text-3xl
          font-bold
          text-white">

          Still need help?

        </h2>

        <p
          class="mt-4
          text-gray-300
          max-w-2xl
          mx-auto
          leading-7">

          Can't find the answer you're looking for?
          Our support team is always ready to help you with bookings,
          payments, offices, or account-related questions.

        </p>

        <button

          @click="contactSupport"

          class="mt-8
          bg-[#F9A825]
          hover:bg-[#e89d12]
          transition
          text-white
          font-semibold
          px-8
          py-3
          rounded-xl">

          Contact Support

        </button>

      </div>

    </div>

  </div>

</section>

</main>

</template>
<style scoped>
.faq-enter-active,
.faq-leave-active{

  transition: all .3s ease;

}

.faq-enter-from,
.faq-leave-to{

  opacity:0;

  transform:translateY(-10px);

}
</style>