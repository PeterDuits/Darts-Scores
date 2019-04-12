<template>
  <v-container class="splash pt-5" fluid fill-height text-xs-center>
    <v-layout column>
      <v-flex xs12>
        <h1 class="display-2 mb-4">{{ title }}</h1>
        <span class="subheading font-italic">{{ subtext }}</span>
      </v-flex>
      <v-spacer></v-spacer>
      <v-flex xs12>
        <v-btn :to="{name: 'register'}" large color="primary" depressed>{{ button }}</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    title: "Foosball",
    subtext:
      "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt ",
    button: "Get started"
  })
};
</script>

<style lang="scss" scoped>
.splash {
  background: #edf8ef;
}
</style>
