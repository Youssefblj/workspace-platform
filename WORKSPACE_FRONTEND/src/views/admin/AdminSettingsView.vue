<template>
  <div class="space-y-6">

    <div>
      <h1 class="text-2xl font-bold text-[#23394e]">
        Settings
      </h1>

      <p class="mt-1 text-sm text-[#9f9f9f]">
        Manage your administrator profile and password.
      </p>
    </div>

    <div class="grid gap-6 xl:grid-cols-3">

      <!-- Account info -->

      <div
        class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
      >

        <div class="flex items-center gap-3">

<div class="relative">

  <div
    class="flex h-14 w-14 items-center justify-center overflow-hidden rounded-xl bg-[#f29200]/10"
  >

    <img
      v-if="
        imagePreview ||
        adminStore.adminProfile?.profile_image
      "
      :src="
        imagePreview ||
        adminStore.adminProfile?.profile_image
      "
      alt="Admin profile"
      class="h-full w-full object-cover"
    />

    <User
      v-else
      class="h-5 w-5 text-[#f29200]"
    />

  </div>

  <button
    type="button"
    @click="openImagePicker"
    title="Change profile photo"
    class="absolute -bottom-2 -right-2 flex h-8 w-8 items-center justify-center rounded-full border-2 border-white bg-[#f29200] text-white shadow-sm transition hover:bg-[#d98200]"
  >
    <Camera class="h-4 w-4" />
  </button>

  <input
    ref="fileInput"
    type="file"
    accept="image/jpeg,image/png,image/webp"
    class="hidden"
    @change="handleImageChange"
  />

</div>

          <div>
            <p class="font-semibold text-[#23394e]">
              {{ adminStore.adminProfile?.username || "-" }}
            </p>

            <p class="text-sm text-[#9f9f9f]">
              Administrator
            </p>
          </div>

        </div>

        <div class="mt-6 space-y-4">

          <div>
            <p class="text-xs text-[#9f9f9f]">
              Email
            </p>

            <p class="mt-1 text-sm font-medium text-[#23394e]">
              {{ adminStore.adminProfile?.email || "-" }}
            </p>
          </div>

          <div>
            <p class="text-xs text-[#9f9f9f]">
              Phone
            </p>

            <p class="mt-1 text-sm font-medium text-[#23394e]">
              {{ adminStore.adminProfile?.phone || "Not provided" }}
            </p>
          </div>

          <div>
            <p class="text-xs text-[#9f9f9f]">
              Account Status
            </p>

            <span
              class="mt-1 inline-flex rounded-full bg-green-50 px-3 py-1 text-xs font-medium text-green-700"
            >
              Active
            </span>
          </div>

          <div>
            <p class="text-xs text-[#9f9f9f]">
              Joined
            </p>

            <p class="mt-1 text-sm font-medium text-[#23394e]">
              {{ formatDate(adminStore.adminProfile?.date_joined) }}
            </p>
          </div>

        </div>

      </div>

      <!-- Profile -->

      <form
        @submit.prevent="saveProfile"
        class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm xl:col-span-2"
      >

        <div class="mb-5 flex items-center gap-3">

          <UserRoundPen class="h-5 w-5 text-[#f29200]" />

          <div>
            <h2 class="font-bold text-[#23394e]">
              Profile Information
            </h2>

            <p class="text-sm text-[#9f9f9f]">
              Update your personal information.
            </p>
          </div>

        </div>

        <div class="grid gap-4 sm:grid-cols-2">

          <div>
            <label class="mb-2 block text-sm font-medium text-[#23394e]">
              Username
            </label>

            <input
              v-model="profile.username"
              type="text"
              class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm outline-none focus:border-[#f29200]"
            />

            <p
              v-if="profileErrors.username"
              class="mt-1 text-xs text-red-500"
            >
              {{ profileErrors.username }}
            </p>
          </div>

          <div>
            <label class="mb-2 block text-sm font-medium text-[#23394e]">
              Email
            </label>

            <input
              v-model="profile.email"
              type="email"
              class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm outline-none focus:border-[#f29200]"
            />

            <p
              v-if="profileErrors.email"
              class="mt-1 text-xs text-red-500"
            >
              {{ profileErrors.email }}
            </p>
          </div>

          <div class="sm:col-span-2">
            <label class="mb-2 block text-sm font-medium text-[#23394e]">
              Phone
            </label>

            <VueTelInput
              v-model="profile.phone"
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
              :class="[
                'admin-settings-phone-input',
                profileErrors.phone ? 'phone-error' : ''
              ]"
            />

            <p
              v-if="profileErrors.phone"
              class="mt-1 text-xs text-red-500"
            >
              {{ profileErrors.phone }}
            </p>
          </div>

        </div>

        <div class="mt-5 flex justify-end">

          <button
            type="submit"
            :disabled="adminStore.loading"
            class="inline-flex items-center gap-2 rounded-lg bg-[#f29200] px-4 py-2 text-sm font-medium text-white disabled:opacity-50"
          >
            <Save class="h-4 w-4" />

            Save Changes
          </button>

        </div>

      </form>

    </div>

    <!-- Password -->

    <form
      @submit.prevent="changePassword"
      class="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm"
    >

      <div class="mb-5 flex items-center gap-3">

        <LockKeyhole class="h-5 w-5 text-[#f29200]" />

        <div>
          <h2 class="font-bold text-[#23394e]">
            Change Password
          </h2>

          <p class="text-sm text-[#9f9f9f]">
            Use your current password to set a new one.
          </p>
        </div>

      </div>

      <div class="grid gap-4 md:grid-cols-3">

        <div>
          <label class="mb-2 block text-sm font-medium text-[#23394e]">
            Current Password
          </label>

          <input
            v-model="password.old_password"
            type="password"
            autocomplete="current-password"

            class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm outline-none focus:border-[#f29200]"
          />
        </div>

        <div>
          <label class="mb-2 block text-sm font-medium text-[#23394e]">
            New Password
          </label>

          <input
            v-model="password.new_password"
            type="password"
            autocomplete="new-password"
            class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm outline-none focus:border-[#f29200]"
          />
        </div>

        <div>
          <label class="mb-2 block text-sm font-medium text-[#23394e]">
            Confirm Password
          </label>

          <input
            v-model="password.confirm_password"
            type="password"
            autocomplete="new-password"
            class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm outline-none focus:border-[#f29200]"
          />
        </div>

      </div>

      <p
        v-if="passwordError"
        class="mt-3 text-sm text-red-500"
      >
        {{ passwordError }}
      </p>

      <div class="mt-5 flex justify-end">

        <button
          type="submit"
          :disabled="adminStore.loading"
          class="inline-flex items-center gap-2 rounded-lg bg-[#23394e] px-4 py-2 text-sm font-medium text-white disabled:opacity-50"
        >
          <KeyRound class="h-4 w-4" />

          Change Password
        </button>

      </div>

    </form>

  </div>
</template>

<script setup>
import {
  reactive,
  ref,
  onMounted,
  onUnmounted
} from "vue";
import { useAuthStore } from "@/stores/auth"
import { VueTelInput } from "vue-tel-input";
import "vue-tel-input/vue-tel-input.css";


import Swal from "sweetalert2";

import {
  User,
  UserRoundPen,
  Save,
  LockKeyhole,
  KeyRound,
  Camera
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";
const auth = useAuthStore()
const adminStore = useAdminStore();
const selectedImage = ref(null);
const imagePreview = ref(null);
const fileInput = ref(null);
const phoneData = ref(null);


const profile = reactive({
  username: "",
  email: "",
  phone: ""
});

const profileErrors = reactive({
  username: "",
  email: "",
  phone: ""
});

const password = reactive({
  old_password: "",
  new_password: "",
  confirm_password: ""
});

const passwordError = ref("");

const loadProfile = async () => {

  try {

    const data =
      await adminStore.fetchAdminProfile();

    profile.username =
      data.username || "";

    profile.email =
      data.email || "";

    profile.phone =
      data.phone || "";

    phoneData.value = null;
    profileErrors.phone = "";

  } catch {

    Swal.fire({
      icon: "error",
      title: "Unable to load profile"
    });

  }

};

const clearProfileErrors = () => {
  profileErrors.username = "";
  profileErrors.email = "";
  profileErrors.phone = "";
};

const handlePhoneValidation = (data) => {
  phoneData.value = data;

  if (!profile.phone) {
    profileErrors.phone = "";
    return;
  }

  profileErrors.phone =
    data.valid
      ? ""
      : "Enter a valid phone number.";
};

const saveProfile = async () => {

  clearProfileErrors();

  if (
    profile.phone &&
    phoneData.value?.valid === false
  ) {
    profileErrors.phone = "Enter a valid phone number.";
    return;
  }

  try {

    const payload = new FormData();

    payload.append(
      "username",
      profile.username.trim()
    );

    payload.append(
      "email",
      profile.email.trim()
    );

    const normalizedPhone = profile.phone
      ? (
          phoneData.value?.number ||
          profile.phone
        )
          .replace(/[^\d+]/g, "")
          .replace(/(?!^)\+/g, "")
      : "";

    payload.append(
      "phone",
      normalizedPhone
    );

    if (
      selectedImage.value instanceof File
    ) {
      payload.append(
        "profile_image",
        selectedImage.value
      );
    }

    const data =
      await adminStore.updateAdminProfile(
        payload
      );
      const refreshedProfile =
  await adminStore.fetchAdminProfile()

auth.user = {
  ...auth.user,
  ...refreshedProfile
}

localStorage.setItem(
  "user",
  JSON.stringify(auth.user)
)

    selectedImage.value = null;
    clearImagePreview();
    phoneData.value = null;

    if (fileInput.value) {
      fileInput.value.value = "";
    }

    window.dispatchEvent(
      new Event("user-profile-updated")
    );

    Swal.fire({
      icon: "success",
      title: "Profile Updated",
      timer: 1400,
      showConfirmButton: false
    });

  } catch (err) {

    const data = err.response?.data || {};

    profileErrors.username =
      data.username?.[0] || "";

    profileErrors.email =
      data.email?.[0] || "";

    profileErrors.phone =
      data.phone?.[0] || "";

    if (data.profile_image) {
      Swal.fire({
        icon: "error",
        title: "Image Upload Failed",
        text: Array.isArray(
          data.profile_image
        )
          ? data.profile_image[0]
          : data.profile_image
      });
    }

  }

};

const changePassword = async () => {

  passwordError.value = "";

  if (
    !password.old_password ||
    !password.new_password ||
    !password.confirm_password
  ) {

    passwordError.value =
      "All password fields are required.";

    return;
  }

  if (
    password.new_password !==
    password.confirm_password
  ) {

    passwordError.value =
      "New passwords do not match.";

    return;
  }

  if (password.new_password.length < 8) {

    passwordError.value =
      "New password must contain at least 8 characters.";

    return;
  }

  try {

    await adminStore.changeAdminPassword({
      old_password:
        password.old_password,

      new_password:
        password.new_password
    });

    password.old_password = "";
    password.new_password = "";
    password.confirm_password = "";

    Swal.fire({
      icon: "success",
      title: "Password Changed",
      text: "Your password was updated successfully.",
      timer: 1600,
      showConfirmButton: false
    });

  } catch (err) {

    passwordError.value =
      err.response?.data?.error ||
      err.response?.data?.new_password?.[0] ||
      "Unable to change password.";

  }

};

const formatDate = (value) => {

  if (!value) return "-";

  return new Date(value).toLocaleDateString(
    undefined,
    {
      day: "2-digit",
      month: "short",
      year: "numeric"
    }
  );

};


const clearImagePreview = () => {
  if (imagePreview.value) {
    URL.revokeObjectURL(imagePreview.value);
  }

  imagePreview.value = null;
};

const openImagePicker = () => {
  fileInput.value?.click();
};

const handleImageChange = (event) => {
  const file = event.target.files?.[0];

  if (!file) return;

  const allowedTypes = [
    "image/jpeg",
    "image/png",
    "image/webp"
  ];

  if (!allowedTypes.includes(file.type)) {
    Swal.fire({
      icon: "error",
      title: "Invalid Image",
      text: "Please choose a JPG, PNG or WEBP image."
    });

    event.target.value = "";
    return;
  }

  if (file.size > 2 * 1024 * 1024) {
    Swal.fire({
      icon: "error",
      title: "Image Too Large",
      text: "Profile image must be 2 MB or smaller."
    });

    event.target.value = "";
    return;
  }

  clearImagePreview();

  selectedImage.value = file;
  imagePreview.value = URL.createObjectURL(file);
};

onMounted(() => {
  loadProfile();
});

onUnmounted(() => {
  clearImagePreview();
});
</script>

<style>
.admin-settings-phone-input {
  border: 1px solid #e5e7eb !important;
  border-radius: 0.5rem !important;
  min-height: 40px;
  background: white;
  transition: 0.2s;
}

.admin-settings-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow: 0 0 0 3px rgba(242, 146, 0, 0.1);
}

.admin-settings-phone-input.phone-error {
  border-color: #ef4444 !important;
}

.admin-settings-phone-input.phone-error:focus-within {
  border-color: #ef4444 !important;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.08);
}

.admin-settings-phone-input .vti__input {
  font-size: 14px;
  color: #23394e;
  background: transparent;
}

.admin-settings-phone-input .vti__dropdown {
  border-radius: 0.5rem 0 0 0.5rem;
}
</style>
