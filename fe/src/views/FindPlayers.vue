<template>
  <div>
    <v-container>
      <v-layout>
        <v-flex xs12>
          <h1 class="headline">Select players</h1>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container grid-list-xs>
      <v-layout row wrap>
        <v-flex d-flex xs3 v-for="player in playerlist" :key="player.username">
          <v-card
            @click="select(player)"
            ripple
            :color="player.selected ? 'primary lighten-1' : 'white' "
            flat
          >
            <v-responsive :aspect-ratio="1/1">
              <v-container text-xs-center>
                <v-layout column>
                  <v-flex xs12>
                    <v-avatar size="32" color="pink"></v-avatar>
                  </v-flex>
                  <v-flex xs12>
                    <span class="caption font-weight-bold">{{ player.username }}</span>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-responsive>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container>
      <v-layout row wrap>
        <v-flex xs12>
          <v-btn :disabled="!ready" color="primary" @click="submit" large depressed block>Play</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
    <v-footer app fixed color="white">
      <v-btn :to="{name: 'Feed'}" color="primary" flat icon>
        <v-icon>arrow_back</v-icon>
      </v-btn>
    </v-footer>
  </div>
</template>

<script>
import axios from "axios";

import { mapActions, mapGetters } from "vuex";

export default {
  name: "FindPlayers",
  data: () => ({
    playerbase: [],
    selected: []
  }),
  beforeMount() {
    axios({
      method: "get",
      url: `${process.env.VUE_APP_API_URL}/players`
    }).then(players => {
      this.playerbase = players.data;
    });
  },
  methods: {
    ...mapActions("game", ["addPlayer", "removePlayer"]),
    ...mapActions(["setStep"]),
    select(player) {
      if (this.selected.includes(player.id)) {
        this.removePlayer(player);
        this.selected.splice(this.selected.indexOf(player.id), 1);
      } else {
        this.addPlayer(player).then(() => {
          this.selected.push(player.id);
        });
      }
    },
    submit() {
      this.setStep(2).then(() => {
        this.$router.push({ name: "Setup" });
      });
    },
    previousStep() {
      this.setStep(1).then(() => {
        this.$router.push({ name: "Feed" });
      });
    }
  },
  mounted() {},
  computed: {
    ...mapGetters("game", ["players", "teams"]),
    ready() {
      if (this.players.length !== 4) {
        return false;
      } else {
        return true;
      }
    },
    playerlist() {
      const list = [];

      this.playerbase.forEach(player => {
        let selected = false;

        if (this.selected.includes(player.uuid)) {
          selected = true;
        }

        list.push({
          username: player.username,
          id: player.uuid,
          selected: selected
        });
      });

      return list;
    }
  }
};
</script>

