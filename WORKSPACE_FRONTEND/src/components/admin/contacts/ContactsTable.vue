<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm"
  >

    <div
      v-if="
        adminStore.loading &&
        adminStore.contacts.length === 0
      "
      class="flex items-center justify-center gap-3 py-14"
    >
      <LoaderCircle
        class="h-5 w-5 animate-spin text-[#f29200]"
      />

      <span class="text-sm text-[#9f9f9f]">
        Loading messages...
      </span>
    </div>

    <div v-else class="overflow-x-auto">

      <table class="min-w-full">

        <thead class="bg-[#23394e]">
          <tr>
            <th class="px-5 py-4 text-left text-xs font-semibold uppercase text-white">
              Sender
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase text-white">
              Subject
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase text-white">
              Category
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase text-white">
              Status
            </th>

            <th class="px-5 py-4 text-left text-xs font-semibold uppercase text-white">
              Date
            </th>

            <th class="px-5 py-4 text-center text-xs font-semibold uppercase text-white">
              Actions
            </th>
          </tr>
        </thead>

        <tbody>

          <tr
            v-for="contact in adminStore.contacts"
            :key="contact.id"
            class="border-t border-gray-100 transition hover:bg-gray-50"
          >

            <td class="px-5 py-4">

              <div class="flex items-center gap-3">

                <div
  class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-xl bg-[#f29200]/10"
>
  <img
    v-if="contact.user_profile_image"
    :src="contact.user_profile_image"
    :alt="contact.name || 'User'"
    class="h-full w-full object-cover"
  />

  <User
    v-else
    class="h-4 w-4 text-[#f29200]"
  />
</div>

                <div>
                  <p class="text-sm font-semibold text-[#23394e]">
                    {{ contact.name }}
                  </p>

                  <p class="text-xs text-[#9f9f9f]">
                    {{ contact.email }}
                  </p>
                </div>

              </div>

            </td>

            <td class="px-5 py-4">
              <p
                class="max-w-[240px] truncate text-sm font-medium text-[#23394e]"
                :title="contact.subject"
              >
                {{ contact.subject }}
              </p>
            </td>

            <td class="px-5 py-4 text-center">
              <span
                class="rounded-full bg-[#23394e]/5 px-3 py-1 text-xs font-medium text-[#23394e]"
              >
                {{ formatLabel(contact.category) }}
              </span>
            </td>

            <td class="px-5 py-4 text-center">

              <span
                class="inline-flex items-center rounded-full px-3 py-1 text-xs font-semibold"
                :class="statusClass(contact.status)"
              >
                {{ formatLabel(contact.status) }}
              </span>

            </td>

            <td class="px-5 py-4 text-sm text-[#9f9f9f]">
              {{ formatDate(contact.created_at) }}
            </td>

            <td class="px-5 py-4">

              <div class="flex items-center justify-center gap-1">

                <button
                  @click="emit('view', contact)"
                  title="View message"
                  class="rounded-lg p-2 text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200]"
                >
                  <Eye class="h-4 w-4" />
                </button>

                <button
                  @click="emit('reply', contact)"
                  title="Reply"
                  class="rounded-lg p-2 text-[#f29200] transition hover:bg-[#f29200]/10"
                >
                  <Reply class="h-4 w-4" />
                </button>

                <button
                  v-if="contact.status !== 'in_progress'"
                  @click="changeStatus(contact, 'in_progress')"
                  title="Set in progress"
                  class="rounded-lg p-2 text-[#9f9f9f] transition hover:bg-gray-100 hover:text-[#23394e]"
                >
                  <Clock3 class="h-4 w-4" />
                </button>

                <button
                  v-if="contact.status !== 'closed'"
                  @click="changeStatus(contact, 'closed')"
                  title="Close message"
                  class="rounded-lg p-2 text-[#23394e] transition hover:bg-gray-100"
                >
                  <Archive class="h-4 w-4" />
                </button>

                <button
                  @click="deleteContact(contact)"
                  title="Delete message"
                  class="rounded-lg p-2 text-red-500 transition hover:bg-red-50"
                >
                  <Trash2 class="h-4 w-4" />
                </button>

              </div>

            </td>

          </tr>

          <tr v-if="adminStore.contacts.length === 0">
            <td colspan="6" class="py-14">

              <div class="flex flex-col items-center text-center">
                <MailX class="h-9 w-9 text-[#9f9f9f]" />

                <p class="mt-3 text-sm font-semibold text-[#23394e]">
                  No messages found
                </p>

                <p class="mt-1 text-xs text-[#9f9f9f]">
                  Try another search or filter.
                </p>
              </div>

            </td>
          </tr>

        </tbody>

      </table>

      <div
        v-if="adminStore.totalContacts > 0"
        class="flex flex-col gap-3 border-t border-gray-200 px-5 py-4 sm:flex-row sm:items-center sm:justify-between"
      >

        <p class="text-sm text-[#9f9f9f]">
          Total
          <span class="font-semibold text-[#23394e]">
            {{ adminStore.totalContacts }}
          </span>
          messages
        </p>

        <div class="flex items-center gap-2">

          <button
            @click="previousPage"
            :disabled="
              adminStore.contactCurrentPage <= 1 ||
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
              page === adminStore.contactCurrentPage
                ? 'bg-[#f29200] text-white'
                : 'border border-gray-200 text-[#23394e]'
            "
          >
            {{ page }}
          </button>

          <button
            @click="nextPage"
            :disabled="
              adminStore.contactCurrentPage >= adminStore.contactTotalPages ||
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
</template>

<script setup>
import { computed } from "vue";
import Swal from "sweetalert2";

import {
  User,
  Eye,
  Reply,
  Trash2,
  Clock3,
  Archive,
  MailX,
  LoaderCircle,
  ChevronLeft,
  ChevronRight
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

const adminStore = useAdminStore();

const emit = defineEmits([
  "view",
  "reply"
]);

const formatLabel = (value) => {
  if (!value) return "-";

  return value
    .replaceAll("_", " ")
    .replace(/\b\w/g, char => char.toUpperCase());
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

const statusClass = (status) => {
  switch (status) {
    case "answered":
      return "bg-green-50 text-green-700";

    case "closed":
      return "bg-gray-100 text-[#23394e]";

    case "in_progress":
      return "bg-[#f29200]/10 text-[#f29200]";

    default:
      return "bg-[#23394e]/10 text-[#23394e]";
  }
};

const changeStatus = async (
  contact,
  status
) => {
  try {
    await adminStore.updateContactStatus(
      contact.id,
      status
    );
  } catch {
    Swal.fire({
      icon: "error",
      title: "Update Failed",
      text: "Unable to update message status."
    });
  }
};

const deleteContact = async (contact) => {

  const result = await Swal.fire({
    title: "Delete Message?",
    text: `Delete "${contact.subject}"?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Delete",
    cancelButtonText: "Cancel",
    confirmButtonColor: "#f29200",
    cancelButtonColor: "#9f9f9f"
  });

  if (!result.isConfirmed) return;

  try {
    await adminStore.deleteContact(
      contact.id
    );

    Swal.fire({
      icon: "success",
      title: "Message Deleted",
      timer: 1300,
      showConfirmButton: false
    });

  } catch {
    Swal.fire({
      icon: "error",
      title: "Delete Failed"
    });
  }
};

const visiblePages = computed(() => {

  const total =
    adminStore.contactTotalPages;

  const current =
    adminStore.contactCurrentPage;

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
    page > adminStore.contactTotalPages ||
    page === adminStore.contactCurrentPage
  ) return;

  adminStore.fetchContacts(page);
};

const previousPage = () => {
  goToPage(
    adminStore.contactCurrentPage - 1
  );
};

const nextPage = () => {
  goToPage(
    adminStore.contactCurrentPage + 1
  );
};
</script>