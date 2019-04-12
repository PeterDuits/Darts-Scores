<template>
  <v-list two-line>
    <template v-for="(match, index) in matches">
      <match :match="match" :key="match.date"/>
      <v-divider v-if="index < matches.length - 1" :key="index"></v-divider>
    </template>
  </v-list>
</template>

<script>
import Match from "./Match.vue";

export default {
  name: "MatchHistory",
  data: () => ({
    matches: [
      {
        date: Date.now(),
        teamHome: [
          {
            username: "Jimme",
            goals: 5
          },
          {
            username: "Roy",
            goals: 5
          }
        ],
        teamAway: [
          {
            username: "Pim",
            goals: 0
          },
          {
            username: "Neal",
            goals: 0
          }
        ]
      }
    ]
  }),
  components: { Match }
};
</script>
