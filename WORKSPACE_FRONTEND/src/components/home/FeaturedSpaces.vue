<template>
  <section class="bg-[#F7F8FA] py-24">
    <div class="mx-auto max-w-7xl px-6">

      <!-- Header -->

      <div
        class="mb-14 flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between"
      >
        <div>

          <div
            class="mb-5 inline-flex items-center gap-2 rounded-full bg-[#f29200]/10 px-4 py-2 font-semibold text-[#f29200]"
          >
            <Sparkles class="h-5 w-5" />
            Featured Workspaces
          </div>

          <h2
            class="text-4xl font-extrabold text-[#23394e] md:text-5xl"
          >
            Discover our
            <span class="text-[#f29200]">
              featured offices
            </span>
          </h2>

          <p
            class="mt-5 max-w-2xl text-lg leading-8 text-[#9f9f9f]"
          >
            Hand-picked workspaces selected for quality,
            comfort and productivity. Explore premium offices
            ready for your next project.
          </p>

        </div>

        <RouterLink
          to="/browse-offices"
          class="inline-flex items-center gap-3 font-semibold text-[#f29200] transition hover:gap-5"
        >
          View All Offices

          <ArrowRight class="h-5 w-5" />
        </RouterLink>
      </div>

      <!-- Loading -->

      <div
        v-if="loading"
        class="grid gap-8 lg:grid-cols-3"
      >
        <div
          v-for="i in 3"
          :key="i"
          class="h-[430px] animate-pulse rounded-3xl bg-white"
        />
      </div>

      <!-- Cards -->

      <div
        v-else
        class="grid gap-8 lg:grid-cols-3"
      >
        <article
          v-for="office in offices"
          :key="office.id"
          class="group overflow-hidden rounded-[28px] border border-gray-200 bg-white shadow-sm transition-all duration-500 hover:-translate-y-2 hover:shadow-xl"
        >

          <!-- Image -->

          <div class="relative h-64 overflow-hidden">

            <img
              :src="getOfficeImage(office)"
              :alt="office.title"
              @error="handleImageError"
              class="h-full w-full object-cover transition duration-700 group-hover:scale-110"
            />

            <!-- Gradient -->

            <div
              class="absolute inset-0 bg-gradient-to-t from-black/50 via-black/10 to-transparent"
            />

            <!-- Rating -->

            <div
              class="absolute left-5 top-5 flex items-center gap-2 rounded-xl bg-white px-3 py-2 shadow-lg"
            >
              <Star
                class="h-4 w-4 fill-[#f29200] text-[#f29200]"
              />

              <span
                class="text-sm font-semibold text-[#23394e]"
              >
                {{ office.average_rating || 0 }}
              </span>
            </div>

            <!-- Availability -->

            <div class="absolute right-5 top-5">

              <span
                v-if="office.available"
                class="rounded-full bg-green-500 px-3 py-2 text-xs font-semibold text-white"
              >
                Available
              </span>

              <span
                v-else
                class="rounded-full bg-red-500 px-3 py-2 text-xs font-semibold text-white"
              >
                Booked
              </span>

            </div>

          </div>

          <!-- Body -->

          <div class="p-7">

            <div
              class="flex items-start justify-between gap-4"
            >

              <div class="min-w-0">

                <h3
                  class="text-2xl font-bold text-[#23394e] transition group-hover:text-[#f29200]"
                >
                  {{ office.title }}
                </h3>

                <div
                  class="mt-2 flex items-center gap-2 text-[#9f9f9f]"
                >
                  <MapPin class="h-4 w-4" />
                  {{ office.city }}
                </div>

              </div>

              <div class="shrink-0 text-right">

                <div
                  class="text-2xl font-extrabold text-[#f29200]"
                >
                  {{ office.price }} DH
                </div>

                <div
                  class="text-sm capitalize text-[#9f9f9f]"
                >
                  / {{ office.rent_type }}
                </div>

              </div>

            </div>

            <!-- Amenities -->

            <div
              class="mt-8 grid grid-cols-2 gap-3"
            >

              <div
                class="flex items-center gap-2 text-[#23394e]"
              >
                <Users class="h-5 w-5 text-[#f29200]" />

                {{ office.capacity }} People
              </div>

              <div
                v-if="office.wifi"
                class="flex items-center gap-2 text-[#23394e]"
              >
                <Wifi class="h-5 w-5 text-[#f29200]" />
                WiFi
              </div>

              <div
                v-if="office.parking"
                class="flex items-center gap-2 text-[#23394e]"
              >
                <Car class="h-5 w-5 text-[#f29200]" />
                Parking
              </div>

              <div
                v-if="office.air_conditioning"
                class="flex items-center gap-2 text-[#23394e]"
              >
                <Snowflake class="h-5 w-5 text-[#f29200]" />
                A/C
              </div>

            </div>

            <!-- Button -->

            <RouterLink
              :to="`/office/${office.id}`"
              class="group/button mt-8 flex w-full items-center justify-center gap-3 rounded-2xl bg-[#23394e] py-4 font-semibold text-white transition hover:bg-[#f29200]"
            >
              View Details

              <ArrowRight
                class="h-5 w-5 transition group-hover/button:translate-x-2"
              />
            </RouterLink>

          </div>

        </article>

      </div>

    </div>
  </section>
</template>

<script setup>
import {
  ref,
  onMounted
} from "vue";

import api from "@/services/api";

import {
  Sparkles,
  ArrowRight,
  Star,
  MapPin,
  Users,
  Wifi,
  Car,
  Snowflake
} from "lucide-vue-next";

const loading = ref(true);

const offices = ref([]);

const API_ORIGIN =
  "http://127.0.0.1:8000";

const placeholderImage =
  "https://placehold.co/800x600?text=Workspace";

const getOfficeImage = (office) => {

  if (!office?.images?.length) {
    return placeholderImage;
  }

  const primaryImage =
    office.images.find(
      image => image.is_primary
    );

  let image =
    primaryImage?.image ||
    office.images[0]?.image;

  if (!image) {
    return placeholderImage;
  }

  // Full URL already returned by Django
  if (
    image.startsWith(
      "http://127.0.0.1:8000"
    ) ||
    image.startsWith(
      "http://localhost:8000"
    ) ||
    image.startsWith("https://")
  ) {
    return image;
  }

  // DRF/testserver URL
  if (
    image.startsWith(
      "http://testserver"
    )
  ) {
    return image.replace(
      "http://testserver",
      API_ORIGIN
    );
  }

  // /media/...
  if (image.startsWith("/")) {
    return `${API_ORIGIN}${image}`;
  }

  // media/...
  return `${API_ORIGIN}/${image}`;
};

const handleImageError = (event) => {

  console.error(
    "Office image failed:",
    event.target.src
  );

  event.target.onerror = null;

  event.target.src =
    placeholderImage;
};

onMounted(async () => {

  loading.value = true;

  try {

    const res =
      await api.get("offices/");

    const data =
      res.data.results ??
      res.data ??
      [];

    console.log(
      "Featured offices:",
      data
    );

    console.log(
      "First office images:",
      data?.[0]?.images
    );

    offices.value =
      Array.isArray(data)
        ? data.slice(0, 3)
        : [];

  } catch (err) {

    console.error(
      "Failed to load featured offices:",
      err.response?.data ||
      err.message
    );

    offices.value = [];

  } finally {

    loading.value = false;

  }

});
</script>