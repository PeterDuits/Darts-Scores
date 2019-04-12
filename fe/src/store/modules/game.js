import _ from "lodash";

export default {
  namespaced: true,
  state: {
    createdBy: "",
    players: [],
    timePlayed: undefined,
    teams: {
      home: {
        score: 0,
        players: []
      },
      away: {
        score: 0,
        players: []
      }
    }
  },
  mutations: {
    setCreatedBy(state, payload) {
      state.createdBy = payload;
    },
    addPlayer(state, payload) {
      const player = {
        name: payload.username,
        id: payload.id,
        goals: []
      };
      state.players.push(player);
    },
    removePlayer(state, payload) {
      state.players.splice(state.players.indexOf(payload), 1);
    },
    setTeam(state, payload) {
      state.teams[payload.team].players = payload.players;
    },
    scoreGoal(state, payload) {
      const { player, goal, team } = payload;

      const playerIndex = _.findIndex(state.teams[team].players, {
        id: player.id
      });
      state.teams[team].players[playerIndex].goals.push(goal);

      state.teams[team].score++;

      if (goal.super) {
        if (team === "home") {
          if (state.teams.away.score === 0) return;
          state.teams.away.score--;
        } else {
          if (state.teams.home.score === 0) return;
          state.teams.home.score--;
        }
      }
    },
    setTimePlayed(state, payload) {
      state.timePlayed = payload;
    }
  },
  actions: {
    setCreatedBy(context, payload) {
      context.commit("setCreatedBy", payload);
    },
    addPlayer(context, payload) {
      context.commit("addPlayer", payload);
    },
    removePlayer(context, payload) {
      context.commit("removePlayer", payload);
    },
    setTeam(context, payload) {
      context.commit("setTeam", payload);
    },
    scoreGoal(context, payload) {
      context.commit("scoreGoal", payload);
    },
    setTimePlayed(context, payload) {
      context.commit("setTimePlayed", payload);
    }
  },
  getters: {
    players(state) {
      return state.players;
    },
    teams(state) {
      return state.teams;
    },
    teamHome(state) {
      return state.teams.home;
    },
    teamAway(state) {
      return state.teams.away;
    },
    timePlayed(state) {
      return state.timePlayed;
    },
    score(state) {
      return {
        home: state.teams.home.score,
        away: state.teams.away.score
      };
    }
  }
};
