<template>
  <div>
    <start-game @startGame="submit"/>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12>
          <v-subheader>Match history</v-subheader>
        </v-flex>
        <v-flex xs12>
          <match-history/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import MatchHistory from "@/components/feed/MatchHistory";
import StartGame from "@/components/feed/StartGame";

export default {
  name: "UserFeed",
  data: () => ({
    headline: "Nobody is playing"
  }),
  methods: {
    submit() {
      console.log("Lekker spelen");
      this.$router.push({ name: "FindPlayers" });
    }
  },
  components: { MatchHistory, StartGame }
};
</script>

