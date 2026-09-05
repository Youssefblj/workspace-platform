<template>
  <section class="py-24 bg-[#F7F8FA]">
    <div class="max-w-5xl mx-auto px-6">

      <!-- Heading -->

      <div class="text-center mb-16">

        <div
          class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#F9A825]/10 text-[#F9A825] font-semibold mb-5"
        >
          <CircleHelp class="w-5 h-5" />
          Frequently Asked Questions
        </div>

        <h2
          class="text-4xl md:text-5xl font-extrabold text-[#1F2937]"
        >
          Got questions?
          <span class="text-[#F9A825]">
            We've got answers
          </span>
        </h2>

        <p
          class="mt-6 text-lg text-gray-500 max-w-2xl mx-auto leading-8"
        >
          Everything you need to know before booking your next workspace.
        </p>

      </div>

      <!-- FAQ -->

      <div class="space-y-5">

        <div
          v-for="(faq,index) in faqs"
          :key="index"
          class="bg-white rounded-3xl border border-[#E5E7EB] overflow-hidden transition hover:shadow-xl"
        >

          <button
            @click="toggle(index)"
            class="w-full flex justify-between items-center p-7 text-left"
          >

            <h3
              class="font-bold text-lg text-[#1F2937]"
            >
              {{ faq.question }}
            </h3>

            <ChevronDown
              class="w-6 h-6 text-[#F9A825] transition duration-300"
              :class="{ 'rotate-180': active===index }"
            />

          </button>

          <transition
            enter-active-class="transition-all duration-300"
            leave-active-class="transition-all duration-300"
            enter-from-class="opacity-0 max-h-0"
            enter-to-class="opacity-100 max-h-96"
            leave-from-class="opacity-100 max-h-96"
            leave-to-class="opacity-0 max-h-0"
          >

            <div
              v-if="active===index"
              class="px-7 pb-7 text-gray-600 leading-8"
            >
              {{ faq.answer }}
            </div>

          </transition>

        </div>

      </div>

    </div>
  </section>
</template>

<script setup>
import { ref } from "vue"

import {
  CircleHelp,
  ChevronDown
} from "lucide-vue-next"

const active = ref(0)

const toggle = (index)=>{
  active.value = active.value===index ? null : index
}

const faqs = [

{
question:"How do I book a workspace?",
answer:"Browse available workspaces, select the one that matches your needs, choose your preferred date and complete your reservation securely online."
},

{
question:"Can I cancel my booking?",
answer:"Yes. Cancellation depends on the workspace owner's policy. The applicable cancellation terms are displayed before confirming your booking."
},

{
question:"Are all workspaces verified?",
answer:"Yes. Every workspace published on WorkSpace is reviewed before becoming available to ensure quality and accurate information."
},

{
question:"Can I rent for one day only?",
answer:"Absolutely. Many offices and meeting rooms support hourly or daily bookings, while others offer weekly or monthly plans."
}

]
</script>