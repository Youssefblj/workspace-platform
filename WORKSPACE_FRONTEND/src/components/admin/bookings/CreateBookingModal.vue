<template>
  <div
    v-if="show"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4"
  >
    <div
      class="max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-gray-200 bg-white p-6 shadow-xl"
    >
      <!-- Header -->
      <div class="mb-5 flex items-start justify-between gap-4">
        <div>
          <h2 class="text-xl font-bold text-[#23394e]">
            Create Booking
          </h2>

          <p class="mt-1 text-sm text-[#9f9f9f]">
            Create a reservation for a customer.
          </p>
        </div>

        <button
          type="button"
          @click="closeModal"
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg text-[#9f9f9f] transition hover:bg-gray-100 hover:text-[#23394e]"
        >
          <X class="h-5 w-5" />
        </button>
      </div>

      <form
        class="space-y-5"
        @submit.prevent="submitBooking"
      >
        <!-- User -->
        <div>
          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            User
          </label>

          <select
            v-model="form.user"
            class="w-full rounded-lg border border-gray-200 px-3 py-2.5 text-sm text-[#23394e] outline-none transition focus:border-[#f29200]"
          >
            <option value="">
              Select user
            </option>

            <option
              v-for="user in adminStore.users"
              :key="user.id"
              :value="user.id"
            >
              {{ user.username }} - {{ user.email }}
            </option>
          </select>

          <p
            v-if="errors.user"
            class="mt-1 text-xs text-red-500"
          >
            {{ errors.user }}
          </p>
        </div>

        <!-- Office -->
        <div>
          <label
            class="mb-2 block text-sm font-medium text-[#23394e]"
          >
            Office
          </label>

          <select
            v-model="form.office"
            class="w-full rounded-lg border border-gray-200 px-3 py-2.5 text-sm text-[#23394e] outline-none transition focus:border-[#f29200]"
          >
            <option value="">
              Select office
            </option>

            <option
              v-for="office in adminStore.offices"
              :key="office.id"
              :value="office.id"
            >
              {{ office.title }} - {{ office.city }}
            </option>
          </select>

          <p
            v-if="errors.office"
            class="mt-1 text-xs text-red-500"
          >
            {{ errors.office }}
          </p>
        </div>

        <!-- Dates -->
        <div class="space-y-3">
          <label
            class="block text-sm font-medium text-[#23394e]"
          >
            Booking Dates
          </label>

          <div class="grid gap-3 sm:grid-cols-2">
            <!-- Check-in -->
            <div>
              <label
                class="mb-1 block text-xs font-medium text-[#9f9f9f]"
              >
                Check-in
              </label>

              <button
                type="button"
                :disabled="!form.office"
                @click="openDatePicker('start')"
                :class="[
                  'flex w-full items-center justify-between rounded-xl border px-3.5 py-3 text-left text-sm transition disabled:cursor-not-allowed disabled:opacity-50',
                  activeDateField === 'start'
                    ? 'border-[#f29200] bg-[#f29200]/5'
                    : 'border-gray-200 hover:border-[#f29200]/60'
                ]"
              >
                <span
                  :class="
                    bookingDates.start
                      ? 'font-medium text-[#23394e]'
                      : 'text-[#9f9f9f]'
                  "
                >
                  {{
                    bookingDates.start
                      ? formatBookingDate(
                          bookingDates.start
                        )
                      : "Select date"
                  }}
                </span>

                <Calendar
                  class="h-4 w-4 shrink-0 text-[#f29200]"
                />
              </button>

              <p
                v-if="errors.start_date"
                class="mt-1 text-xs text-red-500"
              >
                {{ errors.start_date }}
              </p>
            </div>

            <!-- Check-out -->
            <div>
              <label
                class="mb-1 block text-xs font-medium text-[#9f9f9f]"
              >
                Check-out
              </label>

              <button
                type="button"
                :disabled="
                  !form.office ||
                  !bookingDates.start
                "
                @click="openDatePicker('end')"
                :class="[
                  'flex w-full items-center justify-between rounded-xl border px-3.5 py-3 text-left text-sm transition disabled:cursor-not-allowed disabled:opacity-50',
                  activeDateField === 'end'
                    ? 'border-[#f29200] bg-[#f29200]/5'
                    : 'border-gray-200 hover:border-[#f29200]/60'
                ]"
              >
                <span
                  :class="
                    bookingDates.end
                      ? 'font-medium text-[#23394e]'
                      : 'text-[#9f9f9f]'
                  "
                >
                  {{
                    bookingDates.end
                      ? formatBookingDate(
                          bookingDates.end
                        )
                      : "Select date"
                  }}
                </span>

                <Calendar
                  class="h-4 w-4 shrink-0 text-[#f29200]"
                />
              </button>

              <p
                v-if="errors.end_date"
                class="mt-1 text-xs text-red-500"
              >
                {{ errors.end_date }}
              </p>
            </div>
          </div>

          <!-- Calendar -->
          <div
            v-if="activeDateField"
            class="rounded-2xl border border-gray-200 bg-white p-3 shadow-sm"
          >
            <div
              class="mb-3 flex items-center justify-between gap-3"
            >
              <div>
                <p
                  class="text-sm font-bold text-[#23394e]"
                >
                  {{ calendarMonthLabel }}
                </p>

                <p
                  class="text-[11px] text-[#9f9f9f]"
                >
                  Select
                  {{
                    activeDateField === "start"
                      ? "check-in"
                      : "check-out"
                  }}
                  date
                </p>
              </div>

              <div class="flex items-center gap-1">
                <button
                  type="button"
                  @click="changeCalendarMonth(-1)"
                  class="flex h-8 w-8 items-center justify-center rounded-lg text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200]"
                >
                  <ChevronLeft
                    class="h-4 w-4"
                  />
                </button>

                <button
                  type="button"
                  @click="changeCalendarMonth(1)"
                  class="flex h-8 w-8 items-center justify-center rounded-lg text-[#23394e] transition hover:bg-[#f29200]/10 hover:text-[#f29200]"
                >
                  <ChevronRight
                    class="h-4 w-4"
                  />
                </button>
              </div>
            </div>

            <div
              class="grid grid-cols-7 gap-1 text-center"
            >
              <span
                v-for="weekday in calendarWeekdays"
                :key="weekday"
                class="py-1 text-[10px] font-bold uppercase text-[#9f9f9f]"
              >
                {{ weekday }}
              </span>

              <template
                v-for="(day, index) in calendarDays"
                :key="
                  day
                    ? day.key
                    : `empty-${index}`
                "
              >
                <span
                  v-if="!day"
                  class="h-9"
                />

                <button
                  v-else
                  type="button"
                  :disabled="
                    isCalendarDateDisabled(day)
                  "
                  @click="
                    selectCalendarDate(day)
                  "
                  :class="
                    calendarDayClasses(day)
                  "
                >
                  {{ day.day }}
                </button>
              </template>
            </div>

            <div
              class="mt-3 flex flex-wrap items-center gap-4 border-t border-gray-100 pt-3 text-[10px] text-[#9f9f9f]"
            >
              <span class="flex items-center gap-1.5">
                <span
                  class="h-2.5 w-2.5 rounded-full border border-gray-300 bg-white"
                />
                Available
              </span>

              <span class="flex items-center gap-1.5">
                <span
                  class="h-2.5 w-2.5 rounded-full bg-[#f29200]"
                />
                Selected
              </span>

              <span class="flex items-center gap-1.5">
                <span
                  class="h-2.5 w-2.5 rounded-full bg-red-200"
                />
                Reserved
              </span>
            </div>
          </div>
        </div>

        <!-- General error -->
        <div
          v-if="errors.general"
          class="rounded-lg border border-red-100 bg-red-50 px-3 py-2 text-sm text-red-600"
        >
          {{ errors.general }}
        </div>

        <!-- Actions -->
        <div
          class="flex justify-end gap-3 border-t border-gray-100 pt-4"
        >
          <button
            type="button"
            @click="closeModal"
            :disabled="saving"
            class="rounded-lg border border-gray-200 px-4 py-2 text-sm font-medium text-[#23394e] transition hover:bg-gray-50 disabled:opacity-50"
          >
            Cancel
          </button>

          <button
            type="submit"
            :disabled="saving"
            class="inline-flex items-center gap-2 rounded-lg bg-[#f29200] px-4 py-2 text-sm font-medium text-white transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"
          >
            <LoaderCircle
              v-if="saving"
              class="h-4 w-4 animate-spin"
            />

            <Save
              v-else
              class="h-4 w-4"
            />

            {{ saving ? "Creating..." : "Create Booking" }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import {
  reactive,
  ref,
  watch,
  computed
} from "vue";

import {
  X,
  Save,
  LoaderCircle,
  Calendar,
  ChevronLeft,
  ChevronRight
} from "lucide-vue-next";

import api from "@/services/api";
import { useAdminStore } from "@/stores/admin";

const props = defineProps({
  show: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits([
  "close",
  "created"
]);

const adminStore = useAdminStore();

const saving = ref(false);

const form = reactive({
  user: "",
  office: ""
});

const errors = reactive({
  user: "",
  office: "",
  start_date: "",
  end_date: "",
  general: ""
});

/*
|--------------------------------------------------------------------------
| Calendar state
|--------------------------------------------------------------------------
*/

const todayStr =
  new Date()
    .toISOString()
    .split("T")[0];

const bookingDates = reactive({
  start: "",
  end: ""
});

const reservedDateRanges = ref([]);

const activeDateField = ref(null);

const calendarMonth = ref(
  new Date(
    new Date().getFullYear(),
    new Date().getMonth(),
    1
  )
);

const calendarWeekdays = [
  "Su",
  "Mo",
  "Tu",
  "We",
  "Th",
  "Fr",
  "Sa"
];

/*
|--------------------------------------------------------------------------
| Calendar helpers
|--------------------------------------------------------------------------
*/

const createDateFromKey = (dateKey) => {
  const [year, month, day] =
    dateKey
      .split("-")
      .map(Number);

  return new Date(
    year,
    month - 1,
    day
  );
};

const getDateKey = (date) => {
  const year =
    date.getFullYear();

  const month =
    String(
      date.getMonth() + 1
    ).padStart(2, "0");

  const day =
    String(
      date.getDate()
    ).padStart(2, "0");

  return `${year}-${month}-${day}`;
};

const calendarMonthLabel =
  computed(() =>
    calendarMonth.value
      .toLocaleDateString(
        undefined,
        {
          month: "long",
          year: "numeric"
        }
      )
  );

const calendarDays =
  computed(() => {
    const year =
      calendarMonth.value
        .getFullYear();

    const month =
      calendarMonth.value
        .getMonth();

    const firstWeekday =
      new Date(
        year,
        month,
        1
      ).getDay();

    const daysInMonth =
      new Date(
        year,
        month + 1,
        0
      ).getDate();

    const leadingDays =
      Array.from(
        {
          length: firstWeekday
        },
        () => null
      );

    const monthDays =
      Array.from(
        {
          length: daysInMonth
        },
        (_, index) => {
          const date =
            new Date(
              year,
              month,
              index + 1
            );

          return {
            date,
            day: index + 1,
            key: getDateKey(date)
          };
        }
      );

    return [
      ...leadingDays,
      ...monthDays
    ];
  });

const formatBookingDate =
  (dateKey) =>
    createDateFromKey(
      dateKey
    ).toLocaleDateString(
      undefined,
      {
        month: "short",
        day: "numeric",
        year: "numeric"
      }
    );

/*
|--------------------------------------------------------------------------
| Reserved dates
|--------------------------------------------------------------------------
*/

const isReservedDate =
  (dateKey) =>
    reservedDateRanges.value
      .some(
        range =>
          range.start_date &&
          range.end_date &&
          dateKey >=
            range.start_date &&
          dateKey <=
            range.end_date
      );

const hasReservedDateInRange =
  (
    startDate,
    endDate
  ) =>
    reservedDateRanges.value
      .some(
        range =>
          range.start_date &&
          range.end_date &&
          range.start_date <=
            endDate &&
          range.end_date >=
            startDate
      );

/*
|--------------------------------------------------------------------------
| Selection logic
|--------------------------------------------------------------------------
*/

const isCalendarDateSelected =
  (day) =>
    day.key ===
      bookingDates.start ||
    day.key ===
      bookingDates.end;

const isCalendarDateInSelectedRange =
  (day) =>
    bookingDates.start &&
    bookingDates.end &&
    day.key >
      bookingDates.start &&
    day.key <
      bookingDates.end;

const isCalendarDateDisabled =
  (day) => {
    if (
      !day ||
      day.key < todayStr ||
      isReservedDate(day.key)
    ) {
      return true;
    }

    if (
      activeDateField.value ===
        "end" &&
      bookingDates.start
    ) {
      return (
        day.key <
          bookingDates.start ||
        hasReservedDateInRange(
          bookingDates.start,
          day.key
        )
      );
    }

    return false;
  };

const calendarDayClasses =
  (day) => {
    const baseClasses =
      "flex h-9 w-full items-center justify-center rounded-lg text-xs font-semibold transition focus:outline-none focus:ring-2 focus:ring-[#f29200]/20";

    if (
      isCalendarDateSelected(day)
    ) {
      return `${baseClasses} bg-[#f29200] text-white shadow-sm`;
    }

    if (
      isReservedDate(day.key)
    ) {
      return `${baseClasses} cursor-not-allowed bg-red-50 text-red-300 line-through`;
    }

    if (
      isCalendarDateDisabled(day)
    ) {
      return `${baseClasses} cursor-not-allowed text-gray-300`;
    }

    if (
      isCalendarDateInSelectedRange(
        day
      )
    ) {
      return `${baseClasses} bg-[#f29200]/10 text-[#f29200]`;
    }

    return `${baseClasses} text-[#23394e] hover:bg-[#f29200]/10 hover:text-[#f29200]`;
  };

const openDatePicker =
  (field) => {
    activeDateField.value =
      activeDateField.value ===
      field
        ? null
        : field;

    if (
      !activeDateField.value
    ) {
      return;
    }

    const selectedDate =
      bookingDates[field] ||
      todayStr;

    const date =
      createDateFromKey(
        selectedDate
      );

    calendarMonth.value =
      new Date(
        date.getFullYear(),
        date.getMonth(),
        1
      );
  };

const changeCalendarMonth =
  (monthOffset) => {
    calendarMonth.value =
      new Date(
        calendarMonth.value
          .getFullYear(),
        calendarMonth.value
          .getMonth() +
          monthOffset,
        1
      );
  };

const selectCalendarDate =
  (day) => {
    if (
      isCalendarDateDisabled(day)
    ) {
      return;
    }

    if (
      activeDateField.value ===
      "start"
    ) {
      bookingDates.start =
        day.key;

      if (
        bookingDates.end &&
        (
          bookingDates.end <
            day.key ||
          hasReservedDateInRange(
            day.key,
            bookingDates.end
          )
        )
      ) {
        bookingDates.end = "";
      }

      activeDateField.value =
        "end";
    }

    else if (
      activeDateField.value ===
      "end"
    ) {
      bookingDates.end =
        day.key;

      activeDateField.value =
        null;
    }
  };

/*
|--------------------------------------------------------------------------
| Load reserved dates
|--------------------------------------------------------------------------
*/

const loadReservedDates =
  async (officeId) => {
    reservedDateRanges.value =
      [];

    bookingDates.start = "";
    bookingDates.end = "";

    activeDateField.value =
      null;

    if (!officeId) {
      return;
    }

    try {
      const response =
        await api.get(
          `bookings/office/${officeId}/reserved-dates/`
        );

      const data =
        response.data;

      reservedDateRanges.value =
        Array.isArray(data)
          ? data
          : data?.results ?? [];

    } catch (error) {
      console.error(
        "Failed to load reserved dates:",
        error
      );

      reservedDateRanges.value =
        [];
    }
  };

/*
|--------------------------------------------------------------------------
| Form helpers
|--------------------------------------------------------------------------
*/

const clearErrors = () => {
  errors.user = "";
  errors.office = "";
  errors.start_date = "";
  errors.end_date = "";
  errors.general = "";
};

const resetForm = () => {
  form.user = "";
  form.office = "";

  bookingDates.start = "";
  bookingDates.end = "";

  reservedDateRanges.value =
    [];

  activeDateField.value =
    null;

  clearErrors();
};

const closeModal = () => {
  if (saving.value) {
    return;
  }

  resetForm();

  emit("close");
};

/*
|--------------------------------------------------------------------------
| Submit
|--------------------------------------------------------------------------
*/

const submitBooking =
  async () => {
    clearErrors();

    if (!form.user) {
      errors.user =
        "Please select a user.";
    }

    if (!form.office) {
      errors.office =
        "Please select an office.";
    }

    if (!bookingDates.start) {
      errors.start_date =
        "Please select a check-in date.";
    }

    if (!bookingDates.end) {
      errors.end_date =
        "Please select a check-out date.";
    }

    if (
      errors.user ||
      errors.office ||
      errors.start_date ||
      errors.end_date
    ) {
      return;
    }

    saving.value = true;

    try {
      await adminStore.createBooking({
        user: form.user,
        office: form.office,
        start_date:
          bookingDates.start,
        end_date:
          bookingDates.end
      });

      resetForm();

      emit("created");

    } catch (error) {
      const data =
        error.response?.data || {};

      errors.user =
        data.user?.[0] || "";

      errors.office =
        data.office?.[0] || "";

      errors.start_date =
        data.start_date?.[0] || "";

      errors.end_date =
        data.end_date?.[0] || "";

      if (
        Array.isArray(
          data.non_field_errors
        )
      ) {
        errors.general =
          data.non_field_errors[0];
      }

      else if (
        typeof data.detail ===
        "string"
      ) {
        errors.general =
          data.detail;
      }

      else if (
        typeof data === "string"
      ) {
        errors.general =
          data;
      }

      else if (
        !errors.user &&
        !errors.office &&
        !errors.start_date &&
        !errors.end_date
      ) {
        errors.general =
          "Unable to create booking.";
      }

    } finally {
      saving.value = false;
    }
  };

/*
|--------------------------------------------------------------------------
| Watchers
|--------------------------------------------------------------------------
*/
watch(
  () => props.show,

  async (isOpen) => {
    if (!isOpen) {
      return;
    }

    resetForm();

    try {
      const requests = [];

      if (!adminStore.users.length) {
        requests.push(
          adminStore.fetchUsers(1)
        );
      }

      if (!adminStore.offices.length) {
        requests.push(
          adminStore.fetchOffices(1)
        );
      }

      if (requests.length) {
        await Promise.all(requests);
      }

    } catch (error) {
      console.error(
        "Failed to load booking form options:",
        error
      );

      errors.general =
        "Unable to load users or offices.";
    }
  }
);
/* =========================================
   Load reserved dates when office changes
========================================= */

watch(
  () => form.office,
  async (officeId) => {
    if (!officeId) {
      reservedDateRanges.value = [];
      bookingDates.start = "";
      bookingDates.end = "";
      activeDateField.value = null;
      return;
    }

    await loadReservedDates(officeId);
  }
);

</script>