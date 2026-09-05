<script setup>
import api from "@/services/api"
import { onMounted } from "vue"
import { useRouter } from "vue-router"
import {

ref,

computed,

watch

} from "vue"
import {
  BadgeDollarSign,
  CalendarDays,
  Clock3,
  Building2,
  ArrowRight, 
  Wifi,
  Coffee,
  Users,
  Car,
  ShieldCheck,
  MapPinned,
  Ruler,
  Sparkles,
  CalendarClock
} from "lucide-vue-next"

const pricingPlans = ref([

  {
    id:1,
    type:"daily",
    title:"Daily Rental",
    icon: Clock3,
    price:null,
    unit:"/ day",
    description:"Perfect for freelancers, meetings, or one-day workspace needs."
  },

  {
    id:2,
    type:"weekly",
    title:"Weekly Rental",
    icon: CalendarDays,
    price:null,
    unit:"/ week",
    description:"Ideal for short projects or temporary business stays."
  },

  {
    id:3,
    type:"monthly",
    title:"Monthly Rental",
    icon: Building2,
    price:null,
    unit:"/ month",
    description:"Best value for startups, remote teams, and long-term businesses."
  }

])

const offices = ref([])
const loading = ref(false)
const router = useRouter()

const goToOffices = () => {

    router.push("/")

}
const calculator = ref({

    rentType: "daily",

    price: 250,

    duration: 1

})
const estimatedTotal = computed(() => {

    const price = Number(calculator.value.price)

    const duration = Number(calculator.value.duration)

    if (price <= 0 || duration <= 0) {

        return 0

    }

    return price * duration

})
const filteredOffices = computed(() => {

    return offices.value.filter(

        office => office.rent_type === calculator.value.rentType

    )

})
watch(filteredOffices, (value) => {

    if(value.length){

        calculator.value.price = value[0].price

    }

})

const loadPricing = async () => {

    loading.value = true

    try{

        const response = await api.get("offices/")

        const offices = response.data.results || response.data

        const daily = offices
            .filter(o => o.rent_type === "daily")
            .map(o => Number(o.price))

        const weekly = offices
            .filter(o => o.rent_type === "weekly")
            .map(o => Number(o.price))

        const monthly = offices
            .filter(o => o.rent_type === "monthly")
            .map(o => Number(o.price))

        pricingPlans.value[0].price =
            daily.length
            ? Math.min(...daily)
            : null

        pricingPlans.value[1].price =
            weekly.length
            ? Math.min(...weekly)
            : null

        pricingPlans.value[2].price =
            monthly.length
            ? Math.min(...monthly)
            : null

    }

    catch(error){

        console.error(error)

    }

    finally{

        loading.value = false

    }

}
onMounted(() => {

    loadPricing()

})
</script>

<template>

<main class="bg-[#F7F8FA] min-h-screen">

    <!-- HERO -->

    <section class="pt-6 pb-6.5">

        <div class="max-w-6xl mx-auto px-6 text-center">

            <div
                class="inline-flex items-center gap-2 bg-[#F9A825]/10 text-[#F9A825] px-4 py-1 rounded-full font-medium">

                <BadgeDollarSign :size="18"/>

                Transparent Pricing

            </div>

            <h1
                class="mt-6 text-4xl font-bold text-[#1F2937]">

                Flexible Pricing for Every Workspace

            </h1>

            <p
                class="mt-5 max-w-3xl mx-auto text-gray-600 leading-8">

                Workspace prices depend on the office,
                rental duration, and available amenities.
                Our pricing is transparent with no hidden fees.

            </p>

        </div>

    </section>

    <!-- PRICING CARDS -->

    <section class="pb-20">

        <div
            class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-8">

            <div

                v-for="plan in pricingPlans"

                :key="plan.id"

                class="bg-white rounded-3xl border border-[#E5E7EB]
                p-8 transition duration-300 hover:-translate-y-2
                hover:shadow-xl">

                <div
                    class="w-16 h-16 rounded-2xl
                    bg-[#F9A825]/10
                    flex items-center justify-center">

                    <component

                        :is="plan.icon"

                        :size="30"

                        class="text-[#F9A825]"/>

                </div>

                <h2
                    class="mt-8 text-2xl font-bold text-[#1F2937]">

                    {{ plan.title }}

                </h2>

                <p
                    class="mt-4 text-gray-600 leading-7">

                    {{ plan.description }}

                </p>

                <div class="mt-8">

                    <span
                        class="text-sm uppercase tracking-wide text-gray-400">

                        Starting from

                    </span>

                    <div
                        class="mt-3 flex items-end gap-2">

                        <span
                            class="text-4xl font-black text-[#1F2937]">

                            {{ plan.price ?? "--" }}

                        </span>

                        <span
                            class="text-lg text-gray-500">

                            MAD {{ plan.unit }}

                        </span>

                    </div>

                </div>

                <button
    @click="goToOffices"
    class="mt-8 flex items-center gap-2 text-[#F9A825] font-semibold hover:gap-3 transition-all">

    View Available Offices

    <ArrowRight :size="18"/>

</button>

            </div>

        </div>

    </section>

  


<!-- Example Booking -->

<section class="pb-24">

  <div class="max-w-7xl mx-auto px-6">

    <div class="grid lg:grid-cols-2 gap-10 items-center">

      <!-- Left -->

      <div>

        <span
          class="inline-flex items-center px-4 py-2 rounded-full
          bg-[#F9A825]/10 text-[#F9A825] font-semibold">

          Example Booking

        </span>

        <h2
          class="mt-6 text-4xl font-black text-[#1F2937] leading-tight">

          See How Your Booking Price
          Is Calculated

        </h2>

        <p
          class="mt-6 text-gray-600 leading-8">

          Every workspace has its own rental price.
          Your final booking amount depends on the rental duration
          and the workspace you choose.

        </p>

        <div class="mt-10 space-y-4">

          <div class="flex items-center gap-4">

            <div
              class="w-12 h-12 rounded-xl bg-[#F9A825]/10
              flex items-center justify-center">

              <Building2 class="text-[#F9A825]" :size="22"/>

            </div>

            <div>

              <h4 class="font-bold">

                Premium Workspace

              </h4>

              <p class="text-gray-500">

                Casablanca Finance City

              </p>

            </div>

          </div>

          <div class="flex items-center justify-between">

            <span>Rental Type</span>

            <strong>Daily</strong>

          </div>

          <div class="flex items-center justify-between">

            <span>Daily Price</span>

            <strong>250 MAD</strong>

          </div>

          <div class="flex items-center justify-between">

            <span>Duration</span>

            <strong>5 Days</strong>

          </div>

          <div
            class="border-t pt-5 flex items-center justify-between
            text-2xl font-black">

            <span>Total</span>

            <span class="text-[#F9A825]">

              1250 MAD

            </span>

          </div>

        </div>

      </div>

      <!-- Right -->

      <div
        class="bg-[#1F2937]
        rounded-[32px]
        p-10
        text-white">

        <h3
          class="text-3xl font-bold">

          What's Included?

        </h3>

        <div class="mt-8 space-y-6">

          <div class="flex items-center gap-4">

            <Wifi class="text-[#F9A825]" :size="22"/>

            <span>High-Speed Internet</span>

          </div>

          <div class="flex items-center gap-4">

            <Coffee class="text-[#F9A825]" :size="22"/>

            <span>Free Coffee & Refreshments</span>

          </div>

          <div class="flex items-center gap-4">

            <Users class="text-[#F9A825]" :size="22"/>

            <span>Meeting Room Access</span>

          </div>

          <div class="flex items-center gap-4">

            <Car class="text-[#F9A825]" :size="22"/>

            <span>Private Parking</span>

          </div>

          <div class="flex items-center gap-4">

            <ShieldCheck class="text-[#F9A825]" :size="22"/>

            <span>24/7 Secure Access</span>

          </div>

        </div>

      </div>

    </div>

  </div>

</section>

<!-- Why Prices Vary -->

<section class="pb-24">

    <div class="max-w-7xl mx-auto px-6">

        <div class="text-center">

            <span
                class="inline-flex items-center
                px-4 py-2
                rounded-full
                bg-[#F9A825]/10
                text-[#F9A825]
                font-semibold">

                Pricing Factors

            </span>

            <h2
                class="mt-6
                text-4xl
                font-black
                text-[#1F2937]">

                What Affects Workspace Pricing?

            </h2>

            <p
                class="mt-5
                max-w-3xl
                mx-auto
                text-gray-600
                leading-8">

                Workspace prices are calculated based on several factors to
                ensure fair and transparent pricing for every customer.

            </p>

        </div>

        <!-- Timeline -->

        <div class="mt-20 relative">

            <!-- Center Line -->

            <div
                class="hidden lg:block
                absolute
                left-1/2
                top-0
                bottom-0
                w-1
                bg-[#F9A825]/20
                -translate-x-1/2">

            </div>

            <div class="space-y-14">

                <!-- Item -->

                <div
                    class="grid lg:grid-cols-2 gap-12 items-center">

                    <div
                        class="bg-white rounded-3xl p-8 border">

                        <MapPinned
                            class="text-[#F9A825]"
                            :size="36"/>

                        <h3
                            class="mt-5 text-2xl font-bold">

                            Location

                        </h3>

                        <p
                            class="mt-4 text-gray-600 leading-7">

                            Offices located in premium business districts
                            such as Casablanca Finance City usually have
                            higher rental prices.

                        </p>

                    </div>

                    <div></div>

                </div>

                <!-- Item -->

                <div
                    class="grid lg:grid-cols-2 gap-12 items-center">

                    <div></div>

                    <div
                        class="bg-white rounded-3xl p-8 border">

                        <Ruler
                            class="text-[#F9A825]"
                            :size="36"/>

                        <h3
                            class="mt-5 text-2xl font-bold">

                            Workspace Size

                        </h3>

                        <p
                            class="mt-4 text-gray-600 leading-7">

                            Larger private offices generally cost more than
                            coworking desks or shared spaces.

                        </p>

                    </div>

                </div>

                <!-- Item -->

                <div
                    class="grid lg:grid-cols-2 gap-12 items-center">

                    <div
                        class="bg-white rounded-3xl p-8 border">

                        <Sparkles
                            class="text-[#F9A825]"
                            :size="36"/>

                        <h3
                            class="mt-5 text-2xl font-bold">

                            Amenities

                        </h3>

                        <p
                            class="mt-4 text-gray-600 leading-7">

                            Meeting rooms, parking, coffee areas,
                            printing services and fast internet
                            increase the overall value.

                        </p>

                    </div>

                    <div></div>

                </div>

                <!-- Item -->

                <div
                    class="grid lg:grid-cols-2 gap-12 items-center">

                    <div></div>

                    <div
                        class="bg-white rounded-3xl p-8 border">

                        <CalendarClock
                            class="text-[#F9A825]"
                            :size="36"/>

                        <h3
                            class="mt-5 text-2xl font-bold">

                            Rental Duration

                        </h3>

                        <p
                            class="mt-4 text-gray-600 leading-7">

                            Weekly and monthly bookings usually benefit from
                            better pricing compared to daily rentals.

                        </p>

                    </div>

                </div>

            </div>

        </div>

    </div>
<!-- Final CTA -->


</section>
</main>

</template>