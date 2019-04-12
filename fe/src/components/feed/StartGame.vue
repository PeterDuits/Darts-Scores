<template>
  <v-card flat color="green lighten-4">
    <v-responsive :aspect-ratio="2/1">
      <v-container text-xs-center fill-height>
        <v-layout>
          <v-flex xs12>
            <span class="headline">{{ headline }}</span>
            <v-btn @click="$emit('startGame')" depressed large block color="primary">{{ button }}</v-btn>
          </v-flex>
        </v-layout>
      </v-container>
    </v-responsive>
  </v-card>
</template>

<script>
export default {
  name: "StartNewGame",
  data: () => ({
    headline: "Nobody is playing",
    button: "Start a game"
  })
};
</script>
