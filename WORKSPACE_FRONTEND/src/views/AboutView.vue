<template>

<main class="bg-[#F7F8FA]">

<!-- HERO -->

<section class="relative overflow-hidden">

  <!-- Background Decoration -->

  <div
    class="absolute top-0 right-0 w-[650px] h-[650px] rounded-full bg-[#F9A825]/10 blur-3xl">
  </div>

  <div
    class="absolute -left-40 bottom-0 w-[420px] h-[420px] rounded-full bg-[#F9A825]/5 blur-3xl">
  </div>

<div class="max-w-7xl mx-auto px-6 pt-14 pb-20 relative z-10">
    <div class="grid lg:grid-cols-2 gap-20 items-center">

      <!-- LEFT -->

      <div>

        <span
          class="inline-flex items-center gap-2
          bg-[#F9A825]/10
          text-[#F9A825]
          px-5
          py-2
          rounded-full
          font-semibold">

          <Sparkles class="w-4 h-4"/>

          About WorkSpace

        </span>

        <h1
          class="mt-8
          text-6xl
          lg:text-7xl
          font-black
          leading-tight
          text-[#1F2937]">

          Where

          <span class="text-[#F9A825]">

            Great Work

          </span>

          Begins.

        </h1>

        <p
          class="mt-10
          text-xl
          leading-10
          text-[#4B5563]
          max-w-xl">

          WorkSpace connects professionals, entrepreneurs,
          freelancers and growing businesses with inspiring office
          spaces designed for productivity, collaboration and success.

        </p>

        <div class="mt-12 flex flex-wrap gap-5">

          <RouterLink
            to="/browse-offices"
            class="inline-flex items-center gap-3
            bg-[#F9A825]
            hover:bg-[#e59c11]
            transition
            text-white
            font-semibold
            px-8
            py-4
            rounded-2xl">

            Explore Offices

            <ArrowRight class="w-5 h-5"/>

          </RouterLink>

          <RouterLink
            to="/contact"
            class="inline-flex items-center
            border
            border-[#E5E7EB]
            hover:border-[#F9A825]
            hover:text-[#F9A825]
            transition
            px-8
            py-4
            rounded-2xl
            font-semibold">

            Contact Us

          </RouterLink>

        </div>

      </div>

      <!-- RIGHT -->

      <div class="relative">

        <!-- Main Card -->

        <div
          class="bg-white
          rounded-[40px]
          shadow-xl
          border
          border-[#E5E7EB]
          p-10">

          <div
            class="w-20
            h-20
            rounded-3xl
            bg-[#F9A825]/10
            flex
            items-center
            justify-center">

            <Building2
              class="text-[#F9A825]"
              :size="40"/>

          </div>

          <h3
            class="mt-8
            text-3xl
            font-black
            text-[#1F2937]">

            More Than

            Office Rental

          </h3>

          <p
            class="mt-6
            leading-9
            text-[#4B5563]">

            We believe that every successful business starts with
            the right environment. Our mission is to simplify the
            way professionals discover, compare and book flexible
            workspaces.

          </p>

<!-- Real Statistics -->
<div
  class="grid grid-cols-3 gap-6 mt-10"
>
  <div>
    <h4
      class="text-3xl font-black text-[#F9A825]"
    >
      {{ stats.workspaces }}
    </h4>

    <p class="text-sm text-gray-500">
      Offices
    </p>
  </div>

  <div>
    <h4
      class="text-3xl font-black text-[#F9A825]"
    >
      {{ stats.cities }}
    </h4>

    <p class="text-sm text-gray-500">
      Cities
    </p>
  </div>

  <div>
    <h4
      class="text-3xl font-black text-[#F9A825]"
    >
      {{ stats.satisfaction }}%
    </h4>

    <p class="text-sm text-gray-500">
      Satisfaction
    </p>
  </div>
</div>

        </div>

        <!-- Floating Card -->
<div
  class="relative z-10 mx-auto -mt-8 mb-4 w-[340px]
         rounded-[26px] bg-[#1F2937] px-6 py-5
         text-white shadow-xl"
>
  <p
    class="text-xs uppercase tracking-wider text-gray-400"
  >
    Our Vision
  </p>

  <h4
    class="mt-1 text-lg font-bold"
  >
    Inspiring Better Workspaces.
  </h4>
</div>

      </div>

    </div>

  </div>

</section>
<!-- OUR JOURNEY -->

<section class="py-28 bg-white">

  <div class="max-w-7xl mx-auto px-6">

    <!-- Header -->

    <div class="max-w-3xl mb-20">

      <span
        class="inline-flex items-center gap-2
        bg-[#F9A825]/10
        text-[#F9A825]
        px-5 py-2
        rounded-full
        font-semibold">

        Our Journey

      </span>

      <h2
        class="mt-8
        text-5xl
        font-black
        text-[#1F2937]
        leading-tight">

        Every Great Workspace
        Starts With
        <span class="text-[#F9A825]">
          A Great Idea.
        </span>

      </h2>

    </div>

    <!-- Story 1 -->

    <div class="grid lg:grid-cols-2 gap-20 items-center">

      <!-- Visual -->

      <div>

        <div
          class="rounded-[36px]
          bg-[#F7F8FA]
          border
          border-[#E5E7EB]
          p-12
          h-[420px]
          flex
          flex-col
          justify-center">

          <div
            class="w-20 h-20
            rounded-3xl
            bg-[#F9A825]/10
            flex
            items-center
            justify-center">

            <Building2
              class="text-[#F9A825]"
              :size="42"/>

          </div>

          <h3
            class="mt-10
            text-3xl
            font-black
            text-[#1F2937]">

            It Started With
            One Question

          </h3>

          <p
            class="mt-6
            leading-9
            text-[#4B5563]">

            Why is finding the perfect office
            still so complicated?

          </p>

        </div>

      </div>

      <!-- Content -->

      <div>

        <span
          class="text-[#F9A825]
          font-bold
          uppercase
          tracking-[4px]">

          Chapter 01

        </span>

        <h3
          class="mt-6
          text-4xl
          font-black
          text-[#1F2937]">

          Simplifying
          Office Discovery

        </h3>

        <p
          class="mt-8
          text-lg
          leading-10
          text-[#4B5563]">

          Professionals waste valuable time comparing
          office spaces across multiple platforms.
          Our goal was simple:

          create one trusted place where businesses can
          easily discover, compare and reserve flexible
          workspaces without unnecessary complexity.

        </p>

      </div>

    </div>

    <!-- Story 2 -->

    <div
      class="grid lg:grid-cols-2 gap-20 items-center mt-32">

      <!-- Content -->

      <div class="order-2 lg:order-1">

        <span
          class="text-[#F9A825]
          font-bold
          uppercase
          tracking-[4px]">

          Chapter 02

        </span>

        <h3
          class="mt-6
          text-4xl
          font-black
          text-[#1F2937]">

          Building Trust
          Through Technology

        </h3>

        <p
          class="mt-8
          text-lg
          leading-10
          text-[#4B5563]">

          Every office listed on WorkSpace is presented
          with clear information, transparent pricing,
          real images and verified availability,
          allowing companies to make confident decisions.

        </p>

      </div>

      <!-- Visual -->

      <div class="order-1 lg:order-2">

        <div
          class="rounded-[36px]
          bg-[#1F2937]
          text-white
          h-[420px]
          p-12
          flex
          flex-col
          justify-center">

          <div
            class="w-20 h-20
            rounded-3xl
            bg-white/10
            flex
            items-center
            justify-center">

            <ShieldCheck
              class="text-[#F9A825]"
              :size="42"/>

          </div>

          <h3
            class="mt-10
            text-3xl
            font-black">

            Trust Comes
            First

          </h3>

          <p
            class="mt-6
            leading-9
            text-gray-300">

            Secure bookings.
            Transparent pricing.
            Reliable office partners.

          </p>

        </div>

      </div>

    </div>

  </div>

</section>

<!-- WHY WORKSPACE -->

<section class="py-28 bg-[#F7F8FA]">

  <div class="max-w-7xl mx-auto px-6">

    <!-- Heading -->

    <div class="text-center max-w-3xl mx-auto mb-20">

      <span
        class="inline-flex items-center gap-2
        bg-[#F9A825]/10
        text-[#F9A825]
        px-5 py-2
        rounded-full
        font-semibold">

        Why Choose Us

      </span>

      <h2
        class="mt-8
        text-5xl
        font-black
        text-[#1F2937]">

        Designed Around
        The Way
        <span class="text-[#F9A825]">
          You Work
        </span>

      </h2>

      <p
        class="mt-6
        text-lg
        text-[#4B5563]
        leading-9">

        Every feature is built to simplify office discovery,
        save valuable time and create a seamless booking experience.

      </p>

    </div>

    <!-- Bento Grid -->

    <div class="grid lg:grid-cols-4 gap-6">

      <!-- Large Card -->

      <div
        class="lg:col-span-2
        bg-white
        rounded-[32px]
        border border-[#E5E7EB]
        p-10
        hover:shadow-xl
        transition">

        <div
          class="w-16 h-16
          rounded-2xl
          bg-[#F9A825]/10
          flex items-center justify-center">

          <Rocket
            class="text-[#F9A825]"
            :size="34"/>

        </div>

        <h3
          class="mt-8
          text-3xl
          font-black
          text-[#1F2937]">

          Fast Office Booking

        </h3>

        <p
          class="mt-6
          text-[#4B5563]
          leading-9">

          Browse available workspaces,
          compare options and complete your reservation
          within minutes.

        </p>

      </div>

      <!-- Small -->

      <div
        class="bg-[#1F2937]
        rounded-[32px]
        p-8
        text-white
        hover:-translate-y-2
        transition">

        <Users
          class="text-[#F9A825]"
          :size="34"/>

        <h3
          class="mt-8
          text-2xl
          font-bold">

          Built
          For Everyone

        </h3>

        <p
          class="mt-5
          text-gray-300
          leading-8">

          Freelancers,
          startups,
          agencies,
          and enterprises.

        </p>

      </div>

      <!-- Small -->

      <div
        class="bg-white
        rounded-[32px]
        border border-[#E5E7EB]
        p-8
        hover:border-[#F9A825]
        transition">

        <BriefcaseBusiness
          class="text-[#F9A825]"
          :size="34"/>

        <h3
          class="mt-8
          text-2xl
          font-bold
          text-[#1F2937]">

          Flexible
          Workspaces

        </h3>

        <p
          class="mt-5
          text-[#4B5563]
          leading-8">

          Hourly,
          daily
          and monthly rentals.

        </p>

      </div>

      <!-- Wide -->

      <div
        class="lg:col-span-2
        bg-[#F9A825]
        rounded-[32px]
        p-10
        text-white
        hover:scale-[1.02]
        transition">

        <Target
          :size="38"/>

        <h3
          class="mt-8
          text-3xl
          font-black">

          Our Mission

        </h3>

        <p
          class="mt-6
          leading-9">

          To become the easiest and most trusted platform
          for discovering and booking professional workspaces.

        </p>

      </div>

      <!-- Wide -->

      <div
        class="lg:col-span-2
        bg-white
        rounded-[32px]
        border border-[#E5E7EB]
        p-10
        hover:shadow-xl
        transition">

        <Building2
          class="text-[#F9A825]"
          :size="38"/>

        <h3
          class="mt-8
          text-3xl
          font-black
          text-[#1F2937]">

          Verified Offices

        </h3>

        <p
          class="mt-6
          leading-9
          text-[#4B5563]">

          Every listing includes detailed information,
          pricing transparency,
          images,
          amenities,
          and availability updates.

        </p>

      </div>

    </div>

  </div>

</section>
<!-- BY THE NUMBERS -->

<section class="bg-[#1F2937] py-28 overflow-hidden">

  <div class="max-w-7xl mx-auto px-6">

    <!-- Header -->

    <div class="text-center max-w-3xl mx-auto">

      <span
        class="inline-flex items-center gap-2
        bg-white/10
        text-[#F9A825]
        px-5 py-2
        rounded-full
        font-semibold">

        By The Numbers

      </span>

      <h2
        class="mt-8
        text-5xl
        font-black
        text-white">

        Trusted By
        Professionals
        Every Day

      </h2>

      <p
        class="mt-6
        text-lg
        leading-9
        text-gray-300">

        Every reservation represents a business,
        a meeting,
        a startup,
        or an entrepreneur taking the next step.

      </p>

    </div>

<!-- Numbers -->
<div
  class="grid md:grid-cols-2 lg:grid-cols-4 gap-10 mt-24"
>
  <!-- Offices -->
  <div class="text-center">

    <h3
      class="text-7xl font-black text-[#F9A825]"
    >
      {{ stats.workspaces }}
    </h3>

    <div
      class="w-16 h-1 bg-[#F9A825] mx-auto my-6 rounded-full"
    />

    <p
      class="text-xl text-white font-semibold"
    >
      Premium Offices
    </p>

  </div>

  <!-- Cities -->
  <div class="text-center">

    <h3
      class="text-7xl font-black text-[#F9A825]"
    >
      {{ stats.cities }}
    </h3>

    <div
      class="w-16 h-1 bg-[#F9A825] mx-auto my-6 rounded-full"
    />

    <p
      class="text-xl text-white font-semibold"
    >
      Cities Covered
    </p>

  </div>

  <!-- Bookings -->
  <div class="text-center">

    <h3
      class="text-7xl font-black text-[#F9A825]"
    >
      {{ stats.bookings.toLocaleString() }}
    </h3>

    <div
      class="w-16 h-1 bg-[#F9A825] mx-auto my-6 rounded-full"
    />

    <p
      class="text-xl text-white font-semibold"
    >
      Successful Bookings
    </p>

  </div>

  <!-- Satisfaction -->
  <div class="text-center">

    <h3
      class="text-7xl font-black text-[#F9A825]"
    >
      {{ stats.satisfaction }}%
    </h3>

    <div
      class="w-16 h-1 bg-[#F9A825] mx-auto my-6 rounded-full"
    />

    <p
      class="text-xl text-white font-semibold"
    >
      Customer Satisfaction
    </p>

  </div>
</div>

  </div>

</section>
<!-- FINAL CTA -->

<section class="relative py-28 overflow-hidden">

  <!-- Background Decoration -->

  <div
    class="absolute -top-32 -right-32 w-96 h-96 rounded-full bg-[#F9A825]/10 blur-3xl">
  </div>

  <div
    class="absolute -bottom-32 -left-32 w-80 h-80 rounded-full bg-[#F9A825]/10 blur-3xl">
  </div>

  <div class="max-w-6xl mx-auto px-6 relative z-10">

    <div
      class="bg-white
      border border-[#E5E7EB]
      rounded-[40px]
      overflow-hidden
      shadow-xl">

      <div
        class="grid lg:grid-cols-2">

        <!-- Left -->

        <div class="p-12 lg:p-16">

          <span
            class="inline-flex items-center gap-2
            bg-[#F9A825]/10
            text-[#F9A825]
            px-5 py-2
            rounded-full
            font-semibold">

            Start Today

          </span>

          <h2
            class="mt-8
            text-5xl
            font-black
            leading-tight
            text-[#1F2937]">

            Ready To Find
            Your Next

            <span class="text-[#F9A825]">
              Workspace?
            </span>

          </h2>

          <p
            class="mt-8
            text-lg
            leading-9
            text-[#4B5563]
            max-w-lg">

            Whether you're a freelancer, startup, or growing company,
            WorkSpace helps you discover flexible offices that fit
            your needs and your budget.

          </p>

        </div>

        <!-- Right -->

        <div
          class="bg-[#1F2937]
          p-12 lg:p-16
          flex flex-col
          justify-center">

          <div class="space-y-6">

            <RouterLink
              to="/"
              class="flex items-center justify-between
              bg-[#F9A825]
              hover:bg-[#e59d12]
              transition
              text-white
              rounded-2xl
              px-8
              py-5
              font-bold">

              Browse Available Offices

              <ArrowRight class="w-6 h-6"/>

            </RouterLink>

            <RouterLink
              to="/contact"
              class="flex items-center justify-between
              border
              border-white/20
              hover:border-[#F9A825]
              hover:text-[#F9A825]
              transition
              text-white
              rounded-2xl
              px-8
              py-5
              font-semibold">

              Contact Our Team

              <ArrowRight class="w-6 h-6"/>

            </RouterLink>

          </div>

          <!-- Bottom -->

          <div
            class="mt-12
            pt-10
            border-t border-white/10">

            <p
              class="text-gray-400
              leading-8">

              Join hundreds of professionals who trust
              WorkSpace to discover productive,
              flexible and inspiring places to work.

            </p>

          </div>

        </div>

      </div>

    </div>

  </div>

</section>

</main>

</template>

<script setup>
import {
  ref,
  onMounted
} from "vue";

import {
  Building2,
  ArrowRight,
  Sparkles,
  ShieldCheck,
  Rocket,
  Users,
  BriefcaseBusiness,
  Target
} from "lucide-vue-next";

import api from "@/services/api";

const stats = ref({
  workspaces: 0,
  members: 0,
  bookings: 0,
  cities: 0,
  average_rating: 0,
  satisfaction: 0
});

const loadingStats = ref(false);

const fetchStats = async () => {
  loadingStats.value = true;

  try {
    const response = await api.get(
      "dashboard/public-stats/"
    );

    const data = response.data;

    stats.value = {
      workspaces:
        Number(data.workspaces || 0),

      members:
        Number(data.members || 0),

      bookings:
        Number(data.bookings || 0),

      cities:
        Number(data.cities || 0),

      average_rating:
        Number(data.average_rating || 0),

      satisfaction:
        Number(data.satisfaction || 0)
    };

  } catch (error) {
    console.error(
      "Failed to load About Us stats:",
      error
    );

  } finally {
    loadingStats.value = false;
  }
};

onMounted(() => {
  fetchStats();
});
</script>

