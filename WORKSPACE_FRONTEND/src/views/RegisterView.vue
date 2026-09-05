<template>
<section class="relative min-h-screen overflow-hidden bg-[#F8FAFC]">

  <!-- Background -->

  <div class="absolute inset-0 overflow-hidden">

    <div class="absolute -top-32 -right-32 h-96 w-96 rounded-full bg-amber-400/10 blur-3xl"></div>

    <div class="absolute -bottom-32 -left-32 h-80 w-80 rounded-full bg-amber-300/10 blur-3xl"></div>

  </div>

  <div class="relative mx-auto flex min-h-screen max-w-7xl items-center px-6 py-8">

    <div class="grid w-full items-center gap-14 lg:grid-cols-2">

      <!-- LEFT SIDE -->

      <div class="hidden lg:block">

        <div class="inline-flex items-center rounded-full bg-amber-100 px-4 py-2 text-sm font-semibold text-[#F59E0B]">

          Create Your Workspace

        </div>

        <h1 class="mt-6 text-5xl font-black leading-tight text-gray-900">

          Join Our

          <span class="text-[#F59E0B]">

            Community

          </span>

          Today.

        </h1>

        <p class="mt-6 max-w-lg text-lg leading-8 text-gray-600">

          Create your account to book workspaces, manage reservations,
          and access premium office solutions from anywhere.

        </p>

        <div class="mt-10 flex gap-4">

          <router-link
            to="/workspace"
            class="rounded-xl bg-[#F59E0B] px-6 py-3 font-semibold text-white transition duration-300 hover:-translate-y-0.5 hover:bg-amber-500 hover:shadow-lg hover:shadow-amber-300/30">

            Browse Offices

          </router-link>

          <router-link
            to="/login"
            class="rounded-xl border border-gray-200 bg-white px-6 py-3 font-semibold text-gray-800 transition hover:border-[#F59E0B] hover:text-[#F59E0B]">

            Sign In

          </router-link>

        </div>

      </div>

      <!-- REGISTER CARD -->

      <div class="flex justify-center">

        <div
          class="w-full max-w-md rounded-3xl border border-white/70 bg-white/90 p-6 shadow-[0_20px_60px_rgba(15,23,42,.08)] backdrop-blur">

          <!-- HEADER -->

          <div class="flex items-center gap-4">

            <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-amber-100">

              <UserPlus class="h-7 w-7 text-[#F59E0B]" />

            </div>

            <div>

              <h2 class="text-3xl font-black text-gray-900">

                Create Account

              </h2>

              <p class="mt-1 text-sm text-gray-500">

                Start your workspace journey.

              </p>

            </div>

          </div>

          <p class="mt-5 text-sm text-gray-500">

            Already have an account?

            <router-link
              to="/login"
              class="font-semibold text-[#F59E0B] hover:underline">

              Sign In

            </router-link>

          </p>

          <!-- FORM -->

          <form
            class="mt-6 space-y-3"
            @submit.prevent="handleRegister"
            novalidate
            >

            <!-- ERROR -->

            <div
              v-if="errorMsg"
              class="rounded-xl border border-red-200 bg-red-50 p-3">

              <div class="flex items-start gap-2">

                <CircleAlert
                  class="mt-0.5 h-5 w-5 shrink-0 text-red-500" />

                <div class="text-sm text-red-600">

                  <template v-if="typeof errorMsg === 'object'">

                    <ul class="space-y-1">

                      <li
                        v-for="(val, key) in errorMsg"
                        :key="key">

                        <span class="font-semibold capitalize">

                          {{ key }}

                        </span>

                        :
                        {{ Array.isArray(val) ? val.join(', ') : val }}

                      </li>

                    </ul>

                  </template>

                  <template v-else>

                    {{ errorMsg }}

                  </template>

                </div>

              </div>

            </div>

            <!-- USERNAME -->
            <div>

  <div class="relative">

    <User
      class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2"
      :class="
        fieldErrors.username
          ? 'text-red-400'
          : 'text-[#9f9f9f]'
      "
    />

    <input
  v-model="username"
  @input="handleUsernameInput"
  type="text"
  maxlength="14"
  autocomplete="username"
  placeholder="Username"
  :class="[
    'h-11 w-full rounded-xl border bg-white pl-12 pr-4 text-sm text-[#23394e] outline-none transition',
    fieldErrors.username
      ? 'border-red-400 focus:border-red-500 focus:ring-4 focus:ring-red-50'
      : 'border-gray-200 focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10'
  ]"
/>

  </div>

  <p
    v-if="fieldErrors.username"
    class="mt-1.5 text-xs text-red-500"
  >
    {{ fieldErrors.username }}
  </p>

</div>
             

            <!-- EMAIL -->

           <div>

  <div class="relative">

    <Mail
      class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2"
      :class="
        fieldErrors.email
          ? 'text-red-400'
          : 'text-[#9f9f9f]'
      "
    />

<input
  v-model="email"
  type="email"
  maxlength="30"
  autocomplete="email"
  placeholder="Email Address"
  :class="[
    'h-11 w-full rounded-xl border bg-white pl-12 pr-4 text-sm text-[#23394e] outline-none transition',
    fieldErrors.email
      ? 'border-red-400 focus:border-red-500 focus:ring-4 focus:ring-red-50'
      : 'border-gray-200 focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10'
  ]"
/>

  </div>

  <p
    v-if="fieldErrors.email"
    class="mt-1.5 text-xs text-red-500"
  >
    {{ fieldErrors.email }}
  </p>

</div>

<!-- PHONE -->
<div>
  <VueTelInput
    v-model="phone"
    mode="international"
    :auto-format="true"
    :valid-characters-only="true"
    :preferred-countries="['MA', 'FR', 'ES', 'US', 'GB']"
    :dropdown-options="{
      showDialCodeInList: true,
      showFlags: true,
      showSearchBox: true
    }"
    :input-options="{
      placeholder: 'Phone Number',
      autocomplete: 'tel',
      maxlength: 20

    }"
    @validate="handlePhoneValidation"
    class="workspace-phone-input"
  />

  <p
    v-if="fieldErrors.phone"
    class="mt-1.5 text-xs text-red-500"
  >
    {{ fieldErrors.phone }}
  </p>
</div>

                  <!-- PASSWORD -->

<div>

  <div class="relative">

    <Lock
      class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2"
      :class="
        fieldErrors.password
          ? 'text-red-400'
          : 'text-[#9f9f9f]'
      "
    />

<input
  v-model="password"
  :type="showPassword ? 'text' : 'password'"
  minlength="8"
  maxlength="20"
  autocomplete="new-password"
  placeholder="Password"
  :class="[
    'h-11 w-full rounded-xl border bg-white pl-12 pr-12 text-sm text-[#23394e] outline-none transition',
    fieldErrors.password
      ? 'border-red-400 focus:border-red-500 focus:ring-4 focus:ring-red-50'
      : 'border-gray-200 focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10'
  ]"
/>

    <button
      type="button"
      @click="showPassword = !showPassword"
      class="absolute right-4 top-1/2 -translate-y-1/2 text-[#9f9f9f] transition hover:text-[#f29200]"
    >
      <Eye
        v-if="!showPassword"
        class="h-5 w-5"
      />

      <EyeOff
        v-else
        class="h-5 w-5"
      />
    </button>

  </div>

  <p
    v-if="fieldErrors.password"
    class="mt-1.5 text-xs text-red-500"
  >
    {{ fieldErrors.password }}
  </p>

</div>

            <!-- REGISTER BUTTON -->

            <button
              type="submit"
              :disabled="loading"
              class="group flex h-11 w-full items-center justify-center gap-2 rounded-xl bg-[#F59E0B] font-semibold text-white transition duration-300 hover:-translate-y-0.5 hover:bg-amber-500 hover:shadow-lg hover:shadow-amber-300/40 disabled:cursor-not-allowed disabled:opacity-60">

              <template v-if="loading">

                <Loader2 class="h-5 w-5 animate-spin" />

                Creating Account...

              </template>

              <template v-else>

                <UserPlus class="h-5 w-5" />

                Create Account

                <ArrowRight
                  class="h-4 w-4 transition duration-300 group-hover:translate-x-1" />

              </template>

            </button>

            <!-- DIVIDER -->

            <div class="relative py-2">

              <div class="absolute inset-0 flex items-center">

                <div class="w-full border-t border-gray-200"></div>

              </div>

            </div>

            <!-- SECURITY -->

            <div class="rounded-2xl bg-gray-50 p-3">

              <div class="flex items-center gap-3">

                <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-emerald-100">

                  <ShieldCheck class="h-5 w-5 text-emerald-600" />

                </div>

                <div>

                  <p class="text-sm font-semibold text-gray-900">

                    Secure Registration

                  </p>

                  <p class="text-xs text-gray-500">

                    Your personal information is encrypted and protected.

                  </p>

                </div>

              </div>

            </div>

          </form>

        </div>

      </div>

    </div>

  </div>

</section>

</template>

<script setup>
import {
  ref,
  onMounted,
  onUnmounted
} from "vue";

import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { VueTelInput } from "vue-tel-input";
import {
  UserPlus,
  User,
  Mail,
  Phone,
  Lock,
  Eye,
  EyeOff,
  ArrowRight,
  ShieldCheck,
  Loader2,
  CircleAlert
} from "lucide-vue-next";


const router = useRouter();
const authStore = useAuthStore();


const username = ref("");
const email = ref("");
const phone = ref("");
const password = ref("");

const loading = ref(false);
const errorMsg = ref(null);

const showPassword = ref(false);

const phoneData = ref(null);

const fieldErrors = ref({
  username: "",
  email: "",
  phone: "",
  password: ""
});


const validateForm = () => {

  fieldErrors.value = {
    username: "",
    email: "",
    phone: "",
    password: ""
  };

  let valid = true;

  const cleanUsername =
    username.value.trim();

  const cleanEmail =
    email.value.trim();

  const cleanPhone =
    phone.value.trim();


  // =========================
  // Username
  // Letters only
  // Min 3 / Max 14
  // =========================

  const usernameRegex =
    /^[A-Za-z]+$/;

  if (!cleanUsername) {

    fieldErrors.value.username =
      "Username is required.";

    valid = false;

  } else if (
    cleanUsername.length < 3
  ) {

    fieldErrors.value.username =
      "Username must contain at least 3 characters.";

    valid = false;

  } else if (
    cleanUsername.length > 14
  ) {

    fieldErrors.value.username =
      "Username cannot exceed 14 characters.";

    valid = false;

  } else if (
    !usernameRegex.test(cleanUsername)
  ) {

    fieldErrors.value.username =
      "Username must contain letters only.";

    valid = false;

  }


  // =========================
  // Email
  // Valid email
  // Max 30
  // =========================

  const emailRegex =
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!cleanEmail) {

    fieldErrors.value.email =
      "Email address is required.";

    valid = false;

  } else if (
    cleanEmail.length > 30
  ) {

    fieldErrors.value.email =
      "Email cannot exceed 30 characters.";

    valid = false;

  } else if (
    !emailRegex.test(cleanEmail)
  ) {

    fieldErrors.value.email =
      "Enter a valid email address.";

    valid = false;

  }


  // =========================
  // Phone
  // Digits only
  // Exactly 10
  // =========================

const normalizedPhone =
  (phoneData.value?.number || cleanPhone)
    .replace(/[^\d+]/g, "");

if (!cleanPhone) {
  fieldErrors.value.phone =
    "Phone number is required.";

  valid = false;

} else if (normalizedPhone.length > 16) {
  fieldErrors.value.phone =
    "Phone number is too long.";

  valid = false;

} else if (!phoneData.value?.valid) {
  fieldErrors.value.phone =
    "Enter a valid phone number.";

  valid = false;
}


  // =========================
  // Password
  // Min 8 / Max 20
  // =========================

  if (!password.value) {

    fieldErrors.value.password =
      "Password is required.";

    valid = false;

  } else if (
    password.value.length < 8
  ) {

    fieldErrors.value.password =
      "Password must contain at least 8 characters.";

    valid = false;

  } else if (
    password.value.length > 20
  ) {

    fieldErrors.value.password =
      "Password cannot exceed 20 characters.";

    valid = false;

  }


  return valid;
};


const handleRegister = async () => {

  errorMsg.value = null;

  if (!validateForm()) {
    return;
  }

  loading.value = true;

  try {

const success =
  await authStore.register(
    username.value.trim(),
    email.value.trim().toLowerCase(),
    phoneData.value?.number || phone.value,
    password.value
  );

    if (success) {

      router.push({
        name: "login",
        query: {
          registered: "true"
        }
      });

      return;
    }


    // Backend validation errors

    const errors =
      authStore.error;

    if (
      errors &&
      typeof errors === "object"
    ) {

      fieldErrors.value.username =
        Array.isArray(errors.username)
          ? errors.username[0]
          : errors.username || "";

      fieldErrors.value.email =
        Array.isArray(errors.email)
          ? errors.email[0]
          : errors.email || "";

      fieldErrors.value.phone =
        Array.isArray(errors.phone)
          ? errors.phone[0]
          : errors.phone || "";

      fieldErrors.value.password =
        Array.isArray(errors.password)
          ? errors.password[0]
          : errors.password || "";

    } else {

      errorMsg.value =
        errors ||
        "Registration failed. Please try again.";

    }

  } catch (err) {

    const errors =
      err.response?.data ||
      authStore.error;

    if (
      errors &&
      typeof errors === "object"
    ) {

      fieldErrors.value.username =
        Array.isArray(errors.username)
          ? errors.username[0]
          : errors.username || "";

      fieldErrors.value.email =
        Array.isArray(errors.email)
          ? errors.email[0]
          : errors.email || "";

      fieldErrors.value.phone =
        Array.isArray(errors.phone)
          ? errors.phone[0]
          : errors.phone || "";

      fieldErrors.value.password =
        Array.isArray(errors.password)
          ? errors.password[0]
          : errors.password || "";

    } else {

      errorMsg.value =
        errors ||
        "Registration failed. Please try again.";

    }

  } finally {

    loading.value = false;

  }

};


// =========================
// Username Input
// Remove everything except letters
// Max 14
// =========================

const handleUsernameInput = (event) => {

  const cleanValue =
    event.target.value
      .replace(/[^A-Za-z]/g, "")
      .slice(0, 14);

  username.value = cleanValue;

};


// =========================
// Phone Input
// Remove everything except digits
// Max 10
// =========================


const handlePhoneValidation = (data) => {
  phoneData.value = data;

  const normalized =
    (data?.number || phone.value || "")
      .replace(/[^\d+]/g, "");

  if (normalized.length > 16) {
    fieldErrors.value.phone =
      "Phone number is too long.";

    return;
  }

  if (phone.value) {
    fieldErrors.value.phone =
      data.valid
        ? ""
        : "Enter a valid phone number.";
  }
};
// =========================
// Page
// =========================

onMounted(() => {

  document.body.style.overflow =
    "hidden";

});


onUnmounted(() => {

  document.body.style.overflow =
    "auto";

});
</script>

<style>
.workspace-phone-input {
  border: 1px solid #e5e7eb !important;
  border-radius: 0.75rem !important;
  min-height: 44px;
  background: white;
}

.workspace-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow: 0 0 0 4px rgba(242, 146, 0, 0.1);
}

.workspace-phone-input .vti__input {
  font-size: 14px;
  color: #23394e;
}

.workspace-phone-input .vti__dropdown {
  border-radius: 0.75rem 0 0 0.75rem;
}
</style>