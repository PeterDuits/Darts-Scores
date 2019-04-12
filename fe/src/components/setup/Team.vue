<template>
  <v-list>
    <v-list-tile>
      <v-list-tile-content>
        <v-subheader>{{ teamName }}</v-subheader>
      </v-list-tile-content>
    </v-list-tile>
    <draggable v-model="list" group="players" @start="drag=true" @end="drag=false">
      <template v-for="(player, index) in players">
        <player :player="player" :position="index === 0 ? 'offense' : 'defense' " :key="player"></player>
      </template>
    </draggable>
  </v-list>
</template>

<script>
import Draggable from "vuedraggable";

import Player from "@/components/setup/Player";

export default {
  name: "Team",
  props: ["teamName", "players"],
  data: () => ({
    team: []
  }),
  computed: {
    list: {
      get: function() {
        return this.players;
      },
      set: function(newValue) {
        this.$emit("changed", newValue);
      }
    }
  },
  components: { Draggable, Player }
};
</script>
