<template>
  <div
    v-if="show && notification"
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
            Notification Details
          </h2>

          <p class="mt-1 text-sm text-[#9f9f9f]">
            Notification #{{ notification.id }}
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
              User
            </p>

            <p class="mt-1 font-semibold text-[#23394e]">
              {{ notification.username || "-" }}
            </p>
          </div>

          <div>
            <p class="text-xs text-[#9f9f9f]">
              Status
            </p>

            <p
              class="mt-1 font-semibold"
              :class="
                notification.is_read
                  ? 'text-[#23394e]'
                  : 'text-[#f29200]'
              "
            >
              {{ notification.is_read ? "Read" : "Unread" }}
            </p>
          </div>

        </div>

        <div>

          <p class="mb-2 text-xs text-[#9f9f9f]">
            Message
          </p>

          <div
            class="whitespace-pre-wrap rounded-xl border border-gray-200 bg-gray-50 p-4 text-sm leading-6 text-[#23394e]"
          >
            {{ notification.message }}
          </div>

        </div>

        <div>

          <p class="text-xs text-[#9f9f9f]">
            Created At
          </p>

          <p class="mt-1 text-sm font-medium text-[#23394e]">
            {{ formatDate(notification.created_at) }}
          </p>

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
  X
} from "lucide-vue-next";

defineProps({

  show: Boolean,

  notification: {
    type: Object,
    default: null
  }

});

const emit = defineEmits([
  "close"
]);

const formatDate = (value) => {

  if (!value) return "-";

  return new Date(value).toLocaleString(
    undefined,
    {
      day: "2-digit",
      month: "short",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit"
    }
  );

};
</script>