<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12>
                <v-list>
                    <v-list-tile>
                        <v-list-tile-content>
                            <v-subheader>Team 1</v-subheader>
                        </v-list-tile-content>
                    </v-list-tile>
                    <draggable
                        :options="{animation: 150}"
                        v-model="team1"
                        group="players"
                        @start="drag=true"
                        @end="drag=false"
                    >
                        <template v-for="(player, index) in team1">
                            <player
                                :player="player"
                                :position="index === 0 ? 'offense' : 'defense' "
                                :key="index"
                            ></player>
                        </template>
                    </draggable>
                </v-list>
            </v-flex>
            <v-flex xs12>
                <v-divider></v-divider>
            </v-flex>
            <v-flex xs12>
                <v-list>
                    <v-list-tile>
                        <v-list-tile-content>
                            <v-subheader>Team 2</v-subheader>
                        </v-list-tile-content>
                    </v-list-tile>
                    <draggable
                        :options="{animation:
                        150}"
                        v-model="team2"
                        group="players"
                        @start="drag=true"
                        @end="drag=false"
                    >
                        <template v-for="(player, index) in team2">
                            <player
                                :player="player"
                                :position="index === 0 ? 'offense' : 'defense' "
                                :key="index"
                            ></player>
                        </template>
                    </draggable>
                </v-list>
            </v-flex>
            <v-flex xs12 text-xs-right>
                <v-btn @click="randomize" flat color="primary">
                    <v-icon left>refresh</v-icon>randomize
                </v-btn>
            </v-flex>
            <v-flex xs12>
                <v-btn
                    @click="nextStep"
                    large
                    block
                    depressed
                    color="primary"
                    :disabled="!canPlay"
                >Start</v-btn>
            </v-flex>
            <v-fade-transition>
                <v-flex text-xs-center v-if="!canPlay" xs12>
                    <span class="caption">please assign 2 players to each team</span>
                </v-flex>
            </v-fade-transition>
        </v-layout>

        <v-footer app fixed color="white">
            <v-btn @click="previousStep" color="primary" flat icon>
                <v-icon>arrow_back</v-icon>
            </v-btn>
        </v-footer>
    </v-container>
</template>

<script>
import Draggable from "vuedraggable";
import { mapGetters, mapActions } from "vuex";
import _ from "lodash";

import Player from "@/components/setup/Player";

export default {
    name: "Setup",
    data: () => ({
        team1: [],
        team2: []
    }),
    beforeMount() {
        this.team1.push(this.players[0], this.players[1]);
        this.team2.push(this.players[2], this.players[3]);
    },
    watch: {
        team1(val) {
            this.setTeam({
                team: "home",
                players: val
            });
        },
        team2(val) {
            this.setTeam({
                team: "away",
                players: val
            });
        }
    },
    methods: {
        ...mapActions("game", ["setTeam"]),
        ...mapActions(["setStep"]),
        nextStep() {
            this.setStep(3).then(() => {
                this.$router.push({ name: "CoinFlip" });
            });
        },
        previousStep() {
            this.setStep(1).then(() => {
                this.$router.push({ name: "FindPlayers" });
            });
        },
        randomize() {
            this.team1 = [];
            this.team2 = [];

            let playerlist = [];
            this.players.forEach(player => {
                playerlist.push(player);
            });

            playerlist = _.shuffle(playerlist);

            this.team1.push(playerlist[0], playerlist[1]);
            this.team2.push(playerlist[2], playerlist[3]);
        }
    },
    computed: {
        ...mapGetters("game", ["players", "teamHome", "teamAway"]),
        canPlay() {
            if (
                this.teamHome.players.length == 2 &&
                this.teamAway.players.length == 2
            ) {
                return true;
            } else {
                return false;
            }
        }
    },
    components: { Draggable, Player }
};
</script>
