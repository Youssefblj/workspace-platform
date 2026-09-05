import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import PrivacyPolicyView from '@/views/PrivacyPolicyView.vue'
import TermsView from '@/views/TermsView.vue'
import CookiesPolicyView from '@/views/CookiesPolicyView.vue'
import ConfidentialityView from '@/views/ConfidentialityView.vue'
import AboutView from '@/views/AboutView.vue'
import HowBookingWorksView from '@/views/BookingGuideView.vue'
import PricingView from '@/views/PricingView.vue'
import FAQsView from '@/views/FAQView.vue'
import ContactView from '@/views/ContactView.vue'
import CoworkingSpacesView from '@/views/CoworkingSpacesView.vue'
import MeetingRoomsView from '@/views/MeetingRoomsView.vue'
import VirtualOfficesView from '@/views/VirtualOfficesView.vue'
import AdminLayout from '@/layouts/AdminLayout.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/HomeView.vue'),
    meta: { requiresAuth: false }
  },
  {
  path: "/browse-offices",
  name: "browse-offices",
  component: () => import("@/views/BrowseOfficesView.vue"),
  meta: { requiresAuth: false }
},
{
  path: "/login",
  name: "login",
  component: () => import("@/views/LoginView.vue"),
  meta: {
    guestOnly: true,
    hideFooter: true
  }
},
{
  path: "/register",
  name: "register",
  component: () => import("@/views/RegisterView.vue"),
  meta: {
    guestOnly: true,
    hideFooter: true
  }
},

{
  path: "/forgot-password",
  name: "forgot-password",
  component: () =>
    import(
      "@/views/ForgotPasswordView.vue"
    )
},
{
  path: "/reset-password",
  name: "reset-password",
  component: () =>
    import(
      "@/views/ResetPasswordView.vue"
    )
},
  {
    path: '/office/:id',
    name: 'office-detail',
    component: () => import('@/views/OfficeDetailView.vue'),
    meta: { requiresAuth: false }
  },

  {
  path: '/coworking-spaces',
  name: 'coworking-spaces',
  component: () => import('@/views/CoworkingSpacesView.vue'),
  meta: { requiresAuth: false }
},
{
  path: '/meeting-rooms',
  name: 'meeting-rooms',
  component: () => import('@/views/MeetingRoomsView.vue'),
  meta: { requiresAuth: false }
},
{
  path: '/virtual-offices',
  name: 'virtual-offices',
  component: () => import('@/views/VirtualOfficesView.vue'),
  meta: { requiresAuth: false }
},
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/views/DashboardView.vue'),
    meta: { requiresAuth: true }
  },

  {
  path: "/favorites",
  name: "favorites",
  component: () => import("@/views/FavoritesView.vue"),
  meta: {
    requiresAuth: true
  }
},
{
  path: "/admin",
  component: () => import("@/layouts/AdminLayout.vue"),
  meta: {
    requiresAuth: true,
    requiresAdmin: true,
  },

  children: [
    {
      path: "",
      name: "admin-dashboard",
      component: () => import("@/views/admin/AdminDashboardView.vue"),
    },
    {
  path: "users",
  name: "admin-users",
  component: () => import("@/views/admin/AdminUsersView.vue"),

},
{
    path: "offices",
    name: "admin-offices",
    component: () => import("@/views/admin/AdminOfficeView.vue"),
},

{
  path: "bookings",
  name: "admin-bookings",
  component: () =>
    import("@/views/admin/AdminBookingsView.vue"),
},
{
  path: "payments",
  name: "admin-payments",
  component: () =>
    import("@/views/admin/AdminPaymentsView.vue"),
},
{
  path: "contacts",
  name: "admin-contacts",
  component: () =>
    import("@/views/admin/AdminContactsView.vue"),
},
{
  path: "reviews",
  name: "admin-reviews",
  component: () =>
    import("@/views/admin/AdminReviewsView.vue"),
},

{
  path: "notifications",
  name: "admin-notifications",
  component: () =>
    import("@/views/admin/AdminNotificationsView.vue"),
},
{
  path: "analytics",
  name: "admin-analytics",
  component: () =>
    import("@/views/admin/AdminAnalyticsView.vue"),
},
{
  path: "site-settings",
  name: "admin-site-settings",
  component: () =>
    import("@/views/admin/AdminSiteSettingsView.vue"),
},
{
  path: "settings",
  name: "admin-settings",
  component: () =>
    import("@/views/admin/AdminSettingsView.vue"),
},

  ]
},
  
  {
  path: '/privacy-policy',
  name: 'privacy-policy',
  component: PrivacyPolicyView,
  meta: { requiresAuth: false }
},
{
  path: '/terms',
  name: 'terms',
  component: TermsView,
  meta: { requiresAuth: false }
},
{
  path: '/cookies-policy',
  name: 'cookies-policy',
  component: CookiesPolicyView,
  meta: { requiresAuth: false }
},
{
  path: '/confidentiality',
  name: 'confidentiality',
  component: ConfidentialityView,
  meta: { requiresAuth: false }
},
{
  path: '/about',
  name: 'about',
  component: AboutView,
  meta: { requiresAuth: false }
},
{
  path: '/how-booking-works',
  name: 'how-booking-works',
  component: HowBookingWorksView,
  meta: { requiresAuth: false }
},
{
  path: '/pricing',
  name: 'pricing',
  component: PricingView,
  meta: { requiresAuth: false }
},
{
  path: '/faqs',
  name: 'faqs',
  component: FAQsView,
  meta: { requiresAuth: false }
},
{
  path: '/contact',
  name: 'contact',
  component: ContactView,
  meta: { requiresAuth: false }
},
  
  // Fallback redirect
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    return { top: 0 }
  }
})

// Navigation Guard
// Navigation Guard
router.beforeEach((to) => {
  const authStore = useAuthStore()

  const isAuthenticated = authStore.isAuthenticated
  const isAdmin = authStore.isAdmin

  const requiresAuth = to.matched.some(
    record => record.meta.requiresAuth
  )

  const requiresAdmin = to.matched.some(
    record => record.meta.requiresAdmin
  )

  const guestOnly = to.matched.some(
    record => record.meta.guestOnly
  )


  /* ==========================================
     1. Protected route without authentication
  ========================================== */

  if (requiresAuth && !isAuthenticated) {
    return {
      name: "login",
      query: {
        redirect: to.fullPath
      }
    }
  }


  /* ==========================================
     2. Normal user trying to access Admin
  ========================================== */

  if (
    requiresAdmin &&
    (!isAuthenticated || !isAdmin)
  ) {
    return {
      name: "home"
    }
  }


  /* ==========================================
     3. Admin must stay inside Admin Panel
  ========================================== */

  if (
    isAuthenticated &&
    isAdmin &&
    !requiresAdmin
  ) {
    return {
      name: "admin-dashboard"
    }
  }


  /* ==========================================
     4. Logged-in normal user opening
        login/register
  ========================================== */

  if (
    guestOnly &&
    isAuthenticated
  ) {
    return {
      name: "dashboard"
    }
  }


  return true
})

export default router
