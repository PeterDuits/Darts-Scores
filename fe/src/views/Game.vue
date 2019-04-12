<template>
    <v-container fluid fill-height class="field green">
        <v-dialog v-model="endGameDialog">
            <end-game/>
        </v-dialog>

        <v-layout row wrap justify-space-between fill-height>
            <v-flex d-flex xs12>
                <v-layout row wrap justify-space-between>
                    <v-flex xs5 :order-xs2="team1Swap" class="playerContainer">
                        <player
                            v-if="$store.state.game.teams.home.players[0]"
                            :player="$store.state.game.teams.home.players[0]"
                            team="1"
                        />
                    </v-flex>

                    <v-flex xs5 :order-xs1="team1Swap" class="playerContainer">
                        <player
                            v-if="$store.state.game.teams.home.players[1]"
                            :player="$store.state.game.teams.home.players[1]"
                            team="1"
                        />
                    </v-flex>
                </v-layout>
            </v-flex>

            <v-flex d-flex text-xs-center xs12>
                <v-layout column justify-space-around>
                    <v-flex xs12>
                        <span class="timer headline">{{ humanTime }}</span>
                    </v-flex>
                    <v-flex xs12>
                        <span class="score display-2">{{ score.home }} - {{ score.away }}</span>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex d-flex xs12>
                <v-layout row wrap align-end justify-space-between>
                    <v-flex xs5 :order-xs2="team2Swap">
                        <player
                            v-if="$store.state.game.teams.away.players[1]"
                            :player="$store.state.game.teams.away.players[1]"
                            team="2"
                        />
                    </v-flex>

                    <v-flex xs5 :order-xs1="team2Swap">
                        <player
                            v-if="$store.state.game.teams.away.players[0]"
                            :player="$store.state.game.teams.away.players[0]"
                            team="2"
                        />
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
        <v-speed-dial
            transition="slide-x-reverse-transition"
            centered
            right
            absolute
            v-model="speedDial"
            direction="left"
        >
            <template v-slot:activator>
                <v-btn fab dark>
                    <v-icon>menu</v-icon>
                    <v-icon>close</v-icon>
                </v-btn>
            </template>
            <v-btn fab small>
                <v-icon>pause</v-icon>
            </v-btn>
            <v-btn fab small>
                <v-icon>stop</v-icon>
            </v-btn>
            <v-btn fab small>
                <v-icon>undo</v-icon>
            </v-btn>
        </v-speed-dial>
    </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

import Player from "@/components/game/Player";
import EndGame from "@/components/game/EndGame";

export default {
    name: "Game",
    data: () => ({
        unit: 50,
        time: 0,
        timer: null,
        endGameDialog: false,
        speedDial: false
    }),
    watch: {
        score: {
            handler: function(newValue) {
                if (newValue.home === 10 || newValue.away === 10) {
                    this.endGame();
                }
            },
            deep: true
        }
    },
    methods: {
        ...mapActions("game", ["scoreGoal", "setTimePlayed"]),
        ...mapActions("statistics", ["setTeam", "setStartTime", "setTime"]),
        endGame() {
            this.endGameDialog = true;
            this.setTimePlayed(this.time);
        },
        pauseGame() {
            this.timer = null;
        }
    },
    computed: {
        ...mapGetters("game", ["teamHome", "teamAway", "score"]),
        ...mapGetters("statistics", ["teams"]),
        team1() {
            return this.$store.state.statistics.teams;
        },
        team2() {
            return this.$store.state.statistics.teams;
        },
        team1Swap() {
            let swap = false;

            this.score.home >= 5 ? (swap = true) : (swap = false);
            return swap;
        },
        team2Swap() {
            let swap = false;
            this.score.away >= 5 ? (swap = true) : (swap = false);
            return swap;
        },
        humanTime() {
            let minutes = Math.floor(this.time / 60);
            let seconds = this.time - minutes * 60;

            if (minutes < 10) {
                minutes = `0${minutes}`;
            }

            if (seconds < 10) {
                seconds = `0${seconds}`;
            }

            return `${minutes}:${seconds}`;
        }
    },
    mounted() {
        this.setStartTime();

        const team1 = [
            {
                name: this.teamHome[0],
                startingPosition: "offense"
            },
            {
                name: this.teamHome[1],
                startingPosition: "defense"
            }
        ];

        const team2 = [
            {
                name: this.teamAway[0],
                startingPosition: "offense"
            },
            {
                name: this.teamAway[1],
                startingPosition: "defense"
            }
        ];

        this.setTeam({
            players: team1,
            team: 0
        });

        this.setTeam({
            players: team2,
            team: 1
        });

        this.timer = setInterval(() => {
            this.time++;
        }, 1000);
    },
    components: { Player, EndGame }
};
</script>

<style lang="scss">
.field {
}

.player {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.player-name {
    font-size: 21px;
}

.player-goals {
    margin-left: auto;
    font-size: 21px;
}
</style>
