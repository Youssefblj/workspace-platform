<template>
  <section
    ref="sectionRef"
    class="relative overflow-hidden py-28 bg-[#f8f9fc]"
    @mousemove="handleMouseMove"
    @mouseleave="resetMouse"
  >
    <!-- Animated Background -->

    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    <div class="blob blob-3"></div>

    <div
      class="absolute inset-0 opacity-[0.06]"
      style="
        background-image:
        radial-gradient(circle,#ffffff 1px,transparent 1px);
        background-size:40px 40px;
      "
    />

    <div class="relative max-w-7xl mx-auto px-6">

      <div
        class="relative overflow-hidden rounded-[40px] shadow-[0_30px_80px_rgba(249,168,37,.25)] bg-gradient-to-br from-[#F9A825] via-[#FDBA12] to-[#F59E0B]"
      >

        <!-- animated light -->

        <div class="absolute inset-0 light-overlay"></div>

        <div class="grid lg:grid-cols-2 gap-16 items-center p-10 lg:p-16">

          <!-- LEFT -->

          <div
            class="transition-all duration-1000"
            :class="visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'"
          >

            <div
              class="inline-flex items-center gap-2 rounded-full bg-white/20 backdrop-blur px-5 py-2 text-white font-medium"
            >
              <Sparkles class="w-5 h-5 animate-pulse"/>

              Join Workspace Today

            </div>

            <h2
              class="mt-8 text-4xl lg:text-6xl font-extrabold leading-tight text-white"
            >
              Ready to find your
              <span class="block">
                next workspace?
              </span>
            </h2>

            <p
              class="mt-8 text-lg leading-9 text-orange-50 max-w-xl"
            >
              Discover flexible offices, coworking spaces and meeting rooms
              across Morocco. Book instantly and work from inspiring locations.
            </p>

            <div class="flex flex-wrap gap-5 mt-10">

              <RouterLink
                to="/browse-offices"
                class="group px-8 py-4 rounded-2xl bg-white text-[#F9A825] font-bold flex items-center gap-3 transition-all duration-500 hover:scale-110 hover:shadow-2xl"
              >
                Browse Offices

                <ArrowRight
                  class="w-5 h-5 transition-all duration-500 group-hover:translate-x-2"
                />
              </RouterLink>

              <RouterLink
                to="/register"
                class="group px-8 py-4 rounded-2xl border border-white/40 text-white font-semibold hover:bg-white/10 transition-all duration-500 hover:scale-105"
              >
                Create Account
              </RouterLink>

            </div>

          </div>

          <!-- RIGHT -->

          <div>

            <div class="grid grid-cols-2 gap-6">

              <div
                v-for="(item,index) in stats"
                :key="item.title"
                class="card group"
                :style="{
                  animationDelay: `${index * .25}s`,
                  transform: `
                    translate(
                      ${mouse.x * (index+1) * 0.5}px,
                      ${mouse.y * (index+1) * 0.5}px
                    )
                  `
                }"
              >

                <!-- Shine -->

                <div class="shine"></div>

                <!-- Glow -->

                <div
                  class="relative w-16 h-16 rounded-2xl bg-white/20 flex items-center justify-center mb-6 overflow-hidden"
                >

                  <div class="icon-glow"></div>

                  <component
                    :is="item.icon"
                    class="relative z-10 w-8 h-8 text-white transition-all duration-500 group-hover:rotate-12 group-hover:scale-125"
                  />

                </div>

                <div class="text-4xl font-extrabold text-white">

                  {{ item.display }}

                </div>

                <div class="mt-3 text-orange-50">

                  {{ item.title }}

                </div>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>

  </section>
</template>
<script setup>

import { ref, onMounted, onUnmounted } from "vue";
import api from "@/services/api";
import {
  Sparkles,
  ArrowRight,
  Building2,
  Users,
  Star,
  CalendarCheck2,
} from "lucide-vue-next";

const visible = ref(false);

const sectionRef = ref(null);

const mouse = ref({
  x: 0,
  y: 0,
});

const stats = ref([
  {
    icon: Building2,
    value: 0,
    suffix: "",
    display: "0",
    title: "Workspaces",
  },
  {
    icon: Users,
    value: 0,
    suffix: "",
    display: "0",
    title: "Members",
  },
  {
    icon: CalendarCheck2,
    value: 0,
    suffix: "",
    display: "0",
    title: "Bookings",
  },
  {
    icon: Star,
    value: 0,
    suffix: "",
    display: "0",
    title: "Average Rating",
  },
]);

const statsLoaded = ref(false);

const fetchStats = async () => {
  try {
    const response =
      await api.get(
        "dashboard/public-stats/"
      );

    const data = response.data;

    stats.value[0].value =
      Number(data.workspaces || 0);

    stats.value[1].value =
      Number(data.members || 0);

    stats.value[2].value =
      Number(data.bookings || 0);

    stats.value[3].value =
      Number(data.average_rating || 0);

    statsLoaded.value = true;

  } catch (error) {
    console.error(
      "Failed to load public stats:",
      error
    );
  }
};

function animateCounters() {
  stats.value.forEach((item) => {
    let start = 0;

    const duration = 1800;
    const frameTime = 16;

    const steps =
      duration / frameTime;

    const increment =
      item.value / steps;

    const timer =
      setInterval(() => {
        start += increment;

        if (start >= item.value) {
          item.display =
            item.value % 1 === 0
              ? item.value.toLocaleString() +
                item.suffix
              : item.value.toFixed(1);

          clearInterval(timer);

          return;
        }

        item.display =
          item.value % 1 === 0
            ? Math.floor(start)
                .toLocaleString()
            : start.toFixed(1);

      }, frameTime);
  });
}

let observer;

onMounted(async () => {
  await fetchStats();

  observer =
    new IntersectionObserver(
      ([entry]) => {
        if (
          entry.isIntersecting &&
          statsLoaded.value
        ) {
          visible.value = true;

          animateCounters();

          observer.disconnect();
        }
      },
      {
        threshold: 0.35,
      }
    );

  if (sectionRef.value) {
    observer.observe(
      sectionRef.value
    );
  }
});

onUnmounted(() => {
  observer?.disconnect();
});

function handleMouseMove(e) {
  const rect = sectionRef.value.getBoundingClientRect();

  mouse.value.x = (e.clientX - rect.width / 2) / 120;

  mouse.value.y = (e.clientY - rect.height / 2) / 120;
}

function resetMouse() {
  mouse.value.x = 0;
  mouse.value.y = 0;
}
</script>

<style scoped>
.blob {
  position: absolute;
  border-radius: 9999px;
  filter: blur(80px);
  opacity: .25;
  animation: blob 14s ease-in-out infinite;
}

.blob-1 {
  width: 350px;
  height: 350px;
  background: #fbbf24;
  top: -120px;
  left: -100px;
}

.blob-2 {
  width: 300px;
  height: 300px;
  background: #fde68a;
  right: -80px;
  bottom: -100px;
  animation-delay: 3s;
}

.blob-3 {
  width: 240px;
  height: 240px;
  background: #ffffff;
  left: 45%;
  top: 20%;
  opacity: .08;
  animation-delay: 6s;
}

@keyframes blob {
  0% {
    transform: translate(0,0) scale(1);
  }

  25% {
    transform: translate(40px,-30px) scale(1.1);
  }

  50% {
    transform: translate(-20px,20px) scale(.95);
  }

  75% {
    transform: translate(25px,15px) scale(1.05);
  }

  100% {
    transform: translate(0,0) scale(1);
  }
}

.light-overlay {
  position: absolute;
  inset: -50%;
  background: linear-gradient(
    120deg,
    transparent 20%,
    rgba(255,255,255,.18) 40%,
    transparent 60%
  );
  animation: lightMove 8s linear infinite;
}

@keyframes lightMove {
  from {
    transform: translateX(-40%);
  }

  to {
    transform: translateX(40%);
  }
}

.card {
  position: relative;
  overflow: hidden;

  padding: 30px;

  border-radius: 28px;

  backdrop-filter: blur(18px);

  background: rgba(255,255,255,.15);

  border: 1px solid rgba(255,255,255,.2);

  transition: .55s;

  animation: floating 5s ease-in-out infinite;
}

.card:nth-child(2) {
  animation-duration: 6s;
}

.card:nth-child(3) {
  animation-duration: 7s;
}

.card:nth-child(4) {
  animation-duration: 8s;
}

.card:hover {
  transform:
    translateY(-14px)
    scale(1.05)
    rotate(1deg) !important;

  background: rgba(255,255,255,.23);

  box-shadow:
    0 25px 60px rgba(0,0,0,.15);
}

@keyframes floating {

  0%,
  100% {
    transform: translateY(0px);
  }

  50% {
    transform: translateY(-12px);
  }

}

.shine {
  position: absolute;

  inset: 0;

  background:
    linear-gradient(
      120deg,
      transparent,
      rgba(255,255,255,.4),
      transparent
    );

  transform: translateX(-160%) skewX(-25deg);

  transition: 1s;
}

.card:hover .shine {
  transform: translateX(160%) skewX(-25deg);
}

.icon-glow {
  position: absolute;

  inset: 0;

  border-radius: 999px;

  background: rgba(255,255,255,.65);

  filter: blur(18px);

  opacity: 0;

  transition: .5s;
}

.card:hover .icon-glow {
  opacity: 1;
}

.card::after {
  content: "";

  position: absolute;

  inset: 0;

  border-radius: inherit;

  border: 1px solid rgba(255,255,255,.15);

  pointer-events: none;
}

.card:hover::after {
  border-color: rgba(255,255,255,.45);
}

@media (max-width:768px){

.card{
padding:24px;
}

}
</style>