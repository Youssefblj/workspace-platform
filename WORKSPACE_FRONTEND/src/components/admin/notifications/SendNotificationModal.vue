<template>
  <div
    v-if="show"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4"
    @click.self="emit('close')"
  >

    <form
      @submit.prevent="submitNotification"
      class="w-full max-w-lg rounded-2xl bg-white shadow-xl"
    >

      <div
        class="flex items-center justify-between border-b border-gray-200 px-6 py-4"
      >

        <div>

          <h2 class="text-lg font-bold text-[#23394e]">
            Send Notification
          </h2>

          <p class="mt-1 text-sm text-[#9f9f9f]">
            Send an in-app notification to a user.
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

      <div class="space-y-5 p-6">

        <div>

          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            User
          </label>

          <select
            v-model="selectedUser"
            class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
          >

            <option value="">
              Select user
            </option>

            <option
              v-for="user in adminStore.users"
              :key="user.id"
              :value="user.id"
            >
              {{ user.username }} — {{ user.email }}
            </option>

          </select>

          <p
            v-if="errors.user"
            class="mt-2 text-xs text-red-500"
          >
            {{ errors.user }}
          </p>

        </div>

        <div>

          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            Message
          </label>

          <textarea
            v-model="message"
            rows="6"
            placeholder="Write notification message..."
            class="w-full resize-none rounded-xl border border-gray-200 p-3 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
          />

          <div class="mt-2 flex items-center justify-between">

            <p
              v-if="errors.message"
              class="text-xs text-red-500"
            >
              {{ errors.message }}
            </p>

            <p
              class="ml-auto text-xs text-[#9f9f9f]"
            >
              {{ message.length }} characters
            </p>

          </div>

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

          {{
            adminStore.loading
              ? "Sending..."
              : "Send Notification"
          }}

        </button>

      </div>

    </form>

  </div>
</template>

<script setup>
import {
  reactive,
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
  show: Boolean
});

const emit = defineEmits([
  "close"
]);

const adminStore = useAdminStore();

const selectedUser = ref("");
const message = ref("");

const errors = reactive({
  user: "",
  message: ""
});

const resetForm = () => {

  selectedUser.value = "";
  message.value = "";

  errors.user = "";
  errors.message = "";

};

watch(
  () => props.show,
  async (show) => {

    if (!show) {
      resetForm();
      return;
    }

    if (adminStore.users.length === 0) {
      await adminStore.fetchUsers();
    }

  }
);

const submitNotification = async () => {

  errors.user = "";
  errors.message = "";

  if (!selectedUser.value) {
    errors.user =
      "Please select a user.";
  }

  if (!message.value.trim()) {
    errors.message =
      "Message is required.";
  }

  if (
    !selectedUser.value ||
    !message.value.trim()
  ) {
    return;
  }

  try {

    await adminStore.sendNotification(
      selectedUser.value,
      message.value.trim()
    );

    Swal.fire({
      icon: "success",
      title: "Notification Sent",
      text: "The notification was sent successfully.",
      timer: 1500,
      showConfirmButton: false
    });

    resetForm();

    emit("close");

  } catch (err) {

    Swal.fire({
      icon: "error",
      title: "Send Failed",
      text:
        err.response?.data?.error ||
        "Unable to send notification."
    });

  }

};
</script>