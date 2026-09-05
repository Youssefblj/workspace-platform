<template>
  <div class="space-y-5">
    <div class="flex items-end justify-between px-1">
      <div>
        <h1 class="text-xl font-bold tracking-tight text-[#23394e] sm:text-2xl">
          Offices Management
        </h1>

        <p class="mt-1 text-sm text-[#9f9f9f]">
          Manage all workspace listings.
        </p>
      </div>
    </div>

    <div class="flex flex-col gap-3 rounded-xl border border-gray-200 bg-white p-3 shadow-sm transition duration-200 sm:flex-row sm:items-center sm:justify-between">
      <div class="relative w-full sm:max-w-xs">
        <Search
          class="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9f9f9f]"
        />

        <input
          v-model="adminStore.officeSearch"
          type="text"
          placeholder="Search offices..."
          class="w-full rounded-lg border border-gray-200 bg-white py-2.5 pl-11 pr-4 text-sm text-[#23394e] outline-none transition duration-200 placeholder:text-[#9f9f9f] focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10"
        />
      </div>

      <button
        @click="openCreateModal"
        class="w-full rounded-lg bg-[#f29200] px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition duration-200 hover:scale-[1.02] hover:shadow-md active:scale-100 sm:w-auto"
      >
        Add Office
      </button>
    </div>

    <OfficeTable
      class="rounded-3xl border border-gray-100 bg-white shadow-sm transition duration-300 hover:shadow-md"
      @edit="editOffice"
      @upload="openGallery"
      @delete="deleteOffice"
      @toggle-active="toggleOfficeActive",
      @toggle-availability="toggleOfficeAvailability"
    />

    <OfficeFormModal
      :show="showCreateModal"
      :office="selectedOffice"
      @close="closeCreateModal"
    />



    <OfficeGalleryModal
      :show="showGalleryModal"
      :office="selectedOffice"
      @close="closeGallery"
      @primary="makePrimaryImage"
      @delete="deleteOfficeImage"
      @upload="uploadOfficeImage"
    />
  <!-- Pagination -->
    <div
      class="mt-6 flex flex-wrap items-center justify-between gap-3 rounded-xl border border-gray-200 bg-white px-4 py-3 shadow-sm sm:flex-nowrap sm:px-5"
    >
      <button
        :disabled="adminStore.currentPage <= 1"
        @click="adminStore.fetchOffices(adminStore.currentPage - 1)"
        class="rounded-xl border border-gray-200 px-4 py-2.5 text-sm font-semibold text-[#23394e] transition duration-200 hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
      >
        Previous
      </button>

      <span
        class="order-first w-full text-center text-sm font-semibold text-[#9f9f9f] sm:order-none sm:w-auto"
      >
        Page {{ adminStore.currentPage }}
        of {{ adminStore.totalPages }}
      </span>

      <button
        :disabled="adminStore.currentPage >= adminStore.totalPages"
        @click="adminStore.fetchOffices(adminStore.currentPage + 1)"
        class="rounded-xl border border-gray-200 px-4 py-2.5 text-sm font-semibold text-[#23394e] transition duration-200 hover:border-[#f29200] hover:text-[#f29200] disabled:cursor-not-allowed disabled:opacity-50"
      >
        Next
      </button>
    </div>

  </div>
</template>

  


<script setup>
import { ref } from "vue";
import { Search } from "lucide-vue-next";
import Swal from "sweetalert2";

import { useAdminStore } from "@/stores/admin";

import OfficeTable from "@/components/admin/offices/OfficeTable.vue";
import OfficeFormModal from "@/components/admin/offices/OfficeFormModal.vue";
import OfficeGalleryModal from "@/components/admin/offices/OfficeGalleryModal.vue";

const adminStore = useAdminStore();

const showCreateModal = ref(false);

const selectedOffice = ref(null);
const showGalleryModal = ref(false);

const openCreateModal = () => {

  selectedOffice.value = null;

  showCreateModal.value = true;

};

const closeCreateModal = () => {

  showCreateModal.value = false;

  selectedOffice.value = null;

};

const editOffice = (office) => {

  selectedOffice.value = office;

  showCreateModal.value = true;

};
const deleteOffice = async (office) => {

  const result = await Swal.fire({

    title: "Delete Office?",

    text: `Are you sure you want to delete "${office.title}" ?`,

    icon: "warning",

    showCancelButton: true,

    confirmButtonColor: "#f29200",

    cancelButtonColor: "#9f9f9f",

    confirmButtonText: "Delete",

    cancelButtonText: "Cancel"

  });

  if (!result.isConfirmed) return;

  try {

    await adminStore.deleteOffice(office.id);

    Swal.fire({

      icon: "success",

      title: "Deleted",

      text: "Office deleted successfully.",

      timer: 1800,

      showConfirmButton: false

    });

  }

  catch (err) {

    Swal.fire({

      icon: "error",

      title: "Error",

      text: "Unable to delete office."

    });

  }

};

const toggleOfficeActive = async (office) => {

  const isCurrentlyActive =
    office.is_active;


  const result = await Swal.fire({

    title: isCurrentlyActive
      ? "Deactivate Office?"
      : "Activate Office?",

    text: isCurrentlyActive
      ? `This will hide "${office.title}" from the public website.`
      : `This will make "${office.title}" visible on the public website again.`,

    icon: "warning",

    showCancelButton: true,

    confirmButtonText: isCurrentlyActive
      ? "Deactivate"
      : "Activate",

    cancelButtonText: "Cancel",

    confirmButtonColor: isCurrentlyActive
      ? "#dc2626"
      : "#f29200",

    cancelButtonColor: "#9f9f9f"

  });


  if (!result.isConfirmed) {
    return;
  }


  const response =
    await adminStore.toggleOfficeActive(
      office.id
    );


  if (!response.success) {

    await Swal.fire({

      icon: "error",

      title: "Unable to update office",

      text:
        response.error ||
        "Unable to update office status."

    });

    return;
  }


  await Swal.fire({

    icon: "success",

    title: response.office?.is_active
      ? "Office Activated"
      : "Office Deactivated",

    text: response.office?.is_active
      ? `"${office.title}" is now visible on the public website.`
      : `"${office.title}" is now hidden from the public website.`,

    timer: 1800,

    showConfirmButton: false

  });

};

const toggleOfficeAvailability = async (office) => {

  const isAvailable =
    office.available;


  const result = await Swal.fire({

    title: isAvailable
      ? "Mark Office Unavailable?"
      : "Mark Office Available?",

    text: isAvailable
      ? `"${office.title}" will remain visible, but users will not be able to book it.`
      : `"${office.title}" will become bookable again.`,

    icon: "warning",

    showCancelButton: true,

    confirmButtonText: isAvailable
      ? "Make Unavailable"
      : "Make Available",

    cancelButtonText: "Cancel",

    confirmButtonColor: "#f29200",

    cancelButtonColor: "#9f9f9f"

  });


  if (!result.isConfirmed) {
    return;
  }


  const response =
    await adminStore.toggleOfficeAvailability(
      office.id
    );


  if (!response.success) {

    await Swal.fire({

      icon: "error",

      title: "Unable to update availability",

      text:
        response.error ||
        "Unable to update office availability."

    });

    return;
  }


  await Swal.fire({

    icon: "success",

    title: response.office?.available
      ? "Office Available"
      : "Office Unavailable",

    text: response.office?.available
      ? `"${office.title}" can now be booked.`
      : `"${office.title}" is still visible but cannot be booked.`,

    timer: 1700,

    showConfirmButton: false

  });

};

const openGallery = (office) => {

  selectedOffice.value = office;

  showGalleryModal.value = true;

};
const closeGallery = () => {

  showGalleryModal.value = false;

};
const makePrimaryImage = async (image) => {

  try {

    await adminStore.setPrimaryOfficeImage(
      image.id
    );

    await adminStore.fetchOffices();

    selectedOffice.value =
      adminStore.offices.find(
        office => office.id === selectedOffice.value.id
      );

    Swal.fire({

      icon: "success",

      title: "Updated",

      text: "Primary image updated.",

      timer: 1800,

      showConfirmButton: false

    });

  }

  catch (err) {

    Swal.fire({

      icon: "error",

      title: "Error",

      text: "Unable to update image."

    });

  }

};
const uploadOfficeImage = async (file) => {

  const formData = new FormData();

  formData.append("image", file);

  try {

    await adminStore.uploadOfficeImage(

      selectedOffice.value.id,

      formData

    );

    await adminStore.fetchOffices();

    selectedOffice.value =
      adminStore.offices.find(

        office => office.id === selectedOffice.value.id

      );

    Swal.fire({

      icon: "success",

      title: "Success",

      text: "Image uploaded successfully.",

      timer: 1800,

      showConfirmButton: false

    });

  }

  catch {

    Swal.fire({

      icon: "error",

      title: "Error",

      text: "Unable to upload image."

    });

  }

};
const deleteOfficeImage = async (image) => {

  try {

    await adminStore.deleteOfficeImage(
      image.id
    );

    await adminStore.fetchOffices();

    selectedOffice.value =
      adminStore.offices.find(

        office => office.id === selectedOffice.value.id

      );

    Swal.fire({

      icon: "success",

      title: "Deleted",

      text: "Image removed successfully.",

      timer: 1800,

      showConfirmButton: false

    });

  }

  catch {

    Swal.fire({

      icon: "error",

      title: "Error",

      text: "Unable to delete image."

    });

  }

};
</script>
