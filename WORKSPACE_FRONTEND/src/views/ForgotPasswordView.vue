<template>
  <section
    class="relative min-h-screen overflow-hidden bg-[#F8FAFC]"
  >

    <!-- Background -->

    <div class="absolute inset-0 overflow-hidden">
      <div
        class="absolute -right-32 -top-32 h-96 w-96 rounded-full bg-[#f29200]/10 blur-3xl"
      />

      <div
        class="absolute -bottom-24 -left-24 h-80 w-80 rounded-full bg-[#f29200]/10 blur-3xl"
      />
    </div>

    <div
      class="relative mx-auto flex min-h-screen max-w-7xl items-center px-6 py-8"
    >

      <div
        class="grid w-full items-center gap-14 lg:grid-cols-2"
      >

        <!-- LEFT -->

        <div class="hidden lg:block">

          <div
            class="inline-flex items-center rounded-full bg-[#f29200]/10 px-4 py-2 text-sm font-semibold text-[#f29200]"
          >
            Password Recovery
          </div>

          <h1
            class="mt-6 text-5xl font-black leading-tight text-[#23394e]"
          >
            Forgot your

            <span class="text-[#f29200]">
              password?
            </span>
          </h1>

          <p
            class="mt-6 max-w-lg text-lg leading-8 text-[#9f9f9f]"
          >
            Enter the email connected to your account.
            We'll send you a verification code to reset your
            password.
          </p>

          <RouterLink
            to="/login"
            class="mt-8 inline-flex items-center gap-2 font-semibold text-[#23394e] transition hover:text-[#f29200]"
          >
            <ArrowLeft class="h-4 w-4" />

            Back to Sign In
          </RouterLink>

        </div>

        <!-- CARD -->

        <div class="flex justify-center">

          <div
            class="w-full max-w-md rounded-3xl border border-white/70 bg-white/90 p-7 shadow-[0_20px_60px_rgba(15,23,42,.08)] backdrop-blur"
          >

            <!-- Header -->

            <div class="flex items-center gap-4">

              <div
                class="flex h-14 w-14 items-center justify-center rounded-2xl bg-[#f29200]/10"
              >
                <KeyRound class="h-7 w-7 text-[#f29200]" />
              </div>

              <div>

                <h2
                  class="text-2xl font-black text-[#23394e]"
                >
                  Reset Password
                </h2>

                <p
                  class="mt-1 text-sm text-[#9f9f9f]"
                >
                  Enter your account email.
                </p>

              </div>

            </div>

            <!-- FORM -->

            <form
              class="mt-7 space-y-4"
              @submit.prevent="handleForgotPassword"
              novalidate
            >

              <!-- General error -->

              <div
                v-if="errorMsg"
                class="flex items-start gap-2 rounded-xl border border-red-200 bg-red-50 p-3 text-sm text-red-600"
              >
                <CircleAlert class="mt-0.5 h-5 w-5 shrink-0" />

                {{ errorMsg }}
              </div>

              <!-- Email -->

              <div>

                <label
                  class="mb-2 block text-sm font-semibold text-[#23394e]"
                >
                  Email Address
                </label>

                <div class="relative">

                  <Mail
                    class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2"
                    :class="
                      emailError
                        ? 'text-red-400'
                        : 'text-[#9f9f9f]'
                    "
                  />

                  <input
                    v-model="email"
                    type="email"
                    maxlength="30"
                    autocomplete="email"
                    placeholder="you@example.com"
                    :class="[
                      'h-12 w-full rounded-xl border bg-white pl-12 pr-4 text-sm text-[#23394e] outline-none transition',
                      emailError
                        ? 'border-red-400 focus:border-red-500 focus:ring-4 focus:ring-red-50'
                        : 'border-gray-200 focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10'
                    ]"
                  />

                </div>

                <p
                  v-if="emailError"
                  class="mt-1.5 text-xs text-red-500"
                >
                  {{ emailError }}
                </p>

              </div>

              <!-- Submit -->

              <button
                type="submit"
                :disabled="loading"
                class="flex h-12 w-full items-center justify-center gap-2 rounded-xl bg-[#f29200] font-semibold text-white transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"
              >

                <Loader2
                  v-if="loading"
                  class="h-5 w-5 animate-spin"
                />

                <Send
                  v-else
                  class="h-5 w-5"
                />

                {{ loading ? "Sending..." : "Send Reset Code" }}

              </button>

              <p
                class="text-center text-sm text-[#9f9f9f]"
              >
                Remember your password?

                <RouterLink
                  to="/login"
                  class="font-semibold text-[#f29200]"
                >
                  Sign In
                </RouterLink>
              </p>

            </form>

          </div>

        </div>

      </div>

    </div>

  </section>
</template>

<script setup>
import {
  ref
} from "vue";

import {
  useRouter
} from "vue-router";

import api from "@/services/api";

import {
  Mail,
  KeyRound,
  Send,
  Loader2,
  CircleAlert,
  ArrowLeft
} from "lucide-vue-next";


const router = useRouter();

const email = ref("");

const emailError = ref("");
const errorMsg = ref("");
const loading = ref(false);


const validateEmail = () => {

  emailError.value = "";

  const value =
    email.value.trim().toLowerCase();

  const emailRegex =
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!value) {

    emailError.value =
      "Email address is required.";

    return false;
  }

  if (value.length > 30) {

    emailError.value =
      "Email cannot exceed 30 characters.";

    return false;
  }

  if (!emailRegex.test(value)) {

    emailError.value =
      "Enter a valid email address.";

    return false;
  }

  return true;
};


const handleForgotPassword = async () => {

  errorMsg.value = "";

  if (!validateEmail()) {
    return;
  }

  loading.value = true;

  try {

    await api.post(
      "forgot-password/",
      {
        email:
          email.value.trim().toLowerCase()
      }
    );

    router.push({
      name: "reset-password",
      query: {
        email:
          email.value.trim().toLowerCase()
      }
    });

  } catch (err) {

    const data =
      err.response?.data;

    emailError.value =
      data?.email?.[0] || "";

    if (!emailError.value) {

      errorMsg.value =
        data?.error ||
        data?.detail ||
        "Unable to send reset code.";

    }

  } finally {

    loading.value = false;
  }

};
</script>