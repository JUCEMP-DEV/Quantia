import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    accessProfile: "",
  }),

  actions: {
    setUser(user) {
      this.user = user;
    },

    setAccessProfile(profile) {
      this.accessProfile = profile;
    },

    logout() {
      this.user = null;
      this.accessProfile = "";
    },
  },
});