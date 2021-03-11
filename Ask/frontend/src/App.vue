<template>
  <div class="container">
      <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import { apiService } from "@/common/api.service.js";

export default {
  name: "App",
  components: {
    Navbar
  },
  methods: {
    getUser() {
      let endpoint = "/api/user/";
      apiService(endpoint)
        .then( data => {
          window.localStorage.setItem("username", data.username);
        })
    }
  },
  created() {
    this.getUser();
  }
}
</script>
