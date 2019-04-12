import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import register from "./modules/register";
import user from "./modules/user";
import game from "./modules/game";
import createGame from "./modules/createGame";
import statistics from "./modules/statistics";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState],
  state: {},
  mutations: {},
  actions: {},
  modules: {
    register,
    user,
    createGame,
    game,
    statistics
  }
});
