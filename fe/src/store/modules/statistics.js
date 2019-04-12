export default {
  namespaced: true,
  state: {
    startedAt: Date,
    time: 0,
    teams: [
      {
        home: true,
        switched: false,
        score: 0,
        players: []
      },
      {
        home: false,
        switched: false,
        score: 0,
        players: []
      }
    ]
  },
  mutations: {
    setStartTime: state => {
      state.startedAt = Date.now();
    },
    setTimePlayed: (state, payload) => {
      state.time = payload;
    },
    switchPlayers: (state, team) => {
      state.teams[team].switched = true;
      state.teams[team].players = state.teams.players.reverse();
    },
    setTeam: (state, payload) => {
      payload.players.forEach(player => {
        state.teams[payload.team].players.push({
          name: player.name,
          startingPosition: player.startingPosition,
          goals: []
        });
      });
    },
    scoreGoal: (state, payload) => {
      state.teams.forEach(team => {
        team.players.forEach(player => {
          if (player.name === payload.playername) {
            player.goals.push({
              timestamp: payload.goal.timestamp,
              position: payload.goal.position,
              super: payload.goal.super
            });

            team.score++;

            const indexTeam = state.teams.indexOf(team);

            if (payload.goal.super) {
              if (indexTeam === 0 && state.teams[1].score > 0) {
                state.teams[1].score--;
              } else {
                if (state.teams[0].score > 0) {
                  state.teams[0].score--;
                }
              }
            }
          }
        });
      });
    }
  },
  actions: {
    setTeam(context, payload) {
      context.commit("setTeam", payload);
    },
    setStartTime(context) {
      context.commit("setStartTime");
    },
    setTime(context, payload) {
      context.commit("setTimePlayed", payload);
    },
    scoreGoal(context, payload) {
      context.commit("scoreGoal", payload);
    }
  },
  getters: {
    teams(state) {
      return state.teams;
    },
    score(state) {
      return {
        home: state.teams[0].score,
        away: state.teams[1].score
      };
    }
  }
};
