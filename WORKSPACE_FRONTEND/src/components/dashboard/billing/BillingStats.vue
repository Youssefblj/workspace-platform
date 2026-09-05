<script setup>
import { computed } from "vue";

import {
  Wallet,
  Receipt,
  BadgeCheck,
  CreditCard
} from "lucide-vue-next";

const props = defineProps({
  payments: {
    type: Array,
    default: () => []
  }
});

const totalPaid = computed(() =>
  props.payments.reduce(
    (sum, payment) => sum + Number(payment.amount),
    0
  )
);

const totalInvoices = computed(() => props.payments.length);

const paidInvoices = computed(() =>
  props.payments.filter(
    payment => payment.status === "paid"
  ).length
);

const lastPayment = computed(() => {
  if (!props.payments.length) return null;

  return [...props.payments].sort(
    (a, b) =>
      new Date(b.created_at) - new Date(a.created_at)
  )[0];
});

const formatDate = (date) => {
  return new Date(date).toLocaleDateString("en-US", {
    day: "numeric",
    month: "short",
    year: "numeric"
  });
};
</script>

<template>

<section>

<div class="mb-5 px-1">

<h2 class="text-2xl font-bold tracking-tight text-[#23394E] sm:text-3xl">
Billing
</h2>

<p class="mt-1.5 text-sm text-[#9F9F9F] sm:text-base">
Track your payments and invoices.
</p>

</div>

<div class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">

<!-- Total Paid -->

<div class="min-h-[164px] rounded-2xl border border-gray-100 bg-white p-5 shadow-sm transition duration-200 hover:-translate-y-0.5 hover:shadow-md">

<div
class="flex h-11 w-11 items-center justify-center rounded-xl bg-[#F29200]/10"
>
<Wallet class="h-5 w-5 text-[#F29200]" />
</div>

<p class="mt-5 text-xs font-semibold uppercase tracking-wide text-[#9F9F9F]">
Total Paid
</p>

<h3 class="mt-1.5 text-2xl font-black text-[#23394E]">

{{ totalPaid.toLocaleString() }}

<span class="text-sm font-semibold text-[#9F9F9F]">MAD</span>

</h3>

</div>

<!-- Invoices -->

<div class="min-h-[164px] rounded-2xl border border-gray-100 bg-white p-5 shadow-sm transition duration-200 hover:-translate-y-0.5 hover:shadow-md">

<div
class="flex h-11 w-11 items-center justify-center rounded-xl bg-[#23394E]/5"
>
<Receipt class="h-5 w-5 text-[#23394E]" />
</div>

<p class="mt-5 text-xs font-semibold uppercase tracking-wide text-[#9F9F9F]">
Invoices
</p>

<h3 class="mt-1.5 text-2xl font-black text-[#23394E]">

{{ totalInvoices }}

</h3>

</div>

<!-- Paid -->

<div class="min-h-[164px] rounded-2xl border border-gray-100 bg-white p-5 shadow-sm transition duration-200 hover:-translate-y-0.5 hover:shadow-md">

<div
class="flex h-11 w-11 items-center justify-center rounded-xl bg-green-100"
>
<BadgeCheck class="h-5 w-5 text-green-600"/>
</div>

<p class="mt-5 text-xs font-semibold uppercase tracking-wide text-[#9F9F9F]">
Paid Payments
</p>

<h3 class="mt-1.5 text-2xl font-black text-green-600">

{{ paidInvoices }}

</h3>

</div>

<!-- Last Payment -->

<div class="min-h-[164px] rounded-2xl border border-gray-100 bg-white p-5 shadow-sm transition duration-200 hover:-translate-y-0.5 hover:shadow-md">

<div
class="flex h-11 w-11 items-center justify-center rounded-xl bg-[#F29200]/10"
>
<CreditCard class="h-5 w-5 text-[#F29200]"/>
</div>

<p class="mt-5 text-xs font-semibold uppercase tracking-wide text-[#9F9F9F]">
Last Payment
</p>

<h3
class="mt-1.5 text-lg font-bold text-[#23394E]"
>

{{ lastPayment
? formatDate(lastPayment.created_at)
: "--"
}}

</h3>

<p
v-if="lastPayment"
class="mt-1.5 text-sm font-semibold text-[#F29200]"
>

{{ lastPayment.amount }}

{{ lastPayment.currency }}

</p>

</div>

</div>

</section>

</template>
