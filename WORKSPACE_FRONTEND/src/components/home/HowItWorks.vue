<template>
  <section
    ref="sectionRef"
    class="process-section bg-white py-24"
    :class="{ 'is-visible': hasEntered }"
  >
    <div class="mx-auto max-w-7xl px-6">

      <!-- Header -->

      <div class="mx-auto mb-20 max-w-3xl text-center">

        <div
          class="process-badge mb-5 inline-flex items-center gap-2 rounded-full bg-[#f29200]/10 px-4 py-2 font-semibold text-[#f29200]"
        >
          <Activity class="h-5 w-5" />
          How It Works
        </div>

        <h2
          class="process-heading text-4xl font-extrabold leading-tight text-[#23394e] md:text-5xl"
        >
          Book your workspace

          <span class="text-[#f29200]">
            in four simple steps
          </span>
        </h2>

        <p
          class="process-description mt-6 text-lg leading-8 text-[#9f9f9f]"
        >
          Finding your next office has never been easier.
          From searching to booking, everything happens
          within minutes.
        </p>

      </div>

      <!-- Timeline -->

      <div class="relative">

        <!-- Connecting Line -->

        <div
          class="timeline-line absolute left-[12%] right-[12%] top-10 hidden h-px bg-[#f29200]/25 lg:block"
        />

        <!-- Steps -->

        <div
          class="relative grid gap-8 sm:grid-cols-2 lg:grid-cols-4"
        >

          <article
            v-for="(step, index) in steps"
            :key="step.number"
            class="process-step group relative text-center"
            :class="`process-step-${index + 1}`"
          >

            <!-- Icon -->

            <div class="process-icon-entrance relative z-10 mx-auto h-20 w-20">
              <div
                class="process-icon flex h-full w-full items-center justify-center rounded-2xl border border-[#f29200]/20 bg-white shadow-sm transition duration-300 group-hover:-translate-y-0.5 group-hover:scale-[1.05] group-hover:border-[#f29200] group-hover:shadow-md"
              >
                <component
                  :is="step.icon"
                  class="h-8 w-8 text-[#f29200]"
                />
              </div>
            </div>

            <!-- Number -->

            <div
              class="process-number mx-auto mt-6 flex h-7 w-fit items-center justify-center rounded-full bg-[#f29200]/10 px-3 text-xs font-bold text-[#f29200]"
            >
              {{ step.number }}
            </div>

            <!-- Content -->

            <h3
              class="mt-4 text-xl font-bold text-[#23394e]"
            >
              {{ step.title }}
            </h3>

            <p
              class="mx-auto mt-3 max-w-[240px] text-sm leading-6 text-[#9f9f9f]"
            >
              {{ step.description }}
            </p>

          </article>

        </div>

      </div>

    </div>
  </section>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from "vue";
import {
  Activity,
  Search,
  CalendarDays,
  CreditCard,
  Rocket
} from "lucide-vue-next";

const sectionRef = ref(null);
const hasEntered = ref(false);

let observer;

onMounted(() => {
  if (!("IntersectionObserver" in window)) {
    hasEntered.value = true;
    return;
  }

  observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        hasEntered.value = true;
        observer.disconnect();
      }
    },
    { threshold: 0.2 }
  );

  observer.observe(sectionRef.value);
});

onUnmounted(() => {
  observer?.disconnect();
});

const steps = [
  {
    number: "01",
    icon: Search,
    title: "Search",
    description:
      "Browse available offices using smart filters."
  },
  {
    number: "02",
    icon: CalendarDays,
    title: "Choose",
    description:
      "Select the workspace and booking period."
  },
  {
    number: "03",
    icon: CreditCard,
    title: "Book",
    description:
      "Complete your reservation securely."
  },
  {
    number: "04",
    icon: Rocket,
    title: "Work",
    description:
      "Receive confirmation and start working."
  }
];
</script>

<style scoped>
.process-badge,
.process-heading,
.process-description,
.process-step {
  opacity: 0;
}

.process-badge,
.process-heading,
.process-description {
  transform: translateY(12px);
}

.process-step {
  transform: translateY(18px);
}

.timeline-line {
  transform: scaleX(0);
  transform-origin: left;
}

.process-section.is-visible .process-badge {
  animation: process-reveal 450ms ease-out both;
}

.process-section.is-visible .process-heading {
  animation: process-reveal 480ms 120ms ease-out both;
}

.process-section.is-visible .process-description {
  animation: process-reveal 480ms 240ms ease-out both;
}

.process-section.is-visible .process-step {
  animation: step-reveal 550ms 820ms cubic-bezier(0.22, 1, 0.36, 1) both;
}

.process-section.is-visible .process-step-2 {
  animation-delay: 940ms;
}

.process-section.is-visible .process-step-3 {
  animation-delay: 1060ms;
}

.process-section.is-visible .process-step-4 {
  animation-delay: 1180ms;
}

.process-section.is-visible .process-icon-entrance {
  animation: icon-reveal 380ms 900ms ease-out both;
}

.process-section.is-visible .process-step-2 .process-icon-entrance {
  animation-delay: 1020ms;
}

.process-section.is-visible .process-step-3 .process-icon-entrance {
  animation-delay: 1140ms;
}

.process-section.is-visible .process-step-4 .process-icon-entrance {
  animation-delay: 1260ms;
}

.process-section.is-visible .process-number {
  animation: number-reveal 320ms 1000ms ease-out both;
}

.process-section.is-visible .process-step-2 .process-number {
  animation-delay: 1120ms;
}

.process-section.is-visible .process-step-3 .process-number {
  animation-delay: 1240ms;
}

.process-section.is-visible .process-step-4 .process-number {
  animation-delay: 1360ms;
}

@media (min-width: 1024px) {
  .process-section.is-visible .timeline-line {
    animation: draw-timeline 950ms 750ms ease-out both;
  }

  .process-section.is-visible .process-step {
    animation-delay: 1720ms;
  }

  .process-section.is-visible .process-step-2 {
    animation-delay: 1840ms;
  }

  .process-section.is-visible .process-step-3 {
    animation-delay: 1960ms;
  }

  .process-section.is-visible .process-step-4 {
    animation-delay: 2080ms;
  }

  .process-section.is-visible .process-icon-entrance {
    animation-delay: 1800ms;
  }

  .process-section.is-visible .process-step-2 .process-icon-entrance {
    animation-delay: 1920ms;
  }

  .process-section.is-visible .process-step-3 .process-icon-entrance {
    animation-delay: 2040ms;
  }

  .process-section.is-visible .process-step-4 .process-icon-entrance {
    animation-delay: 2160ms;
  }

  .process-section.is-visible .process-number {
    animation-delay: 1900ms;
  }

  .process-section.is-visible .process-step-2 .process-number {
    animation-delay: 2020ms;
  }

  .process-section.is-visible .process-step-3 .process-number {
    animation-delay: 2140ms;
  }

  .process-section.is-visible .process-step-4 .process-number {
    animation-delay: 2260ms;
  }
}

@keyframes process-reveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes draw-timeline {
  to {
    transform: scaleX(1);
  }
}

@keyframes step-reveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes icon-reveal {
  from {
    opacity: 0;
    transform: scale(0.92) rotate(-3deg);
  }

  to {
    opacity: 1;
    transform: scale(1) rotate(0);
  }
}

@keyframes number-reveal {
  from {
    opacity: 0;
    transform: translateY(6px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .process-badge,
  .process-heading,
  .process-description,
  .process-step,
  .process-icon-entrance,
  .process-icon,
  .process-number,
  .timeline-line {
    animation: none !important;
    opacity: 1;
    transform: none;
  }
}
</style>
