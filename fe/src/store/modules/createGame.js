export default {
  state: {
    step: 1,
    players: []
  },
  mutations: {
    setStep(state, step) {
      state.step = step;
    }
  },
  actions: {
    setStep(context, step) {
      context.commit("setStep", step);
    }
  },
  getters: {
    step(state) {
      return state.step;
    }
  }
};
