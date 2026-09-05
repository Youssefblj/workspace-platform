<template>
  <div
    v-if="show"
    class="fixed inset-0 z-50 flex items-center justify-center bg-[#23394e]/60 px-4 py-6 backdrop-blur-sm"
    @click.self="$emit('close')"
  >
    <div
      class="flex max-h-[92vh] w-full max-w-[1100px] flex-col overflow-hidden rounded-3xl bg-white shadow-2xl transition-all duration-300"
    >
      <!-- Header -->
      <div
        class="flex shrink-0 items-start justify-between gap-5 border-b border-[#9f9f9f]/20 px-6 py-6 sm:px-8"
      >
        <div>
          <h2 class="text-3xl font-bold tracking-tight text-[#23394e]">
            {{ office ? "Edit Office" : "Create Office" }}
          </h2>

          <p class="mt-1 text-sm font-medium text-[#9f9f9f]">
            Update workspace information and settings
          </p>
        </div>

        <button
          type="button"
          @click="$emit('close')"
          class="inline-flex h-11 w-11 shrink-0 items-center justify-center rounded-full border border-[#9f9f9f]/25 bg-white text-[#23394e] shadow-sm transition hover:border-[#23394e] hover:shadow-md"
        >
          <X class="h-5 w-5" />
        </button>
      </div>

      <!-- Content -->
      <div class="flex-1 overflow-y-auto">
        <div class="space-y-8 p-6 sm:p-8">

          <!-- Basic Information -->
          <section
            class="rounded-2xl border border-[#9f9f9f]/20 bg-white p-5 shadow-sm sm:p-6"
          >
            <div class="mb-6 flex items-center gap-3">
              <div
                class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10 text-[#f29200]"
              >
                <Building2 class="h-5 w-5" />
              </div>

              <div>
                <h3 class="text-lg font-bold text-[#23394e]">
                  Basic Information
                </h3>

                <p class="text-xs font-medium text-[#9f9f9f]">
                  Core workspace details shown to customers
                </p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-5 md:grid-cols-2">

              <!-- Workspace Type -->
              <div>
                <label
                  class="mb-2 flex items-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <Tag class="h-4 w-4 text-[#9f9f9f]" />
                  Workspace Type
                </label>

                <select
                  v-model="form.workspace_type"
                  class="h-12 w-full rounded-xl border border-[#9f9f9f]/30 bg-white px-4 text-sm font-medium text-[#23394e] outline-none transition focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/15"
                >
                  <option value="office">
                    Office
                  </option>

                  <option value="coworking">
                    Coworking Space
                  </option>

                  <option value="meeting">
                    Meeting Room
                  </option>

                  <option value="virtual">
                    Virtual Office
                  </option>
                </select>
              </div>

              <!-- Title -->
              <div>
                <label
                  class="mb-2 flex items-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <Building2 class="h-4 w-4 text-[#9f9f9f]" />
                  Title
                </label>

                <input
                  v-model.trim="form.title"
                  type="text"
                  :class="[
                    'h-12 w-full rounded-xl border bg-white px-4 text-sm font-medium text-[#23394e] outline-none transition placeholder:text-[#9f9f9f] focus:ring-4',
                    errors.title
                      ? 'border-red-500 focus:border-red-500 focus:ring-red-100'
                      : 'border-[#9f9f9f]/30 focus:border-[#f29200] focus:ring-[#f29200]/15'
                  ]"
                />

                <p
                  v-if="errors.title"
                  class="mt-1 text-sm font-medium text-red-500"
                >
                  {{ errors.title }}
                </p>
              </div>

              <!-- City -->
              <div>
                <label
                  class="mb-2 flex items-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <MapPin class="h-4 w-4 text-[#9f9f9f]" />
                  City
                </label>

                <input
                  v-model.trim="form.city"
                  type="text"
                  :class="[
                    'h-12 w-full rounded-xl border bg-white px-4 text-sm font-medium text-[#23394e] outline-none transition placeholder:text-[#9f9f9f] focus:ring-4',
                    errors.city
                      ? 'border-red-500 focus:border-red-500 focus:ring-red-100'
                      : 'border-[#9f9f9f]/30 focus:border-[#f29200] focus:ring-[#f29200]/15'
                  ]"
                />

                <p
                  v-if="errors.city"
                  class="mt-1 text-sm font-medium text-red-500"
                >
                  {{ errors.city }}
                </p>
              </div>

              <!-- Address -->
              <div>
                <label
                  class="mb-2 flex items-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <MapPin class="h-4 w-4 text-[#9f9f9f]" />
                  Address
                </label>

                <input
                  v-model.trim="form.address"
                  type="text"
                  :class="[
                    'h-12 w-full rounded-xl border bg-white px-4 text-sm font-medium text-[#23394e] outline-none transition placeholder:text-[#9f9f9f] focus:ring-4',
                    errors.address
                      ? 'border-red-500 focus:border-red-500 focus:ring-red-100'
                      : 'border-[#9f9f9f]/30 focus:border-[#f29200] focus:ring-[#f29200]/15'
                  ]"
                />

                <p
                  v-if="errors.address"
                  class="mt-1 text-sm font-medium text-red-500"
                >
                  {{ errors.address }}
                </p>
              </div>

              <!-- Description -->
              <div class="md:col-span-2">
                <label
                  class="mb-2 block text-sm font-semibold text-[#23394e]"
                >
                  Description
                </label>

                <textarea
                  v-model="form.description"
                  rows="7"
                  :class="[
                    'min-h-40 w-full resize-none rounded-xl border bg-white px-4 py-3 text-sm font-medium leading-relaxed text-[#23394e] outline-none transition placeholder:text-[#9f9f9f] focus:ring-4',
                    errors.description
                      ? 'border-red-500 focus:border-red-500 focus:ring-red-100'
                      : 'border-[#9f9f9f]/30 focus:border-[#f29200] focus:ring-[#f29200]/15'
                  ]"
                ></textarea>

                <p
                  v-if="errors.description"
                  class="mt-1 text-sm font-medium text-red-500"
                >
                  {{ errors.description }}
                </p>
              </div>
            </div>
          </section>

          <!-- Pricing -->
          <section
            class="rounded-2xl border border-[#9f9f9f]/20 bg-white p-5 shadow-sm sm:p-6"
          >
            <div class="mb-6 flex items-center gap-3">
              <div
                class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10 text-[#f29200]"
              >
                <Wallet class="h-5 w-5" />
              </div>

              <div>
                <h3 class="text-lg font-bold text-[#23394e]">
                  Pricing
                </h3>

                <p class="text-xs font-medium text-[#9f9f9f]">
                  Rental terms, capacity, and listing availability
                </p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-5 md:grid-cols-2">

              <!-- Price -->
              <div>
                <label
                  class="mb-2 flex items-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <Wallet class="h-4 w-4 text-[#9f9f9f]" />
                  Price
                </label>

                <input
                  v-model.number="form.price"
                  type="number"
                  :class="[
                    'h-12 w-full rounded-xl border bg-white px-4 text-sm font-medium text-[#23394e] outline-none transition placeholder:text-[#9f9f9f] focus:ring-4',
                    errors.price
                      ? 'border-red-500 focus:border-red-500 focus:ring-red-100'
                      : 'border-[#9f9f9f]/30 focus:border-[#f29200] focus:ring-[#f29200]/15'
                  ]"
                />

                <p
                  v-if="errors.price"
                  class="mt-1 text-sm font-medium text-red-500"
                >
                  {{ errors.price }}
                </p>
              </div>

              <!-- Rent Type -->
              <div>
                <label
                  class="mb-2 flex items-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <Tag class="h-4 w-4 text-[#9f9f9f]" />
                  Rent Type
                </label>

                <select
                  v-model="form.rent_type"
                  class="h-12 w-full rounded-xl border border-[#9f9f9f]/30 bg-white px-4 text-sm font-medium text-[#23394e] outline-none transition focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/15"
                >
                  <option value="daily">
                    Daily
                  </option>

                  <option value="weekly">
                    Weekly
                  </option>

                  <option value="monthly">
                    Monthly
                  </option>
                </select>
              </div>

              <!-- Capacity -->
              <div>
                <label
                  class="mb-2 flex items-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <Users class="h-4 w-4 text-[#9f9f9f]" />
                  Capacity
                </label>

                <input
                  v-model.number="form.capacity"
                  type="number"
                  :class="[
                    'h-12 w-full rounded-xl border bg-white px-4 text-sm font-medium text-[#23394e] outline-none transition placeholder:text-[#9f9f9f] focus:ring-4',
                    errors.capacity
                      ? 'border-red-500 focus:border-red-500 focus:ring-red-100'
                      : 'border-[#9f9f9f]/30 focus:border-[#f29200] focus:ring-[#f29200]/15'
                  ]"
                />

                <p
                  v-if="errors.capacity"
                  class="mt-1 text-sm font-medium text-red-500"
                >
                  {{ errors.capacity }}
                </p>
              </div>

              <!-- Availability -->
              <label
                :class="[
                  'flex min-h-12 cursor-pointer items-center justify-between gap-4 rounded-xl border px-4 py-3 shadow-sm transition hover:shadow-md',
                  form.available
                    ? 'border-[#f29200] bg-[#f29200]/10'
                    : 'border-[#9f9f9f]/25 bg-white'
                ]"
              >
                <div class="flex items-center gap-3">
                  <CheckCircle
                    class="h-5 w-5"
                    :class="
                      form.available
                        ? 'text-[#f29200]'
                        : 'text-[#9f9f9f]'
                    "
                  />

                  <div>
                    <span class="block text-sm font-bold text-[#23394e]">
                      Availability
                    </span>

                    <span class="block text-xs font-medium text-[#9f9f9f]">
                      Mark this workspace as bookable
                    </span>
                  </div>
                </div>

                <input
                  v-model="form.available"
                  type="checkbox"
                  class="peer sr-only"
                />

                <span
                  class="relative h-6 w-11 rounded-full bg-[#9f9f9f]/30 transition peer-checked:bg-[#f29200]"
                >
                  <span
                    :class="[
                      'absolute left-1 top-1 h-4 w-4 rounded-full bg-white shadow-sm transition',
                      form.available
                        ? 'translate-x-5'
                        : 'translate-x-0'
                    ]"
                  ></span>
                </span>
              </label>
            </div>
          </section>

          <!-- Amenities -->
          <section
            class="rounded-2xl border border-[#9f9f9f]/20 bg-white p-5 shadow-sm sm:p-6"
          >
            <div class="mb-6 flex items-center gap-3">
              <div
                class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#f29200]/10 text-[#f29200]"
              >
                <CheckCircle class="h-5 w-5" />
              </div>

              <div>
                <h3 class="text-lg font-bold text-[#23394e]">
                  Amenities
                </h3>

                <p class="text-xs font-medium text-[#9f9f9f]">
                  Enable the services included with this workspace
                </p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-4 md:grid-cols-2">

              <!-- Wifi -->
              <label
                :class="[
                  'flex cursor-pointer items-center justify-between gap-4 rounded-2xl border p-4 shadow-sm transition hover:shadow-md',
                  form.wifi
                    ? 'border-[#f29200] bg-[#f29200]/10'
                    : 'border-[#9f9f9f]/25 bg-white'
                ]"
              >
                <div class="flex items-center gap-3">
                  <div
                    :class="[
                      'flex h-11 w-11 items-center justify-center rounded-xl transition',
                      form.wifi
                        ? 'bg-[#f29200] text-white'
                        : 'bg-[#9f9f9f]/10 text-[#9f9f9f]'
                    ]"
                  >
                    <Wifi class="h-5 w-5" />
                  </div>

                  <div>
                    <span class="block text-sm font-bold text-[#23394e]">
                      Wifi
                    </span>

                    <span class="block text-xs font-medium text-[#9f9f9f]">
                      High-speed internet access
                    </span>
                  </div>
                </div>

                <input
                  v-model="form.wifi"
                  type="checkbox"
                  class="peer sr-only"
                />

                <span
                  class="relative h-6 w-11 rounded-full bg-[#9f9f9f]/30 transition peer-checked:bg-[#f29200]"
                >
                  <span
                    :class="[
                      'absolute left-1 top-1 h-4 w-4 rounded-full bg-white shadow-sm transition',
                      form.wifi
                        ? 'translate-x-5'
                        : 'translate-x-0'
                    ]"
                  ></span>
                </span>
              </label>

              <!-- Parking -->
              <label
                :class="[
                  'flex cursor-pointer items-center justify-between gap-4 rounded-2xl border p-4 shadow-sm transition hover:shadow-md',
                  form.parking
                    ? 'border-[#f29200] bg-[#f29200]/10'
                    : 'border-[#9f9f9f]/25 bg-white'
                ]"
              >
                <div class="flex items-center gap-3">
                  <div
                    :class="[
                      'flex h-11 w-11 items-center justify-center rounded-xl transition',
                      form.parking
                        ? 'bg-[#f29200] text-white'
                        : 'bg-[#9f9f9f]/10 text-[#9f9f9f]'
                    ]"
                  >
                    <Car class="h-5 w-5" />
                  </div>

                  <div>
                    <span class="block text-sm font-bold text-[#23394e]">
                      Parking
                    </span>

                    <span class="block text-xs font-medium text-[#9f9f9f]">
                      Dedicated parking access
                    </span>
                  </div>
                </div>

                <input
                  v-model="form.parking"
                  type="checkbox"
                  class="peer sr-only"
                />

                <span
                  class="relative h-6 w-11 rounded-full bg-[#9f9f9f]/30 transition peer-checked:bg-[#f29200]"
                >
                  <span
                    :class="[
                      'absolute left-1 top-1 h-4 w-4 rounded-full bg-white shadow-sm transition',
                      form.parking
                        ? 'translate-x-5'
                        : 'translate-x-0'
                    ]"
                  ></span>
                </span>
              </label>

              <!-- Meeting Room -->
              <label
                :class="[
                  'flex cursor-pointer items-center justify-between gap-4 rounded-2xl border p-4 shadow-sm transition hover:shadow-md',
                  form.meeting_room
                    ? 'border-[#f29200] bg-[#f29200]/10'
                    : 'border-[#9f9f9f]/25 bg-white'
                ]"
              >
                <div class="flex items-center gap-3">
                  <div
                    :class="[
                      'flex h-11 w-11 items-center justify-center rounded-xl transition',
                      form.meeting_room
                        ? 'bg-[#f29200] text-white'
                        : 'bg-[#9f9f9f]/10 text-[#9f9f9f]'
                    ]"
                  >
                    <Users class="h-5 w-5" />
                  </div>

                  <div>
                    <span class="block text-sm font-bold text-[#23394e]">
                      Meeting Room
                    </span>

                    <span class="block text-xs font-medium text-[#9f9f9f]">
                      Rooms for calls and collaboration
                    </span>
                  </div>
                </div>

                <input
                  v-model="form.meeting_room"
                  type="checkbox"
                  class="peer sr-only"
                />

                <span
                  class="relative h-6 w-11 rounded-full bg-[#9f9f9f]/30 transition peer-checked:bg-[#f29200]"
                >
                  <span
                    :class="[
                      'absolute left-1 top-1 h-4 w-4 rounded-full bg-white shadow-sm transition',
                      form.meeting_room
                        ? 'translate-x-5'
                        : 'translate-x-0'
                    ]"
                  ></span>
                </span>
              </label>

              <!-- Air Conditioning -->
              <label
                :class="[
                  'flex cursor-pointer items-center justify-between gap-4 rounded-2xl border p-4 shadow-sm transition hover:shadow-md',
                  form.air_conditioning
                    ? 'border-[#f29200] bg-[#f29200]/10'
                    : 'border-[#9f9f9f]/25 bg-white'
                ]"
              >
                <div class="flex items-center gap-3">
                  <div
                    :class="[
                      'flex h-11 w-11 items-center justify-center rounded-xl transition',
                      form.air_conditioning
                        ? 'bg-[#f29200] text-white'
                        : 'bg-[#9f9f9f]/10 text-[#9f9f9f]'
                    ]"
                  >
                    <Wind class="h-5 w-5" />
                  </div>

                  <div>
                    <span class="block text-sm font-bold text-[#23394e]">
                      Air Conditioning
                    </span>

                    <span class="block text-xs font-medium text-[#9f9f9f]">
                      Climate-controlled workspace
                    </span>
                  </div>
                </div>

                <input
                  v-model="form.air_conditioning"
                  type="checkbox"
                  class="peer sr-only"
                />

                <span
                  class="relative h-6 w-11 rounded-full bg-[#9f9f9f]/30 transition peer-checked:bg-[#f29200]"
                >
                  <span
                    :class="[
                      'absolute left-1 top-1 h-4 w-4 rounded-full bg-white shadow-sm transition',
                      form.air_conditioning
                        ? 'translate-x-5'
                        : 'translate-x-0'
                    ]"
                  ></span>
                </span>
              </label>
            </div>
          </section>
        </div>
      </div>

      <!-- Footer -->
      <div
        class="flex shrink-0 flex-col-reverse gap-3 border-t border-[#9f9f9f]/20 px-6 py-5 sm:flex-row sm:justify-end sm:px-8"
      >
        <button
          type="button"
          @click="$emit('close')"
          class="inline-flex h-12 items-center justify-center rounded-xl border border-[#9f9f9f]/30 bg-white px-6 text-sm font-bold text-[#23394e] transition hover:border-[#23394e] hover:shadow-sm"
        >
          Cancel
        </button>

        <button
          type="button"
          @click="submit"
          class="inline-flex h-12 items-center justify-center gap-2 rounded-xl bg-[#f29200] px-6 text-sm font-bold text-white shadow-sm transition hover:bg-[#f29200]/90 hover:shadow-lg"
        >
          <Save class="h-4 w-4" />
          {{ office ? "Save Changes" : "Create Office" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import {
  Building2,
  Car,
  CheckCircle,
  MapPin,
  Save,
  Tag,
  Users,
  Wallet,
  Wifi,
  Wind,
  X
} from "lucide-vue-next";

import { reactive, watch } from "vue";
import { useAdminStore } from "@/stores/admin";

const props = defineProps({
  show: Boolean,

  office: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(["close"]);

const adminStore = useAdminStore();

const form = reactive({
  workspace_type: "office",
  title: "",
  description: "",
  city: "",
  address: "",
  price: "",
  rent_type: "daily",
  capacity: 1,
  available: true,
  wifi: false,
  parking: false,
  meeting_room: false,
  air_conditioning: false
});

/*
|--------------------------------------------------------------------------
| Validation errors
|--------------------------------------------------------------------------
*/

const errors = reactive({
  title: "",
  city: "",
  address: "",
  description: "",
  price: "",
  capacity: ""
});

const clearErrors = () => {
  errors.title = "";
  errors.city = "";
  errors.address = "";
  errors.description = "";
  errors.price = "";
  errors.capacity = "";
};

const validateForm = () => {
  clearErrors();

  let valid = true;

  if (!form.title?.trim()) {
    errors.title = "Title is required.";
    valid = false;
  }

  if (!form.city?.trim()) {
    errors.city = "City is required.";
    valid = false;
  }

  if (!form.address?.trim()) {
    errors.address = "Address is required.";
    valid = false;
  }

  if (!form.description?.trim()) {
    errors.description = "Description is required.";
    valid = false;
  }

  if (
    form.price === "" ||
    form.price === null ||
    form.price === undefined
  ) {
    errors.price = "Price is required.";
    valid = false;
  } else if (
    Number.isNaN(Number(form.price)) ||
    Number(form.price) <= 0
  ) {
    errors.price = "Price must be greater than 0.";
    valid = false;
  }

  if (
    form.capacity === "" ||
    form.capacity === null ||
    form.capacity === undefined
  ) {
    errors.capacity = "Capacity is required.";
    valid = false;
  } else if (
    Number.isNaN(Number(form.capacity)) ||
    Number(form.capacity) <= 0
  ) {
    errors.capacity = "Capacity must be greater than 0.";
    valid = false;
  }

  return valid;
};

/*
|--------------------------------------------------------------------------
| Edit office
|--------------------------------------------------------------------------
*/

watch(
  () => props.office,

  (office) => {
    clearErrors();

    if (!office) {
      return;
    }

    Object.assign(
      form,
      office
    );
  },

  {
    immediate: true
  }
);

/*
|--------------------------------------------------------------------------
| Submit
|--------------------------------------------------------------------------
*/

const submit = async () => {
  /*
   * Stop here if any required
   * field is missing.
   */
  if (!validateForm()) {
    return;
  }

  try {
    if (props.office) {
      await adminStore.updateOffice(
        props.office.id,
        form
      );
    } else {
      await adminStore.createOffice(
        form
      );
    }

    emit("close");

  } catch (err) {
    console.error(err);
  }
};
</script>