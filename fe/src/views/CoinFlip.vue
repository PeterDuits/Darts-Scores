<template>
  <v-container fill-height fluid text-xs-center>
    <v-layout row wrap>
      <v-flex xs12>
        <h1 class="title">The coinflip</h1>
      </v-flex>
      <v-flex xs12 v-if="flipped">
        <span class="display-2">{{ result }}</span>
      </v-flex>
      <v-flex xs12 v-if="loading">
        <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
      </v-flex>
      <v-flex xs12>
        <v-btn flat color="primary" @click="flip">Flip a coin</v-btn>
        <v-btn :to="{name: 'Game'}" large block depressed color="primary">PLAY!</v-btn>
      </v-flex>
    </v-layout>

    <v-footer app fixed color="white">
      <v-btn :to="{name: 'Setup'}" color="primary" flat icon>
        <v-icon>arrow_back</v-icon>
      </v-btn>
    </v-footer>
  </v-container>
</template>

<script>
import _ from "lodash";

export default {
  data: () => ({
    flipped: false,
    result: "head",
    loading: false
  }),
  methods: {
    flip() {
      const results = ["heads", "tails"];

      this.flipped = false;
      this.loading = true;

      setTimeout(() => {
        this.flipped = true;
        this.loading = false;
        this.result = _.sample(results);
      }, 1000);
    }
  }
};
</script>

<style lang="scss">
</style>
