<template>
  <div
    v-if="show && contact"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4"
    @click.self="emit('close')"
  >
    <form
      @submit.prevent="submitReply"
      class="w-full max-w-lg rounded-2xl bg-white shadow-xl"
    >

      <div
        class="flex items-center justify-between border-b border-gray-200 px-6 py-4"
      >
        <div>
          <h2 class="text-lg font-bold text-[#23394e]">
            Reply to Message
          </h2>

          <p class="mt-1 text-sm text-[#9f9f9f]">
            {{ contact.name }}
          </p>
        </div>

        <button
          type="button"
          @click="emit('close')"
          class="rounded-lg p-2 text-[#9f9f9f] hover:bg-gray-100"
        >
          <X class="h-5 w-5" />
        </button>
      </div>

      <div class="space-y-4 p-6">

        <div
          class="rounded-xl border border-gray-200 bg-gray-50 p-4"
        >
          <p class="text-xs text-[#9f9f9f]">
            Subject
          </p>

          <p class="mt-1 text-sm font-medium text-[#23394e]">
            {{ contact.subject }}
          </p>
        </div>

        <div>
          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            Your Reply
          </label>

          <textarea
            v-model="reply"
            rows="7"
            placeholder="Write your reply..."
            class="w-full resize-none rounded-xl border border-gray-200 p-3 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
          />

          <p
            v-if="error"
            class="mt-2 text-xs text-red-500"
          >
            {{ error }}
          </p>
        </div>

      </div>

      <div
        class="flex justify-end gap-3 border-t border-gray-200 px-6 py-4"
      >
        <button
          type="button"
          @click="emit('close')"
          class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e]"
        >
          Cancel
        </button>

        <button
          type="submit"
          :disabled="adminStore.loading"
          class="inline-flex items-center gap-2 rounded-lg bg-[#f29200] px-4 py-2 text-sm font-medium text-white disabled:opacity-50"
        >
          <Send class="h-4 w-4" />

          {{ adminStore.loading ? "Sending..." : "Send Reply" }}
        </button>
      </div>

    </form>
  </div>
</template>

<script setup>
import {
  ref,
  watch
} from "vue";

import Swal from "sweetalert2";

import {
  X,
  Send
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const props = defineProps({
  show: Boolean,

  contact: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(["close"]);

const adminStore = useAdminStore();

const reply = ref("");
const error = ref("");

watch(
  () => props.contact,
  () => {
    reply.value = "";
    error.value = "";
  }
);

const submitReply = async () => {

  error.value = "";

  if (reply.value.trim().length < 10) {
    error.value =
      "Reply must contain at least 10 characters.";

    return;
  }

  try {

    await adminStore.replyContact(
      props.contact.id,
      reply.value.trim()
    );

    Swal.fire({
      icon: "success",
      title: "Reply Sent",
      text: "The customer has been answered successfully.",
      timer: 1500,
      showConfirmButton: false
    });

    emit("close");

  } catch (err) {

    error.value =
      err.response?.data?.admin_reply?.[0] ||
      err.response?.data?.error ||
      "Unable to send reply.";

  }
};
</script>