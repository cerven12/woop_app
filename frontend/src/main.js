import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueAxios from "vue-axios";
import jwt_decode from "jwt-decode";
import "./assets/sass/style.scss";
import mavonEditor from "mavon-editor";
import "mavon-editor/dist/css/index.css";

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);
Vue.use(mavonEditor);

new Vue({
  router,
  store,
  vuetify,
  jwt_decode,
  render: (h) => h(App),
}).$mount("#app");
