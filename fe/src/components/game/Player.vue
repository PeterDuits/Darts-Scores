<template>
  <v-menu
    v-model="klinkerMenu"
    transition="scale-transition"
    origin="center center"
    :top="top"
    :bottom="bottom"
    offset-y
  >
    <template v-slot:activator="{ on }">
      <v-card ripple v-on="on" flat :color="teamColor">
        <div class="player pa-3">
          <v-avatar size="28" class="mr-3" color="white">
            <v-icon color="primary">person</v-icon>
          </v-avatar>

          <span class="font-weight-bold player-name">{{ player.name }}</span>
          <span class="player-goals">{{ player.goals.length }}</span>
        </div>
      </v-card>
    </template>
    <v-list class="pb-0 elevation-0">
      <v-list-tile color="primary" ripple @click="goal">
        <v-list-tile-action>
          <v-icon color="primary">gps_fixed</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title class="title">normal goal</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile color="primary" ripple @click="superGoal">
        <v-list-tile-action>
          <v-icon color="red">gps_fixed</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title class="title">Super goal</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-progress-linear class="ma-0" v-model="klinkerTimer"></v-progress-linear>
    </v-list>
  </v-menu>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Player",
  props: ["player", "team"],
  data: () => ({
    klinkerMenu: false,
    klinkerTimer: 50
  }),
  methods: {
    ...mapActions("game", ["scoreGoal"]),
    goal() {
      let team = "away";
      if (this.team === "1") team = "home";

      this.scoreGoal({
        team: team,
        player: {
          name: this.player.name,
          id: this.player.id
        },
        goal: {
          timestamp: 12,
          position: "offense",
          super: false
        }
      });
    },
    superGoal() {
      let team = "away";
      if (this.team === "1") team = "home";

      this.scoreGoal({
        team: team,
        player: {
          name: this.player.name,
          id: this.player.id
        },
        goal: {
          timestamp: 12,
          position: "offense",
          super: true
        }
      });
    }
  },
  computed: {
    teamColor() {
      if (this.team === "1") {
        return "white";
      } else {
        return "orange lighten-1";
      }
    },
    bottom() {
      if (this.team === "1") {
        return true;
      } else {
        return false;
      }
    },

    top() {
      if (this.team === "2") {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>

<style>
</style>
