<template>
  <div class="space-y-6">

    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >

      <div>
        <h1 class="text-2xl font-bold text-[#23394e]">
          Reviews Management
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Review customer feedback and ratings.
        </p>
      </div>

<button
  type="button"
  @click="refreshReviews"
  :disabled="refreshing"
  class="inline-flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
>
  <RefreshCw
    class="h-4 w-4"
    :class="{
      'animate-spin': refreshing
    }"
  />

  {{ refreshing ? "Refreshing..." : "Refresh" }}
</button>

    </div>

    <!-- Filters -->

    <div
      class="flex flex-col gap-3 rounded-xl border border-gray-200 bg-white p-4 sm:flex-row sm:items-center"
    >

      <div class="relative flex-1">

        <Search
          class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9f9f9f]"
        />

        <input
          v-model="adminStore.reviewSearch"
          type="text"
          placeholder="Search user, office or comment..."
          class="w-full rounded-lg border border-gray-200 py-2 pl-10 pr-4 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
        />

      </div>

      <select
        v-model="adminStore.reviewRatingFilter"
        class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
      >

        <option value="">
          All Ratings
        </option>

        <option value="5">
          5 Stars
        </option>

        <option value="4">
          4 Stars
        </option>

        <option value="3">
          3 Stars
        </option>

        <option value="2">
          2 Stars
        </option>

        <option value="1">
          1 Star
        </option>

      </select>

      <button
        v-if="
          adminStore.reviewSearch ||
          adminStore.reviewRatingFilter
        "
        @click="resetFilters"
        class="inline-flex items-center gap-2 rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#9f9f9f] transition hover:border-[#f29200] hover:text-[#f29200]"
      >

        <X class="h-4 w-4" />

        Reset

      </button>

    </div>

    <ReviewsTable
      @view="openReview"
    />

    <ReviewDetailModal
      :show="showReviewModal"
      :review="selectedReview"
      @close="closeReview"
    />

  </div>
</template>

<script setup>
import {
  ref,
  watch,
  onMounted,
  onBeforeUnmount
} from "vue";

import {
  Search,
  RefreshCw,
  X
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

import ReviewsTable from "@/components/admin/reviews/ReviewsTable.vue";
import ReviewDetailModal from "@/components/admin/reviews/ReviewDetailModal.vue";
import { toast } from "vue-sonner";
const refreshing = ref(false);
const adminStore = useAdminStore();

const showReviewModal = ref(false);
const selectedReview = ref(null);

let searchTimeout = null;

const refreshReviews = async () => {

  if (refreshing.value) {
    return;
  }

  refreshing.value = true;

  try {

    adminStore.reviewSearch = "";
    adminStore.reviewRatingFilter = "";

    clearTimeout(searchTimeout);

    await adminStore.fetchReviews(1);

    toast.success(
      "Reviews refreshed successfully."
    );

  } catch (error) {

    console.error(
      "Failed to refresh reviews:",
      error
    );

    toast.error(
      "Unable to refresh reviews."
    );

  } finally {

    refreshing.value = false;

  }

};

const resetFilters = () => {

  adminStore.reviewSearch = "";
  adminStore.reviewRatingFilter = "";

};

const openReview = (review) => {

  selectedReview.value = review;
  showReviewModal.value = true;

};

const closeReview = () => {

  showReviewModal.value = false;
  selectedReview.value = null;

};

watch(
  () => adminStore.reviewSearch,
  () => {

    clearTimeout(searchTimeout);

    searchTimeout = setTimeout(() => {

      adminStore.fetchReviews(1);

    }, 400);

  }
);

watch(
  () => adminStore.reviewRatingFilter,
  () => {

    adminStore.fetchReviews(1);

  }
);

onMounted(() => {

  adminStore.fetchReviews(1);

});

onBeforeUnmount(() => {

  clearTimeout(searchTimeout);

});
</script>