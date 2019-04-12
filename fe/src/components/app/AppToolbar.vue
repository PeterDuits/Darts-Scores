<template>
  <v-toolbar flat color="white" class="primary--text">
    <v-toolbar-title>{{ this.$route.name }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items v-if="$store.state.user.loggedIn">
      <v-btn flat color="primary" disabled>profile</v-btn>
      <v-btn flat color="primary">{{ username }}</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "AppToolbar",
  data: () => ({
    title: "Title"
  }),
  computed: {
    ...mapGetters("user", ["username"])
  }
};
</script>
