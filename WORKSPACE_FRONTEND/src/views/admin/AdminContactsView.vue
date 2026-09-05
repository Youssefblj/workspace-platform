<template>
  <div class="space-y-6">

    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold text-[#23394e]">
          Contacts Management
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Review and manage customer messages.
        </p>
      </div>

<button
  type="button"
  @click="refreshContacts"
  :disabled="refreshing"
  class="inline-flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-[#23394e] transition hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
>
  <RefreshCw
    class="h-4 w-4"
    :class="{
      'animate-spin': refreshing
    }"
  />

  {{ refreshing ? "Refreshing..." : "Refresh" }}
</button>
    </div>

    <div
      class="flex flex-col gap-3 rounded-xl border border-gray-200 bg-white p-4 lg:flex-row lg:items-center"
    >

      <div class="relative flex-1">
        <Search
          class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9f9f9f]"
        />

        <input
          v-model="adminStore.contactSearch"
          type="text"
          placeholder="Search name, email, subject..."
          class="w-full rounded-lg border border-gray-200 py-2 pl-10 pr-4 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
        />
      </div>

      <select
        v-model="adminStore.contactStatusFilter"
        class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
      >
        <option value="">All Statuses</option>
        <option value="new">New</option>
        <option value="in_progress">In Progress</option>
        <option value="answered">Answered</option>
        <option value="closed">Closed</option>
      </select>

      <select
        v-model="adminStore.contactCategoryFilter"
        class="rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#23394e] outline-none focus:border-[#f29200]"
      >
        <option value="">All Categories</option>
        <option value="general">General</option>
        <option value="booking">Booking</option>
        <option value="payment">Payment</option>
        <option value="technical">Technical</option>
        <option value="complaint">Complaint</option>
        <option value="suggestion">Suggestion</option>
      </select>

      <button
        v-if="
          adminStore.contactSearch ||
          adminStore.contactStatusFilter ||
          adminStore.contactCategoryFilter
        "
        @click="resetFilters"
        class="inline-flex items-center gap-2 rounded-lg border border-gray-200 px-4 py-2 text-sm text-[#9f9f9f] transition hover:border-[#f29200] hover:text-[#f29200]"
      >
        <X class="h-4 w-4" />
        Reset
      </button>

    </div>

    <ContactsTable
      @view="openDetails"
      @reply="openReply"
    />

    <ContactDetailModal
      :show="showDetailModal"
      :contact="selectedContact"
      @close="closeDetails"
      @reply="openReply"
    />

    <ContactReplyModal
      :show="showReplyModal"
      :contact="selectedContact"
      @close="closeReply"
    />

  </div>
</template>

<script setup>
import {
  ref,
  watch,
  onMounted,
  onBeforeUnmount
} from "vue";

import {
  Search,
  RefreshCw,
  X
} from "lucide-vue-next";

import { useAdminStore } from "@/stores/admin";

import ContactsTable from "@/components/admin/contacts/ContactsTable.vue";
import ContactDetailModal from "@/components/admin/contacts/ContactDetailModal.vue";
import ContactReplyModal from "@/components/admin/contacts/ContactReplyModal.vue";
import { toast } from "vue-sonner";
const adminStore = useAdminStore();

const showDetailModal = ref(false);
const showReplyModal = ref(false);
const selectedContact = ref(null);
const refreshing = ref(false);

let searchTimeout = null;

const refreshContacts = async () => {
  if (refreshing.value) return;

  refreshing.value = true;

  try {
    adminStore.contactSearch = "";
    adminStore.contactStatusFilter = "";
    adminStore.contactCategoryFilter = "";

    clearTimeout(searchTimeout);

    await adminStore.fetchContacts(1);

    toast.success(
      "Contacts refreshed successfully."
    );

  } catch (error) {

    console.error(
      "Failed to refresh contacts:",
      error
    );

    toast.error(
      "Unable to refresh contacts."
    );

  } finally {
    refreshing.value = false;
  }
};

const resetFilters = () => {
  adminStore.contactSearch = "";
  adminStore.contactStatusFilter = "";
  adminStore.contactCategoryFilter = "";
};

const openDetails = (contact) => {
  selectedContact.value = contact;
  showDetailModal.value = true;
};

const closeDetails = () => {
  showDetailModal.value = false;
};

const openReply = (contact) => {
  selectedContact.value = contact;
  showDetailModal.value = false;
  showReplyModal.value = true;
};

const closeReply = () => {
  showReplyModal.value = false;
  selectedContact.value = null;
};

watch(
  () => adminStore.contactSearch,
  () => {
    clearTimeout(searchTimeout);

    searchTimeout = setTimeout(() => {
      adminStore.fetchContacts(1);
    }, 400);
  }
);

watch(
  () => adminStore.contactStatusFilter,
  () => {
    adminStore.fetchContacts(1);
  }
);

watch(
  () => adminStore.contactCategoryFilter,
  () => {
    adminStore.fetchContacts(1);
  }
);

onMounted(() => {
  adminStore.fetchContacts(1);
});

onBeforeUnmount(() => {
  clearTimeout(searchTimeout);
});
</script>