<template>
  <v-list-tile avatar :key="player.id">
    <v-list-tile-action>
      <v-icon size="14" color="grey">drag_handle</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title class="title">
        <span class="player-name text--primary">{{player.name}}</span>
      </v-list-tile-title>
    </v-list-tile-content>
    <v-list-tile-action>
      <span class="caption">{{ position }}</span>
    </v-list-tile-action>
  </v-list-tile>
</template>

<script>
export default {
  name: "Player",
  props: ["player", "position"]
};
</script>

<style lang="scss" scoped>
.player-name {
  text-transform: capitalize;
}
</style>
