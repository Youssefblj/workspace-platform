<template>
  <div
    v-if="show"
    class="fixed inset-0 z-50 flex items-center justify-center bg-[#23394e]/60 px-4 py-6 backdrop-blur-sm"
  >
    <div
      class="flex max-h-[92vh] w-full max-w-7xl flex-col overflow-hidden rounded-2xl bg-white shadow-2xl"
    >
      <div class="flex flex-col gap-4 border-b border-[#9f9f9f]/20 px-5 py-5 sm:flex-row sm:items-center sm:justify-between sm:px-7">
        <div>
          <h2 class="text-2xl font-bold text-[#23394e]">
            Office Images
          </h2>
          <p class="mt-1 text-sm font-semibold text-[#23394e]">
            {{ office?.title || "Untitled office" }}
          </p>
          <p class="text-xs font-medium text-[#9f9f9f]">
            Manage office gallery
          </p>
        </div>

        <button
          @click="$emit('close')"
          class="inline-flex items-center justify-center gap-2 rounded-xl border border-[#9f9f9f]/30 bg-white px-4 py-2.5 text-sm font-semibold text-[#23394e] transition hover:border-[#23394e] hover:shadow-sm"
        >
          <X class="h-4 w-4" />
          Close
        </button>
      </div>

      <div class="overflow-y-auto px-5 py-6 sm:px-7">
        <div class="mb-6 flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
          <div class="flex flex-wrap gap-3">
            <div class="rounded-xl border border-[#9f9f9f]/20 bg-white px-4 py-3 shadow-sm">
              <p class="text-xs font-semibold uppercase text-[#9f9f9f]">
                Images
              </p>
              <p class="mt-1 text-2xl font-bold text-[#23394e]">
                {{ office?.images?.length || 0 }}
              </p>
            </div>

            <div class="rounded-xl border border-[#9f9f9f]/20 bg-white px-4 py-3 shadow-sm">
              <p class="text-xs font-semibold uppercase text-[#9f9f9f]">
                Primary
              </p>
              <p class="mt-1 text-2xl font-bold text-[#23394e]">
                {{ office?.images?.filter(image => image.is_primary).length || 0 }}
              </p>
            </div>
          </div>

          <div>
            <input
              ref="fileInput"
              type="file"
              accept="image/*"
              @change="selectImage"
              class="hidden"
            >

            <button
              @click="fileInput.click()"
              class="inline-flex items-center justify-center gap-2 rounded-xl bg-[#f29200] px-5 py-3 text-sm font-bold text-white shadow-sm transition hover:bg-[#f29200]/90 hover:shadow-lg"
            >
              <ImagePlus class="h-4 w-4" />
              Upload New Image
            </button>
          </div>
        </div>

        <div
          v-if="office?.images?.length"
          class="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-4"
        >
          <div
            v-for="image in office.images"
            :key="image.id"
            :class="[
              'group w-full overflow-hidden rounded-xl border bg-white shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg',
              image.is_primary
                ? 'border-[#f29200] bg-[#f29200]/5'
                : 'border-[#9f9f9f]/20'
            ]"
          >
            <div class="relative h-52 overflow-hidden bg-[#9f9f9f]/10">
              <img
                :src="`http://127.0.0.1:8000${image.image}`"
                class="h-full w-full object-cover transition duration-500 group-hover:scale-105"
                @error="console.log('Image Error:', image.image)"
              />

              <div class="absolute inset-0 bg-gradient-to-t from-[#23394e]/55 via-[#23394e]/5 to-transparent opacity-0 transition duration-300 group-hover:opacity-100"></div>

              <span
                v-if="image.is_primary"
                class="absolute left-3 top-3 inline-flex items-center gap-1.5 rounded-full bg-[#f29200] px-3 py-1.5 text-xs font-bold text-white shadow-sm"
              >
                <Star class="h-3.5 w-3.5 fill-white" />
                Primary
              </span>
            </div>

            <div class="space-y-3 p-4">
              <div class="min-h-7">
                <span
                  v-if="image.is_primary"
                  class="inline-flex items-center gap-1.5 rounded-full border border-[#f29200]/30 bg-[#f29200]/10 px-3 py-1 text-xs font-bold text-[#f29200]"
                >
                  <Star class="h-3.5 w-3.5 fill-[#f29200]" />
                  Primary Image
                </span>
              </div>

              <div class="grid grid-cols-1 gap-2 sm:grid-cols-2 xl:grid-cols-1 2xl:grid-cols-2">
                <button
                  v-if="!image.is_primary"
                  @click="makePrimary(image)"
                  class="inline-flex items-center justify-center gap-2 rounded-xl bg-[#23394e] px-3 py-2.5 text-xs font-bold text-white transition hover:bg-[#23394e]/90"
                >
                  <Star class="h-4 w-4" />
                  Make Primary
                </button>

                <button
                  @click="deleteImage(image)"
                  :class="[
                    'inline-flex items-center justify-center gap-2 rounded-xl bg-red-600 px-3 py-2.5 text-xs font-bold text-white transition hover:bg-red-700',
                    image.is_primary ? 'sm:col-span-2 xl:col-span-1 2xl:col-span-2' : ''
                  ]"
                >
                  <Trash2 class="h-4 w-4" />
                  Delete
                </button>
              </div>
            </div>
          </div>
        </div>

        <div
          v-else
          class="flex min-h-[360px] flex-col items-center justify-center rounded-2xl border border-dashed border-[#9f9f9f]/40 bg-white px-6 py-16 text-center"
        >
          <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-[#f29200]/10 text-[#f29200]">
            <ImageIcon class="h-8 w-8" />
          </div>
          <h3 class="mt-5 text-lg font-bold text-[#23394e]">
            No images uploaded yet
          </h3>
          <p class="mt-2 text-sm font-medium text-[#9f9f9f]">
            Upload the first office image
          </p>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import Swal from "sweetalert2";

import { ref } from "vue";

import {
  ImageIcon,
  ImagePlus,
  Star,
  Trash2,
  X
} from "lucide-vue-next";

const fileInput = ref(null);

const selectImage = (event) => {

  if (!event.target.files.length)
    return;

  emit(
    "upload",
    event.target.files[0]
  );

  event.target.value = "";

};




const props = defineProps({

  show: Boolean,

  office: Object

});

const emit = defineEmits([

  "close",

  "primary",

  "delete",

  "upload"

]);

const makePrimary = async (image) => {

  const result = await Swal.fire({

    title: "Set as primary image?",

    text: "This image will become the main office image.",

    icon: "question",

    showCancelButton: true,

    confirmButtonColor: "#f29200",

    cancelButtonColor: "#9f9f9f",

    confirmButtonText: "Yes",

    cancelButtonText: "Cancel"

  });

  if (!result.isConfirmed) return;

  emit("primary", image);

};

const deleteImage = async (image) => {

  const result = await Swal.fire({

    title: "Delete image?",

    text: "This action cannot be undone.",

    icon: "warning",

    showCancelButton: true,

    confirmButtonColor: "#d33",

    cancelButtonColor: "#9f9f9f",

    confirmButtonText: "Delete",

    cancelButtonText: "Cancel"

  });

  if (!result.isConfirmed) return;

  emit("delete", image);

};

</script>
