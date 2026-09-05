<script setup>
import { ref, onMounted, onUnmounted, computed } from "vue";
import api from "@/services/api";

import { useForm } from "vee-validate";
import * as yup from "yup";
import { toast } from "vue-sonner";
import { VueTelInput } from "vue-tel-input";
import "vue-tel-input/vue-tel-input.css";

import {
  User,
  Mail,
  Phone,
  CalendarDays,
  ShieldCheck,
  Save,
  CheckCircle2,
  AlertCircle,
  Camera
} from "lucide-vue-next";

const loading = ref(true);
const saving = ref(false);

const profile = ref({});
const selectedImage = ref(null);
const imagePreview = ref(null);
const fileInput = ref(null);
const phoneData = ref(null);

const clearImagePreview = () => {

  if (imagePreview.value) {
    URL.revokeObjectURL(imagePreview.value);
  }

  imagePreview.value = null;

};

const handleImageChange = (event) => {

  const [file] = event.target.files || [];

  if (!file) {
    return;
  }

  const allowedTypes = [
    "image/jpeg",
    "image/png",
    "image/webp"
  ];

  if (!allowedTypes.includes(file.type)) {

    toast.error("Please choose a JPEG, PNG, or WEBP image.");
    event.target.value = "";
    return;

  }

  if (file.size > 2 * 1024 * 1024) {

    toast.error("Profile image must be 2 MB or smaller.");
    event.target.value = "";
    return;

  }

  clearImagePreview();

  selectedImage.value = file;
  imagePreview.value = URL.createObjectURL(file);

};

const schema = yup.object({

  username: yup
    .string()
    .required("Username is required")
    .matches(
      /^[A-Za-z]+$/,
      "Username must contain letters only."
    )
    .min(3, "Username must contain at least 3 characters.")
    .max(30, "Username cannot exceed 30 characters."),

  email: yup
    .string()
    .required("Email is required")
    .email("Please enter a valid email address.")
    .max(100, "Email is too long."),

  phone: yup
  .string()
  .required("Phone number is required")
  .test(
    "valid-phone",
    "Enter a valid phone number.",
    function (value) {
      if (!value) return false;

      if (phoneData.value?.valid !== undefined) {
        return phoneData.value.valid;
      }

      return /^\+[1-9]\d{7,14}$/.test(value);
    }
  )

});

const {
  values,
  errors,
  defineField,
  setValues,
  setErrors,
  handleSubmit
} = useForm({

  validationSchema: schema,

  initialValues: {
    username: "",
    email: "",
    phone: ""
  }

});

const [username] = defineField("username");
const [email] = defineField("email");
const [phone] = defineField("phone");

const loadProfile = async () => {

  loading.value = true;

  try {

    const { data } = await api.get("profile/");

    profile.value = {
      ...data
    };

    setValues({
      username: data.username,
      email: data.email,
      phone: data.phone
    });

  } catch (err) {

    console.error(err);

    toast.error("Failed to load profile.");

  } finally {

    loading.value = false;

  }

};

const hasChanges = computed(() => {

  return (
    values.username !== profile.value.username ||
    values.email !== profile.value.email ||
    values.phone !== profile.value.phone ||
    selectedImage.value !== null
  );

});

const saveProfile = handleSubmit(async (formData) => {

  saving.value = true;

  try {

    const payload = new FormData();
    const normalizedPhone = formData.phone
      .replace(/[^\d+]/g, "")
      .replace(/(?!^)\+/g, "");
    payload.append("username", formData.username);
    payload.append("email", formData.email);
    payload.append("phone", normalizedPhone);
    if (selectedImage.value) {
      payload.append("profile_image", selectedImage.value);
    }

    const { data } = await api.patch(
      "profile/update/",
      payload
    );

    profile.value = {
      ...profile.value,
      ...data
    };

    const storedUser = JSON.parse(
      localStorage.getItem("user") || "{}"
    );

    const updatedUser = {
      ...storedUser,
      ...data
    };

    localStorage.setItem(
      "user",
      JSON.stringify(updatedUser)
    );

    window.dispatchEvent(
      new Event("user-profile-updated")
    );

    setValues({
      username: data.username,
      email: data.email,
      phone: data.phone
    });

    selectedImage.value = null;
    clearImagePreview();

    if (fileInput.value) {
      fileInput.value.value = "";
    }

    toast.success("Profile updated successfully.");

  } catch (err) {

    if (err.response?.data) {

      const {
        profile_image: profileImageError,
        ...fieldErrors
      } = err.response.data;

      if (profileImageError) {

        toast.error(
          Array.isArray(profileImageError)
            ? profileImageError[0]
            : profileImageError
        );

      }

      const backendErrors = {};

      Object.entries(fieldErrors).forEach(
        ([field, messages]) => {

          backendErrors[field] = Array.isArray(messages)
            ? messages[0]
            : messages;

        }
      );

      setErrors(backendErrors);

    } else {

      toast.error("Something went wrong.");

    }

  } finally {

    saving.value = false;

  }

});
const handlePhoneInput = (event) => {
  let value = event.target.value;

  value = value.replace(/[^\d+]/g, "");

  value = value.replace(
    /(?!^)\+/g,
    ""
  );

  if (
    value &&
    !value.startsWith("+")
  ) {
    value = "+" + value;
  }

  phone.value =
    value.slice(0, 16);
};
const handlePhoneValidation = (data) => {
  phoneData.value = data;
};

onMounted(loadProfile);
onUnmounted(clearImagePreview);
</script>

<template>
  <section>

    <!-- Header -->

    <div class="mb-6">

      <h2 class="text-3xl font-black text-gray-900">
        My Profile
      </h2>

      <p class="mt-2 text-gray-500">
        Update your personal information and account details.
      </p>

    </div>

    <!-- Loading -->

    <div
      v-if="loading"
      class="rounded-3xl border border-gray-100 bg-white p-10 shadow-sm"
    >

      <div class="animate-pulse flex flex-col items-center">

        <div class="h-24 w-24 rounded-full bg-gray-200"></div>

        <div class="mt-5 h-6 w-40 rounded bg-gray-200"></div>

        <div class="mt-3 h-4 w-56 rounded bg-gray-100"></div>

      </div>

    </div>

    <!-- Content -->

    <div
      v-else
      class="grid gap-6 xl:grid-cols-[300px_1fr]"
    >

      <!-- Left Card -->

      <div
        class="rounded-3xl border border-gray-100 bg-white p-6 shadow-sm h-fit"
      >

        <div class="flex flex-col items-center">

          <div class="relative">

            <img
              v-if="imagePreview || profile.profile_image"
              :src="imagePreview || profile.profile_image"
              :alt="`${profile.username || 'User'} profile image`"
              class="h-24 w-24 rounded-full object-cover shadow-lg"
            >

            <div
              v-else
              class="flex h-24 w-24 items-center justify-center rounded-full bg-gradient-to-br from-amber-400 to-orange-500 text-4xl font-black text-white shadow-lg"
            >
              {{ profile.username?.charAt(0).toUpperCase() }}
            </div>

            <input
              ref="fileInput"
              type="file"
              accept="image/jpeg,image/png,image/webp"
              class="hidden"
              @change="handleImageChange"
            >

            <button
              type="button"
              title="Change profile image"
              aria-label="Change profile image"
              class="absolute -bottom-1 -right-1 flex h-8 w-8 items-center justify-center rounded-full border-2 border-white bg-[#f29200] text-white shadow-md transition duration-200 hover:scale-105 hover:bg-[#f29200]/90 focus:outline-none focus:ring-4 focus:ring-[#f29200]/20"
              @click="fileInput?.click()"
            >
              <Camera class="h-4 w-4" />
            </button>

          </div>

          <h3 class="mt-5 text-2xl font-bold text-gray-900">
            {{ profile.username }}
          </h3>

          <p class="mt-1 text-center text-gray-500 break-all">
            {{ profile.email }}
          </p>

          <span
            class="mt-5 rounded-full px-4 py-2 text-sm font-semibold"
            :class="
              profile.is_active
                ? 'bg-emerald-100 text-emerald-700'
                : 'bg-red-100 text-red-600'
            "
          >
            {{ profile.is_active ? "Active Account" : "Inactive Account" }}
          </span>

        </div>

        <div class="mt-8 space-y-5">

          <!-- Member -->

          <div class="flex items-center gap-4">

            <div
              class="flex h-11 w-11 items-center justify-center rounded-xl bg-amber-100"
            >
              <CalendarDays
                class="h-5 w-5 text-amber-600"
              />
            </div>

            <div>

              <p class="text-xs uppercase tracking-wide text-gray-400">
                Member Since
              </p>

              <p class="font-semibold text-gray-800">
                {{ new Date(profile.date_joined).toLocaleDateString() }}
              </p>

            </div>

          </div>

          <!-- Account Type -->

          <div class="flex items-center gap-4">

            <div
              class="flex h-11 w-11 items-center justify-center rounded-xl bg-blue-100"
            >
              <User
                class="h-5 w-5 text-blue-600"
              />
            </div>

            <div>

              <p class="text-xs uppercase tracking-wide text-gray-400">
                Account Type
              </p>

              <p class="font-semibold text-gray-800">
                {{ profile.is_staff ? "Administrator" : "Customer" }}
              </p>

            </div>

          </div>

          <!-- Status -->

          <div class="flex items-center gap-4">

            <div
              class="flex h-11 w-11 items-center justify-center rounded-xl bg-emerald-100"
            >
              <ShieldCheck
                class="h-5 w-5 text-emerald-600"
              />
            </div>

            <div>

              <p class="text-xs uppercase tracking-wide text-gray-400">
                Status
              </p>

              <p
                class="font-semibold"
                :class="
                  profile.is_active
                    ? 'text-emerald-600'
                    : 'text-red-600'
                "
              >
                {{ profile.is_active ? "Verified" : "Disabled" }}
              </p>

            </div>

          </div>

        </div>

      </div>

      <!-- Right Card -->

<div
  class="rounded-3xl border border-gray-100 bg-white p-6 shadow-sm"
>

  <h3 class="text-2xl font-bold text-gray-900">
    Personal Information
  </h3>

  <p class="mt-2 text-gray-500">
    Update your profile information.
  </p>

  <form
    class="mt-8"
    @submit.prevent="saveProfile"
  >

    <div class="grid gap-6 md:grid-cols-2">

      <!-- Username -->

      <div>

        <label
          class="mb-2 flex items-center gap-2 font-semibold text-gray-700"
        >
          <User class="h-5 w-5 text-amber-500"/>
          Username
        </label>

        <div class="relative">

          <input
            v-model="username"
            type="text"
            maxlength="30"
            autocomplete="off"
            @input="username = username.replace(/[^A-Za-z]/g,'')"
            :class="[
              'w-full rounded-2xl border px-5 py-3 pr-12 outline-none transition',

              errors.username
                ? 'border-red-400 focus:ring-red-100 focus:border-red-500'
                : 'border-gray-200 focus:ring-amber-100 focus:border-amber-400'
            ]"
          >

          <CheckCircle2
            v-if="!errors.username && values.username"
            class="absolute right-4 top-1/2 h-5 w-5 -translate-y-1/2 text-emerald-500"
          />

          <AlertCircle
            v-if="errors.username"
            class="absolute right-4 top-1/2 h-5 w-5 -translate-y-1/2 text-red-500"
          />

        </div>

        <div class="mt-2 flex justify-between text-xs">

          <p class="text-red-500">
            {{ errors.username }}
          </p>

          <span class="text-gray-400">
            {{ values.username.length }}/30
          </span>

        </div>

      </div>

      <!-- Phone -->

<!-- Phone -->
<div>

  <label
    class="mb-2 flex items-center gap-2 font-semibold text-gray-700"
  >
    <Phone class="h-5 w-5 text-amber-500" />
    Phone Number
  </label>

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
      autocomplete: 'tel'
    }"
    @validate="handlePhoneValidation"
    :class="[
      'workspace-phone-input',
      errors.phone ? 'phone-error' : ''
    ]"
  />

  <div
    class="mt-2 flex justify-between text-xs"
  >
    <p class="text-red-500">
      {{ errors.phone }}
    </p>

    <span class="text-gray-400">
      {{ values.phone?.length || 0 }}/20
    </span>
  </div>

</div>

    </div>

    <!-- Email -->

    <div class="mt-6">

      <label
        class="mb-2 flex items-center gap-2 font-semibold text-gray-700"
      >
        <Mail class="h-5 w-5 text-amber-500"/>
        Email Address
      </label>

      <div class="relative">

        <input
          v-model="email"
          type="email"
          maxlength="100"
          autocomplete="off"
          :class="[
            'w-full rounded-2xl border px-5 py-3 pr-12 outline-none transition',

            errors.email
              ? 'border-red-400 focus:ring-red-100 focus:border-red-500'
              : 'border-gray-200 focus:ring-amber-100 focus:border-amber-400'
          ]"
        >

        <CheckCircle2
          v-if="!errors.email && values.email"
          class="absolute right-4 top-1/2 h-5 w-5 -translate-y-1/2 text-emerald-500"
        />

        <AlertCircle
          v-if="errors.email"
          class="absolute right-4 top-1/2 h-5 w-5 -translate-y-1/2 text-red-500"
        />

      </div>

      <div class="mt-2 flex justify-between text-xs">

        <p class="text-red-500">
          {{ errors.email }}
        </p>

        <span class="text-gray-400">
          {{ values.email.length }}/100
        </span>

      </div>

    </div>

    <!-- Info Cards -->

    <div class="mt-8 grid gap-4 md:grid-cols-2">

      <div class="rounded-2xl bg-slate-50 p-5">

        <p class="text-sm text-gray-500">
          Account Type
        </p>

        <h4 class="mt-1 font-bold text-gray-900">
          {{ profile.is_staff ? "Administrator" : "Customer" }}
        </h4>

      </div>

      <div class="rounded-2xl bg-slate-50 p-5">

        <p class="text-sm text-gray-500">
          Status
        </p>

        <h4
          class="mt-1 font-bold"
          :class="profile.is_active ? 'text-emerald-600' : 'text-red-600'"
        >
          {{ profile.is_active ? "Active" : "Inactive" }}
        </h4>

      </div>

    </div>

    <!-- Save Button -->

<div class="mt-8 flex items-center justify-between border-t border-gray-100 pt-6">

  <p
    class="text-sm text-gray-500"
  >
    Changes will be saved to your account immediately.
  </p>

  <button
    type="submit"
    :disabled="saving || !hasChanges"
    class="inline-flex items-center gap-3 rounded-2xl bg-amber-500 px-7 py-3 font-semibold text-white transition-all duration-300 hover:bg-amber-600 hover:shadow-xl disabled:cursor-not-allowed disabled:opacity-50"
  >

    <!-- Save Icon -->

    <Save
      v-if="!saving"
      class="h-5 w-5"
    />

    <!-- Spinner -->

    <svg
      v-else
      class="h-5 w-5 animate-spin"
      viewBox="0 0 24 24"
      fill="none"
    >

      <circle
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        stroke-width="4"
        class="opacity-20"
      />

      <path
        d="M22 12A10 10 0 0012 2"
        stroke="currentColor"
        stroke-width="4"
        stroke-linecap="round"
      />

    </svg>

    {{ saving ? "Saving..." : "Save Changes" }}

  </button>

</div>

</form>

</div>

</div>

</section>
</template>


<style>
.workspace-phone-input {
  border: 1px solid #e5e7eb !important;
  border-radius: 1rem !important;
  min-height: 50px;
  background: white;
  transition: 0.2s;
}

.workspace-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow: 0 0 0 4px rgba(242, 146, 0, 0.1);
}

.workspace-phone-input.phone-error {
  border-color: #f87171 !important;
}

.workspace-phone-input.phone-error:focus-within {
  border-color: #ef4444 !important;
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.08);
}

.workspace-phone-input .vti__input {
  font-size: 16px;
  color: #23394e;
  background: transparent;
}

.workspace-phone-input .vti__dropdown {
  border-radius: 1rem 0 0 1rem;
}
</style>