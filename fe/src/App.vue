<template>
  <v-app>
    <app-toolbar v-if="!this.$route.meta.hideToolbar"/>
    <router-view></router-view>
  </v-app>
</template>

<script>
import AppToolbar from "@/components/app/AppToolbar.vue";

export default {
  name: "App",
  components: {
    AppToolbar
  }
};
</script>
