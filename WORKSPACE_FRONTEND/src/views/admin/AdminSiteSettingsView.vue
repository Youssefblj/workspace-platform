<script setup>
import { onMounted, ref } from "vue"
import Swal from "sweetalert2"

import {
  Globe2,
  Mail,
  Phone,
  MapPin,
  Instagram,
  Facebook,
  Linkedin,
  Save,
  MessageCircle,
  AtSign
} from "lucide-vue-next"

import { VueTelInput } from "vue-tel-input"
import "vue-tel-input/vue-tel-input.css"

import { useSiteSettingsStore } from "@/stores/siteSettings"


const siteSettingsStore = useSiteSettingsStore()


const form = ref({
  website_name: "",
  website_url: "",
  contact_email: "",
  contact_phone: "",
  whatsapp_number: "",
  address: "",
  instagram_url: "",
  facebook_url: "",
  linkedin_url: "",
  twitter_url: "",

})


const errors = ref({
  website_name: "",
  contact_email: "",
  contact_phone: "",
  whatsapp_number: "",
})


const contactPhoneData = ref(null)
const whatsappPhoneData = ref(null)


const loadSettings = async () => {
  try {
    const data =
      await siteSettingsStore.fetchSettings()

    form.value = {
      website_name:
        data.website_name || "",

      website_url:
        data.website_url || "",

      contact_email:
        data.contact_email || "",

      contact_phone:
        data.contact_phone || "",

      whatsapp_number:
        data.whatsapp_number || "",

      address:
        data.address || "",

      instagram_url:
        data.instagram_url || "",

      facebook_url:
        data.facebook_url || "",

      linkedin_url:
        data.linkedin_url || "",
      twitter_url:
        data.twitter_url || "",
    }

    contactPhoneData.value = null
    whatsappPhoneData.value = null
  }
  catch (error) {
    console.error(error)

    Swal.fire({
      icon: "error",
      title: "Unable to load settings",
      text:
        "Website settings could not be loaded.",
      confirmButtonColor: "#f29200"
    })
  }
}


const handleContactPhoneValidation = (
  data
) => {

  contactPhoneData.value = data

  if (!form.value.contact_phone) {
    errors.value.contact_phone = ""
    return
  }

  errors.value.contact_phone =
    data.valid
      ? ""
      : "Enter a valid phone number."
}


const handleWhatsappValidation = (
  data
) => {

  whatsappPhoneData.value = data

  if (!form.value.whatsapp_number) {
    errors.value.whatsapp_number = ""
    return
  }

  errors.value.whatsapp_number =
    data.valid
      ? ""
      : "Enter a valid WhatsApp number."
}


const validateForm = () => {

  errors.value = {
    website_name: "",
    contact_email: "",
    contact_phone: "",
    whatsapp_number: "",
  }

  let valid = true


  if (
    !form.value.website_name.trim()
  ) {
    errors.value.website_name =
      "Website name is required."

    valid = false
  }


  if (
    form.value.contact_email &&
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(
      form.value.contact_email
    )
  ) {
    errors.value.contact_email =
      "Enter a valid email address."

    valid = false
  }


  if (
    form.value.contact_phone &&
    contactPhoneData.value &&
    !contactPhoneData.value.valid
  ) {
    errors.value.contact_phone =
      "Enter a valid phone number."

    valid = false
  }


  if (
    form.value.whatsapp_number &&
    whatsappPhoneData.value &&
    !whatsappPhoneData.value.valid
  ) {
    errors.value.whatsapp_number =
      "Enter a valid WhatsApp number."

    valid = false
  }


  return valid
}


const normalizePhone = (
  phone,
  phoneData
) => {

  if (!phone) {
    return ""
  }

  return (
    phoneData?.number || phone
  )
    .replace(/[^\d+]/g, "")
    .replace(/(?!^)\+/g, "")
}


const saveSettings = async () => {

  if (!validateForm()) {
    return
  }


  const payload = {

    website_name:
      form.value.website_name.trim(),

    website_url:
      form.value.website_url.trim(),

    contact_email:
      form.value.contact_email.trim(),

    contact_phone:
      normalizePhone(
        form.value.contact_phone,
        contactPhoneData.value
      ),

    whatsapp_number:
      normalizePhone(
        form.value.whatsapp_number,
        whatsappPhoneData.value
      ),

    address:
      form.value.address.trim(),

    instagram_url:
      form.value.instagram_url.trim(),

    facebook_url:
      form.value.facebook_url.trim(),

    linkedin_url:
      form.value.linkedin_url.trim(),
    twitter_url:
      form.value.twitter_url.trim(),
  }


  try {

    const updated =
      await siteSettingsStore
        .updateSettings(payload)


    form.value = {
      ...form.value,
      ...updated,
    }


    contactPhoneData.value = null
    whatsappPhoneData.value = null


    await Swal.fire({
      icon: "success",
      title:
        "Website Settings Updated",
      text:
        "Your website information has been saved successfully.",
      confirmButtonColor:
        "#f29200"
    })
  }
  catch (error) {

    console.error(error)


    const data =
      error.response?.data


    if (data?.website_name) {
      errors.value.website_name =
        data.website_name[0]
    }


    if (data?.contact_email) {
      errors.value.contact_email =
        data.contact_email[0]
    }


    if (data?.contact_phone) {
      errors.value.contact_phone =
        data.contact_phone[0]
    }


    if (data?.whatsapp_number) {
      errors.value.whatsapp_number =
        data.whatsapp_number[0]
    }


    if (
      !data?.website_name &&
      !data?.contact_email &&
      !data?.contact_phone &&
      !data?.whatsapp_number
    ) {

      Swal.fire({
        icon: "error",
        title:
          "Unable to save settings",
        text:
          "Please check the information and try again.",
        confirmButtonColor:
          "#f29200"
      })
    }
  }
}


onMounted(() => {
  loadSettings()
})
</script>


<template>
  <div class="space-y-6">

    <!-- Header -->

    <div>
      <div
        class="flex items-center gap-3"
      >
        <div
          class="
            flex
            h-10
            w-10
            items-center
            justify-center
            rounded-xl
            bg-[#f29200]/10
            text-[#f29200]
          "
        >
          <Globe2 :size="20" />
        </div>

        <div>
          <h1
            class="
              text-2xl
              font-bold
              text-[#23394e]
            "
          >
            Website Settings
          </h1>

          <p
            class="
              mt-1
              text-sm
              text-[#9f9f9f]
            "
          >
            Manage your website name,
            contact details and social links.
          </p>
        </div>
      </div>
    </div>


    <!-- Loading -->

    <div
      v-if="siteSettingsStore.loading"
      class="
        rounded-2xl
        border
        border-gray-200
        bg-white
        p-6
        text-sm
        text-[#9f9f9f]
      "
    >
      Loading website settings...
    </div>


    <form
      v-else
      @submit.prevent="saveSettings"
      class="space-y-6"
    >

      <!-- General Information -->

      <section
        class="
          rounded-2xl
          border
          border-gray-200
          bg-white
          p-5
          shadow-sm
          sm:p-6
        "
      >

        <div
          class="
            mb-6
            flex
            items-center
            gap-3
          "
        >
          <Globe2
            :size="20"
            class="text-[#f29200]"
          />

          <div>
            <h2
              class="
                font-bold
                text-[#23394e]
              "
            >
              General Information
            </h2>

            <p
              class="
                text-sm
                text-[#9f9f9f]
              "
            >
              Main website identity.
            </p>
          </div>
        </div>


        <div
          class="
            grid
            gap-5
            md:grid-cols-2
          "
        >

          <div>
            <label
              class="
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              Website Name
            </label>

            <input
              v-model="form.website_name"
              type="text"
              maxlength="100"
              placeholder="WorkSpace"
              class="
                mt-2
                h-11
                w-full
                rounded-xl
                border
                border-gray-200
                px-4
                text-sm
                text-[#23394e]
                outline-none
                transition
                focus:border-[#f29200]
                focus:ring-2
                focus:ring-[#f29200]/10
              "
            />

            <p
              v-if="errors.website_name"
              class="
                mt-1
                text-xs
                text-red-500
              "
            >
              {{ errors.website_name }}
            </p>
          </div>


          <div>
            <label
              class="
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              Website URL
            </label>

            <input
              v-model="form.website_url"
              type="url"
              placeholder="https://example.com"
              class="
                mt-2
                h-11
                w-full
                rounded-xl
                border
                border-gray-200
                px-4
                text-sm
                text-[#23394e]
                outline-none
                transition
                focus:border-[#f29200]
                focus:ring-2
                focus:ring-[#f29200]/10
              "
            />
          </div>

        </div>
      </section>


      <!-- Contact Information -->

      <section
        class="
          rounded-2xl
          border
          border-gray-200
          bg-white
          p-5
          shadow-sm
          sm:p-6
        "
      >

        <div
          class="
            mb-6
            flex
            items-center
            gap-3
          "
        >
          <Phone
            :size="20"
            class="text-[#f29200]"
          />

          <div>
            <h2
              class="
                font-bold
                text-[#23394e]
              "
            >
              Contact Information
            </h2>

            <p
              class="
                text-sm
                text-[#9f9f9f]
              "
            >
              Information visible to customers.
            </p>
          </div>
        </div>


        <div
          class="
            grid
            gap-5
            md:grid-cols-2
          "
        >

          <!-- Email -->

          <div>
            <label
              class="
                flex
                items-center
                gap-2
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              <Mail :size="15" />

              Contact Email
            </label>

            <input
              v-model="form.contact_email"
              type="email"
              placeholder="contact@example.com"
              class="
                mt-2
                h-11
                w-full
                rounded-xl
                border
                border-gray-200
                px-4
                text-sm
                outline-none
                transition
                focus:border-[#f29200]
                focus:ring-2
                focus:ring-[#f29200]/10
              "
            />

            <p
              v-if="errors.contact_email"
              class="
                mt-1
                text-xs
                text-red-500
              "
            >
              {{ errors.contact_email }}
            </p>
          </div>


          <!-- Contact Phone -->

          <div>
            <label
              class="
                flex
                items-center
                gap-2
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              <Phone :size="15" />

              Contact Phone
            </label>

            <VueTelInput
              v-model="form.contact_phone"
              mode="international"
              :auto-format="true"
              :valid-characters-only="true"
              :preferred-countries="[
                'MA',
                'FR',
                'ES',
                'US',
                'GB'
              ]"
              :dropdown-options="{
                showDialCodeInList: true,
                showFlags: true,
                showSearchBox: true
              }"
              :input-options="{
                placeholder: 'Phone Number',
                autocomplete: 'tel',
                maxlength: 16
              }"
              @validate="
                handleContactPhoneValidation
              "
              :class="[
                'site-phone-input',
                errors.contact_phone
                  ? 'phone-error'
                  : ''
              ]"
            />

            <p
              v-if="errors.contact_phone"
              class="
                mt-1
                text-xs
                text-red-500
              "
            >
              {{ errors.contact_phone }}
            </p>
          </div>


          <!-- WhatsApp -->

          <div>
            <label
              class="
                flex
                items-center
                gap-2
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              <MessageCircle :size="15" />

              WhatsApp Number
            </label>

            <VueTelInput
              v-model="form.whatsapp_number"
              mode="international"
              :auto-format="true"
              :valid-characters-only="true"
              :preferred-countries="[
                'MA',
                'FR',
                'ES',
                'US',
                'GB'
              ]"
              :dropdown-options="{
                showDialCodeInList: true,
                showFlags: true,
                showSearchBox: true
              }"
              :input-options="{
                placeholder: 'WhatsApp Number',
                autocomplete: 'tel',
                maxlength: 16
              }"
              @validate="
                handleWhatsappValidation
              "
              :class="[
                'site-phone-input',
                errors.whatsapp_number
                  ? 'phone-error'
                  : ''
              ]"
            />

            <p
              v-if="errors.whatsapp_number"
              class="
                mt-1
                text-xs
                text-red-500
              "
            >
              {{ errors.whatsapp_number }}
            </p>
          </div>


          <!-- Address -->

          <div>
            <label
              class="
                flex
                items-center
                gap-2
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              <MapPin :size="15" />

              Address
            </label>

            <input
              v-model="form.address"
              type="text"
              maxlength="255"
              placeholder="Business address"
              class="
                mt-2
                h-11
                w-full
                rounded-xl
                border
                border-gray-200
                px-4
                text-sm
                outline-none
                transition
                focus:border-[#f29200]
                focus:ring-2
                focus:ring-[#f29200]/10
              "
            />
          </div>

        </div>
      </section>


      <!-- Social Media -->

      <section
        class="
          rounded-2xl
          border
          border-gray-200
          bg-white
          p-5
          shadow-sm
          sm:p-6
        "
      >

        <div
          class="mb-6"
        >
          <h2
            class="
              font-bold
              text-[#23394e]
            "
          >
            Social Media
          </h2>

          <p
            class="
              mt-1
              text-sm
              text-[#9f9f9f]
            "
          >
            Optional social profile links.
          </p>
        </div>


        <div
          class="
            grid
            gap-5
            md:grid-cols-3
          "
        >

          <div>
            <label
              class="
                flex
                items-center
                gap-2
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              <Instagram :size="15" />

              Instagram
            </label>

            <input
              v-model="form.instagram_url"
              type="url"
              placeholder="https://instagram.com/..."
              class="settings-input"
            />
          </div>


          <div>
            <label
              class="
                flex
                items-center
                gap-2
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              <Facebook :size="15" />

              Facebook
            </label>

            <input
              v-model="form.facebook_url"
              type="url"
              placeholder="https://facebook.com/..."
              class="settings-input"
            />
          </div>


          <div>
            <label
              class="
                flex
                items-center
                gap-2
                text-sm
                font-semibold
                text-[#23394e]
              "
            >
              <Linkedin :size="15" />

              LinkedIn
            </label>

            <input
              v-model="form.linkedin_url"
              type="url"
              placeholder="https://linkedin.com/..."
              class="settings-input"
            />
          </div>

          <div>
  <label
    class="
      flex
      items-center
      gap-2
      text-sm
      font-semibold
      text-[#23394e]
    "
  >
  <AtSign :size="15" />
  X / Twitter
</label>

  <input
    v-model="form.twitter_url"
    type="url"
    placeholder="https://x.com/..."
    class="settings-input"
  />
</div>

        </div>
      </section>


      <!-- Save -->

      <div
        class="
          flex
          justify-end
        "
      >
        <button
          type="submit"
          :disabled="
            siteSettingsStore.loading
          "
          class="
            inline-flex
            items-center
            gap-2
            rounded-xl
            bg-[#f29200]
            px-5
            py-3
            text-sm
            font-bold
            text-white
            transition
            hover:bg-[#f29200]/90
            disabled:cursor-not-allowed
            disabled:opacity-50
          "
        >
          <Save :size="17" />

          {{
            siteSettingsStore.loading
              ? "Saving..."
              : "Save Changes"
          }}
        </button>
      </div>

    </form>
  </div>
</template>


<style scoped>
.settings-input {
  margin-top: 0.5rem;
  height: 2.75rem;
  width: 100%;
  border-radius: 0.75rem;
  border: 1px solid #e5e7eb;
  padding: 0 1rem;
  font-size: 0.875rem;
  color: #23394e;
  outline: none;
  transition: 0.2s;
}

.settings-input:focus {
  border-color: #f29200;
  box-shadow:
    0 0 0 3px
    rgba(242, 146, 0, 0.1);
}


.site-phone-input {
  margin-top: 0.5rem;
  min-height: 44px;
  border: 1px solid #e5e7eb !important;
  border-radius: 0.75rem !important;
  background: white;
  transition: 0.2s;
}

.site-phone-input:focus-within {
  border-color: #f29200 !important;
  box-shadow:
    0 0 0 3px
    rgba(242, 146, 0, 0.1);
}

.site-phone-input.phone-error {
  border-color: #ef4444 !important;
}

.site-phone-input.phone-error:focus-within {
  border-color: #ef4444 !important;
  box-shadow:
    0 0 0 3px
    rgba(239, 68, 68, 0.08);
}

.site-phone-input :deep(.vti__input) {
  font-size: 14px;
  color: #23394e;
  background: transparent;
}

.site-phone-input :deep(.vti__dropdown) {
  border-radius:
    0.75rem 0 0 0.75rem;
}
</style>