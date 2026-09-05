<template>
<section ref="page" class="relative h-screen overflow-hidden bg-[#F8FAFC]">

  <!-- Background -->

  <div class="absolute inset-0 overflow-hidden">

    <div data-login-background="top" class="absolute -top-32 -right-32 h-96 w-96 rounded-full bg-amber-400/10 blur-3xl"></div>

    <div data-login-background="bottom" class="absolute -bottom-24 -left-24 h-80 w-80 rounded-full bg-amber-300/10 blur-3xl"></div>

  </div>

<div class="relative mx-auto flex h-full max-w-7xl items-center px-6">
    <div class="grid w-full items-center gap-14 lg:grid-cols-2">

      <!-- LEFT -->

      <div class="hidden lg:block">

        <div data-login-badge class="inline-flex items-center rounded-full bg-amber-100 px-4 py-2 text-sm font-semibold text-[#F59E0B]">

          Welcome Back

        </div>

        <h1 class="mt-6 text-5xl font-black leading-tight text-gray-900">

          <span class="block overflow-hidden">
            <span data-login-title-line class="block">
              Your

              <span class="text-[#F59E0B]">

                Workspace

              </span>
            </span>
          </span>

          <span class="block overflow-hidden">
            <span data-login-title-line class="block">Awaits.</span>
          </span>

        </h1>

        <p data-login-description class="mt-6 max-w-lg text-lg leading-8 text-gray-600">

          Sign in to manage bookings, discover inspiring workspaces,
          and grow your business with flexible office solutions.

        </p>

        <div class="mt-10 flex gap-4">

          <router-link
            to="/workspace"
            data-login-left-action
            class="rounded-xl bg-[#F59E0B] px-6 py-3 font-semibold text-white transition duration-300 hover:-translate-y-0.5 hover:bg-amber-500 hover:shadow-lg hover:shadow-amber-300/30">

            Browse Offices

          </router-link>

          <router-link
            to="/register"
            data-login-left-action
            class="rounded-xl border border-gray-200 bg-white px-6 py-3 font-semibold text-gray-800 transition hover:border-[#F59E0B] hover:text-[#F59E0B]">

            Create Account

          </router-link>

        </div>

      </div>

      <!-- LOGIN CARD -->

      <div class="flex justify-center">

        <div data-login-card class="w-full max-w-md rounded-3xl border border-white/60 bg-white/90 p-7 shadow-[0_20px_60px_rgba(15,23,42,.08)] backdrop-blur">

          <!-- HEADER -->

          <div data-login-card-item class="flex items-center gap-4">

            <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-amber-100">

              <LogIn class="h-7 w-7 text-[#F59E0B]" />

            </div>

            <div>

              <h2 class="text-3xl font-black text-gray-900">

                Welcome Back

              </h2>

              <p class="mt-1 text-sm text-gray-500">

                Sign in to continue.

              </p>

            </div>

          </div>

          <p data-login-card-item class="mt-5 text-sm text-gray-500">

            Don't have an account?

            <router-link
              to="/register"
              class="font-semibold text-[#F59E0B] hover:underline">

              Create Account

            </router-link>

          </p>

          <!-- FORM -->

          <form
            class="mt-6 space-y-4"
            @submit.prevent="handleLogin"
            novalidate>

            <!-- ERROR -->

            <div
              v-if="errorMsg"
              ref="errorAlert"
              class="flex items-center gap-2 rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-600">

              <CircleAlert class="h-5 w-5 shrink-0" />

              {{ errorMsg }}

            </div>

            <!-- USERNAME -->

            <div ref="usernameField" data-login-card-item>

  <div class="relative" @focusin="animateInputFocus(usernameField, true)" @focusout="animateInputFocus(usernameField, false)">

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
    'h-12 w-full rounded-xl border bg-white pl-12 pr-4 text-sm text-[#23394e] outline-none transition',
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

                        <!-- PASSWORD -->

<div ref="passwordField" data-login-card-item>

  <div class="relative" @focusin="animateInputFocus(passwordField, true)" @focusout="animateInputFocus(passwordField, false)">

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
      autocomplete="current-password"
      placeholder="Password"
      :class="[
        'h-12 w-full rounded-xl border bg-white pl-12 pr-12 text-sm text-[#23394e] outline-none transition',
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

            <!-- OPTIONS -->

            <div data-login-card-item class="flex items-center justify-between">

              <label class="flex cursor-pointer items-center gap-2">

                <input
  type="checkbox"
  class="h-4 w-4 rounded border-gray-300 accent-[#f29200]"
/>

                <span class="text-sm text-gray-600">

                  Remember me

                </span>

              </label>

              <router-link
                to="/forgot-password"
                class="text-sm font-medium text-[#F59E0B] transition hover:underline">

                Forgot Password?

              </router-link>

            </div>

            <!-- BUTTON -->

            <button
              ref="signInButton"
              data-login-card-item
              type="submit"
              :disabled="loading"
              @mouseenter="animateSignInButton(true)"
              @mouseleave="animateSignInButton(false)"
              class="group flex h-12 w-full items-center justify-center gap-2 rounded-xl bg-[#F59E0B] font-semibold text-white transition duration-300 hover:-translate-y-0.5 hover:bg-amber-500 hover:shadow-lg hover:shadow-amber-300/40 disabled:cursor-not-allowed disabled:opacity-60">

              <template v-if="loading">

                <Loader2 class="h-5 w-5 animate-spin" />

                Signing In...

              </template>

              <template v-else>

                <LogIn class="h-5 w-5" />

                Sign In

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

            <div data-login-card-item class="rounded-2xl bg-gray-50 p-3">

              <div class="flex items-center gap-3">

                <div data-login-shield class="flex h-10 w-10 items-center justify-center rounded-xl bg-emerald-100">

                  <ShieldCheck class="h-5 w-5 text-emerald-600" />

                </div>

                <div>

                  <p class="text-sm font-semibold text-gray-900">

                    Secure Login

                  </p>

                  <p class="text-xs text-gray-500">

                    Your credentials are protected with encrypted authentication.

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
  nextTick,
  onMounted,
  onUnmounted,
  watch
} from "vue";

import gsap from "gsap";

import {
  useRouter,
  useRoute
} from "vue-router";

import { useAuthStore } from "@/stores/auth";

import {
  LogIn,
  User,
  Lock,
  Eye,
  EyeOff,
  ArrowRight,
  ShieldCheck,
  Loader2,
  CircleAlert
} from "lucide-vue-next";


const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const page = ref(null);
const usernameField = ref(null);
const passwordField = ref(null);
const signInButton = ref(null);
const errorAlert = ref(null);

let ctx;
let prefersReducedMotion = false;


const username = ref("");
const password = ref("");

const loading = ref(false);
const errorMsg = ref("");

const showPassword = ref(false);


const fieldErrors = ref({
  username: "",
  password: ""
});


const validateForm = () => {

  fieldErrors.value = {
    username: "",
    password: ""
  };

  let valid = true;

  const cleanUsername =
    username.value.trim();


  // Username

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
  }


  // Password

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


  if (!valid) {
    nextTick(() => {
      if (fieldErrors.value.username) {
        animateFieldError(usernameField.value);
      }

      if (fieldErrors.value.password) {
        animateFieldError(passwordField.value);
      }
    });
  }

  return valid;


  const usernameRegex =
  /^[A-Za-z]+$/;

if (!cleanUsername) {

  fieldErrors.value.username =
    "Username is required.";

  valid = false;

} else if (cleanUsername.length < 3) {

  fieldErrors.value.username =
    "Username must contain at least 3 characters.";

  valid = false;

} else if (cleanUsername.length > 14) {

  fieldErrors.value.username =
    "Username cannot exceed 14 characters.";

  valid = false;

} else if (!usernameRegex.test(cleanUsername)) {

  fieldErrors.value.username =
    "Username must contain letters only.";

  valid = false;
}

};





const handleLogin = async () => {

  errorMsg.value = "";

  if (!validateForm()) {
    return;
  }

  loading.value = true;

  try {

    const success =
      await authStore.login(
        username.value.trim(),
        password.value
      );

    if (success) {

      if (route.query.redirect) {

        router.replace(
          route.query.redirect
        );

      } else if (
        authStore.isAdmin
      ) {

        router.replace("/admin");

      } else {

        router.replace("/dashboard");

      }

      return;
    }

    errorMsg.value =
      authStore.error ||
      "Invalid username or password.";

  } catch (err) {

    errorMsg.value =
      authStore.error ||
      err.response?.data?.detail ||
      "Invalid username or password.";

  } finally {

    loading.value = false;
  }

};

const handleUsernameInput = (event) => {
  const cleanValue =
    event.target.value
      .replace(/[^A-Za-z]/g, "")
      .slice(0, 14);

  username.value = cleanValue;
};

/* ==========================================================
   Input Interactions & Validation Errors
========================================================== */

const animateInputFocus = (field, isFocused) => {
  if (prefersReducedMotion || !field) {
    return;
  }

  gsap.to(field, {
    scale: isFocused ? 1.01 : 1,
    y: isFocused ? -1 : 0,
    duration: 0.2,
    ease: "power2.out",
    overwrite: "auto"
  });
};

const animateSignInButton = (isHovering) => {
  if (prefersReducedMotion || loading.value || !signInButton.value) {
    return;
  }

  gsap.to(signInButton.value, {
    y: isHovering ? -2 : 0,
    scale: isHovering ? 1.01 : 1,
    duration: 0.2,
    ease: "power2.out",
    overwrite: "auto"
  });
};

const animateFieldError = (field) => {
  if (prefersReducedMotion || !field) {
    return;
  }

  gsap.to(field, {
    keyframes: [
      { x: -4 },
      { x: 4 },
      { x: -3 },
      { x: 3 },
      { x: 0 }
    ],
    duration: 0.3,
    ease: "power1.inOut",
    overwrite: "auto"
  });
};

const animateGlobalError = () => {
  if (prefersReducedMotion || !errorAlert.value) {
    return;
  }

  gsap.fromTo(
    errorAlert.value,
    { opacity: 0, y: -5, scale: 0.98 },
    {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 0.3,
      ease: "power2.out",
      overwrite: "auto"
    }
  );
};

watch(errorMsg, value => {
  if (value) {
    nextTick(animateGlobalError);
  }
});


onMounted(() => {
  document.body.style.overflow =
    "hidden";
});


onUnmounted(() => {
  document.body.style.overflow =
    "auto";
});
</script>
