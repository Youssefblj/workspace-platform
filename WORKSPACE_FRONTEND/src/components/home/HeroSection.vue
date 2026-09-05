<template>
  <section
    ref="hero"
    class="relative overflow-hidden bg-gradient-to-br
           from-[#F9A825] via-[#FDBA12] to-[#F59E0B]"
  >
    <!-- Background Pattern -->
    <div
      class="absolute inset-0 opacity-[0.06]"
      style="
        background-image:
          radial-gradient(circle at 25% 25%, white 2px, transparent 2px),
          radial-gradient(circle at 75% 75%, white 2px, transparent 2px);
        background-size: 60px 60px;
      "
    />

    <!-- Animated Glow -->
    <div
      class="glow-one absolute -top-20 -left-20
             h-80 w-80 rounded-full bg-white/10 blur-3xl"
    />

    <div
      class="glow-two absolute -bottom-32 right-0
             h-[450px] w-[450px]
             rounded-full bg-orange-300/20 blur-3xl"
    />

    <div
      class="relative max-w-7xl mx-auto
             px-6 pt-10 pb-12
             lg:pt-14 lg:pb-14"
    >
      <div class="grid lg:grid-cols-2 gap-16 items-center">

        <!-- LEFT -->
        <div class="relative z-10">

          <!-- Badge -->
          <div
            class="hero-badge inline-flex items-center gap-2
                   bg-white/15 backdrop-blur-md
                   border border-white/20
                   text-white px-5 py-2
                   rounded-full mb-8"
          >
            <Sparkles class="sparkles w-5 h-5" />

            <span class="font-semibold">
              Flexible Workspace Platform
            </span>
          </div>

          <!-- Title -->
          <h1
            class="hero-title text-5xl md:text-7xl
                   font-extrabold leading-tight text-white"
          >
            <span class="title-line block overflow-hidden">
              <span class="title-inner block">
                Find Your
              </span>
            </span>

            <span class="title-line block overflow-hidden">
              <span class="title-inner block">
                Perfect Workspace
              </span>
            </span>
          </h1>

          <!-- Description -->
          <p
            class="hero-description mt-8
                   text-lg md:text-xl
                   text-orange-50 leading-9
                   max-w-xl"
          >
            Discover premium offices, coworking spaces, meeting rooms,
            and virtual offices designed to help freelancers,
            startups and growing companies work smarter.
          </p>

          <!-- Buttons -->
          <div class="hero-buttons flex flex-wrap gap-5 mt-10">

            <RouterLink
              to="/browse-offices"
              class="primary-button group
                     flex items-center gap-3
                     bg-white text-[#F9A825]
                     px-8 py-4 rounded-2xl
                     font-bold shadow-2xl
                     transition-shadow duration-300"
            >
              Browse Offices

              <ArrowRight
                class="w-5 h-5 transition-transform duration-300
                       group-hover:translate-x-2"
              />
            </RouterLink>

            <RouterLink
              to="/register"
              class="secondary-button
                     flex items-center gap-3
                     px-8 py-4 rounded-2xl
                     border border-white/40
                     text-white backdrop-blur-md
                     hover:bg-white/10 transition"
            >
              Get Started
            </RouterLink>

          </div>

          <!-- Trust -->
          <div class="trust-section flex flex-wrap gap-10 mt-14">

            <div class="trust-item flex items-center gap-3">
              <ShieldCheck class="w-8 h-8 text-white" />

              <div>
                <p class="text-white font-semibold">
                  Secure Booking
                </p>

                <p class="text-orange-100 text-sm">
                  Protected payments
                </p>
              </div>
            </div>

            <div class="trust-item flex items-center gap-3">
              <Clock3 class="w-8 h-8 text-white" />

              <div>
                <p class="text-white font-semibold">
                  Instant Confirmation
                </p>

                <p class="text-orange-100 text-sm">
                  Book within seconds
                </p>
              </div>
            </div>

          </div>
        </div>

        <!-- RIGHT -->
        <div
          class="hero-visual relative hidden lg:block"
          @mousemove="handleMouseMove"
          @mouseleave="resetMouseMove"
        >
          <!-- Main Card -->
          <div
            ref="officeCard"
            class="office-card relative
                   bg-white rounded-[40px]
                   p-8 shadow-2xl"
          >
            <div class="overflow-hidden rounded-3xl">
              <img
                src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=900&q=80"
                alt="Modern workspace"
                class="office-image rounded-3xl
                       h-[420px] w-full object-cover"
              />
            </div>

            <!-- Search -->
            <div
              class="float-card search-card
                     absolute left-6 top-8
                     bg-white rounded-2xl
                     shadow-xl px-5 py-4
                     flex items-center gap-3"
            >
              <Search class="w-5 h-5 text-[#F9A825]" />

              <div>
                <p class="font-semibold text-gray-900">
                  Casablanca Office
                </p>

                <p class="text-sm text-gray-500">
                  Available Today
                </p>
              </div>
            </div>

            <!-- Rating -->
            <div
              class="float-card rating-card
                     absolute right-5 bottom-8
                     bg-white rounded-2xl
                     shadow-xl px-5 py-4
                     flex gap-3 items-center"
            >
              <Star
                class="w-5 h-5
                       fill-yellow-400
                       text-yellow-400"
              />

              <div>
                <p class="font-bold text-gray-900">
                  4.9 Rating
                </p>

                <p class="text-sm text-gray-500">
                  1200+ Reviews
                </p>
              </div>
            </div>

          </div>

          <!-- Seats -->
          <div
            class="float-card seats-card
                   absolute -left-10 bottom-16
                   bg-white rounded-2xl
                   shadow-xl p-5"
          >
            <Users class="w-8 h-8 text-[#F9A825]" />

            <p class="font-bold mt-2">
              8 Seats
            </p>
          </div>

          <!-- Wifi -->
          <div
            class="float-card wifi-card
                   absolute right-0 -top-8
                   bg-white rounded-2xl
                   shadow-xl p-5"
          >
            <Wifi class="w-8 h-8 text-[#F9A825]" />

            <p class="font-bold mt-2">
              High Speed
            </p>
          </div>

        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import {
  ref,
  onMounted,
  onUnmounted
} from "vue";

import gsap from "gsap";

import {
  ArrowRight,
  Sparkles,
  Search,
  Star,
  ShieldCheck,
  Users,
  Wifi,
  Clock3
} from "lucide-vue-next";


const hero = ref(null);
const officeCard = ref(null);

let ctx;


/* -----------------------------
   Hero entrance
------------------------------ */

onMounted(() => {

  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  if (reduceMotion) return;

  /*
   * gsap.context keeps all selectors
   * scoped to this component.
   */
  ctx = gsap.context(() => {

    const tl = gsap.timeline({
      defaults: {
        ease: "power4.out"
      }
    });


    /* Badge */
    tl.from(".hero-badge", {
      opacity: 0,
      y: -25,
      scale: 0.92,
      duration: 0.7
    });


    /* Title lines */
    tl.from(
      ".title-inner",
      {
        yPercent: 115,
        opacity: 0,
        duration: 0.9,
        stagger: 0.12
      },
      "-=0.4"
    );


    /* Description */
    tl.from(
      ".hero-description",
      {
        opacity: 0,
        y: 30,
        duration: 0.7
      },
      "-=0.45"
    );


    /* CTA buttons */
    tl.from(
      ".hero-buttons > *",
      {
        opacity: 0,
        y: 25,
        scale: 0.95,
        duration: 0.6,
        stagger: 0.12
      },
      "-=0.4"
    );


    /* Trust elements */
    tl.from(
      ".trust-item",
      {
        opacity: 0,
        y: 20,
        duration: 0.55,
        stagger: 0.12
      },
      "-=0.3"
    );


    /*
     * Big visual enters
     * with 3D effect
     */
    tl.from(
      ".hero-visual",
      {
        opacity: 0,
        x: 100,
        rotationY: -14,
        rotationZ: 4,
        scale: 0.9,
        duration: 1.15,
        ease: "power4.out"
      },
      0.2
    );


    /* Image zoom */
    tl.from(
      ".office-image",
      {
        scale: 1.16,
        duration: 1.5,
        ease: "power3.out"
      },
      0.25
    );


    /* Floating cards entrance */
    tl.from(
      ".float-card",
      {
        opacity: 0,
        scale: 0.75,
        y: 30,
        duration: 0.65,
        stagger: 0.12,
        ease: "back.out(1.7)"
      },
      "-=0.65"
    );


    /* --------------------------------
       Continuous floating animations
    --------------------------------- */

    gsap.to(".search-card", {
      y: -10,
      rotation: 1,
      duration: 2.8,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });


    gsap.to(".rating-card", {
      y: 9,
      duration: 3.2,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut",
      delay: 0.4
    });


    gsap.to(".seats-card", {
      y: -12,
      rotation: -2,
      duration: 2.6,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut",
      delay: 0.8
    });


    gsap.to(".wifi-card", {
      y: -9,
      rotation: 2,
      duration: 3,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut",
      delay: 1
    });


    /* Sparkles icon */
    gsap.to(".sparkles", {
      rotation: 12,
      scale: 1.18,
      duration: 1.4,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });


    /* Background blobs */
    gsap.to(".glow-one", {
      x: 80,
      y: 40,
      scale: 1.15,
      duration: 7,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });


    gsap.to(".glow-two", {
      x: -70,
      y: -45,
      scale: 1.1,
      duration: 9,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });


    /* Button micro interaction */
    const primaryButton =
      hero.value.querySelector(".primary-button");

    if (primaryButton) {

      primaryButton.addEventListener(
        "mouseenter",
        buttonEnter
      );

      primaryButton.addEventListener(
        "mouseleave",
        buttonLeave
      );

    }

  }, hero.value);

});


/* -----------------------------
   Mouse 3D parallax
------------------------------ */

const handleMouseMove = (event) => {

  if (!officeCard.value) return;

  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  if (reduceMotion) return;


  const bounds =
    event.currentTarget.getBoundingClientRect();


  const mouseX =
    event.clientX - bounds.left;

  const mouseY =
    event.clientY - bounds.top;


  const centerX =
    bounds.width / 2;

  const centerY =
    bounds.height / 2;


  const rotateY =
    ((mouseX - centerX) / centerX) * 3;

  const rotateX =
    -((mouseY - centerY) / centerY) * 3;


  gsap.to(officeCard.value, {
    rotationY: rotateY,
    rotationX: rotateX,
    rotationZ: 1,
    transformPerspective: 1000,
    duration: 0.8,
    ease: "power3.out",
    overwrite: "auto"
  });

};


const resetMouseMove = () => {

  if (!officeCard.value) return;

  gsap.to(officeCard.value, {
    rotationX: 0,
    rotationY: 0,
    rotationZ: 2,
    duration: 1,
    ease: "power3.out"
  });

};


/* -----------------------------
   Button animation
------------------------------ */

const buttonEnter = (event) => {

  gsap.to(event.currentTarget, {
    y: -5,
    scale: 1.03,
    duration: 0.3,
    ease: "power2.out"
  });

};


const buttonLeave = (event) => {

  gsap.to(event.currentTarget, {
    y: 0,
    scale: 1,
    duration: 0.35,
    ease: "power2.out"
  });

};


/* -----------------------------
   Cleanup
------------------------------ */

onUnmounted(() => {

  ctx?.revert();

});
</script>

<style scoped>
.hero-visual {
  perspective: 1200px;
}

.office-card {
  transform-style: preserve-3d;
  will-change: transform;
}

.office-image {
  will-change: transform;
}

.float-card {
  z-index: 20;
  will-change: transform;
}

.primary-button,
.secondary-button {
  will-change: transform;
}
</style>