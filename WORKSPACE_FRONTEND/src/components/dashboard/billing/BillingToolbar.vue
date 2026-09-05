<script setup>
import { ref, watch } from "vue";

import {
  Search,
  Filter,
  Download
} from "lucide-vue-next";

const props = defineProps({
  search: String,
  status: String
});

const emit = defineEmits([
  "update:search",
  "update:status",
  "export"
]);

const searchValue = ref(props.search || "");
const statusValue = ref(props.status || "all");

watch(searchValue, value => {
  emit("update:search", value);
});

watch(statusValue, value => {
  emit("update:status", value);
});
</script>

<template>

<div
class="flex flex-col gap-3 rounded-2xl border border-gray-100 bg-white p-4 shadow-sm lg:flex-row lg:items-center lg:justify-between"
>

<div class="flex flex-col flex-1 gap-3 sm:flex-row">

<div class="relative flex-1">

<Search
class="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9F9F9F]"
/>

<input

v-model="searchValue"

type="text"

placeholder="Search office or invoice..."

class="h-10 w-full rounded-xl border border-gray-200 bg-white py-2 pl-10 pr-4 text-sm text-[#23394E] outline-none transition duration-200 placeholder:text-[#9F9F9F] focus:border-[#F29200] focus:ring-4 focus:ring-[#F29200]/10"
/>

</div>

<div class="relative w-full sm:w-48">

<Filter
class="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#9F9F9F]"
/>

<select

v-model="statusValue"

class="h-10 w-full appearance-none rounded-xl border border-gray-200 bg-white py-2 pl-10 pr-4 text-sm text-[#23394E] outline-none transition duration-200 focus:border-[#F29200] focus:ring-4 focus:ring-[#F29200]/10"
>

<option value="all">
All Payments
</option>

<option value="paid">
Paid
</option>

<option value="pending">
Pending
</option>

<option value="failed">
Failed
</option>

</select>

</div>

</div>

<button

@click="$emit('export')"

class="inline-flex h-10 items-center justify-center gap-2 rounded-xl bg-[#F29200] px-4 text-sm font-semibold text-white shadow-sm transition duration-200 hover:-translate-y-0.5 hover:bg-[#F29200]/90 hover:shadow-md focus:outline-none focus:ring-4 focus:ring-[#F29200]/20"
>

<Download class="h-4 w-4"/>

Export CSV

</button>

</div>

</template>
