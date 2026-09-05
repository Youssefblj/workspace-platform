<script setup>
import {
  ShieldCheck,
  Eye,
  UserRound,
  Database,
  CalendarDays,
  CreditCard,
  Activity,
  Settings2,
  Building2,
  BellRing,
  Sparkles,
  BadgeCheck,
  Pencil,
  Download,
  Trash2,
  MessageCircle,
  Lock,
  ArrowRight
} from "lucide-vue-next"
</script>


<template>
    <div>
  <main class="bg-[#F7F8FA] min-h-screen">

    <!-- Hero -->
    <section class="max-w-7xl mx-auto px-6 pt-7 pb-16">

      <div
        class="bg-white rounded-[36px] overflow-hidden border border-[#E5E7EB] shadow-sm grid lg:grid-cols-2">

        <!-- Left -->
        <div class="p-14 flex flex-col justify-center">

          <div
            class="inline-flex items-center gap-2 bg-[#F9A825]/10 text-[#F9A825] px-5 py-2 rounded-full font-semibold w-fit mb-8">

            <ShieldCheck class="w-5 h-5" />

            Privacy Policy

          </div>

          <h1
            class="text-5xl lg:text-6xl font-black leading-tight text-[#1F2937]">

            Your Privacy

            <span class="text-[#F9A825]">

              Comes First

            </span>

          </h1>

          <p
            class="mt-8 text-xl leading-10 text-[#374151] max-w-xl">

            We believe transparency creates trust.
            This page explains how WorkSpace collects,
            uses, stores and protects your information while
            you use our platform.

          </p>

          <div class="flex gap-5 mt-10">

            <button
              class="bg-[#F9A825] hover:bg-[#e39c13]
              text-white font-semibold
              px-8 py-4 rounded-2xl transition">

              Contact Privacy Team

            </button>

            <button
              class="border border-[#E5E7EB]
              hover:border-[#F9A825]
              hover:text-[#F9A825]
              transition
              px-8 py-4 rounded-2xl
              font-semibold
              text-[#1F2937]">

              Learn More

            </button>

          </div>

        </div>

        <!-- Right -->

        <div
          class="bg-[#1F2937]
          p-14
          flex
          flex-col
          justify-center
          gap-8">

          <div
            class="bg-white/10 rounded-3xl p-8 flex items-center gap-6">

            <Eye class="text-[#F9A825]" :size="42"/>

            <div>

              <h3
                class="text-white text-2xl font-bold">

                Transparency

              </h3>

              <p class="text-gray-300 mt-2">

                We clearly explain what data we collect
                and why.

              </p>

            </div>

          </div>

          <div
            class="bg-white/10 rounded-3xl p-8 flex items-center gap-6">

            <ShieldCheck
              class="text-[#F9A825]"
              :size="42"/>

            <div>

              <h3
                class="text-white text-2xl font-bold">

                Security

              </h3>

              <p class="text-gray-300 mt-2">

                Industry-standard protection keeps your
                information secure.

              </p>

            </div>

          </div>

          <div
            class="bg-white/10 rounded-3xl p-8 flex items-center gap-6">

            <UserRound
              class="text-[#F9A825]"
              :size="42"/>

            <div>

              <h3
                class="text-white text-2xl font-bold">

                Your Control

              </h3>

              <p class="text-gray-300 mt-2">

                You remain in control of your personal
                information at all times.

              </p>

            </div>

          </div>

        </div>

      </div>

    </section>

  </main>





<!-- Information We Collect -->

<section class="max-w-7xl mx-auto px-6 py-20">

  <div class="text-center mb-16">

    <span
      class="inline-flex items-center gap-2
      bg-[#F9A825]/10
      text-[#F9A825]
      px-5 py-2
      rounded-full
      font-semibold">

      <Database class="w-5 h-5"/>

      Information We Collect

    </span>

    <h2
      class="mt-6
      text-5xl
      font-black
      text-[#1F2937]">

      Only What We Need

    </h2>

    <p
      class="mt-5
      max-w-3xl
      mx-auto
      text-xl
      text-[#374151]
      leading-9">

      We collect only the information required to provide a
      secure booking experience, improve our services and
      support your WorkSpace account.

    </p>

  </div>

  <div
    class="grid
    lg:grid-cols-2
    gap-8">

    <!-- Card -->

    <div
      class="group
      bg-white
      rounded-3xl
      border
      border-[#E5E7EB]
      p-10
      hover:border-[#F9A825]
      hover:shadow-xl
      transition-all
      duration-300">

      <div
        class="w-16 h-16
        rounded-2xl
        bg-[#F9A825]/10
        flex
        items-center
        justify-center
        mb-8">

        <UserRound
          class="text-[#F9A825]"
          :size="30"/>

      </div>

      <h3
        class="text-2xl
        font-bold
        text-[#1F2937]
        mb-5">

        Account Information

      </h3>

      <ul
        class="space-y-4
        text-[#374151]">

        <li>• Full name</li>

        <li>• Email address</li>

        <li>• Phone number</li>

        <li>• Profile photo (optional)</li>

      </ul>

    </div>

    <!-- Card -->

    <div
      class="group
      bg-white
      rounded-3xl
      border
      border-[#E5E7EB]
      p-10
      hover:border-[#F9A825]
      hover:shadow-xl
      transition-all">

      <div
        class="w-16 h-16
        rounded-2xl
        bg-[#F9A825]/10
        flex
        items-center
        justify-center
        mb-8">

        <CalendarDays
          class="text-[#F9A825]"
          :size="30"/>

      </div>

      <h3
        class="text-2xl
        font-bold
        text-[#1F2937]
        mb-5">

        Booking Activity

      </h3>

      <ul
        class="space-y-4
        text-[#374151]">

        <li>• Reservation history</li>

        <li>• Booking dates</li>

        <li>• Workspace preferences</li>

        <li>• Reviews & ratings</li>

      </ul>

    </div>

    <!-- Card -->

    <div
      class="group
      bg-white
      rounded-3xl
      border
      border-[#E5E7EB]
      p-10
      hover:border-[#F9A825]
      hover:shadow-xl
      transition-all">

      <div
        class="w-16 h-16
        rounded-2xl
        bg-[#F9A825]/10
        flex
        items-center
        justify-center
        mb-8">

        <CreditCard
          class="text-[#F9A825]"
          :size="30"/>

      </div>

      <h3
        class="text-2xl
        font-bold
        text-[#1F2937]
        mb-5">

        Payment Details

      </h3>

      <ul
        class="space-y-4
        text-[#374151]">

        <li>• Secure payment records</li>

        <li>• Transaction history</li>

        <li>• Billing information</li>

        <li>• Refund requests</li>

      </ul>

    </div>

    <!-- Card -->

    <div
      class="group
      bg-white
      rounded-3xl
      border
      border-[#E5E7EB]
      p-10
      hover:border-[#F9A825]
      hover:shadow-xl
      transition-all">

      <div
        class="w-16 h-16
        rounded-2xl
        bg-[#F9A825]/10
        flex
        items-center
        justify-center
        mb-8">

        <Activity
          class="text-[#F9A825]"
          :size="30"/>

      </div>

      <h3
        class="text-2xl
        font-bold
        text-[#1F2937]
        mb-5">

        Technical Data

      </h3>

      <ul
        class="space-y-4
        text-[#374151]">

        <li>• Browser information</li>

        <li>• Device type</li>

        <li>• IP address</li>

        <li>• Security logs</li>

      </ul>

    </div>

  </div>

</section>

<!-- How We Use Your Information -->

<section class="max-w-7xl mx-auto px-6 py-20">

  <div class="text-center mb-20">

    <span
      class="inline-flex items-center gap-2
      bg-[#F9A825]/10
      text-[#F9A825]
      px-5 py-2
      rounded-full
      font-semibold">

      <Settings2 class="w-5 h-5"/>

      How We Use Your Information

    </span>

    <h2
      class="mt-6
      text-5xl
      font-black
      text-[#1F2937]">

      Every Piece Of Data

      <span class="text-[#F9A825]">

        Has A Purpose

      </span>

    </h2>

    <p
      class="mt-6
      text-xl
      text-[#374151]
      max-w-3xl
      mx-auto
      leading-9">

      We never collect information without a reason.
      Every detail helps us improve your booking experience
      while keeping your account secure.

    </p>

  </div>

  <div class="relative max-w-5xl mx-auto">

    <!-- Vertical Line -->

    <div
      class="absolute
      left-8
      top-0
      bottom-0
      w-0.5
      bg-[#F9A825]/20">
    </div>

    <!-- Item 1 -->

    <div class="relative flex gap-8 mb-14">

      <div
        class="w-16 h-16
        rounded-full
        bg-[#F9A825]
        text-white
        flex
        items-center
        justify-center
        shadow-lg
        shrink-0">

        <Building2 :size="28"/>

      </div>

      <div
        class="bg-white
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        flex-1">

        <h3
          class="text-2xl
          font-bold
          text-[#1F2937]">

          Workspace Reservations

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          Your booking information is used to reserve
          offices, manage schedules, prevent double bookings,
          and allow workspace owners to prepare your visit.

        </p>

      </div>

    </div>

    <!-- Item 2 -->

    <div class="relative flex gap-8 mb-14">

      <div
        class="w-16 h-16
        rounded-full
        bg-[#F9A825]
        text-white
        flex
        items-center
        justify-center
        shadow-lg
        shrink-0">

        <ShieldCheck :size="28"/>

      </div>

      <div
        class="bg-white
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        flex-1">

        <h3
          class="text-2xl
          font-bold
          text-[#1F2937]">

          Security & Fraud Prevention

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          We continuously monitor suspicious activity,
          protect user accounts, and secure all transactions
          to maintain a trusted platform.

        </p>

      </div>

    </div>

    <!-- Item 3 -->

    <div class="relative flex gap-8 mb-14">

      <div
        class="w-16 h-16
        rounded-full
        bg-[#F9A825]
        text-white
        flex
        items-center
        justify-center
        shadow-lg
        shrink-0">

        <BellRing :size="28"/>

      </div>

      <div
        class="bg-white
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        flex-1">

        <h3
          class="text-2xl
          font-bold
          text-[#1F2937]">

          Important Notifications

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          We send booking confirmations,
          reservation reminders,
          payment receipts,
          and important account updates.

        </p>

      </div>

    </div>

    <!-- Item 4 -->

    <div class="relative flex gap-8">

      <div
        class="w-16 h-16
        rounded-full
        bg-[#F9A825]
        text-white
        flex
        items-center
        justify-center
        shadow-lg
        shrink-0">

        <Sparkles :size="28"/>

      </div>

      <div
        class="bg-white
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        flex-1">

        <h3
          class="text-2xl
          font-bold
          text-[#1F2937]">

          Improving Your Experience

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          Anonymous analytics help us understand how
          WorkSpace is used so we can improve performance,
          usability and future features.

        </p>

      </div>

    </div>

  </div>

</section>

<!-- Your Privacy Rights -->

<section class="bg-white py-24">

  <div class="max-w-7xl mx-auto px-6">

    <!-- Heading -->

    <div class="text-center mb-16">

      <span
        class="inline-flex items-center gap-2
        bg-[#F9A825]/10
        text-[#F9A825]
        px-5 py-2
        rounded-full
        font-semibold">

        <BadgeCheck class="w-5 h-5"/>

        Your Privacy Rights

      </span>

      <h2
        class="mt-6
        text-5xl
        font-black
        text-[#1F2937]">

        You're Always

        <span class="text-[#F9A825]">

          In Control

        </span>

      </h2>

      <p
        class="mt-6
        max-w-3xl
        mx-auto
        text-xl
        text-[#374151]
        leading-9">

        We believe your personal information belongs to you.
        Our platform provides transparency and gives you
        control over your data.

      </p>

    </div>

    <!-- Cards -->

    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

      <!-- Card -->

      <div
        class="group
        bg-[#F7F8FA]
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        hover:border-[#F9A825]
        hover:-translate-y-2
        hover:shadow-xl
        transition-all duration-300">

        <div
          class="w-16 h-16
          rounded-2xl
          bg-[#F9A825]/10
          flex items-center justify-center">

          <Eye
            class="text-[#F9A825]"
            :size="30"/>

        </div>

        <h3
          class="mt-8
          text-2xl
          font-bold
          text-[#1F2937]">

          Access Your Data

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          Request access to the personal information
          associated with your account at any time.

        </p>

      </div>

      <!-- Card -->

      <div
        class="group
        bg-[#F7F8FA]
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        hover:border-[#F9A825]
        hover:-translate-y-2
        hover:shadow-xl
        transition-all">

        <div
          class="w-16 h-16
          rounded-2xl
          bg-[#F9A825]/10
          flex items-center justify-center">

          <Pencil
            class="text-[#F9A825]"
            :size="30"/>

        </div>

        <h3
          class="mt-8
          text-2xl
          font-bold
          text-[#1F2937]">

          Update Information

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          Keep your profile information accurate and
          up to date from your account dashboard.

        </p>

      </div>

      <!-- Card -->

      <div
        class="group
        bg-[#F7F8FA]
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        hover:border-[#F9A825]
        hover:-translate-y-2
        hover:shadow-xl
        transition-all">

        <div
          class="w-16 h-16
          rounded-2xl
          bg-[#F9A825]/10
          flex items-center justify-center">

          <Download
            class="text-[#F9A825]"
            :size="30"/>

        </div>

        <h3
          class="mt-8
          text-2xl
          font-bold
          text-[#1F2937]">

          Data Portability

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          You may request a copy of your personal
          information when applicable.

        </p>

      </div>

      <!-- Card -->

      <div
        class="group
        bg-[#F7F8FA]
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        hover:border-[#F9A825]
        hover:-translate-y-2
        hover:shadow-xl
        transition-all">

        <div
          class="w-16 h-16
          rounded-2xl
          bg-[#F9A825]/10
          flex items-center justify-center">

          <Trash2
            class="text-[#F9A825]"
            :size="30"/>

        </div>

        <h3
          class="mt-8
          text-2xl
          font-bold
          text-[#1F2937]">

          Account Removal

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          Contact our support team if you wish to
          permanently remove your account.

        </p>

      </div>

      <!-- Card -->

      <div
        class="group
        bg-[#F7F8FA]
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        hover:border-[#F9A825]
        hover:-translate-y-2
        hover:shadow-xl
        transition-all">

        <div
          class="w-16 h-16
          rounded-2xl
          bg-[#F9A825]/10
          flex items-center justify-center">

          <ShieldCheck
            class="text-[#F9A825]"
            :size="30"/>

        </div>

        <h3
          class="mt-8
          text-2xl
          font-bold
          text-[#1F2937]">

          Security & Consent

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          Manage communication preferences and stay
          informed about how your information is protected.

        </p>

      </div>

      <!-- Card -->

      <div
        class="group
        bg-[#F7F8FA]
        rounded-3xl
        border
        border-[#E5E7EB]
        p-8
        hover:border-[#F9A825]
        hover:-translate-y-2
        hover:shadow-xl
        transition-all">

        <div
          class="w-16 h-16
          rounded-2xl
          bg-[#F9A825]/10
          flex items-center justify-center">

          <MessageCircle
            class="text-[#F9A825]"
            :size="30"/>

        </div>

        <h3
          class="mt-8
          text-2xl
          font-bold
          text-[#1F2937]">

          Contact Our Team

        </h3>

        <p
          class="mt-4
          text-[#374151]
          leading-8">

          Questions about privacy?
          Our support team is always available
          to help.

        </p>

      </div>

    </div>

  </div>

</section>
<!-- Data Security -->

<section class="py-24 bg-[#F7F8FA]">

  <div class="max-w-7xl mx-auto px-6">

    <div class="grid lg:grid-cols-2 gap-16 items-center">

      <!-- Left -->

      <div>

        <span
          class="inline-flex items-center gap-2
          bg-[#F9A825]/10
          text-[#F9A825]
          px-5 py-2
          rounded-full
          font-semibold">

          <Lock class="w-5 h-5"/>

          Data Security

        </span>

        <h2
          class="mt-6
          text-5xl
          font-black
          text-[#1F2937]">

          Keeping Your
          Information Safe

        </h2>

        <p
          class="mt-8
          text-xl
          text-[#374151]
          leading-9">

          Security is integrated into every part of WorkSpace.
          We use modern technologies and internal procedures
          to protect your information from unauthorized access,
          accidental loss and misuse.

        </p>

        <div class="mt-10 space-y-6">

          <div class="flex items-center gap-4">

            <ShieldCheck class="text-[#F9A825]" :size="26"/>

            <span class="text-[#374151]">
              Encrypted communication (HTTPS)
            </span>

          </div>

          <div class="flex items-center gap-4">

            <Database class="text-[#F9A825]" :size="26"/>

            <span class="text-[#374151]">
              Secure database storage
            </span>

          </div>

          <div class="flex items-center gap-4">

            <BadgeCheck class="text-[#F9A825]" :size="26"/>

            <span class="text-[#374151]">
              Restricted administrative access
            </span>

          </div>

          <div class="flex items-center gap-4">

            <Activity class="text-[#F9A825]" :size="26"/>

            <span class="text-[#374151]">
              Continuous monitoring & maintenance
            </span>

          </div>

        </div>

      </div>

      <!-- Right -->

      <div class="space-y-6">

        <div
          class="bg-white
          rounded-3xl
          border
          border-[#E5E7EB]
          p-8">

          <div class="flex justify-between mb-3">

            <span class="font-semibold text-[#1F2937]">

              Secure Infrastructure

            </span>

            <span class="text-[#F9A825] font-bold">

              100%

            </span>

          </div>

          <div
            class="w-full h-3 rounded-full bg-gray-200">

            <div
              class="h-3 rounded-full bg-[#F9A825]"
              style="width:100%">
            </div>

          </div>

        </div>

        <div
          class="bg-white
          rounded-3xl
          border
          border-[#E5E7EB]
          p-8">

          <div class="flex justify-between mb-3">

            <span class="font-semibold text-[#1F2937]">

              Data Encryption

            </span>

            <span class="text-[#F9A825] font-bold">

              Enabled

            </span>

          </div>

          <div
            class="w-full h-3 rounded-full bg-gray-200">

            <div
              class="h-3 rounded-full bg-[#F9A825]"
              style="width:100%">
            </div>

          </div>

        </div>

        <div
          class="bg-white
          rounded-3xl
          border
          border-[#E5E7EB]
          p-8">

          <div class="flex justify-between mb-3">

            <span class="font-semibold text-[#1F2937]">

              Privacy Compliance

            </span>

            <span class="text-[#F9A825] font-bold">

              Continuous

            </span>

          </div>

          <div
            class="w-full h-3 rounded-full bg-gray-200">

            <div
              class="h-3 rounded-full bg-[#F9A825]"
              style="width:100%">
            </div>

          </div>

        </div>

      </div>

    </div>

  </div>

</section>
<!-- Contact -->

<section class="py-24 bg-white">

  <div class="max-w-5xl mx-auto px-6">

    <div
      class="bg-[#1F2937]
      rounded-[40px]
      p-16
      text-center">

      <div
        class="w-20 h-20
        rounded-full
        bg-[#F9A825]/20
        flex
        items-center
        justify-center
        mx-auto mb-8">

        <MessageCircle
          class="text-[#F9A825]"
          :size="38"/>

      </div>

      <h2
        class="text-5xl
        font-black
        text-white">

        Questions About Privacy?

      </h2>

      <p
        class="mt-8
        text-xl
        leading-9
        text-gray-300
        max-w-3xl
        mx-auto">

        If you have any questions regarding this Privacy Policy
        or how your information is handled, our team will be
        happy to assist you.

      </p>

      <RouterLink
        to="/contact"
        class="inline-flex
        items-center
        gap-3
        mt-10
        bg-[#F9A825]
        hover:bg-[#e39c13]
        px-8
        py-4
        rounded-2xl
        text-white
        font-semibold
        transition">

        Contact Us

        <ArrowRight :size="20"/>

      </RouterLink>

      <p
        class="mt-8
        text-sm
        text-gray-400">

        Last updated • July 2026

      </p>

    </div>

  </div>

</section>
</div>
</template>