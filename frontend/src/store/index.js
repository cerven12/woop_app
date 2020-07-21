import Vue from "vue";
import Vuex from "vuex";
import Cookies from "js-cookie";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    url: "http://127.0.0.1:8000/api/v1/goals/",
    endpoints: {
      obtainSessionID: "http://127.0.0.1:8000/api/v1/auth/jwt/create/",
    },
    sessionId: "",
  },

  mutations: {
    setSessionId: function(state, newSessionId) {
      state.sessionId = newSessionId.access;
      localStorage.setItem("access", newSessionId.access);
    },
  },
});
