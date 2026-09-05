<template>
  <section class="py-24 bg-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-6">

      <!-- Header -->

      <div class="text-center max-w-3xl mx-auto mb-20">

        <div
          class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#F9A825]/10 text-[#F9A825] font-semibold mb-5"
        >
          <MessageCircleMore class="w-5 h-5" />
          Testimonials
        </div>

        <h2
          class="text-4xl md:text-5xl font-extrabold text-[#1F2937]"
        >
          Loved by
          <span class="text-[#F9A825]">
            professionals
          </span>
        </h2>

        <p
          class="mt-6 text-lg text-gray-500 leading-8"
        >
          Thousands of entrepreneurs, freelancers and companies rely on
          WorkSpace to find inspiring places to work every day.
        </p>

      </div>

      <!-- Cards -->

      <div
        class="grid lg:grid-cols-3 gap-8"
      >

        <article
          v-for="testimonial in testimonials"
          :key="testimonial.name"
          class="group bg-[#F7F8FA] rounded-[32px] p-8 border border-[#E5E7EB] hover:shadow-2xl hover:-translate-y-2 transition duration-500"
        >

          <!-- Rating -->

          <div class="flex gap-1 mb-6">

            <Star
              v-for="i in 5"
              :key="i"
              class="w-5 h-5 fill-[#F9A825] text-[#F9A825]"
            />

          </div>

          <!-- Quote -->

          <p
            class="text-gray-600 leading-8 text-lg italic"
          >
            "{{ testimonial.review }}"
          </p>

          <!-- User -->

          <div
            class="flex items-center gap-4 mt-10"
          >

            <img
              :src="testimonial.avatar"
              class="w-16 h-16 rounded-full object-cover border-4 border-white shadow-lg"
            >

            <div>

              <h3
                class="font-bold text-[#1F2937]"
              >
                {{ testimonial.name }}
              </h3>

              <p
                class="text-sm text-gray-500"
              >
                {{ testimonial.position }}
              </p>

            </div>

          </div>

          <!-- Company -->

          <div
            class="flex items-center justify-between mt-8 pt-6 border-t border-[#E5E7EB]"
          >

            <div
              class="flex items-center gap-2 text-gray-500"
            >
              <Building2 class="w-5 h-5 text-[#F9A825]" />
              {{ testimonial.company }}
            </div>

            <div
              class="flex items-center gap-2 text-gray-500"
            >
              <MapPin class="w-5 h-5 text-[#F9A825]" />
              {{ testimonial.city }}
            </div>

          </div>

        </article>

      </div>

    </div>
  </section>
</template>

<script setup>
import {
  MessageCircleMore,
  Star,
  Building2,
  MapPin
} from "lucide-vue-next"

const testimonials = [
  {
    name: "Ahmed Benali",
    position: "Startup Founder",
    company: "Atlas Tech",
    city: "Casablanca",
    avatar: "https://i.pravatar.cc/150?img=11",
    review:
      "WorkSpace made finding an office incredibly easy. The booking process was fast, transparent and professional."
  },

  {
    name: "Sara El Idrissi",
    position: "Marketing Consultant",
    company: "Freelancer",
    city: "Rabat",
    avatar: "https://i.pravatar.cc/150?img=32",
    review:
      "I use coworking spaces almost every week. This platform saves me hours of searching and comparing locations."
  },

  {
    name: "Youssef Amrani",
    position: "Operations Manager",
    company: "Nova Solutions",
    city: "Tangier",
    avatar: "https://i.pravatar.cc/150?img=18",
    review:
      "Excellent experience from booking to check-in. The office matched the photos perfectly and the support team was very responsive."
  }
]
</script>