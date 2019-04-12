<template>
  <v-list-tile :key="match.date">
    <v-list-tile-content>
      <v-list-tile-title>{{ match.teamHome[0].username }}/{{ match.teamHome[1].username }} VS {{ match.teamAway[0].username }}/{{ match.teamAway[1].username }}</v-list-tile-title>
      <v-list-tile-sub-title
        class="text--primary"
      >{{ match.teamHome[0].goals + match.teamHome[1].goals }} - {{ match.teamAway[0].goals + match.teamAway[1].goals }}</v-list-tile-sub-title>
    </v-list-tile-content>

    <v-list-tile-action>
      <v-list-tile-action-text>{{ match.date }}</v-list-tile-action-text>
    </v-list-tile-action>
  </v-list-tile>
</template>

<script>
export default {
  name: "Match",
  props: ["match"]
};
</script>
