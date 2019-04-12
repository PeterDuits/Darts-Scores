export default {
  namespaced: "user",
  state: {
    username: "",
    guest: false,
    token: "",
    loggedIn: false
  },
  getters: {
    username: state => {
      return state.username;
    }
  },
  mutations: {
    login(state, payload) {
      state.loggedIn = true;
      state.username = payload.username;
      state.token = payload.token;
      if (this.username === "guest") {
        state.guest = true;
      }
    }
  },
  actions: {
    login(context, payload) {
      context.commit("login", payload);
    }
  }
};
