<template>
  <main class="min-h-screen bg-[#f7f8fa]">

    <!-- Header -->
    <section class="border-b border-gray-100 bg-white">
      <div class="mx-auto max-w-6xl px-6 py-10">
        <div class="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">

          <div>
            <div
              class="inline-flex items-center gap-2 rounded-full bg-[#f29200]/10 px-3 py-1.5 text-sm font-semibold text-[#f29200]"
            >
              <Heart class="h-4 w-4" />
              Saved Workspaces
            </div>

            <h1 class="mt-4 text-3xl font-bold text-[#23394e]">
              My Favorites
            </h1>

            <p class="mt-2 text-sm text-[#9f9f9f]">
              Keep your favorite workspaces in one place.
            </p>
          </div>

          <div
            v-if="!favoriteStore.loading"
            class="text-sm font-medium text-[#9f9f9f]"
          >
            {{ favoriteStore.favoriteCount }}
            {{
              favoriteStore.favoriteCount === 1
                ? "workspace"
                : "workspaces"
            }}
          </div>

        </div>
      </div>
    </section>


    <section class="mx-auto max-w-6xl px-6 py-8">

      <!-- Loading -->
      <div
        v-if="favoriteStore.loading"
        class="flex min-h-[300px] items-center justify-center"
      >
        <div class="flex items-center gap-3 text-sm text-[#9f9f9f]">
          <Loader2 class="h-5 w-5 animate-spin text-[#f29200]" />
          Loading favorites...
        </div>
      </div>


      <!-- Error -->
      <div
        v-else-if="favoriteStore.error"
        class="rounded-2xl border border-red-200 bg-red-50 p-5"
      >
        <div class="flex items-start gap-3">

          <CircleAlert
            class="mt-0.5 h-5 w-5 shrink-0 text-red-500"
          />

          <div>
            <p class="font-semibold text-red-700">
              Unable to load favorites
            </p>

            <p class="mt-1 text-sm text-red-600">
              {{ getErrorMessage }}
            </p>

            <button
              @click="loadFavorites"
              class="mt-4 rounded-lg bg-red-600 px-4 py-2 text-sm font-semibold text-white transition hover:bg-red-700"
            >
              Try Again
            </button>
          </div>

        </div>
      </div>


      <!-- Empty -->
      <div
        v-else-if="favoriteStore.favorites.length === 0"
        class="flex min-h-[360px] items-center justify-center"
      >
        <div class="max-w-md text-center">

          <div
            class="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-[#f29200]/10"
          >
            <Heart class="h-6 w-6 text-[#f29200]" />
          </div>

          <h2 class="mt-5 text-xl font-bold text-[#23394e]">
            No favorites yet
          </h2>

          <p class="mt-2 text-sm leading-6 text-[#9f9f9f]">
            Browse available workspaces and save the ones you like.
          </p>

          <RouterLink
            to="/browse-offices"
            class="mt-5 inline-flex items-center gap-2 rounded-xl bg-[#f29200] px-5 py-2.5 text-sm font-semibold text-white transition hover:opacity-90"
          >
            <Search class="h-4 w-4" />
            Browse Offices
          </RouterLink>

        </div>
      </div>


      <!-- Content -->
      <template v-else>

        <!-- Stats -->
        <div class="mb-6 grid gap-3 sm:grid-cols-3">

          <div class="rounded-2xl border border-gray-200 bg-white p-4">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs font-medium text-[#9f9f9f]">
                  Saved Workspaces
                </p>

                <p class="mt-1 text-2xl font-bold text-[#23394e]">
                  {{ favoriteStore.favoriteCount }}
                </p>
              </div>

              <div
                class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
              >
                <Heart class="h-5 w-5 text-[#f29200]" />
              </div>
            </div>
          </div>


          <div class="rounded-2xl border border-gray-200 bg-white p-4">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs font-medium text-[#9f9f9f]">
                  Cities
                </p>

                <p class="mt-1 text-2xl font-bold text-[#23394e]">
                  {{ uniqueCities }}
                </p>
              </div>

              <div
                class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#23394e]/5"
              >
                <MapPin class="h-5 w-5 text-[#23394e]" />
              </div>
            </div>
          </div>


          <div class="rounded-2xl border border-gray-200 bg-white p-4">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs font-medium text-[#9f9f9f]">
                  Average Price
                </p>

                <p class="mt-1 text-2xl font-bold text-[#f29200]">
                  {{ averagePrice }} MAD
                </p>
              </div>

              <div
                class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10"
              >
                <Wallet class="h-5 w-5 text-[#f29200]" />
              </div>
            </div>
          </div>

        </div>


        <!-- Toolbar -->
        <div
          class="mb-5 flex flex-col gap-3 rounded-2xl border border-gray-200 bg-white p-4 sm:flex-row sm:items-center sm:justify-between"
        >

          <div>
            <p class="text-sm font-semibold text-[#23394e]">
              Your saved collection
            </p>

            <p class="mt-0.5 text-xs text-[#9f9f9f]">
              Sort your favorite workspaces.
            </p>
          </div>

          <select
            v-model="sortBy"
            class="h-10 rounded-xl border border-gray-200 bg-white px-3 text-sm text-[#23394e] outline-none transition focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10"
          >
            <option value="newest">
              Newest saved
            </option>

            <option value="price-low">
              Price: Low to High
            </option>

            <option value="price-high">
              Price: High to Low
            </option>

            <option value="city">
              City
            </option>
          </select>

        </div>


        <!-- Favorites Grid -->
        <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">

          <article
            v-for="favorite in sortedFavorites"
            :key="favorite.id"
            class="group overflow-hidden rounded-2xl border border-gray-200 bg-white transition duration-300 hover:-translate-y-1 hover:shadow-lg"
          >

            <div class="relative">

              <img
                :src="getOfficeImage(favorite.office_details)"
                :alt="favorite.office_details?.title || 'Workspace'"
                class="h-48 w-full object-cover"
              />

              <button
                @click="removeFavorite(favorite)"
                :disabled="removingId === favorite.id"
                class="absolute right-3 top-3 flex h-9 w-9 items-center justify-center rounded-full bg-white/95 text-[#f29200] shadow-md transition hover:scale-105 disabled:cursor-not-allowed disabled:opacity-50"
                title="Remove favorite"
              >
                <Loader2
                  v-if="removingId === favorite.id"
                  class="h-4 w-4 animate-spin"
                />

                <Heart
                  v-else
                  class="h-4 w-4 fill-current"
                />
              </button>

            </div>


            <div class="p-5">

              <div class="flex items-start justify-between gap-3">

                <div>
                  <h2
                    class="line-clamp-1 text-lg font-bold text-[#23394e]"
                  >
                    {{ favorite.office_details?.title }}
                  </h2>

                  <p
                    class="mt-1 flex items-center gap-1.5 text-sm text-[#9f9f9f]"
                  >
                    <MapPin class="h-4 w-4" />
                    {{ favorite.office_details?.city }}
                  </p>
                </div>

                <span
                  v-if="favorite.office_details?.rent_type"
                  class="shrink-0 rounded-lg bg-[#23394e]/5 px-2.5 py-1 text-xs font-semibold text-[#23394e]"
                >
                  {{ favorite.office_details?.rent_type }}
                </span>

              </div>


              <div class="mt-5 flex items-end justify-between gap-3">

                <div>
                  <p class="text-xs text-[#9f9f9f]">
                    Starting from
                  </p>

                  <p class="mt-1 text-xl font-bold text-[#f29200]">
                    {{ favorite.office_details?.price }}
                    MAD
                  </p>
                </div>

                <RouterLink
                  :to="{
                    name: 'office-detail',
                    params: {
                      id: favorite.office
                    }
                  }"
                  class="inline-flex h-10 items-center gap-1.5 rounded-lg bg-[#23394e] px-4 text-sm font-semibold text-white transition hover:opacity-90"
                >
                  View

                  <ArrowRight class="h-4 w-4" />
                </RouterLink>

              </div>

            </div>

          </article>

        </div>


        <!-- CTA -->
        <div
          class="mt-10 rounded-2xl border border-[#f29200]/20 bg-[#f29200]/5 p-6"
        >
          <div
            class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
          >

            <div>
              <h3 class="text-lg font-bold text-[#23394e]">
                Looking for more options?
              </h3>

              <p class="mt-1 text-sm text-[#9f9f9f]">
                Discover more workspaces and add them to your favorites.
              </p>
            </div>

            <RouterLink
              to="/browse-offices"
              class="inline-flex h-10 items-center justify-center gap-2 rounded-xl bg-[#f29200] px-5 text-sm font-semibold text-white transition hover:opacity-90"
            >
              Browse Offices

              <ArrowRight class="h-4 w-4" />
            </RouterLink>

          </div>
        </div>

      </template>

    </section>

  </main>
</template>


<script setup>
import {
  computed,
  onMounted,
  ref
} from "vue";

import {
  Heart,
  Search,
  MapPin,
  ArrowRight,
  Loader2,
  CircleAlert,
  Wallet
} from "lucide-vue-next";

import { useFavoriteStore } from "@/stores/favoriteStore";


const favoriteStore =
  useFavoriteStore();

const removingId = ref(null);

const sortBy = ref("newest");


const API_ORIGIN =
  "http://127.0.0.1:8000";

const placeholderImage =
  "https://placehold.co/800x600?text=Workspace";


// ================================
// Favorite Stats
// ================================

const uniqueCities = computed(() => {

  const cities =
    favoriteStore.favorites
      .map(
        favorite =>
          favorite.office_details?.city
      )
      .filter(Boolean);

  return new Set(cities).size;
});


const averagePrice = computed(() => {

  const prices =
    favoriteStore.favorites
      .map(
        favorite =>
          Number(
            favorite.office_details?.price
          )
      )
      .filter(
        price =>
          !Number.isNaN(price)
      );

  if (!prices.length) {
    return 0;
  }

  const total =
    prices.reduce(
      (sum, price) =>
        sum + price,
      0
    );

  return Math.round(
    total / prices.length
  );
});


// ================================
// Sorting
// ================================

const sortedFavorites = computed(() => {

  const items =
    [...favoriteStore.favorites];

  if (
    sortBy.value === "price-low"
  ) {

    return items.sort(
      (a, b) =>
        Number(
          a.office_details?.price || 0
        ) -
        Number(
          b.office_details?.price || 0
        )
    );
  }

  if (
    sortBy.value === "price-high"
  ) {

    return items.sort(
      (a, b) =>
        Number(
          b.office_details?.price || 0
        ) -
        Number(
          a.office_details?.price || 0
        )
    );
  }

  if (
    sortBy.value === "city"
  ) {

    return items.sort(
      (a, b) =>
        (
          a.office_details?.city || ""
        ).localeCompare(
          b.office_details?.city || ""
        )
    );
  }

  return items;
});


// ================================
// Office Image
// ================================

const getOfficeImage = (office) => {

  if (
    !office?.images ||
    office.images.length === 0
  ) {
    return placeholderImage;
  }

  const primaryImage =
    office.images.find(
      image =>
        image.is_primary
    );

  let image =
    primaryImage?.image ||
    office.images[0]?.image;

  if (!image) {
    return placeholderImage;
  }

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

  if (
    image.startsWith("/")
  ) {

    return `${API_ORIGIN}${image}`;
  }

  return `${API_ORIGIN}/${image}`;
};


// ================================
// Error
// ================================

const getErrorMessage = computed(() => {

  const error =
    favoriteStore.error;

  if (!error) {
    return "";
  }

  if (
    typeof error === "string"
  ) {
    return error;
  }

  if (
    error.detail
  ) {
    return error.detail;
  }

  if (
    error.office
  ) {

    return Array.isArray(
      error.office
    )
      ? error.office[0]
      : error.office;
  }

  return "Something went wrong.";
});


// ================================
// Fetch Favorites
// ================================

const loadFavorites = async () => {

  await favoriteStore.fetchFavorites();

};


// ================================
// Remove Favorite
// ================================

const removeFavorite = async (
  favorite
) => {

  removingId.value =
    favorite.id;

  try {

    await favoriteStore.removeFavorite(
      favorite.id
    );

  } finally {

    removingId.value = null;

  }
};


// ================================
// Mounted
// ================================

onMounted(() => {

  loadFavorites();

});
</script>