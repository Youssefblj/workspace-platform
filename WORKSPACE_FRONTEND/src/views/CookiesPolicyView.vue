<script setup>
import {
  Cookie,
  ShieldCheck,
  BarChart3,
  Settings,
  Megaphone,
  ChevronRight,
   Plus,
  Minus,
  Mail
} from "lucide-vue-next"

const openedFAQ = ref(0)

const faqs = [
  {
    title: "Can I disable cookies?",
    answer:
      "Yes. Most browsers allow you to disable or delete cookies. However, disabling essential cookies may affect authentication, bookings, and certain platform features."
  },
  {
    title: "Do cookies store my personal information?",
    answer:
      "Cookies themselves do not store sensitive personal information. They mainly store identifiers and preferences that help improve your browsing experience."
  },
  {
    title: "How long are cookies kept?",
    answer:
      "The duration depends on the cookie type. Session cookies expire when you close your browser, while persistent cookies may remain for a limited period."
  },
  {
    title: "Can I change my cookie preferences later?",
    answer:
      "Yes. You can update your browser settings or revisit our cookie settings whenever available."
  }
]

const toggleFAQ = (index) => {
  openedFAQ.value = openedFAQ.value === index ? -1 : index
}








import { ref } from "vue"

const essential = ref(true)
const analytics = ref(true)
const preferences = ref(true)
const marketing = ref(false)

const scrollToSettings = () => {
  document.getElementById("cookie-settings")?.scrollIntoView({
    behavior: "smooth"
  })
}

const scrollToDetails = () => {
  document.getElementById("cookie-details")?.scrollIntoView({
    behavior: "smooth"
  })
}
</script>

<template>
<main class="bg-[#F7F8FA] min-h-screen">

  <!-- HERO -->
  <section class="max-w-7xl mx-auto px-8 pt-4 pb-16">

    <div
      class="overflow-hidden rounded-[36px] bg-white border border-[#E5E7EB] shadow-sm">

      <div class="grid lg:grid-cols-2">

        <!-- LEFT -->
        <div class="p-10 lg:p-10 flex flex-col justify-center">

          <span
            class="inline-flex items-center gap-2 bg-orange-50 text-[#F9A825] px-5 py-2 rounded-full text-sm font-semibold w-fit">

            <Cookie class="w-4 h-4" />

            Cookies Policy

          </span>

          <h1
            class="mt-8 text-5xl lg:text-6xl font-black leading-tight text-[#1F2937]">

            Better Experience

            <span class="text-[#F9A825]">
              With Smart Cookies
            </span>

          </h1>

          <p
            class="mt-8 text-xl leading-10 text-gray-600 max-w-xl">

            Cookies help WorkSpace remember your preferences,
            keep your account secure, improve performance,
            and provide a smoother booking experience.

          </p>

          <div class="mt-10 flex gap-4">

            <button
  @click="scrollToDetails"
  class="bg-[#F9A825] text-white px-7 py-4 rounded-2xl font-semibold hover:scale-105 transition"
>
  Learn More
</button>

            <button
              @click="scrollToSettings"
              class="border border-[#E5E7EB] px-7 py-4 rounded-2xl font-semibold flex items-center gap-2 hover:border-[#F9A825] hover:text-[#F9A825] transition">

              Cookie Settings

              <ChevronRight class="w-5 h-5"/>

            </button>

          </div>

        </div>

        <!-- RIGHT -->
        <div
          class="bg-[#1F2937] p-10 lg:p-16 flex items-center justify-center">

          <div class="w-full max-w-md space-y-6">

            <!-- CARD -->

            <div
              class="bg-white/10 rounded-3xl p-6 flex items-center gap-5">

              <div
                class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

                <ShieldCheck class="w-7 h-7 text-[#F9A825]" />

              </div>

              <div>

                <h3 class="text-white font-bold text-lg">
                  Essential Cookies
                </h3>

                <p class="text-gray-300">
                  Always active for security.
                </p>

              </div>

            </div>

            <!-- CARD -->

            <div
              class="bg-white/10 rounded-3xl p-6 flex items-center gap-5">

              <div
                class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

                <BarChart3 class="w-7 h-7 text-[#F9A825]" />

              </div>

              <div>

                <h3 class="text-white font-bold text-lg">
                  Analytics
                </h3>

                <p class="text-gray-300">
                  Improve website performance.
                </p>

              </div>

            </div>

            <!-- CARD -->

            <div
              class="bg-white/10 rounded-3xl p-6 flex items-center gap-5">

              <div
                class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

                <Settings class="w-7 h-7 text-[#F9A825]" />

              </div>

              <div>

                <h3 class="text-white font-bold text-lg">
                  Preferences
                </h3>

                <p class="text-gray-300">
                  Remember your language and settings.
                </p>

              </div>

            </div>

            <!-- CARD -->

            <div
              class="bg-white/10 rounded-3xl p-6 flex items-center gap-5">

              <div
                class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

                <Megaphone class="w-7 h-7 text-[#F9A825]" />

              </div>

              <div>

                <h3 class="text-white font-bold text-lg">
                  Marketing
                </h3>

                <p class="text-gray-300">
                  Used only with your permission.
                </p>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>

  </section>
  <!-- Cookie Timeline -->

<section
  id="cookie-details"
  class="max-w-6xl mx-auto px-6 py-24">

  <div class="text-center mb-20">

    <span
      class="inline-block bg-orange-50 text-[#F9A825] px-5 py-2 rounded-full text-sm font-semibold">

      How Cookies Work

    </span>

    <h2
      class="mt-6 text-5xl font-black text-[#1F2937]">

      Every Cookie Has

      <span class="text-[#F9A825]">
        A Purpose
      </span>

    </h2>

    <p
      class="mt-6 max-w-3xl mx-auto text-gray-600 text-lg leading-9">

      We only use cookies that improve your experience,
      protect your account,
      and help us make WorkSpace faster and easier to use.

    </p>

  </div>

  <div class="space-y-12">

    <!-- Item -->

    <div
      class="flex gap-8 items-start">

      <div
        class="w-16 h-16 rounded-2xl bg-orange-100 flex items-center justify-center shrink-0">

        <ShieldCheck class="w-8 h-8 text-[#F9A825]" />

      </div>

      <div>

        <h3
          class="text-2xl font-bold text-[#1F2937]">

          Essential Cookies

        </h3>

        <p
          class="mt-3 text-gray-600 leading-8 max-w-3xl">

          Required for authentication, booking sessions,
          fraud prevention,
          and account security.
          These cookies cannot be disabled.

        </p>

      </div>

    </div>

    <!-- Item -->

    <div
      class="flex gap-8 items-start">

      <div
        class="w-16 h-16 rounded-2xl bg-orange-100 flex items-center justify-center">

        <BarChart3 class="w-8 h-8 text-[#F9A825]" />

      </div>

      <div>

        <h3
          class="text-2xl font-bold text-[#1F2937]">

          Analytics Cookies

        </h3>

        <p
          class="mt-3 text-gray-600 leading-8 max-w-3xl">

          Anonymous usage statistics help us understand
          how visitors navigate the platform,
          allowing continuous improvements.

        </p>

      </div>

    </div>

    <!-- Item -->

    <div
      class="flex gap-8 items-start">

      <div
        class="w-16 h-16 rounded-2xl bg-orange-100 flex items-center justify-center">

        <Settings class="w-8 h-8 text-[#F9A825]" />

      </div>

      <div>

        <h3
          class="text-2xl font-bold text-[#1F2937]">

          Preference Cookies

        </h3>

        <p
          class="mt-3 text-gray-600 leading-8 max-w-3xl">

          Save language,
          interface settings,
          and personal preferences
          so you don't need to configure them every visit.

        </p>

      </div>

    </div>

  </div>

</section>

  <!-- Cookie Preferences -->

<section
  id="cookie-settings"
  class="max-w-6xl mx-auto px-6 pb-24">

  <div
    class="bg-white rounded-[32px] border border-[#E5E7EB] shadow-sm overflow-hidden">

    <!-- Header -->

    <div
      class="px-10 py-8 border-b border-[#E5E7EB]">

      <span
        class="inline-flex items-center gap-2 bg-orange-50 text-[#F9A825] px-5 py-2 rounded-full text-sm font-semibold">

        <Settings class="w-4 h-4"/>

        Cookie Preferences

      </span>

      <h2
        class="mt-6 text-4xl font-black text-[#1F2937]">

        Manage Your Cookie Preferences

      </h2>

      <p
        class="mt-4 text-gray-600 leading-8 max-w-3xl">

        Different cookies serve different purposes. Below is an overview of the
        categories used on WorkSpace and whether they are optional or required.

      </p>

    </div>

    <!-- Content -->

    <div class="divide-y divide-[#E5E7EB]">

      <!-- Essential -->

      <div class="p-8 flex items-center justify-between">

        <div class="flex gap-5">

          <div
            class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

            <ShieldCheck class="w-7 h-7 text-[#F9A825]"/>

          </div>

          <div>

            <h3
              class="text-xl font-bold text-[#1F2937]">

              Essential Cookies

            </h3>

            <p
              class="mt-2 text-gray-600 leading-7">

              Required for login, booking sessions,
              fraud prevention and platform security.

            </p>

          </div>

        </div>

        <!-- Always ON -->

        <span
          class="bg-green-100 text-green-700 font-semibold px-5 py-2 rounded-full">

          Always Active

        </span>

      </div>

      <!-- Analytics -->

      <div class="p-8 flex items-center justify-between">

        <div class="flex gap-5">

          <div
            class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

            <BarChart3 class="w-7 h-7 text-[#F9A825]"/>

          </div>

          <div>

            <h3
              class="text-xl font-bold text-[#1F2937]">

              Analytics Cookies

            </h3>

            <p
              class="mt-2 text-gray-600 leading-7">

              Help us understand how visitors use the platform so we can improve
              performance and user experience.

            </p>

          </div>

        </div>

        <span
          class="bg-gray-100 text-gray-700 font-semibold px-5 py-2 rounded-full">

          Optional

        </span>

      </div>

      <!-- Preferences -->

      <div class="p-8 flex items-center justify-between">

        <div class="flex gap-5">

          <div
            class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

            <Settings class="w-7 h-7 text-[#F9A825]"/>

          </div>

          <div>

            <h3
              class="text-xl font-bold text-[#1F2937]">

              Preference Cookies

            </h3>

            <p
              class="mt-2 text-gray-600 leading-7">

              Remember language,
              theme and interface preferences
              for future visits.

            </p>

          </div>

        </div>

        <span
          class="bg-gray-100 text-gray-700 font-semibold px-5 py-2 rounded-full">

          Optional

        </span>

      </div>

      <!-- Marketing -->

      <div class="p-8 flex items-center justify-between">

        <div class="flex gap-5">

          <div
            class="w-14 h-14 rounded-2xl bg-orange-100 flex items-center justify-center">

            <Megaphone class="w-7 h-7 text-[#F9A825]"/>

          </div>

          <div>

            <h3
              class="text-xl font-bold text-[#1F2937]">

              Marketing Cookies

            </h3>

            <p
              class="mt-2 text-gray-600 leading-7">

              Used only with your permission
              to personalize content and promotional campaigns.

            </p>

          </div>

        </div>

        <span
          class="bg-gray-100 text-gray-700 font-semibold px-5 py-2 rounded-full">

          Optional

        </span>

      </div>

    </div>

  </div>

</section>
<!-- FAQ -->

<section class="max-w-5xl mx-auto px-6 pb-24">

  <div class="text-center mb-16">

    <span
      class="inline-flex items-center gap-2 bg-orange-50 text-[#F9A825] px-5 py-2 rounded-full font-semibold">

      Questions & Answers

    </span>

    <h2
      class="mt-6 text-5xl font-black text-[#1F2937]">

      Frequently Asked Questions

    </h2>

    <p
      class="mt-6 text-gray-600 text-lg leading-9 max-w-3xl mx-auto">

      Everything you need to know about how cookies work on WorkSpace.

    </p>

  </div>

  <div class="space-y-5">

    <div
      v-for="(faq,index) in faqs"
      :key="index"
      class="bg-white rounded-3xl border border-[#E5E7EB] overflow-hidden">

      <button
        @click="toggleFAQ(index)"
        class="w-full flex justify-between items-center px-8 py-6 text-left">

        <span
          class="font-bold text-xl text-[#1F2937]">

          {{ faq.title }}

        </span>

        <Plus
          v-if="openedFAQ!==index"
          class="text-[#F9A825]" />

        <Minus
          v-else
          class="text-[#F9A825]" />

      </button>

      <Transition
        enter-active-class="transition-all duration-300"
        leave-active-class="transition-all duration-300">

        <div
          v-if="openedFAQ===index"
          class="px-8 pb-8 text-gray-600 leading-8">

          {{ faq.answer }}

        </div>

      </Transition>

    </div>

  </div>

</section>
<!-- CTA -->

<section class="pb-24 px-6">

  <div
    class="max-w-6xl mx-auto rounded-[40px] bg-[#1F2937] overflow-hidden">

    <div
      class="grid lg:grid-cols-2">

      <!-- Left -->

      <div class="p-14">

        <span
          class="inline-flex items-center gap-2 bg-white/10 text-[#F9A825] px-5 py-2 rounded-full font-semibold">

          Need Help?

        </span>

        <h2
          class="mt-8 text-5xl font-black text-white">

          Still Have Questions?

        </h2>

        <p
          class="mt-8 text-gray-300 text-lg leading-9">

          Our team is always available to answer any questions
          regarding cookies, privacy, or your account.

        </p>

      </div>

      <!-- Right -->

      <div
        class="flex items-center justify-center p-14">

        <RouterLink
          to="/contact"
          class="inline-flex items-center gap-3 bg-[#F9A825] hover:bg-[#e89d13] transition text-white px-10 py-5 rounded-2xl font-bold text-lg">

          <Mail class="w-5 h-5"/>

          Contact Our Team

        </RouterLink>

      </div>

    </div>

  </div>

</section>

</main>
</template>
