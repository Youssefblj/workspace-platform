<template>
  <section class="py-24 bg-white relative overflow-hidden">
    <!-- Background -->

    <div
      class="absolute -top-52 -right-52 w-[520px] h-[520px] rounded-full bg-[#F9A825]/5 blur-3xl"
    />

    <div
      class="absolute -bottom-40 -left-40 w-[420px] h-[420px] rounded-full bg-[#F9A825]/10 blur-3xl"
    />

    <div class="relative max-w-7xl mx-auto px-6">
      <!-- Heading -->

      <div class="max-w-3xl mx-auto text-center mb-20">
        <div
          class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#F9A825]/10 text-[#F9A825] font-semibold mb-5"
        >
          <ShieldCheck class="w-5 h-5" />

          Why Choose WorkSpace
        </div>

        <h2
          class="text-4xl md:text-5xl font-extrabold text-[#1F2937]"
        >
          Everything you need

          <span class="text-[#F9A825]">
            in one platform
          </span>
        </h2>

        <p
          class="mt-6 text-lg text-gray-500 leading-8"
        >
          WorkSpace helps freelancers, startups and companies discover,
          compare and book premium workspaces across Morocco with complete
          confidence.
        </p>
      </div>

      <!-- Content -->

      <div
        class="grid lg:grid-cols-2 gap-20 items-center"
      >
        <!-- Left -->

        <div
          class="grid sm:grid-cols-2 gap-6"
        >
          <div
            v-for="item in features"
            :key="item.title"
            class="group bg-white rounded-3xl border border-gray-200 p-8 hover:border-[#F9A825]/40 hover:-translate-y-2 hover:shadow-2xl transition duration-500"
          >
            <div
              class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 text-[#F9A825] flex items-center justify-center mb-6 group-hover:scale-110 transition"
            >
              <component
                :is="item.icon"
                class="w-8 h-8"
              />
            </div>

            <h3
              class="text-2xl font-bold text-[#1F2937] mb-4"
            >
              {{ item.title }}
            </h3>

            <p
              class="text-gray-500 leading-7"
            >
              {{ item.description }}
            </p>
          </div>
        </div>

        <!-- Right -->

        <div class="relative">
          <!-- Main Card -->

          <div
            class="rounded-[32px] bg-[#1F2937] text-white p-8 lg:p-10 shadow-2xl"
          >
            <div class="flex items-center gap-4 mb-8">
              <div
                class="w-16 h-16 rounded-2xl bg-[#F9A825] flex items-center justify-center"
              >
                <Building2 class="w-8 h-8 text-white" />
              </div>

              <div>
                <h3 class="text-3xl font-bold">
                  Built for Professionals
                </h3>

                <p class="text-gray-300 mt-1">
                  Smart workspace management
                </p>
              </div>
            </div>

            <!-- Stats -->

            <div class="space-y-4">
              <div
                v-for="stat in stats"
                :key="stat.label"
                class="bg-white/5 rounded-2xl p-5 border border-white/10 flex justify-between items-center transition hover:bg-white/10"
              >
                <div>
                  <div
                    class="text-3xl font-extrabold text-[#F9A825]"
                  >
                    {{ stat.display }}
                  </div>

                  <div class="text-gray-300 mt-1">
                    {{ stat.label }}
                  </div>
                </div>

                <component
                  :is="stat.icon"
                  class="w-8 h-8 text-[#F9A825]"
                />
              </div>
            </div>

            <!-- Trusted Platform -->

            <div
              class="mt-6 flex items-center gap-4 rounded-2xl border border-white/10 bg-white/5 p-5"
            >
              <div
                class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-green-500/10"
              >
                <CheckCircle2 class="h-6 w-6 text-green-400" />
              </div>

              <div>
                <h4 class="font-bold text-white">
                  Trusted Platform
                </h4>

                <p class="mt-1 text-sm text-gray-300">
                  Secure bookings & clear workspace information
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import {
  ref,
  onMounted
} from "vue";

import {
  ShieldCheck,
  Building2,
  BadgeCheck,
  Wallet,
  Clock3,
  MapPinned,
  CheckCircle2,
  Users,
  Star,
  Building,
} from "lucide-vue-next";

import api from "@/services/api";

const features = [
  {
    icon: BadgeCheck,
    title: "Verified Spaces",
    description:
      "Every workspace is reviewed to ensure quality, security and accurate information."
  },

  {
    icon: Wallet,
    title: "Transparent Pricing",
    description:
      "No hidden fees. Compare prices instantly and book with complete confidence."
  },

  {
    icon: Clock3,
    title: "Instant Booking",
    description:
      "Reserve your workspace in minutes with real-time availability."
  },

  {
    icon: MapPinned,
    title: "Prime Locations",
    description:
      "Discover offices, coworking spaces and meeting rooms across Morocco."
  }
];

const stats = ref([
  {
    value: 0,
    display: "0",
    label: "Premium Workspaces",
    icon: Building
  },

  {
    value: 0,
    display: "0",
    label: "Happy Professionals",
    icon: Users
  },

  {
    value: 0,
    display: "0",
    label: "Average Rating",
    icon: Star
  }
]);

const loadingStats = ref(false);

const fetchStats = async () => {
  loadingStats.value = true;

  try {
    const response = await api.get(
      "dashboard/public-stats/"
    );

    const data = response.data;

    stats.value[0].value =
      Number(data.workspaces || 0);

    stats.value[1].value =
      Number(data.members || 0);

    stats.value[2].value =
      Number(data.average_rating || 0);

    animateCounters();

  } catch (error) {
    console.error(
      "Failed to load stats:",
      error
    );

  } finally {
    loadingStats.value = false;
  }
};

const animateCounters = () => {
  stats.value.forEach((item) => {
    let current = 0;

    const duration = 1400;
    const frameTime = 16;

    const steps =
      duration / frameTime;

    const increment =
      item.value / steps;

    const timer =
      setInterval(() => {
        current += increment;

        if (current >= item.value) {
          item.display =
            item.value % 1 === 0
              ? item.value.toLocaleString()
              : item.value.toFixed(1);

          clearInterval(timer);

          return;
        }

        item.display =
          item.value % 1 === 0
            ? Math.floor(current)
                .toLocaleString()
            : current.toFixed(1);

      }, frameTime);
  });
};

onMounted(() => {
  fetchStats();
});
</script>