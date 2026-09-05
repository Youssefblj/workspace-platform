<template>
  <footer class="mt-auto">

    <CTASection />

    <!-- MAIN FOOTER -->
    <div class="border-t border-amber-100 bg-white">

      <div class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">

        <div class="grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-4 lg:gap-8">

          <!-- Brand -->
          <div class="space-y-5 lg:col-span-1">

            <router-link
              to="/"
              class="group inline-flex items-center gap-2.5 font-display text-lg font-bold text-gray-900"
            >

              <div
                class="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-[#F59E0B] text-white shadow-lg shadow-amber-300/40 transition-all duration-300 group-hover:scale-110 group-hover:shadow-amber-300/60"
              >

                <Building class="h-4 w-4" />

              </div>

<span
  v-if="websiteName === 'WorkSpace'"
  class="tracking-tight"
>
  Work<span class="text-[#F59E0B]">Space</span>
</span>

<span
  v-else
  class="tracking-tight text-gray-900"
>
  {{ websiteName }}
</span>

            </router-link>

            <p class="max-w-xs text-[13px] leading-relaxed text-gray-500">
              Premium office spaces and coworking environments tailored for freelancers, startups, and businesses across Morocco.
            </p>

            <div class="flex items-center gap-2.5 pt-1">

              <a
                v-for="social in socials"
                :key="social.label"
                :href="social.href"
                :aria-label="social.label"
                target="_blank"
                rel="noopener noreferrer"
                class="group flex h-8 w-8 items-center justify-center rounded-lg border border-gray-100 bg-gray-50 text-gray-400 transition-all duration-200 hover:scale-110 hover:border-amber-200 hover:bg-amber-50 hover:text-[#F59E0B] hover:shadow-sm hover:shadow-amber-300/30"
              >

                <component :is="social.icon" class="h-3.5 w-3.5" />

              </a>

            </div>

          </div>

          <!-- Properties -->

          <div>

            <h3 class="font-display text-[10px] font-bold uppercase tracking-[0.15em] text-gray-400">

              Our Properties

            </h3>

            <ul class="mt-4 space-y-2.5">

              <li
                v-for="link in propertiesLinks"
                :key="link.label"
              >

                <router-link
                  :to="link.to"
                  class="group inline-flex items-center gap-1.5 text-[13px] font-medium text-gray-500 transition-all duration-200 hover:text-[#F59E0B]"
                >

                  <span class="h-0.5 w-0 rounded-full bg-[#F59E0B] transition-all duration-300 group-hover:w-3"></span>

                  {{ link.label }}

                </router-link>

              </li>

            </ul>

          </div>

          <!-- Information -->

          <div>

            <h3 class="font-display text-[10px] font-bold uppercase tracking-[0.15em] text-gray-400">

              Useful Information

            </h3>

            <ul class="mt-4 space-y-2.5">

              <li
                v-for="link in infoLinks"
                :key="link.label"
              >

                <router-link
                  :to="link.to"
                  class="group inline-flex items-center gap-1.5 text-[13px] font-medium text-gray-500 transition-all duration-200 hover:text-[#F59E0B]"
                >

                  <span class="h-0.5 w-0 rounded-full bg-[#F59E0B] transition-all duration-300 group-hover:w-3"></span>

                  {{ link.label }}

                </router-link>

              </li>

            </ul>

          </div>

          <!-- Legal -->

          <div>

            <h3 class="font-display text-[10px] font-bold uppercase tracking-[0.15em] text-gray-400">

              Legal

            </h3>

            <ul class="mt-4 space-y-2.5">

              <li
                v-for="link in legalLinks"
                :key="link.label"
              >

                <RouterLink
                  :to="link.to"
                  class="group inline-flex items-center gap-1.5 text-[13px] font-medium text-gray-500 transition-all duration-200 hover:text-[#F59E0B]"
                >

                  <span class="h-0.5 w-0 rounded-full bg-[#F59E0B] transition-all duration-300 group-hover:w-3"></span>

                  {{ link.label }}

                </RouterLink>

              </li>

            </ul>

          </div>

        </div>

        <!-- Bottom -->

        <div class="mt-12 flex flex-col items-center justify-between gap-3 border-t border-amber-100 pt-8 sm:flex-row">

          <p class="text-[12px] text-gray-400">

&copy; {{ currentYear }} {{ websiteName }}. All rights reserved.
          </p>

          <p class="inline-flex items-center gap-1.5 text-[12px] text-gray-400">

            <span>Built with</span>

            <span class="font-semibold text-[#F59E0B]">

              Vue.js

            </span>

            <span class="text-gray-300">•</span>

            <span class="font-semibold text-gray-500">

              Django REST Framework

            </span>

            <span class="text-gray-300">•</span>

            <span class="font-semibold text-gray-500">

              MySQL

            </span>

          </p>

        </div>

      </div>

    </div>

  </footer>
</template>

<script setup>
import { computed, h, onMounted } from 'vue'
import { Building } from 'lucide-vue-next'
import CTASection from './home/CTASection.vue';
import { useSiteSettingsStore } from '@/stores/siteSettings'

const siteSettingsStore = useSiteSettingsStore()

onMounted(() => {
  siteSettingsStore.fetchSettings().catch(() => {})
})

const websiteName = computed(() =>
  siteSettingsStore.settings.website_name || 'WorkSpace'
)

const currentYear = computed(() => new Date().getFullYear())

// ── Social icon SVG components (inline so no extra dependency) ──────────────
const LinkedInIcon = {
  render: () => h('svg', { viewBox: '0 0 24 24', fill: 'currentColor' }, [
    h('path', { d: 'M20.447 20.452H17.21v-5.569c0-1.327-.027-3.037-1.852-3.037-1.854 0-2.137 1.446-2.137 2.94v5.666H9.984V9h3.104v1.562h.044c.432-.82 1.487-1.685 3.062-1.685 3.274 0 3.879 2.155 3.879 4.958v6.617zM5.337 7.433a1.8 1.8 0 1 1 0-3.6 1.8 1.8 0 0 1 0 3.6zm1.603 13.019H3.73V9h3.21v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.226.792 24 1.771 24h20.451C23.2 24 24 23.226 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z' })
  ])
}

const FacebookIcon = {
  render: () => h('svg', { viewBox: '0 0 24 24', fill: 'currentColor' }, [
    h('path', { d: 'M24 12.073C24 5.405 18.627 0 12 0S0 5.405 0 12.073c0 6.03 4.438 11.024 10.125 11.927v-8.44H7.077v-3.487h3.048V9.41c0-3.025 1.792-4.697 4.533-4.697 1.313 0 2.686.236 2.686.236v2.967h-1.513c-1.49 0-1.953.93-1.953 1.884v2.25h3.328l-.532 3.487h-2.796v8.44C19.562 23.097 24 18.103 24 12.073z' })
  ])
}

const InstagramIcon = {
  render: () => h('svg', { viewBox: '0 0 24 24', fill: 'currentColor' }, [
    h('path', { d: 'M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z' })
  ])
}

const XTwitterIcon = {
  render: () => h('svg', { viewBox: '0 0 24 24', fill: 'currentColor' }, [
    h('path', { d: 'M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z' })
  ])
}

const socials = computed(() => {
  const settings = siteSettingsStore.settings

  return [
    {
      label: 'LinkedIn',
      href: settings.linkedin_url,
      icon: LinkedInIcon
    },
    {
      label: 'Facebook',
      href: settings.facebook_url,
      icon: FacebookIcon
    },
    {
      label: 'Instagram',
      href: settings.instagram_url,
      icon: InstagramIcon
    },
    {
      label: 'X / Twitter',
      href: settings.twitter_url,
      icon: XTwitterIcon
    }
  ].filter(social => social.href)
})


// ── Navigation data ─────────────────────────────────────────────────────────
const propertiesLinks = [
  { label: 'Offices',           to: '/browse-offices' },
  { label: 'Coworking Spaces',  to: '/coworking-spaces' },
  { label: 'Meeting Rooms',     to: '/meeting-rooms' },
  { label: 'Virtual Offices',   to: '/virtual-offices' },
]

const infoLinks = [
  { label: 'About Us', to: '/about' },
  { label: 'How Booking Works', to: '/how-booking-works' },
  { label: 'Pricing', to: '/pricing' },
  { label: 'FAQs', to: '/faqs' },
  { label: 'Contact Us', to: '/contact' },
]

const legalLinks = [
  {
    label: 'Privacy Policy',
    to: '/privacy-policy',
  },
  {
    label: 'Terms & Conditions',
    to: '/terms',
  },
  {
    label: 'Cookies Policy',
    to: '/cookies-policy',
  },
  {
    label: 'Confidentiality',
    to: '/confidentiality',
  },
]
</script>
