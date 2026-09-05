<template>
  <div
    class="overflow-hidden rounded-3xl border border-gray-100 bg-white shadow-xl shadow-[#23394e]/5"
  >

    <!-- EMPTY STATE -->
    <div
      v-if="filteredOffices.length === 0"
      class="flex min-h-[360px] flex-col items-center justify-center px-6 py-16 text-center"
    >
      <div
        class="flex h-16 w-16 items-center justify-center rounded-2xl bg-[#23394e]/5 text-[#23394e] shadow-sm"
      >
        <Building2 class="h-8 w-8" />
      </div>

      <h3 class="mt-5 text-xl font-bold text-[#23394e]">
        No offices found
      </h3>

      <p class="mt-2 text-sm font-medium text-[#9f9f9f]">
        Create your first office.
      </p>
    </div>


    <div v-else>

      <!-- =====================================================
           DESKTOP TABLE
      ====================================================== -->

      <div class="hidden overflow-x-auto md:block">

        <table class="min-w-full border-separate border-spacing-0">

          <thead class="bg-[#23394e]">

            <tr>

              <th
                class="px-7 py-5 text-left text-sm font-semibold text-white"
              >
                Office
              </th>

              <th
                class="px-7 py-5 text-center text-sm font-semibold text-white"
              >
                City
              </th>

              <th
                class="px-7 py-5 text-center text-sm font-semibold text-white"
              >
                Price
              </th>

              <th
                class="px-7 py-5 text-center text-sm font-semibold text-white"
              >
                Type
              </th>

              <th
                class="px-7 py-5 text-center text-sm font-semibold text-white"
              >
                Status
              </th>

              <th
                class="px-7 py-5 text-center text-sm font-semibold text-white"
              >
                Actions
              </th>

            </tr>

          </thead>


          <tbody class="bg-white">

            <tr
              v-for="office in filteredOffices"
              :key="office.id"
              class="group transition duration-300 hover:bg-[#9f9f9f]/5 hover:shadow-lg"
            >

              <!-- OFFICE -->
              <td
                class="border-b border-[#9f9f9f]/10 px-7 py-5"
              >

                <div class="flex items-center gap-4">

                  <div
                    class="h-20 w-20 shrink-0 overflow-hidden rounded-xl bg-[#9f9f9f]/10 shadow-sm"
                  >

                    <img
                      v-if="office.images?.length"
                      :src="getPrimaryImage(office)"
                      :alt="office.title"
                      class="h-full w-full object-cover transition duration-500 group-hover:scale-105"
                    />

                    <div
                      v-else
                      class="flex h-full w-full items-center justify-center text-[#9f9f9f]"
                    >
                      <Building2 class="h-8 w-8" />
                    </div>

                  </div>


                  <div class="min-w-0">

                    <p
                      class="truncate text-lg font-bold text-[#23394e]"
                    >
                      {{ office.title }}
                    </p>

                    <p
                      class="mt-1 line-clamp-1 text-sm font-medium text-[#9f9f9f]"
                    >
                      {{ office.address }}
                    </p>

                    <p
                      class="mt-2 flex items-center gap-1.5 text-xs font-semibold text-[#9f9f9f]"
                    >
                      <ImageIcon class="h-3.5 w-3.5" />

                      {{ office.images?.length || 0 }}
                      images
                    </p>

                  </div>

                </div>

              </td>


              <!-- CITY -->
              <td
                class="border-b border-[#9f9f9f]/10 px-7 py-5"
              >

                <div
                  class="flex items-center justify-center gap-2 text-sm font-semibold text-[#23394e]"
                >
                  <MapPin class="h-4 w-4 text-[#9f9f9f]" />

                  <span>
                    {{ office.city }}
                  </span>
                </div>

              </td>


              <!-- PRICE -->
              <td
                class="border-b border-[#9f9f9f]/10 px-7 py-5 text-center"
              >

                <div
                  class="font-bold leading-none text-[#f29200]"
                >

                  <span class="text-2xl">
                    {{ office.price }}
                  </span>

                  <span
                    class="ml-1 text-xs font-bold text-[#9f9f9f]"
                  >
                    DH
                  </span>

                </div>

              </td>


              <!-- TYPE -->
              <td
                class="border-b border-[#9f9f9f]/10 px-7 py-5 text-center"
              >

                <span
                  :class="[
                    'inline-flex rounded-full px-3 py-1.5 text-xs font-bold capitalize',

                    office.rent_type === 'daily'
                      ? 'bg-[#f29200]/10 text-[#f29200]'

                      : office.rent_type === 'weekly'
                        ? 'bg-[#23394e]/10 text-[#23394e]'

                        : 'bg-[#9f9f9f]/15 text-[#23394e]'
                  ]"
                >
                  {{ office.rent_type }}
                </span>

              </td>


              <!-- STATUS -->
<td
  class="border-b border-[#9f9f9f]/10 px-7 py-5 text-center"
>
  <div class="flex flex-col items-center gap-2">

    <!-- ACTIVE STATUS -->
    <span
      :class="[
        'inline-flex items-center gap-1.5 rounded-full px-3 py-1.5 text-xs font-bold',

        office.is_active
          ? 'bg-emerald-50 text-emerald-600'
          : 'bg-red-50 text-red-500'
      ]"
    >
      <span
        :class="[
          'h-2 w-2 rounded-full',

          office.is_active
            ? 'bg-emerald-500'
            : 'bg-red-500'
        ]"
      ></span>

      {{ office.is_active ? 'Active' : 'Inactive' }}
    </span>


    <!-- AVAILABILITY STATUS -->
    <span
      :class="[
        'inline-flex rounded-full px-2.5 py-1 text-[10px] font-bold',

        office.available
          ? 'bg-[#f29200]/10 text-[#f29200]'
          : 'bg-[#9f9f9f]/15 text-[#23394e]'
      ]"
    >
      {{
        office.available
          ? 'Available'
          : 'Unavailable'
      }}
    </span>

  </div>
</td>


              <!-- ACTIONS -->
              <td
                class="border-b border-[#9f9f9f]/10 px-7 py-5"
              >

                <div
                  class="flex items-center justify-center gap-2"
                >

                  <!-- EDIT -->
                  <button
                    type="button"
                    @click="emit('edit', office)"
                    title="Edit office"
                    class="flex h-10 w-10 items-center justify-center rounded-xl border border-[#23394e]/10 bg-white text-[#23394e] transition hover:bg-[#23394e] hover:text-white hover:shadow-md"
                  >
                    <Pencil class="h-4 w-4" />
                  </button>


                  <!-- IMAGES -->
                  <button
                    type="button"
                    @click="emit('upload', office)"
                    title="Manage images"
                    class="flex h-10 w-10 items-center justify-center rounded-xl border border-[#f29200]/20 bg-white text-[#f29200] transition hover:bg-[#f29200] hover:text-white hover:shadow-md"
                  >
                    <ImagePlus class="h-4 w-4" />
                  </button>
                  <!-- AVAILABILITY -->
<button
  type="button"
  @click="emit('toggle-availability', office)"
  :title="
    office.available
      ? 'Mark unavailable'
      : 'Mark available'
  "
  :class="[
    'flex h-10 w-10 items-center justify-center rounded-xl border bg-white transition hover:shadow-md',

    office.available
      ? 'border-[#f29200]/25 text-[#f29200] hover:bg-[#f29200] hover:text-white'
      : 'border-[#9f9f9f]/30 text-[#9f9f9f] hover:bg-[#23394e] hover:text-white'
  ]"
>
  <CalendarCheck class="h-4 w-4" />
</button>


                  <!-- ACTIVE / INACTIVE -->
                  <button
                    type="button"
                    @click="emit('toggle-active', office)"
                    :title="
                      office.is_active
                        ? 'Deactivate office'
                        : 'Activate office'
                    "
                    :class="[
                      'flex h-10 w-10 items-center justify-center rounded-xl border bg-white transition hover:shadow-md',

                      office.is_active
                        ? 'border-red-500/20 text-red-500 hover:bg-red-500 hover:text-white'
                        : 'border-emerald-500/20 text-emerald-600 hover:bg-emerald-500 hover:text-white'
                    ]"
                  >
                    <Power class="h-4 w-4" />
                  </button>


                  <!-- DELETE -->
                  <button
                    type="button"
                    @click="emit('delete', office)"
                    title="Delete office"
                    class="flex h-10 w-10 items-center justify-center rounded-xl border border-red-500/20 bg-white text-red-500 transition hover:bg-red-500 hover:text-white hover:shadow-md"
                  >
                    <Trash2 class="h-4 w-4" />
                  </button>

                </div>

              </td>

            </tr>

          </tbody>

        </table>

      </div>


      <!-- =====================================================
           MOBILE CARDS
      ====================================================== -->

      <div
        class="grid grid-cols-1 gap-4 p-4 md:hidden"
      >

        <article
          v-for="office in filteredOffices"
          :key="office.id"
          class="group rounded-2xl border border-[#9f9f9f]/15 bg-white p-4 shadow-sm transition duration-300 hover:-translate-y-0.5 hover:shadow-lg"
        >

          <div class="flex gap-4">

            <!-- IMAGE -->
            <div
              class="h-20 w-20 shrink-0 overflow-hidden rounded-xl bg-[#9f9f9f]/10 shadow-sm"
            >

              <img
                v-if="office.images?.length"
                :src="getPrimaryImage(office)"
                :alt="office.title"
                class="h-full w-full object-cover transition duration-500 group-hover:scale-105"
              />

              <div
                v-else
                class="flex h-full w-full items-center justify-center text-[#9f9f9f]"
              >
                <Building2 class="h-8 w-8" />
              </div>

            </div>


            <!-- INFO -->
            <div class="min-w-0 flex-1">

              <p
                class="truncate text-lg font-bold text-[#23394e]"
              >
                {{ office.title }}
              </p>


              <!-- STATUS -->
              <span
                :class="[
                  'mt-2 inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[10px] font-bold',

                  office.is_active
                    ? 'bg-emerald-50 text-emerald-600'
                    : 'bg-red-50 text-red-500'
                ]"
              >

                <span
                  :class="[
                    'h-1.5 w-1.5 rounded-full',

                    office.is_active
                      ? 'bg-emerald-500'
                      : 'bg-red-500'
                  ]"
                ></span>

                {{
                  office.is_active
                    ? 'Active'
                    : 'Inactive'
                }}

              </span>


              <p
                class="mt-2 line-clamp-2 text-sm font-medium text-[#9f9f9f]"
              >
                {{ office.address }}
              </p>


              <p
                class="mt-2 flex items-center gap-1.5 text-xs font-semibold text-[#9f9f9f]"
              >
                <ImageIcon class="h-3.5 w-3.5" />

                {{ office.images?.length || 0 }}
                images
              </p>

            </div>

          </div>


          <!-- MOBILE DETAILS -->
          <div
            class="mt-4 grid grid-cols-3 gap-3 border-t border-[#9f9f9f]/10 pt-4 text-center"
          >

            <div>

              <p
                class="text-xs font-semibold text-[#9f9f9f]"
              >
                City
              </p>

              <p
                class="mt-1 flex items-center justify-center gap-1 text-sm font-bold text-[#23394e]"
              >
                <MapPin class="h-3.5 w-3.5" />

                {{ office.city }}
              </p>

            </div>


            <div>

              <p
                class="text-xs font-semibold text-[#9f9f9f]"
              >
                Price
              </p>

              <p
                class="mt-1 font-bold text-[#f29200]"
              >
                {{ office.price }}

                <span
                  class="text-xs text-[#9f9f9f]"
                >
                  DH
                </span>
              </p>

            </div>


            <div>

              <p
                class="text-xs font-semibold text-[#9f9f9f]"
              >
                Type
              </p>

              <span
                :class="[
                  'mt-1 inline-flex rounded-full px-3 py-1 text-xs font-bold capitalize',

                  office.rent_type === 'daily'
                    ? 'bg-[#f29200]/10 text-[#f29200]'

                    : office.rent_type === 'weekly'
                      ? 'bg-[#23394e]/10 text-[#23394e]'

                      : 'bg-[#9f9f9f]/15 text-[#23394e]'
                ]"
              >
                {{ office.rent_type }}
              </span>

            </div>

          </div>


          <!-- MOBILE ACTIONS -->
          <div
            class="mt-4 flex justify-end gap-2"
          >

            <!-- EDIT -->
            <button
              type="button"
              @click="emit('edit', office)"
              title="Edit office"
              class="flex h-10 w-10 items-center justify-center rounded-xl border border-[#23394e]/10 bg-white text-[#23394e] transition hover:bg-[#23394e] hover:text-white"
            >
              <Pencil class="h-4 w-4" />
            </button>


            <!-- IMAGES -->
            <button
              type="button"
              @click="emit('upload', office)"
              title="Manage images"
              class="flex h-10 w-10 items-center justify-center rounded-xl border border-[#f29200]/20 bg-white text-[#f29200] transition hover:bg-[#f29200] hover:text-white"
            >
              <ImagePlus class="h-4 w-4" />
            </button>
<button
  type="button"
  @click="emit('toggle-availability', office)"
  :title="
    office.available
      ? 'Mark unavailable'
      : 'Mark available'
  "
  :class="[
    'flex h-10 w-10 items-center justify-center rounded-xl border bg-white transition hover:shadow-md',

    office.available
      ? 'border-[#f29200]/25 text-[#f29200] hover:bg-[#f29200] hover:text-white'
      : 'border-[#9f9f9f]/30 text-[#9f9f9f] hover:bg-[#23394e] hover:text-white'
  ]"
>
  <CalendarCheck class="h-4 w-4" />
</button>

            <!-- ACTIVE / INACTIVE -->
            <button
              type="button"
              @click="emit('toggle-active', office)"
              :title="
                office.is_active
                  ? 'Deactivate office'
                  : 'Activate office'
              "
              :class="[
                'flex h-10 w-10 items-center justify-center rounded-xl border bg-white transition',

                office.is_active
                  ? 'border-red-500/20 text-red-500 hover:bg-red-500 hover:text-white'
                  : 'border-emerald-500/20 text-emerald-600 hover:bg-emerald-500 hover:text-white'
              ]"
            >
              <Power class="h-4 w-4" />
            </button>
            


            <!-- DELETE -->
            <button
              type="button"
              @click="emit('delete', office)"
              title="Delete office"
              class="flex h-10 w-10 items-center justify-center rounded-xl border border-red-500/20 bg-white text-red-500 transition hover:bg-red-500 hover:text-white"
            >
              <Trash2 class="h-4 w-4" />
            </button>

          </div>

        </article>

      </div>

    </div>

  </div>
</template>


<script setup>

import {
  onMounted,
  computed
} from "vue";

import {
  useAdminStore
} from "@/stores/admin";


import {
  Building2,
  Pencil,
  Trash2,
  ImagePlus,
  ImageIcon,
  MapPin,
  Power,
  CalendarCheck
} from "lucide-vue-next";


const adminStore =
  useAdminStore();


/* ==========================================================
   LOAD OFFICES
========================================================== */

onMounted(() => {

  adminStore.fetchOffices();

});


/* ==========================================================
   FILTER OFFICES
========================================================== */

const filteredOffices = computed(() => {

  if (!adminStore.officeSearch) {

    return adminStore.offices;

  }


  const search =
    adminStore.officeSearch
      .toLowerCase();


  return adminStore.offices.filter(
    (office) => {

      const title =
        office.title
          ?.toLowerCase() || '';

      const city =
        office.city
          ?.toLowerCase() || '';


      return (
        title.includes(search) ||
        city.includes(search)
      );

    }
  );

});


/* ==========================================================
   EVENTS
========================================================== */

const emit = defineEmits([
  "edit",
  "upload",
  "delete",
  "toggle-active",
  "toggle-availability"
]);


/* ==========================================================
   PRIMARY IMAGE
========================================================== */

const getPrimaryImage = (office) => {

  if (
    !office.images ||
    office.images.length === 0
  ) {
    return "";
  }


  const primaryImage =
    office.images.find(
      image => image.is_primary
    );


  const image =
    primaryImage ||
    office.images[0];


  if (!image?.image) {
    return "";
  }


  if (
    image.image.startsWith("http://") ||
    image.image.startsWith("https://")
  ) {
    return image.image;
  }


  return (
    `http://127.0.0.1:8000${image.image}`
  );

};

</script>