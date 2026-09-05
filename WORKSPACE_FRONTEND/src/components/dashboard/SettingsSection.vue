<script setup>

import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";
import { useAuthStore } from "@/stores/auth";

import { useForm } from "vee-validate";
import * as yup from "yup";
import { toast } from "vue-sonner";
import Swal from "sweetalert2"



import {
  Lock,
  KeyRound,
  Eye,
  EyeOff,
  Save,
  ShieldCheck,
  Bell,
  TriangleAlert
} from "lucide-vue-next";

const saving = ref(false);
const router = useRouter();
const authStore = useAuthStore();
const emailNotifications = ref(true);
const bookingNotifications = ref(true);
const paymentNotifications = ref(true);

const showOldPassword = ref(false);
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);

const schema = yup.object({

  old_password: yup
    .string()
    .required("Current password is required"),

  new_password: yup
    .string()
    .required("New password is required")
    .min(8, "Password must contain at least 8 characters")
    .matches(/[A-Z]/, "Must contain at least one uppercase letter")
    .matches(/[a-z]/, "Must contain at least one lowercase letter")
    .matches(/[0-9]/, "Must contain at least one number"),

  confirm_password: yup
    .string()
    .required("Please confirm your password")
    .oneOf(
      [yup.ref("new_password")],
      "Passwords do not match"
    )

});

const {

  values,
  errors,
  defineField,
  handleSubmit,
  resetForm,
  setErrors

} = useForm({

  validationSchema: schema,

  initialValues: {

    old_password: "",
    new_password: "",
    confirm_password: ""

  }

});

const [old_password] = defineField("old_password");
const [new_password] = defineField("new_password");
const [confirm_password] = defineField("confirm_password");

const changePassword = handleSubmit(async (formData) => {

  saving.value = true;

  try {

    await api.post("change-password/", {

      old_password: formData.old_password,
      new_password: formData.new_password

    });

    toast.success("Password changed successfully.");

    resetForm();

  }

  catch (err) {

    if (err.response?.data) {

      const backendErrors = {};

      if (err.response.data.error) {

        backendErrors.old_password =
          err.response.data.error;

      }

      setErrors(backendErrors);

    }

    else {

      toast.error("Something went wrong.");

    }

  }

  finally {

    saving.value = false;

  }

});

const logout = () => {
  authStore.logout();
  router.replace({ name: "login" });
};

const deleteAccount = async () => {

  const result = await Swal.fire({
    title: "Delete your account?",
    text: "This action is permanent and cannot be undone.",
    icon: "warning",
    input: "text",
    inputPlaceholder: "Type DELETE to confirm",
    showCancelButton: true,
    confirmButtonText: "Delete Account",
    cancelButtonText: "Cancel",
    confirmButtonColor: "#dc2626",
    cancelButtonColor: "#9f9f9f",
    reverseButtons: true,

    inputValidator: (value) => {
      if (value !== "DELETE") {
        return 'Type "DELETE" to confirm.';
      }
    }
  });

  if (!result.isConfirmed) {
    return;
  }

  try {

    await api.delete(
      "delete-account/"
    );

    authStore.logout();

    await Swal.fire({
      icon: "success",
      title: "Account Deleted",
      text: "Your account has been deleted successfully.",
      timer: 1600,
      showConfirmButton: false
    });

    router.replace({
      name: "login"
    });

  } catch (error) {

    console.error(
      "DELETE ACCOUNT ERROR:",
      error.response?.data || error
    );

    Swal.fire({
      icon: "error",
      title: "Delete Failed",
      text:
        error.response?.data?.error ||
        error.response?.data?.detail ||
        "Unable to delete your account."
    });

  }
};


</script>

<template>

<section class="mx-auto max-w-4xl space-y-5">

  <!-- Header -->

  <div class="px-1">

    <h2 class="text-2xl font-bold tracking-tight text-[#23394E] sm:text-3xl">
      Settings
    </h2>

    <p class="mt-1.5 text-sm text-[#9F9F9F] sm:text-base">
      Manage your account preferences and security.
    </p>

  </div>

  <!-- Security Card -->

  <div
    class="rounded-2xl border border-gray-100 bg-white p-5 shadow-sm transition duration-300 hover:-translate-y-0.5 hover:shadow-md sm:p-6"
  >

    <div class="flex items-center gap-3 border-b border-gray-100 pb-4">

      <div
        class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-[#F29200]/10"
      >
        <ShieldCheck class="h-5 w-5 text-[#F29200]" />
      </div>

      <div>

        <h3 class="text-lg font-bold text-[#23394E]">
          Security
        </h3>

        <p class="mt-0.5 text-sm text-[#9F9F9F]">
          Change your account password.
        </p>

      </div>

    </div>

    <form
      class="mt-5 space-y-4"
      @submit.prevent="changePassword"
    >

      <!-- Current Password -->

      <div>

        <label
          class="mb-1.5 flex items-center gap-2 text-sm font-semibold text-[#23394E]"
        >

          <Lock class="h-4 w-4 text-[#F29200]" />

          Current Password

        </label>

        <div class="relative">

          <input
            v-model="old_password"
            :type="showOldPassword ? 'text' : 'password'"
            autocomplete="current-password"
            :class="errors.old_password ? 'border-red-300 focus:border-red-500 focus:ring-red-100' : 'border-gray-200 focus:border-[#F29200] focus:ring-[#F29200]/10'"
            class="h-11 w-full rounded-xl border bg-white px-4 pr-11 text-sm text-[#23394E] outline-none transition duration-200 placeholder:text-[#9F9F9F] focus:ring-4"
          />

          <button
            type="button"
            class="absolute right-3 top-1/2 flex h-8 w-8 -translate-y-1/2 items-center justify-center rounded-lg text-[#9F9F9F] transition duration-200 hover:bg-gray-100 hover:text-[#23394E] focus:outline-none focus:ring-2 focus:ring-[#F29200]/20"
            aria-label="Toggle current password visibility"
            @click="showOldPassword=!showOldPassword"
          >

            <Eye
              v-if="!showOldPassword"
              class="h-4 w-4"
            />

            <EyeOff
              v-else
              class="h-4 w-4"
            />

          </button>

        </div>

        <p
          v-if="errors.old_password"
          class="mt-1.5 text-xs font-medium text-red-600"
        >
          {{ errors.old_password }}
        </p>

      </div>

      <!-- New Password -->

      <div>

        <label
          class="mb-1.5 flex items-center gap-2 text-sm font-semibold text-[#23394E]"
        >

          <KeyRound class="h-4 w-4 text-[#F29200]" />

          New Password

        </label>

        <div class="relative">

          <input
            v-model="new_password"
            :type="showNewPassword ? 'text' : 'password'"
            autocomplete="new-password"
            :class="errors.new_password ? 'border-red-300 focus:border-red-500 focus:ring-red-100' : 'border-gray-200 focus:border-[#F29200] focus:ring-[#F29200]/10'"
            class="h-11 w-full rounded-xl border bg-white px-4 pr-11 text-sm text-[#23394E] outline-none transition duration-200 placeholder:text-[#9F9F9F] focus:ring-4"
          />

          <button
            type="button"
            class="absolute right-3 top-1/2 flex h-8 w-8 -translate-y-1/2 items-center justify-center rounded-lg text-[#9F9F9F] transition duration-200 hover:bg-gray-100 hover:text-[#23394E] focus:outline-none focus:ring-2 focus:ring-[#F29200]/20"
            aria-label="Toggle new password visibility"
            @click="showNewPassword=!showNewPassword"
          >

            <Eye
              v-if="!showNewPassword"
              class="h-4 w-4"
            />

            <EyeOff
              v-else
              class="h-4 w-4"
            />

          </button>

        </div>

        <p
          v-if="errors.new_password"
          class="mt-1.5 text-xs font-medium text-red-600"
        >
          {{ errors.new_password }}
        </p>

      </div>

      <!-- Confirm Password -->

      <div>

        <label
          class="mb-1.5 flex items-center gap-2 text-sm font-semibold text-[#23394E]"
        >

          <KeyRound class="h-4 w-4 text-[#F29200]" />

          Confirm Password

        </label>

        <div class="relative">

          <input
            v-model="confirm_password"
            :type="showConfirmPassword ? 'text' : 'password'"
            autocomplete="new-password"
            :class="errors.confirm_password ? 'border-red-300 focus:border-red-500 focus:ring-red-100' : 'border-gray-200 focus:border-[#F29200] focus:ring-[#F29200]/10'"
            class="h-11 w-full rounded-xl border bg-white px-4 pr-11 text-sm text-[#23394E] outline-none transition duration-200 placeholder:text-[#9F9F9F] focus:ring-4"
          />

          <button
            type="button"
            class="absolute right-3 top-1/2 flex h-8 w-8 -translate-y-1/2 items-center justify-center rounded-lg text-[#9F9F9F] transition duration-200 hover:bg-gray-100 hover:text-[#23394E] focus:outline-none focus:ring-2 focus:ring-[#F29200]/20"
            aria-label="Toggle confirm password visibility"
            @click="showConfirmPassword=!showConfirmPassword"
          >

            <Eye
              v-if="!showConfirmPassword"
              class="h-4 w-4"
            />

            <EyeOff
              v-else
              class="h-4 w-4"
            />

          </button>

        </div>

        <p
          v-if="errors.confirm_password"
          class="mt-1.5 text-xs font-medium text-red-600"
        >
          {{ errors.confirm_password }}
        </p>

      </div>

      <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-3">

        <p class="text-xs font-semibold text-[#23394E]">
          Password requirements
        </p>

        <div class="mt-2 grid gap-1.5 text-xs text-[#9F9F9F] sm:grid-cols-2">

          <span class="flex items-center gap-2"><span class="h-1.5 w-1.5 rounded-full bg-[#F29200]"></span>At least 8 characters</span>
          <span class="flex items-center gap-2"><span class="h-1.5 w-1.5 rounded-full bg-[#F29200]"></span>One uppercase letter</span>
          <span class="flex items-center gap-2"><span class="h-1.5 w-1.5 rounded-full bg-[#F29200]"></span>One lowercase letter</span>
          <span class="flex items-center gap-2"><span class="h-1.5 w-1.5 rounded-full bg-[#F29200]"></span>One number</span>

        </div>

      </div>

      <!-- Button -->

      <div class="flex justify-end pt-1">

        <button
          type="submit"
          :disabled="saving"
          class="inline-flex h-11 items-center justify-center gap-2 rounded-xl bg-[#F29200] px-5 text-sm font-semibold text-white shadow-sm transition duration-200 hover:-translate-y-0.5 hover:bg-[#F29200]/90 hover:shadow-md disabled:cursor-not-allowed disabled:opacity-50"
        >

          <Save
            v-if="!saving"
            class="h-4 w-4"
          />

          <svg
            v-else
            class="h-4 w-4 animate-spin"
            fill="none"
            viewBox="0 0 24 24"
          >

            <circle
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
              class="opacity-25"
            />

            <path
              d="M22 12a10 10 0 00-10-10"
              stroke="currentColor"
              stroke-width="4"
              stroke-linecap="round"
            />

          </svg>

          {{ saving ? "Updating..." : "Change Password" }}

        </button>

      </div>

    </form>

  </div>
<!-- Notifications -->

<div
  class="rounded-2xl border border-gray-100 bg-white p-5 shadow-sm transition duration-300 hover:-translate-y-0.5 hover:shadow-md sm:p-6"
>

  <div class="flex items-center gap-3 border-b border-gray-100 pb-4">

    <div
      class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-[#23394E]/5"
    >
      <Bell class="h-5 w-5 text-[#23394E]" />
    </div>

    <div>

      <h3 class="text-lg font-bold text-[#23394E]">
        Notifications
      </h3>

      <p class="mt-0.5 text-sm text-[#9F9F9F]">
        Control how you receive updates.
      </p>

    </div>

  </div>

  <div class="mt-5 space-y-3">

    <!-- Email -->

    <label
      class="flex cursor-pointer items-center justify-between gap-4 rounded-xl border border-gray-100 px-4 py-3 transition duration-200 hover:border-[#F29200]/30 hover:bg-[#F29200]/5"
    >

      <div>

        <h4 class="text-sm font-semibold text-[#23394E]">
          Email Notifications
        </h4>

        <p class="mt-0.5 text-xs leading-5 text-[#9F9F9F]">
          Receive important account emails.
        </p>

      </div>

      <span class="relative inline-flex shrink-0 items-center">
        <input
          v-model="emailNotifications"
          type="checkbox"
          class="peer sr-only"
        />
        <span class="h-5 w-9 rounded-full bg-gray-200 transition duration-200 peer-checked:bg-[#F29200] peer-focus-visible:ring-4 peer-focus-visible:ring-[#F29200]/20"></span>
        <span class="pointer-events-none absolute left-0.5 h-4 w-4 rounded-full bg-white shadow-sm transition duration-200 peer-checked:translate-x-4"></span>
      </span>

    </label>

    <!-- Booking -->

    <label
      class="flex cursor-pointer items-center justify-between gap-4 rounded-xl border border-gray-100 px-4 py-3 transition duration-200 hover:border-[#F29200]/30 hover:bg-[#F29200]/5"
    >

      <div>

        <h4 class="text-sm font-semibold text-[#23394E]">
          Booking Updates
        </h4>

        <p class="mt-0.5 text-xs leading-5 text-[#9F9F9F]">
          Reservation confirmations and changes.
        </p>

      </div>

      <span class="relative inline-flex shrink-0 items-center">
        <input
          v-model="bookingNotifications"
          type="checkbox"
          class="peer sr-only"
        />
        <span class="h-5 w-9 rounded-full bg-gray-200 transition duration-200 peer-checked:bg-[#F29200] peer-focus-visible:ring-4 peer-focus-visible:ring-[#F29200]/20"></span>
        <span class="pointer-events-none absolute left-0.5 h-4 w-4 rounded-full bg-white shadow-sm transition duration-200 peer-checked:translate-x-4"></span>
      </span>

    </label>

    <!-- Payment -->

    <label
      class="flex cursor-pointer items-center justify-between gap-4 rounded-xl border border-gray-100 px-4 py-3 transition duration-200 hover:border-[#F29200]/30 hover:bg-[#F29200]/5"
    >

      <div>

        <h4 class="text-sm font-semibold text-[#23394E]">
          Payment Notifications
        </h4>

        <p class="mt-0.5 text-xs leading-5 text-[#9F9F9F]">
          Receive invoices and payment updates.
        </p>

      </div>

      <span class="relative inline-flex shrink-0 items-center">
        <input
          v-model="paymentNotifications"
          type="checkbox"
          class="peer sr-only"
        />
        <span class="h-5 w-9 rounded-full bg-gray-200 transition duration-200 peer-checked:bg-[#F29200] peer-focus-visible:ring-4 peer-focus-visible:ring-[#F29200]/20"></span>
        <span class="pointer-events-none absolute left-0.5 h-4 w-4 rounded-full bg-white shadow-sm transition duration-200 peer-checked:translate-x-4"></span>
      </span>

    </label>

  </div>

</div>
<!-- Danger Zone -->

<div
  class="rounded-2xl border border-red-200/80 bg-red-50/40 p-5 shadow-sm transition duration-300 hover:shadow-md sm:p-6"
>

  <div class="flex items-center gap-3 border-b border-red-100 pb-4">

    <div
      class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-red-100"
    >
      <TriangleAlert class="h-5 w-5 text-red-600" />
    </div>

    <div>

      <h3 class="text-lg font-bold text-red-700">
        Danger Zone
      </h3>

      <p class="mt-0.5 text-sm text-red-500">
        Permanent actions that affect your account.
      </p>

    </div>

  </div>

  <div class="mt-5 space-y-3">

    <!-- Logout -->

    <div
      class="flex flex-col gap-4 rounded-xl border border-red-100 bg-white p-4 sm:flex-row sm:items-center sm:justify-between"
    >

      <div>

        <h4 class="text-sm font-semibold text-[#23394E]">
          Logout
        </h4>

        <p class="mt-1 text-xs leading-5 text-[#9F9F9F]">
          Sign out from your account on this device.
        </p>

      </div>

      <button
        @click="logout"
        class="h-10 w-full rounded-lg bg-[#23394E] px-4 text-sm font-semibold text-white shadow-sm transition duration-200 hover:bg-[#23394E]/90 hover:shadow-md focus:outline-none focus:ring-4 focus:ring-[#23394E]/10 sm:w-auto"
      >
        Logout
      </button>

    </div>

    <!-- Delete -->

    <div
      class="flex flex-col gap-4 rounded-xl border border-red-100 bg-white p-4 sm:flex-row sm:items-center sm:justify-between"
    >

      <div>

        <h4 class="text-sm font-semibold text-red-700">
          Delete Account
        </h4>

        <p class="mt-1 text-xs leading-5 text-[#9F9F9F]">
          This action is permanent and cannot be undone.
        </p>

      </div>

<button
  type="button"
  @click="deleteAccount"
  class="rounded-xl bg-red-600 px-4 py-2 font-semibold text-white transition hover:bg-red-700"
  
>
  Delete
</button>

    </div>

  </div>

</div>
<!-- Delete Modal -->

<div
  v-if="showDeleteModal"
  class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-sm"
>

  <div
    class="w-full max-w-md rounded-2xl border border-gray-100 bg-white p-5 shadow-2xl sm:p-6"
  >

    <div class="flex justify-center">

      <div
      class="flex h-14 w-14 items-center justify-center rounded-full bg-red-100"
      >

        <TriangleAlert
          class="h-7 w-7 text-red-600"
        />

      </div>

    </div>

    <h2
      class="mt-4 text-center text-xl font-bold text-[#23394E]"
    >
      Delete Account
    </h2>

    <p
      class="mt-2 text-center text-sm leading-6 text-[#9F9F9F]"
    >

      This action is permanent.

      <br>

      Type

      <span class="font-bold text-red-600">
        DELETE
      </span>

      below to continue.

    </p>

    <input

      v-model="deleteText"

      class="mt-6 h-11 w-full rounded-xl border border-gray-200 px-4 text-sm text-[#23394E] outline-none transition duration-200 placeholder:text-[#9F9F9F] focus:border-red-500 focus:ring-4 focus:ring-red-100"

      placeholder="Type DELETE"

    />

    <div
      class="mt-6 flex flex-col-reverse gap-3 sm:flex-row sm:justify-end"
    >

      <button

        @click="showDeleteModal=false"

        class="h-10 rounded-lg border border-gray-200 px-4 text-sm font-semibold text-[#23394E] transition duration-200 hover:bg-gray-50 focus:outline-none focus:ring-4 focus:ring-[#23394E]/10"

      >

        Cancel

      </button>

      <button

        @click="deleteAccount"

        :disabled="deleting"

        class="h-10 rounded-lg bg-red-600 px-4 text-sm font-semibold text-white shadow-sm transition duration-200 hover:bg-red-700 hover:shadow-md disabled:cursor-not-allowed disabled:opacity-50"

      >

        {{ deleting ? "Deleting..." : "Delete" }}

      </button>

    </div>

  </div>

</div>
</section>

</template>
