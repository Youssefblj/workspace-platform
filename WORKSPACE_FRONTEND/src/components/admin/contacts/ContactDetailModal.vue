<template>
  <div
    v-if="show && contact"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4"
    @click.self="emit('close')"
  >
    <div
      class="max-h-[85vh] w-full max-w-2xl overflow-y-auto overflow-x-hidden rounded-2xl bg-white shadow-xl"
    >

      <div
        class="flex items-center justify-between gap-4 border-b border-gray-200 px-6 py-4"
      >
        <div class="min-w-0">
          <h2 class="text-lg font-bold text-[#23394e]">
            Message Details
          </h2>

          <p class="mt-1 break-all text-sm text-[#9f9f9f]">
            {{ contact.subject }}
          </p>
        </div>

        <button
          type="button"
          @click="emit('close')"
          class="shrink-0 rounded-lg p-2 text-[#9f9f9f] hover:bg-gray-100"
        >
          <X class="h-5 w-5" />
        </button>
      </div>

      <div class="min-w-0 space-y-5 p-6">

        <div class="grid min-w-0 gap-4 sm:grid-cols-2">

          <div class="min-w-0">
            <p class="text-xs text-[#9f9f9f]">
              Name
            </p>

            <p class="mt-1 break-all font-medium text-[#23394e]">
              {{ contact.name }}
            </p>
          </div>

          <div class="min-w-0">
            <p class="text-xs text-[#9f9f9f]">
              Email
            </p>

            <p class="mt-1 break-all font-medium text-[#23394e]">
              {{ contact.email }}
            </p>
          </div>

          <div class="min-w-0">
            <p class="text-xs text-[#9f9f9f]">
              Phone
            </p>

            <p class="mt-1 break-all font-medium text-[#23394e]">
              {{ contact.phone || "-" }}
            </p>
          </div>

          <div class="min-w-0">
            <p class="text-xs text-[#9f9f9f]">
              Category
            </p>

            <p class="mt-1 break-all font-medium text-[#23394e]">
              {{ formatLabel(contact.category) }}
            </p>
          </div>

        </div>

        <div class="min-w-0">
          <p class="mb-2 text-xs text-[#9f9f9f]">
            Message
          </p>

          <div
            class="max-h-56 w-full overflow-y-auto overflow-x-hidden whitespace-pre-wrap break-all rounded-xl border border-gray-200 bg-gray-50 p-4 text-sm leading-6 text-[#23394e]"
          >
            {{ contact.message }}
          </div>
        </div>

        <div
          v-if="contact.admin_reply"
          class="min-w-0"
        >

          <p class="mb-2 text-xs text-[#9f9f9f]">
            Admin Reply
          </p>

          <div
            class="max-h-56 w-full overflow-y-auto overflow-x-hidden whitespace-pre-wrap break-all rounded-xl border border-[#f29200]/20 bg-[#f29200]/5 p-4 text-sm leading-6 text-[#23394e]"
          >
            {{ contact.admin_reply }}
          </div>

          <p
            v-if="contact.answered_by"
            class="mt-2 break-all text-xs text-[#9f9f9f]"
          >
            Answered by {{ contact.answered_by }}
          </p>

        </div>

      </div>

      <div
        class="flex justify-end gap-3 border-t border-gray-200 px-6 py-4"
      >

        <button
          type="button"
          @click="emit('close')"
          class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e] transition hover:bg-gray-50"
        >
          Close
        </button>

        <button
          type="button"
          @click="emit('reply', contact)"
          class="inline-flex items-center gap-2 rounded-lg bg-[#f29200] px-4 py-2 text-sm font-medium text-white transition hover:bg-[#d97706]"
        >
          <Reply class="h-4 w-4" />
          Reply
        </button>

      </div>

    </div>
  </div>
</template>

<script setup>
import {
  X,
  Reply
} from "lucide-vue-next";

defineProps({
  show: Boolean,
  contact: {
    type: Object,
    default: null
  }
});

const emit = defineEmits([
  "close",
  "reply"
]);

const formatLabel = (value) => {
  if (!value) return "-";

  return value
    .replaceAll("_", " ")
    .replace(/\b\w/g, char => char.toUpperCase());
};
</script>