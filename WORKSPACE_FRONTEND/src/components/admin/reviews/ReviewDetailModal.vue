<template>
  <div
    v-if="show && review"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4"
    @click.self="emit('close')"
  >

    <div
      class="w-full max-w-lg rounded-2xl bg-white shadow-xl"
    >

      <div
        class="flex items-center justify-between border-b border-gray-200 px-6 py-4"
      >

        <div>

          <h2 class="text-lg font-bold text-[#23394e]">
            Review Details
          </h2>

          <p class="mt-1 text-sm text-[#9f9f9f]">
            Review #{{ review.id }}
          </p>

        </div>

        <button
          @click="emit('close')"
          class="rounded-lg p-2 text-[#9f9f9f] hover:bg-gray-100"
        >
          <X class="h-5 w-5" />
        </button>

      </div>

      <div class="space-y-5 p-6">

        <div class="grid gap-4 sm:grid-cols-2">

          <div>
            <p class="text-xs text-[#9f9f9f]">
              Customer
            </p>

            <p class="mt-1 font-semibold text-[#23394e]">
              {{ review.username || "-" }}
            </p>
          </div>

          <div>
            <p class="text-xs text-[#9f9f9f]">
              Office
            </p>

            <p class="mt-1 font-semibold text-[#23394e]">
              {{ review.office_title || "-" }}
            </p>
          </div>

        </div>

        <div>

          <p class="mb-2 text-xs text-[#9f9f9f]">
            Rating
          </p>

          <div class="flex gap-1">

            <Star
              v-for="star in 5"
              :key="star"
              class="h-5 w-5"
              :class="
                star <= review.rating
                  ? 'fill-[#f29200] text-[#f29200]'
                  : 'text-gray-300'
              "
            />

          </div>

        </div>

        <div>

          <p class="mb-2 text-xs text-[#9f9f9f]">
            Comment
          </p>

          <div
            class="whitespace-pre-wrap rounded-xl border border-gray-200 bg-gray-50 p-4 text-sm leading-6 text-[#23394e]"
          >
            {{ review.comment }}
          </div>

        </div>

      </div>

      <div
        class="flex justify-end border-t border-gray-200 px-6 py-4"
      >

        <button
          @click="emit('close')"
          class="rounded-lg bg-[#23394e] px-5 py-2 text-sm font-medium text-white"
        >
          Close
        </button>

      </div>

    </div>

  </div>
</template>

<script setup>
import {
  X,
  Star
} from "lucide-vue-next";

defineProps({

  show: Boolean,

  review: {
    type: Object,
    default: null
  }

});

const emit = defineEmits([
  "close"
]);
</script>