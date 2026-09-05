<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm"
  >

    <div class="overflow-x-auto">

      <table class="min-w-full">

        <thead class="bg-[#23394e]">

          <tr>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase tracking-wide text-white">
              User
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase tracking-wide text-white">
              Phone
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase tracking-wide text-white">
              Role
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase tracking-wide text-white">
              Status
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase tracking-wide text-white">
              Actions
            </th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="user in filteredUsers"
            :key="user.id"
            class="border-t border-gray-100 transition hover:bg-gray-50"
          >

            <td class="px-5 py-4">

              <div class="flex items-center gap-3">

               <div
  class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-lg bg-[#f29200]/10"
>
  <img
    v-if="user.profile_image"
    :src="user.profile_image"
    :alt="user.username"
    class="h-full w-full object-cover"
  />

  <User
    v-else
    class="h-4 w-4 text-[#f29200]"
  />
</div>

                <div>
                  <p class="text-sm font-semibold text-[#23394e]">
                    {{ user.username }}
                  </p>

                  <p class="text-xs text-[#9f9f9f]">
                    {{ user.email }}
                  </p>
                </div>

              </div>

            </td>

            <td class="px-5 py-4 text-sm text-[#23394e]">
              {{ user.phone || "-" }}
            </td>

            <td class="px-5 py-4 text-center">

              <span
                class="rounded-full bg-[#23394e]/5 px-2.5 py-1 text-xs font-medium text-[#23394e]"
              >
                {{ user.is_staff ? "Admin" : "User" }}
              </span>

            </td>

            <td class="px-5 py-4 text-center">

              <span
                v-if="user.is_active"
                class="inline-flex items-center gap-1 rounded-full bg-green-50 px-2.5 py-1 text-xs font-medium text-green-700"
              >
                <CircleCheck class="h-3.5 w-3.5" />

                Active
              </span>

              <span
                v-else
                class="inline-flex items-center gap-1 rounded-full bg-red-50 px-2.5 py-1 text-xs font-medium text-red-600"
              >
                <CircleX class="h-3.5 w-3.5" />

                Disabled
              </span>

            </td>

            <td class="px-5 py-4">

<div
  class="flex items-center justify-center gap-1"
>
  <template v-if="!user.is_staff">
    <button
      @click="openEditModal(user)"
      title="Edit user"
      class="rounded-lg p-2 text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200]"
    >
      <Pencil class="h-4 w-4" />
    </button>

    <button
      @click="toggleUser(user)"
      :title="
        user.is_active
          ? 'Disable user'
          : 'Enable user'
      "
      class="rounded-lg p-2 text-[#f29200] transition hover:bg-[#f29200]/10"
    >
      <Lock
        v-if="user.is_active"
        class="h-4 w-4"
      />

      <Unlock
        v-else
        class="h-4 w-4"
      />
    </button>

    <button
      @click="deleteUser(user)"
      title="Delete user"
      class="rounded-lg p-2 text-red-500 transition hover:bg-red-50"
    >
      <Trash2 class="h-4 w-4" />
    </button>
  </template>

  <span
    v-else
    class="text-xs font-medium text-[#9f9f9f]"
  >
    Protected
  </span>
</div>

            </td>

          </tr>

          <tr v-if="filteredUsers.length === 0">

            <td colspan="5" class="py-12 text-center">

              <div class="flex flex-col items-center gap-3">

                <Users class="h-9 w-9 text-[#9f9f9f]" />

                <p class="text-sm text-[#9f9f9f]">
                  No users found.
                </p>

              </div>

            </td>

          </tr>

        </tbody>

      </table>
      <div
  v-if="adminStore.totalUsers > 0"
  class="flex flex-col gap-3 border-t border-gray-200 px-5 py-4 sm:flex-row sm:items-center sm:justify-between"
>

  <p class="text-sm text-[#9f9f9f]">

    Total

    <span class="font-semibold text-[#23394e]">
      {{ adminStore.totalUsers }}
    </span>

    users

  </p>

  <div class="flex items-center gap-2">

    <button
      @click="previousPage"
      :disabled="
        adminStore.userCurrentPage <= 1 ||
        adminStore.loading
      "
      class="flex items-center gap-1 rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] disabled:opacity-40"
    >

      <ChevronLeft class="h-4 w-4" />

      Previous

    </button>

    <button
      v-for="page in visiblePages"
      :key="page"
      @click="goToPage(page)"
      class="flex h-9 min-w-9 items-center justify-center rounded-lg px-2 text-sm font-medium"
      :class="
        page === adminStore.userCurrentPage
          ? 'bg-[#f29200] text-white'
          : 'border border-gray-200 text-[#23394e]'
      "
    >
      {{ page }}
    </button>

    <button
      @click="nextPage"
      :disabled="
        adminStore.userCurrentPage >=
          adminStore.userTotalPages ||
        adminStore.loading
      "
      class="flex items-center gap-1 rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] disabled:opacity-40"
    >

      Next

      <ChevronRight class="h-4 w-4" />

    </button>

  </div>

</div>

    </div>

  </div>

  <!-- Edit User Modal -->

  <div
    v-if="showEditModal"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4"
    @click.self="closeEditModal"
  >

    <div
      class="w-full max-w-lg rounded-2xl bg-white shadow-xl"
    >

      <div
        class="flex items-center justify-between border-b border-gray-200 px-6 py-4"
      >
        <div>
          <h2 class="text-lg font-bold text-[#23394e]">
            Edit User
          </h2>

          <p class="mt-1 text-sm text-[#9f9f9f]">
            Update user account information.
          </p>
        </div>

        <button
          @click="closeEditModal"
          class="rounded-lg p-2 text-[#9f9f9f] transition hover:bg-gray-100 hover:text-[#23394e]"
        >
          <X class="h-5 w-5" />
        </button>
      </div>

      <div class="space-y-4 p-6">

        <div>
          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            Username
          </label>

          <input
            v-model="selectedUser.username"
            type="text"
            class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
          />
        </div>

        <div>
          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            Email
          </label>

          <input
            v-model="selectedUser.email"
            type="email"
            class="w-full rounded-lg border border-gray-200 px-3 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
          />
        </div>

        <div>
          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            Phone
          </label>

          <VueTelInput
            v-model="selectedUser.phone"
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
              'admin-phone-input',
              phoneError ? 'phone-error' : ''
            ]"
          />

          <p
            v-if="phoneError"
            class="mt-1.5 text-xs text-red-500"
          >
            {{ phoneError }}
          </p>
        </div>



      </div>

      <div
        class="flex justify-end gap-3 border-t border-gray-200 px-6 py-4"
      >

        <button
          @click="closeEditModal"
          class="rounded-lg border border-gray-200 px-4 py-2 text-sm font-medium text-[#23394e] transition hover:bg-gray-50"
        >
          Cancel
        </button>

        <button
          @click="saveUser"
          :disabled="adminStore.loading"
          class="rounded-lg bg-[#f29200] px-4 py-2 text-sm font-medium text-white transition hover:opacity-90 disabled:opacity-50"
        >
          Save Changes
        </button>

      </div>

    </div>

  </div>
</template>

<script setup>
import {
  computed,
  ref
} from "vue";

import Swal from "sweetalert2";
import { VueTelInput } from "vue-tel-input";
import "vue-tel-input/vue-tel-input.css";

import {
  User,
  Users,
  Pencil,
  Trash2,
  CircleCheck,
  CircleX,
  Lock,
  Unlock,
  X,
  ChevronLeft,
  ChevronRight
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const showEditModal = ref(false);
const phoneData = ref(null);
const phoneError = ref("");

const selectedUser = ref({
  id: null,
  username: "",
  email: "",
  phone: "",
});

const filteredUsers = computed(() => {

  const search =
    adminStore.userSearch
      ?.trim()
      .toLowerCase();

  if (!search) {
    return adminStore.users;
  }

  return adminStore.users.filter(user => {

    const username =
      user.username?.toLowerCase() || "";

    const email =
      user.email?.toLowerCase() || "";

    return (
      username.includes(search) ||
      email.includes(search)
    );

  });

});

const openEditModal = (user) => {

  selectedUser.value = {
    id: user.id,
    username: user.username,
    email: user.email,
    phone: user.phone || "",
  };

  phoneData.value = null;
  phoneError.value = "";

  showEditModal.value = true;

};

const closeEditModal = () => {

  showEditModal.value = false;
  phoneData.value = null;
  phoneError.value = "";

};

const handlePhoneValidation = (data) => {
  phoneData.value = data;

  if (!selectedUser.value.phone) {
    phoneError.value = "";
    return;
  }

  phoneError.value =
    data.valid
      ? ""
      : "Enter a valid phone number.";
};

const saveUser = async () => {
  if (
    selectedUser.value.phone &&
    phoneData.value?.valid === false
  ) {
    phoneError.value = "Enter a valid phone number.";
    return;
  }

  const normalizedPhone = selectedUser.value.phone
    ? (
        phoneData.value?.number ||
        selectedUser.value.phone
      )
        .replace(/[^\d+]/g, "")
        .replace(/(?!^)\+/g, "")
    : "";

  try {
    await adminStore.updateUser(
      selectedUser.value.id,
      {
        username:
          selectedUser.value.username,

        email:
          selectedUser.value.email,

        phone:
          normalizedPhone
      }
    );

    closeEditModal();

    Swal.fire({
      icon: "success",
      title: "User Updated",
      timer: 1400,
      showConfirmButton: false
    });

  } catch (err) {
    const data =
      err.response?.data || {};

    Swal.fire({
      icon: "error",
      title: "Update Failed",
      text:
        data.username?.[0] ||
        data.email?.[0] ||
        data.phone?.[0] ||
        "Unable to update user."
    });
  }
};

const deleteUser = async (user) => {

  const result = await Swal.fire({
    title: "Delete User?",
    text: `Delete ${user.username}?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Delete",
    cancelButtonText: "Cancel",
    confirmButtonColor: "#f29200",
    cancelButtonColor: "#9f9f9f"
  });

  if (!result.isConfirmed) return;

  try {

    await adminStore.deleteUser(user.id);

    Swal.fire({
      icon: "success",
      title: "User Deleted",
      timer: 1200,
      showConfirmButton: false
    });

  } catch {

    Swal.fire({
      icon: "error",
      title: "Delete Failed"
    });

  }

};

const toggleUser = async (user) => {

  const wasActive =
    user.is_active;

  try {

    await adminStore.toggleUser(user.id);

    Swal.fire({
      icon: "success",
      title:
        wasActive
          ? "User Disabled"
          : "User Enabled",
      timer: 1200,
      showConfirmButton: false
    });

  } catch {

    Swal.fire({
      icon: "error",
      title: "Operation Failed"
    });

  }

};
const visiblePages = computed(() => {

  const total =
    adminStore.userTotalPages;

  const current =
    adminStore.userCurrentPage;

  if (total <= 5) {

    return Array.from(
      { length: total },
      (_, index) => index + 1
    );

  }

  let start = Math.max(
    current - 2,
    1
  );

  let end = Math.min(
    start + 4,
    total
  );

  if (end - start < 4) {

    start = Math.max(
      end - 4,
      1
    );

  }

  return Array.from(
    { length: end - start + 1 },
    (_, index) => start + index
  );

});

const goToPage = (page) => {

  if (
    page < 1 ||
    page > adminStore.userTotalPages ||
    page === adminStore.userCurrentPage
  ) {
    return;
  }

  adminStore.fetchUsers(page);

};

const previousPage = () => {
  goToPage(
    adminStore.userCurrentPage - 1
  );
};

const nextPage = () => {
  goToPage(
    adminStore.userCurrentPage + 1
  );
};
</script>

<style>
.admin-phone-input {
  border: 1px solid #e5e7eb !important;
  border-radius: 0.5rem !important;
  min-height: 38px;
  background: white;
  transition: 0.2s;
}

.admin-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow: 0 0 0 3px rgba(242, 146, 0, 0.1);
}

.admin-phone-input.phone-error {
  border-color: #ef4444 !important;
}

.admin-phone-input.phone-error:focus-within {
  border-color: #ef4444 !important;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.08);
}

.admin-phone-input .vti__input {
  font-size: 14px;
  color: #23394e;
  background: transparent;
}

.admin-phone-input .vti__dropdown {
  border-radius: 0.5rem 0 0 0.5rem;
}
</style>
