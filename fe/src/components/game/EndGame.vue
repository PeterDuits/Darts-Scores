<template>
    <v-card flat>
        <v-card-title primary-title>
            <span class="title">Game has ended!</span>
        </v-card-title>
        <div class="scoreboard">
            <div class="team team--home">
                <div class="player" v-for="player in teams.home.players" :key="player.id">
                    <span class="player__name">{{ player.name }}</span>
                    <ul class="player__goals" v-if="player.goals && player.goals.length > 0">
                        <li
                            class="player__goal"
                            v-for="goal in player.goals"
                            :key="goal.timestamp"
                        >{{ goal.timestamp }}'</li>
                    </ul>
                </div>
            </div>
            <span class="score">{{ score.home }} - {{ score.away }}</span>
            <div class="team team--away">
                <div class="player" v-for="player in teams.away.players" :key="player.id">
                    <ul class="player__goals" v-if="player.goals && player.goals.length > 0">
                        <li
                            class="player__goal"
                            v-for="goal in player.goals"
                            :key="goal.timestamp"
                        >{{ goal.timestamp }}'</li>
                    </ul>
                    <span class="player__name">{{ player.name }}</span>
                </div>
            </div>
        </div>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="red" flat>Disagree</v-btn>
            <v-btn color="success" flat>Confirm</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import { mapGetters } from "vuex";

export default {
    name: "EndGame",
    computed: {
        ...mapGetters("game", ["teams", "score"])
    }
};
</script>

<style lang="scss">
.scoreboard {
    display: flex;
    background: #4caf50;
    color: white;
    text-align: center;
    flex-direction: row;
    justify-content: space-between;
    padding: 24px 16px;

    .score {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        width: 40%;
        display: flex;
        justify-content: center;
    }

    .team {
        display: flex;
        flex: 0 1 30%;
        flex-direction: column;
        width: 30%;

        &--home {
        }

        &--away {
            text-align: right;
            align-items: flex-end;
        }
    }

    .player {
        display: flex;
        flex-direction: row;
        padding: 10px;

        &__name {
            font-weight: bold;
        }

        &__goals {
            padding: 0;
            margin: 0;
            list-style-type: none;
            display: flex;
            flex-direction: row;
        }

        &__goal {
            margin: 0 8px;
        }
    }
}
</style>
