import { defineStore } from "pinia";
import { ref } from "vue";
import api from "@/services/api";

export const useNotificationStore = defineStore(
  "notification",
  () => {

    const notifications = ref([]);

    const unreadCount = ref(0);

    const totalNotifications = ref(0);

    const currentPage = ref(1);

    const totalPages = ref(1);

    const pageSize = ref(6);

    const loading = ref(false);


    const fetchNotifications = async (
      page = 1
    ) => {

      loading.value = true;

      try {

        const res = await api.get(
          "notifications/",
          {
            params: {
              page
            }
          }
        );

        const raw = res.data;


        if (
          raw &&
          Array.isArray(raw.results)
        ) {

          notifications.value =
            raw.results;

          totalNotifications.value =
            raw.count ?? 0;

          currentPage.value = page;

          totalPages.value =
            Math.max(
              1,
              Math.ceil(
                totalNotifications.value /
                pageSize.value
              )
            );

        } else {

          notifications.value =
            Array.isArray(raw)
              ? raw
              : [];

          totalNotifications.value =
            notifications.value.length;

          currentPage.value = 1;

          totalPages.value = 1;

        }


        const unread = await api.get(
          "notifications/unread-count/"
        );

        unreadCount.value =
          unread.data.unread_count ?? 0;

      } catch (err) {

        console.error(
          "Failed to fetch notifications:",
          err
        );

      } finally {

        loading.value = false;

      }

    };


    const markAsRead = async (
      notification
    ) => {

      if (notification.is_read) {
        return;
      }

      try {

        await api.patch(
          `notifications/read/${notification.id}/`,
          {
            is_read: true
          }
        );

        notification.is_read = true;

        if (unreadCount.value > 0) {
          unreadCount.value--;
        }

      } catch (err) {

        console.error(err);

      }

    };


    const markAllAsRead = async () => {

      try {

        await api.patch(
          "notifications/mark-all-read/"
        );

        notifications.value.forEach(
          notification => {
            notification.is_read = true;
          }
        );

        unreadCount.value = 0;

      } catch (err) {

        console.error(err);

      }

    };


    return {

      notifications,

      unreadCount,

      totalNotifications,

      currentPage,

      totalPages,

      pageSize,

      loading,

      fetchNotifications,

      markAsRead,

      markAllAsRead

    };

  }
);