import { createApp } from "vue";
import { createPinia } from "pinia";

import router from "./router";
import App from "./App.vue";

import "./style.css";

import { useAuthStore } from "./stores/auth";

import { Toaster } from "vue-sonner";
import "vue-sonner/style.css";

import VueTelInput from "vue-tel-input";
import "vue-tel-input/vue-tel-input.css";


const app = createApp(App);

const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(VueTelInput);


// Listen for global logout events from axios client
window.addEventListener("auth-logout", () => {
  const authStore = useAuthStore();

  authStore.logout();

  router.push({
    name: "login"
  });
});


app.mount("#app");