<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import api from '@/services/api'

import {
  Search,
  SlidersHorizontal,
  MapPin,
  Star,
  Wifi,
  Car,
  Users,
  Wind,
  UserCircle,
  Building2,
  Heart
} from 'lucide-vue-next'

const props = defineProps({
  workspaceType: String,
  title: String,
  highlight: String,
  description: String
})

const router = useRouter()
const authStore = useAuthStore()

const loading = ref(false)
const offices = ref([])
const favorites = ref([])

const showFilters = ref(true)

const currentPage = ref(1)
const hasNext = ref(false)
const hasPrev = ref(false)

const filters = reactive({
  search: '',
  city: '',
  min_price: null,
  max_price: null,
  rent_type: '',
  wifi: false,
  parking: false,
  meeting_room: false,
  air_conditioning: false,
  available: false
})

let debounceTimer = null

const activeFiltersCount = computed(() => {
  let count = 0

  if (filters.city) count++
  if (filters.min_price) count++
  if (filters.max_price) count++
  if (filters.rent_type) count++
  if (filters.wifi) count++
  if (filters.parking) count++
  if (filters.meeting_room) count++
  if (filters.air_conditioning) count++
  if (filters.available) count++

  return count
})

const resetFilters = () => {
  filters.search = ''
  filters.city = ''
  filters.min_price = null
  filters.max_price = null
  filters.rent_type = ''
  filters.wifi = false
  filters.parking = false
  filters.meeting_room = false
  filters.air_conditioning = false
  filters.available = false

  fetchOffices(1)
}

const getOfficeImage = (office) => {
  if (office.images?.length) {
    const img = office.images[0].image
    return img.startsWith('http')
      ? img
      : `http://127.0.0.1:8000${img}`
  }

  return 'https://placehold.co/600x400/F3F4F6/9CA3AF?text=Workspace'
}
const fetchOffices = async (page = 1) => {
  loading.value = true

  try {
    const params = {
      page,
      workspace_type: props.workspaceType
    }

    if (filters.search) params.search = filters.search
    if (filters.city) params.city = filters.city
    if (filters.min_price) params.min_price = filters.min_price
    if (filters.max_price) params.max_price = filters.max_price
    if (filters.rent_type) params.rent_type = filters.rent_type

    if (filters.wifi) params.wifi = true
    if (filters.parking) params.parking = true
    if (filters.meeting_room) params.meeting_room = true
    if (filters.air_conditioning) params.air_conditioning = true
    if (filters.available) params.available = true

    const { data } = await api.get('offices/', {
      params
    })

    if (data.results) {
      offices.value = data.results
      hasNext.value = !!data.next
      hasPrev.value = !!data.previous
    } else {
      offices.value = data
      hasNext.value = false
      hasPrev.value = false
    }

    currentPage.value = page
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}

const debouncedFetch = () => {
  clearTimeout(debounceTimer)

  debounceTimer = setTimeout(() => {
    fetchOffices(1)
  }, 350)
}

const fetchFavorites = async () => {
  if (!authStore.isAuthenticated) return

  try {
    const { data } = await api.get('favorites/')

    favorites.value = Array.isArray(data)
      ? data
      : (data.results || [])

  } catch (error) {
    console.error(error)
  }
}

const isFavorite = (officeId) => {
  return favorites.value.some(
    fav => fav.office === officeId
  )
}

const toggleFavorite = async (office) => {

  if (!authStore.isAuthenticated) {
    router.push('/login')
    return
  }

  const favorite = favorites.value.find(
    fav => fav.office === office.id
  )

  try {

    if (favorite) {

      await api.delete(
        `favorites/delete/${favorite.id}/`
      )

      favorites.value =
        favorites.value.filter(
          fav => fav.id !== favorite.id
        )

    } else {

      const { data } = await api.post(
        'favorites/create/',
        {
          office: office.id
        }
      )

      favorites.value.push(data)
    }

  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  fetchOffices()
  fetchFavorites()
})
</script>


<template>
  <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">

    <!-- Hero -->
    <div class="mb-6 text-center">

      <h1 class="font-display text-3xl font-black tracking-tight lg:text-4xl">
  <span class="text-[#23394E]">{{ title }}</span>
  <span class="text-[#F29200]"> {{ highlight }}</span>
   <p
    v-if="description"
class="mx-auto mt-3 max-w-xl text-sm leading-6 text-[#9f9f9f]"    
  >
    {{ description }}
  </p>
</h1>

      <!-- Search -->
      <div class="mx-auto mt-6 flex max-w-2xl flex-col gap-3 sm:flex-row">

        <div class="relative flex-1">

          <Search
            class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-gray-400"
          />

          <input
            v-model="filters.search"
            type="text"
            placeholder="Search workspace..."
            @input="debouncedFetch"
            class="h-12 w-full rounded-xl border border-gray-200 bg-white pl-11 pr-4 text-sm shadow-sm transition-all focus:border-[#f29200] focus:ring-4 focus:ring-[#f29200]/10"
          />

        </div>

        <button
          @click="showFilters = !showFilters"
          class="flex h-12 items-center justify-center gap-2 rounded-xl border border-gray-200 bg-white px-6 text-sm font-semibold text-[#23394e] shadow-sm transition hover:border-[#f29200] hover:text-[#f29200]"
        >

          <SlidersHorizontal class="h-4 w-4" />

          Filters

          <span
            v-if="activeFiltersCount > 0"
            class="flex h-5 w-5 items-center justify-center rounded-full bg-[#f29200] text-[10px] font-bold text-white"
          >
            {{ activeFiltersCount }}
          </span>

        </button>

      </div>

    </div>

    <div class="grid grid-cols-1 gap-6 lg:grid-cols-4">

      <!-- Sidebar -->

      <div
        v-if="showFilters"
        class="self-start rounded-2xl border border-gray-200 bg-white p-5 shadow-sm lg:col-span-1"
      >

        <div class="mb-5 flex items-center justify-between border-b pb-3">

          <h3 class="font-display text-lg font-bold text-[#23394e]">
            Filters
          </h3>

          <button
            @click="resetFilters"
            class="text-sm font-semibold text-[#f29200] transition hover:text-[#d97f00]"
          >
            Reset
          </button>

        </div>
        <!-- City filter -->
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-2">City</label>
          <input 
            v-model="filters.city" 
            type="text" 
            placeholder="e.g. Casablanca"
            @input="debouncedFetch"
            class="block w-full rounded-xl border border-gray-200 px-3.5 py-2.5 text-xs focus:border-[#f29200] focus:outline-none focus:ring-1 focus:ring-[#f29200]/20"
          />
        </div>

        <!-- Price Range -->
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-2">Price Range</label>
          <div class="flex items-center gap-2">
            <input 
              v-model.number="filters.min_price" 
              type="number" 
              placeholder="Min"
              @input="debouncedFetch"
              class="block w-full rounded-xl border border-gray-200 px-3 py-2 text-xs focus:border-[#f29200] focus:outline-none focus:ring-1 focus:ring-[#f29200]/20"
            />
            <span class="text-gray-400 text-xs">to</span>
            <input 
              v-model.number="filters.max_price" 
              type="number" 
              placeholder="Max"
              @input="debouncedFetch"
              class="block w-full rounded-xl border border-gray-200 px-3 py-2 text-xs focus:border-[#f29200] focus:outline-none focus:ring-1 focus:ring-[#f29200]/20"
            />
          </div>
        </div>

        <!-- Rent Type -->
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-2">Rent Type</label>
          <select 
            v-model="filters.rent_type" 
            @change="fetchOffices(1)"
            class="block w-full rounded-xl border border-gray-200 px-3 py-2.5 text-xs focus:border-[#f29200] focus:outline-none focus:ring-1 focus:ring-[#f29200]/20"
          >
            <option value="">All Types</option>
            <option value="daily">Daily</option>
            <option value="weekly">Weekly</option>
            <option value="monthly">Monthly</option>
          </select>
        </div>

        <!-- Amenities -->
        <div class="space-y-2.5">
          <label class="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-1">Amenities</label>
          
          <label class="flex items-center gap-2.5 text-xs text-gray-600 font-medium cursor-pointer">
            <input 
              v-model="filters.wifi" 
              type="checkbox" 
              @change="fetchOffices(1)"
              class="rounded text-brand-f29200 focus:ring-[#f29200] h-4 w-4"
            />
            <span>Free High-Speed Wifi</span>
          </label>

          <label class="flex items-center gap-2.5 text-xs text-gray-600 font-medium cursor-pointer">
            <input 
              v-model="filters.parking" 
              type="checkbox" 
              @change="fetchOffices(1)"
              class="rounded text-[#f29200] focus:ring-[#f29200] h-4 w-4"
            />
            <span>Dedicated Parking</span>
          </label>

          <label class="flex items-center gap-2.5 text-xs text-gray-600 font-medium cursor-pointer">
            <input 
              v-model="filters.meeting_room" 
              type="checkbox" 
              @change="fetchOffices(1)"
              class="rounded text-[#f29200] focus:ring-[#f29200] h-4 w-4"
            />
            <span>Meeting Rooms</span>
          </label>

          <label class="flex items-center gap-2.5 text-xs text-gray-600 font-medium cursor-pointer">
            <input 
              v-model="filters.air_conditioning" 
              type="checkbox" 
              @change="fetchOffices(1)"
              class="rounded text-[#f29200] focus:ring-[#f29200] h-4 w-4"
            />
            <span>Air Conditioning</span>
          </label>

          <label class="flex items-center gap-2.5 text-xs text-gray-600 font-medium cursor-pointer">
            <input 
              v-model="filters.available" 
              type="checkbox" 
              @change="fetchOffices(1)"
              class="rounded text-[#f29200] focus:ring-[#f29200] h-4 w-4"
            />
            <span>Only Available Spaces</span>
          </label>
        </div>
      </div>

      <!-- Office List Grid -->
      <div :class="[showFilters ? 'lg:col-span-3' : 'lg:col-span-4', 'space-y-6']">
        
        <div v-if="loading" class="flex flex-col items-center justify-center py-20 gap-4">
          <svg class="h-10 w-10 animate-spin text-[#f29200]" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span class="text-sm font-medium text-gray-500">Searching workspace databases...</span>
        </div>

        <div v-else-if="offices.length === 0" class="text-center py-20 border border-dashed border-gray-200 rounded-3xl bg-white/50">
          <Building2 class="mx-auto h-12 w-12 text-gray-300" />
          <h3 class="mt-4 font-display font-bold text-gray-900 text-lg">No workspaces found</h3>
          <p class="mt-2 text-sm text-gray-400 max-w-xs mx-auto">Try modifying your filters or checking spelling to find available office spaces.</p>
        </div>

        <template v-else>
          <!-- Grid of office cards -->
          <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            
            <div 
              v-for="office in offices" 
              :key="office.id" 
              class="group relative flex flex-col rounded-3xl border border-gray-100 bg-white overflow-hidden shadow-sm hover:shadow-md transition-all duration-300"
            >
              
              <!-- Card Image / Header banner -->
              <div class="relative aspect-video w-full overflow-hidden bg-gray-100">
                <img 
                  :src="getOfficeImage(office)" 
                  :alt="office.title"
                  class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
                
                <!-- Availability / Rent Type badges -->
                <div class="absolute top-3 left-3 flex flex-wrap gap-1.5">
                  <span class="rounded-lg bg-white/95 backdrop-blur px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider text-gray-900 shadow-sm">
                    {{ office.rent_type }}
                  </span>
                  <span 
                    :class="['rounded-lg px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider text-white shadow-sm', office.available ? 'bg-emerald-500' : 'bg-red-500']"
                  >
                    {{ office.available ? 'Available' : 'Booked' }}
                  </span>
                </div>

                <!-- Favorite heart button -->
                <button 
                  @click.stop="toggleFavorite(office)" 
                  class="absolute top-3 right-3 flex h-8 w-8 items-center justify-center rounded-xl bg-white/90 backdrop-blur text-gray-500 hover:text-red-500 transition-colors shadow-sm"
                >
                  <Heart :class="['h-4.5 w-4.5', isFavorite(office.id) ? 'fill-red-500 text-red-500' : '']" />
                </button>
              </div>

              <!-- Card Content details -->
              <div class="flex flex-1 flex-col p-5">
                <div class="flex items-center justify-between text-xs text-gray-400">
                  <span class="flex items-center gap-1">
                    <MapPin class="h-3.5 w-3.5 text-gray-400" />
                    {{ office.city }}
                  </span>
                  <span class="flex items-center gap-1 font-semibold text-[#f29200]">
                    <Star class="h-3.5 w-3.5 fill-[#f29200]" />
                    {{ office.average_rating }}
                  </span>
                </div>

                <router-link :to="`/office/${office.id}`" class="mt-2 block">
                  <h3 class="font-display font-bold text-gray-900 group-hover:text-[#f29200] transition-colors line-clamp-1">
                    {{ office.title }}
                  </h3>
                </router-link>

                <p class="mt-2 text-xs text-gray-500 line-clamp-2 grow">
                  {{ office.description }}
                </p>

                <!-- Amenities icon ribbon -->
                <div class="mt-4 flex gap-3 text-gray-400 border-t border-gray-50 pt-4">
                  <span v-if="office.wifi" title="Wifi" class="rounded-lg bg-gray-50 p-1.5"><Wifi class="h-4 w-4" /></span>
                  <span v-if="office.parking" title="Parking" class="rounded-lg bg-gray-50 p-1.5"><Car class="h-4 w-4" /></span>
                  <span v-if="office.meeting_room" title="Meeting Rooms" class="rounded-lg bg-gray-50 p-1.5"><Users class="h-4 w-4" /></span>
                  <span v-if="office.air_conditioning" title="AC" class="rounded-lg bg-gray-50 p-1.5"><Wind class="h-4 w-4" /></span>
                  <span title="Capacity" class="ml-auto flex items-center gap-1 text-xs font-semibold text-gray-500 bg-gray-50 rounded-lg px-2 py-0.5">
                    <UserCircle class="h-3.5 w-3.5" />
                    {{ office.capacity }} pax
                  </span>
                </div>

                <!-- Footer pricing / link -->
                <div class="mt-4 flex items-center justify-between border-t border-gray-50 pt-4">
                  <div>
                    <span class="text-xs text-gray-400">Rate starting at</span>
                    <div class="font-display font-extrabold text-gray-900 text-lg">
                      {{ office.price }} DH<span class="text-xs font-medium text-gray-400">/{{ office.rent_type === 'daily' ? 'day' : office.rent_type === 'weekly' ? 'wk' : 'mo' }}</span>
                    </div>
                  </div>
                  <router-link 
                    :to="`/office/${office.id}`" 
                    class="rounded-xl bg-gray-900 hover:bg-gray-800 px-3.5 py-2 text-xs font-bold text-white transition-colors"
                  >
                    View Space
                  </router-link>
                </div>

              </div>

            </div>

          </div>

          <!-- Pagination controls -->
          <div class="mt-8 flex items-center justify-between border-t border-gray-100 pt-6">
            <span class="text-xs text-gray-500">
              Showing page {{ currentPage }}
            </span>
            <div class="flex items-center gap-2">
              <button 
                :disabled="!hasPrev" 
                @click="fetchOffices(currentPage - 1)"
                class="rounded-xl border border-gray-200 bg-white px-4 py-2 text-xs font-semibold text-gray-700 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
              >
                Previous
              </button>
              <button 
                :disabled="!hasNext" 
                @click="fetchOffices(currentPage + 1)"
                class="rounded-xl border border-gray-200 bg-white px-4 py-2 text-xs font-semibold text-gray-700 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
              >
                Next
              </button>
            </div>
          </div>

        </template>

      </div>

    </div>

  </div>
</template>