<template>
  <div class="bg-[#F7F8FA] min-h-screen">

    <!-- Hero -->
    <section class="bg-[#1F2937] text-white">
      <div class="max-w-6xl mx-auto px-6 py-20 text-center">

        <span
          class="inline-flex px-5 py-2 rounded-full bg-[#F9A825]/20 text-[#F9A825] border border-[#F9A825]/30 font-medium">
          Legal Agreement
        </span>

        <h1 class="mt-6 text-5xl font-extrabold">
          Terms &
          <span class="text-[#F9A825]">Conditions</span>
        </h1>

        <p class="mt-6 text-gray-300 max-w-3xl mx-auto leading-8">
          Everything you need to know before using WorkSpace.
          These terms protect both you and workspace owners while ensuring
          a secure booking experience.
        </p>

      </div>
    </section>

    <!-- Timeline -->

    <section class="max-w-6xl mx-auto px-6 py-20">

      <div class="relative">

        <!-- Vertical Line -->

        <div
          class="hidden md:block absolute left-1/2 top-0 bottom-0 w-1 bg-[#E5E7EB] -translate-x-1/2">
        </div>

        <div
          v-for="(item,index) in terms"
          :key="item.id"
          class="relative mb-14">

          <div
            :class="[
              'flex items-center',
              index % 2 === 0
                ? 'md:flex-row'
                : 'md:flex-row-reverse'
            ]">

            <!-- Card -->

            <div class="md:w-1/2">

              <div
                class="bg-white rounded-3xl border border-[#E5E7EB] shadow-sm p-8 hover:shadow-xl transition">

                <div class="flex items-center gap-4 mb-5">

                  <div
                    class="w-14 h-14 rounded-2xl bg-[#F9A825] text-white flex items-center justify-center font-bold text-lg">
                    {{ item.id }}
                  </div>

                  <h2
                    class="text-2xl font-bold text-[#1F2937]">
                    {{ item.title }}
                  </h2>

                </div>

                <p
                  class="text-[#374151] leading-8">
                  {{ item.description }}
                </p>

              </div>

            </div>

            <!-- Timeline Dot -->

            <div
              class="hidden md:flex w-12 justify-center">

              <div
                class="w-6 h-6 rounded-full bg-[#F9A825] border-4 border-white shadow">
              </div>

            </div>

            <div class="md:w-1/2"></div>

          </div>

        </div>

      </div>

    </section>

    <!-- Agreement -->

    <section class="max-w-5xl mx-auto px-6 pb-24">

      <div
        class="bg-[#1F2937] rounded-3xl p-10 text-center">

        <h2
          class="text-3xl font-bold text-white">
          By Using WorkSpace
        </h2>

        <p
          class="mt-5 text-gray-300 leading-8 max-w-3xl mx-auto">
          By creating an account, booking an office,
          or using any feature of WorkSpace,
          you acknowledge that you have read,
          understood and agreed to these Terms &
          Conditions.
        </p>

        <RouterLink
          to="/privacy-policy"
          class="inline-flex mt-8 bg-[#F9A825] hover:bg-yellow-600 text-white px-8 py-3 rounded-xl font-semibold transition">

          Read Privacy Policy

        </RouterLink>

      </div>

    </section>

  </div>
</template>

<script setup>

const terms = [

{
id:'01',
title:'Create an Account',
description:'Provide accurate information when registering. You are responsible for maintaining the confidentiality of your account credentials.'
},

{
id:'02',
title:'Book a Workspace',
description:'Reservations are confirmed only after successful payment. Availability depends on the workspace provider.'
},

{
id:'03',
title:'Payments',
description:'Payments are securely processed through our payment gateway. Prices displayed include applicable booking charges.'
},

{
id:'04',
title:'Cancellation',
description:'Cancellation and refund policies depend on the selected workspace. Please review the provider policy before booking.'
},

{
id:'05',
title:'User Responsibilities',
description:'Respect office rules, maintain professional behavior, and avoid any illegal or abusive activities while using rented workspaces.'
},

{
id:'06',
title:'Platform Responsibility',
description:'WorkSpace connects customers with office providers. We facilitate bookings but are not responsible for disputes between users and providers.'
},

{
id:'07',
title:'Updates',
description:'These Terms & Conditions may change over time. Continued use of the platform means you accept any future updates.'
}

]

</script>