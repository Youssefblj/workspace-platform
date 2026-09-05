<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm"
  >

    <div
      v-if="
        adminStore.loading &&
        adminStore.reviews.length === 0
      "
      class="flex items-center justify-center gap-3 py-14"
    >

      <LoaderCircle
        class="h-5 w-5 animate-spin text-[#f29200]"
      />

      <span class="text-sm text-[#9f9f9f]">
        Loading reviews...
      </span>

    </div>

    <div v-else class="overflow-x-auto">

      <table class="min-w-full">

        <thead class="bg-[#23394e]">

          <tr>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase text-white">
              User
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase text-white">
              Office
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase text-white">
              Rating
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase text-white">
              Comment
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase text-white">
              Date
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase text-white">
              Actions
            </th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="review in adminStore.reviews"
            :key="review.id"
            class="border-t border-gray-100 transition hover:bg-gray-50"
          >

            <!-- User -->

            <td class="px-5 py-4">

              <div class="flex items-center gap-3">

<div
  class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-xl bg-[#f29200]/10"
>
  <img
    v-if="review.user_profile_image"
    :src="review.user_profile_image"
    :alt="review.username || 'User'"
    class="h-full w-full object-cover"
  />

  <User
    v-else
    class="h-4 w-4 text-[#f29200]"
  />
</div>

                <p class="text-sm font-semibold text-[#23394e]">
                  {{ review.username || "Unknown" }}
                </p>

              </div>

            </td>

            <!-- Office -->

            <td class="px-5 py-4">

              <div class="flex items-center gap-2">

                <Building2
                  class="h-4 w-4 text-[#9f9f9f]"
                />

                <p class="text-sm font-medium text-[#23394e]">
                  {{ review.office_title || "-" }}
                </p>

              </div>

            </td>

            <!-- Rating -->

            <td class="px-5 py-4">

              <div
                class="flex items-center justify-center gap-1"
              >

                <Star
                  v-for="star in 5"
                  :key="star"
                  class="h-4 w-4"
                  :class="
                    star <= review.rating
                      ? 'fill-[#f29200] text-[#f29200]'
                      : 'text-gray-300'
                  "
                />

              </div>

            </td>

            <!-- Comment -->

            <td class="px-5 py-4">

              <p
                class="max-w-[280px] truncate text-sm text-[#9f9f9f]"
                :title="review.comment"
              >
                {{ review.comment }}
              </p>

            </td>

            <!-- Date -->

            <td class="px-5 py-4 text-sm text-[#9f9f9f]">
              {{ formatDate(review.created_at) }}
            </td>

            <!-- Actions -->

            <td class="px-5 py-4">

              <div
                class="flex items-center justify-center gap-1"
              >

                <button
                  @click="emit('view', review)"
                  title="View review"
                  class="rounded-lg p-2 text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200]"
                >
                  <Eye class="h-4 w-4" />
                </button>

                <button
                  @click="deleteReview(review)"
                  title="Delete review"
                  class="rounded-lg p-2 text-red-500 transition hover:bg-red-50"
                >
                  <Trash2 class="h-4 w-4" />
                </button>

              </div>

            </td>

          </tr>

          <tr v-if="adminStore.reviews.length === 0">

            <td colspan="6" class="py-14">

              <div
                class="flex flex-col items-center text-center"
              >

                <MessageSquareOff
                  class="h-9 w-9 text-[#9f9f9f]"
                />

                <p class="mt-3 text-sm font-semibold text-[#23394e]">
                  No reviews found
                </p>

                <p class="mt-1 text-xs text-[#9f9f9f]">
                  Try another search or rating filter.
                </p>

              </div>

            </td>

          </tr>

        </tbody>

      </table>

      <!-- Pagination -->

      <div
        v-if="adminStore.totalReviews > 0"
        class="flex flex-col gap-3 border-t border-gray-200 px-5 py-4 sm:flex-row sm:items-center sm:justify-between"
      >

        <p class="text-sm text-[#9f9f9f]">

          Total

          <span class="font-semibold text-[#23394e]">
            {{ adminStore.totalReviews }}
          </span>

          reviews

        </p>

        <div class="flex items-center gap-2">

          <button
            @click="previousPage"
            :disabled="
              adminStore.reviewCurrentPage <= 1 ||
              adminStore.loading
            "
            class="flex items-center gap-1 rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] disabled:opacity-40"
          >
            <ChevronLeft class="h-4 w-4" />
            Previous
          </button>

          <button
            v-for="page in visiblePages"
            :key="page"
            @click="goToPage(page)"
            class="flex h-9 min-w-9 items-center justify-center rounded-lg px-2 text-sm font-medium"
            :class="
              page === adminStore.reviewCurrentPage
                ? 'bg-[#f29200] text-white'
                : 'border border-gray-200 text-[#23394e]'
            "
          >
            {{ page }}
          </button>

          <button
            @click="nextPage"
            :disabled="
              adminStore.reviewCurrentPage >=
                adminStore.reviewTotalPages ||
              adminStore.loading
            "
            class="flex items-center gap-1 rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] disabled:opacity-40"
          >
            Next
            <ChevronRight class="h-4 w-4" />
          </button>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { computed } from "vue";
import Swal from "sweetalert2";

import {
  User,
  Building2,
  Star,
  Eye,
  Trash2,
  MessageSquareOff,
  LoaderCircle,
  ChevronLeft,
  ChevronRight
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const emit = defineEmits([
  "view"
]);

const formatDate = (value) => {

  if (!value) return "-";

  return new Date(value).toLocaleDateString(
    undefined,
    {
      day: "2-digit",
      month: "short",
      year: "numeric"
    }
  );

};

const deleteReview = async (review) => {

  const result = await Swal.fire({

    title: "Delete Review?",

    text: `Delete the review from ${review.username}?`,

    icon: "warning",

    showCancelButton: true,

    confirmButtonText: "Delete",

    cancelButtonText: "Cancel",

    confirmButtonColor: "#f29200",

    cancelButtonColor: "#9f9f9f"

  });

  if (!result.isConfirmed) return;

  try {

    await adminStore.deleteReview(
      review.id
    );

    Swal.fire({
      icon: "success",
      title: "Review Deleted",
      timer: 1300,
      showConfirmButton: false
    });

  } catch {

    Swal.fire({
      icon: "error",
      title: "Delete Failed"
    });

  }

};

const visiblePages = computed(() => {

  const total =
    adminStore.reviewTotalPages;

  const current =
    adminStore.reviewCurrentPage;

  if (total <= 5) {

    return Array.from(
      { length: total },
      (_, index) => index + 1
    );

  }

  let start = Math.max(
    current - 2,
    1
  );

  let end = Math.min(
    start + 4,
    total
  );

  if (end - start < 4) {

    start = Math.max(
      end - 4,
      1
    );

  }

  return Array.from(
    { length: end - start + 1 },
    (_, index) => start + index
  );

});

const goToPage = (page) => {

  if (
    page < 1 ||
    page > adminStore.reviewTotalPages ||
    page === adminStore.reviewCurrentPage
  ) {
    return;
  }

  adminStore.fetchReviews(page);

};

const previousPage = () => {

  goToPage(
    adminStore.reviewCurrentPage - 1
  );

};

const nextPage = () => {

  goToPage(
    adminStore.reviewCurrentPage + 1
  );

};
</script>