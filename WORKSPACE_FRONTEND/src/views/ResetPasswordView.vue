<template>
  <section
    class="relative min-h-screen overflow-hidden bg-[#F8FAFC]"
  >

    <div class="absolute inset-0 overflow-hidden">
      <div
        class="absolute -right-32 -top-32 h-96 w-96 rounded-full bg-[#f29200]/10 blur-3xl"
      />

      <div
        class="absolute -bottom-24 -left-24 h-80 w-80 rounded-full bg-[#f29200]/10 blur-3xl"
      />
    </div>

    <div
      class="relative mx-auto flex min-h-screen max-w-7xl items-center justify-center px-6 py-8"
    >

      <div
        class="w-full max-w-md rounded-3xl border border-white/70 bg-white/90 p-7 shadow-[0_20px_60px_rgba(15,23,42,.08)] backdrop-blur"
      >

        <div class="flex items-center gap-4">

          <div
            class="flex h-14 w-14 items-center justify-center rounded-2xl bg-[#f29200]/10"
          >
            <ShieldCheck class="h-7 w-7 text-[#f29200]" />
          </div>

          <div>

            <h1
              class="text-2xl font-black text-[#23394e]"
            >
              Create New Password
            </h1>

            <p
              class="mt-1 text-sm text-[#9f9f9f]"
            >
              Enter the code sent to your email.
            </p>

          </div>

        </div>

        <form
          class="mt-7 space-y-4"
          @submit.prevent="handleResetPassword"
          novalidate
        >

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
              Email
            </label>

            <input
              v-model="email"
              type="email"
              maxlength="30"
              autocomplete="email"
              class="h-12 w-full rounded-xl border border-gray-200 bg-gray-50 px-4 text-sm text-[#23394e] outline-none"
              readonly
            />

          </div>

          <!-- Code -->

          <div>

            <label
              class="mb-2 block text-sm font-semibold text-[#23394e]"
            >
              Verification Code
            </label>

            <input
              v-model="code"
              @input="handleCodeInput"
              type="text"
              inputmode="numeric"
              maxlength="6"
              autocomplete="one-time-code"
              placeholder="6-digit code"
              :class="[
                'h-12 w-full rounded-xl border bg-white px-4 text-center text-lg font-semibold tracking-[0.35em] text-[#23394e] outline-none transition',
                fieldErrors.code
                  ? 'border-red-400'
                  : 'border-gray-200 focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10'
              ]"
            />

            <p
              v-if="fieldErrors.code"
              class="mt-1.5 text-xs text-red-500"
            >
              {{ fieldErrors.code }}
            </p>

          </div>

          <!-- Password -->

          <div>

            <label
              class="mb-2 block text-sm font-semibold text-[#23394e]"
            >
              New Password
            </label>

            <div class="relative">

              <Lock
                class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-[#9f9f9f]"
              />

              <input
                v-model="newPassword"
                :type="
                  showPassword
                    ? 'text'
                    : 'password'
                "
                minlength="8"
                maxlength="20"
                autocomplete="new-password"
                placeholder="New password"
                :class="[
                  'h-12 w-full rounded-xl border bg-white pl-12 pr-12 text-sm text-[#23394e] outline-none transition',
                  fieldErrors.password
                    ? 'border-red-400'
                    : 'border-gray-200 focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10'
                ]"
              />

              <button
                type="button"
                @click="
                  showPassword =
                    !showPassword
                "
                class="absolute right-4 top-1/2 -translate-y-1/2 text-[#9f9f9f] hover:text-[#f29200]"
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

          <button
            type="submit"
            :disabled="loading"
            class="flex h-12 w-full items-center justify-center gap-2 rounded-xl bg-[#f29200] font-semibold text-white transition hover:opacity-90 disabled:opacity-50"
          >

            <Loader2
              v-if="loading"
              class="h-5 w-5 animate-spin"
            />

            <KeyRound
              v-else
              class="h-5 w-5"
            />

            {{
              loading
                ? "Resetting..."
                : "Reset Password"
            }}

          </button>

        </form>

      </div>

    </div>

  </section>
</template>

<script setup>
import {
  ref
} from "vue";

import {
  useRoute,
  useRouter
} from "vue-router";

import api from "@/services/api";

import {
  ShieldCheck,
  CircleAlert,
  Lock,
  Eye,
  EyeOff,
  Loader2,
  KeyRound
} from "lucide-vue-next";


const route = useRoute();
const router = useRouter();


const email = ref(
  route.query.email || ""
);

const code = ref("");
const newPassword = ref("");

const showPassword = ref(false);
const loading = ref(false);
const errorMsg = ref("");


const fieldErrors = ref({
  code: "",
  password: ""
});


const handleCodeInput = (event) => {

  code.value =
    event.target.value
      .replace(/\D/g, "")
      .slice(0, 6);

};


const validateForm = () => {

  fieldErrors.value = {
    code: "",
    password: ""
  };

  let valid = true;

  if (!/^\d{6}$/.test(code.value)) {

    fieldErrors.value.code =
      "Enter the 6-digit verification code.";

    valid = false;
  }

  if (!newPassword.value) {

    fieldErrors.value.password =
      "New password is required.";

    valid = false;

  } else if (
    newPassword.value.length < 8
  ) {

    fieldErrors.value.password =
      "Password must contain at least 8 characters.";

    valid = false;

  } else if (
    newPassword.value.length > 20
  ) {

    fieldErrors.value.password =
      "Password cannot exceed 20 characters.";

    valid = false;
  }

  return valid;
};


const handleResetPassword = async () => {

  errorMsg.value = "";

  if (!email.value) {

    router.replace(
      "/forgot-password"
    );

    return;
  }

  if (!validateForm()) {
    return;
  }

  loading.value = true;

  try {

    await api.post(
      "reset-password/",
      {
        email:
          email.value.trim().toLowerCase(),

        code:
          code.value,

        new_password:
          newPassword.value
      }
    );

    router.replace({
      name: "login",
      query: {
        reset: "success"
      }
    });

  } catch (err) {

    const data =
      err.response?.data;

    if (data?.code) {

      fieldErrors.value.code =
        Array.isArray(data.code)
          ? data.code[0]
          : data.code;

    } else if (
      data?.new_password
    ) {

      fieldErrors.value.password =
        Array.isArray(
          data.new_password
        )
          ? data.new_password[0]
          : data.new_password;

    } else {

      errorMsg.value =
        data?.error ||
        data?.detail ||
        "Unable to reset password.";

    }

  } finally {

    loading.value = false;
  }

};
</script>