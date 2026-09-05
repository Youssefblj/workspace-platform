<template>
  <section class="py-24 bg-[#F7F8FA] overflow-hidden">
    <div class="max-w-7xl mx-auto px-6">

      <!-- Heading -->

      <div class="max-w-3xl mx-auto text-center mb-16">

        <div
          class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#F9A825]/10 text-[#F9A825] font-semibold mb-5"
        >
          <LayoutGrid class="w-5 h-5" />
          Explore Categories
        </div>

        <h2
          class="text-4xl md:text-5xl font-extrabold text-[#1F2937]"
        >
          Find the
          <span class="text-[#F9A825]">perfect workspace</span>
          for every need
        </h2>

        <p
          class="mt-6 text-lg text-[#6B7280] leading-8"
        >
          Whether you're working alone, meeting clients or building your team,
          WorkSpace offers flexible environments designed for every stage of
          your business.
        </p>

      </div>

      <!-- Cards -->

      <div
        class="grid lg:grid-cols-2 gap-8"
      >

        <RouterLink
          v-for="category in categories"
          :key="category.title"
          :to="category.route"
          class="group relative rounded-3xl overflow-hidden h-[340px] shadow-lg"
        >

          <!-- Image -->

          <img
            :src="category.image"
            class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition duration-700"
          >

          <!-- Overlay -->

          <div
            class="absolute inset-0 bg-gradient-to-r from-black/80 via-black/45 to-transparent"
          />

          <!-- Content -->

          <div
            class="relative h-full flex flex-col justify-between p-10"
          >

            <div>

              <div
                class="w-16 h-16 rounded-2xl bg-white/15 backdrop-blur flex items-center justify-center mb-6 border border-white/20"
              >
                <component
                  :is="category.icon"
                  class="w-8 h-8 text-white"
                />
              </div>

              <h3
                class="text-white text-3xl font-bold mb-4"
              >
                {{ category.title }}
              </h3>

              <p
                class="text-white/90 leading-7 max-w-md"
              >
                {{ category.description }}
              </p>

            </div>

            <!-- Footer -->

            <div
              class="flex items-center justify-between"
            >

              <span
                class="text-white/80 text-sm tracking-wide uppercase"
              >
                {{ category.count }}
              </span>

              <div
                class="flex items-center gap-2 text-white font-semibold"
              >
                Explore

                <ArrowRight
                  class="w-5 h-5 transition group-hover:translate-x-2"
                />
              </div>

            </div>

          </div>

        </RouterLink>

      </div>

    </div>
  </section>
</template>

<script setup>
import {
  LayoutGrid,
  Building2,
  Users,
  Presentation,
  Globe,
  ArrowRight
} from "lucide-vue-next"

const categories = [
  {
    title: "Private Offices",
    description:
      "Fully equipped offices for startups, agencies and growing businesses seeking privacy and productivity.",
    image:
      "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=1200",
    icon: Building2,
    route: "/browse-offices",
    count: "120+ Offices"
  },

  {
    title: "Coworking Spaces",
    description:
      "Collaborative environments with modern amenities, networking opportunities and flexible memberships.",
    image:
      "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=1200",
    icon: Users,
    route: "/coworking-spaces",
    count: "85+ Spaces"
  },

  {
    title: "Meeting Rooms",
    description:
      "Professional meeting rooms equipped with presentation technology for interviews, workshops and conferences.",
    image:
      "https://images.unsplash.com/photo-1517502884422-41eaead166d4?w=1200",
    icon: Presentation,
    route: "/meeting-rooms",
    count: "60+ Rooms"
  },

  {
    title: "Virtual Offices",
    description:
      "Build your professional presence with a prestigious business address without renting a physical office.",
    image:
      "https://images.unsplash.com/photo-1497366412874-3415097a27e7?w=1200",
    icon: Globe,
    route: "/virtual-offices",
    count: "35+ Locations"
  }
]
</script>