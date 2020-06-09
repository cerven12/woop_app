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
import Cookies from 'js-cookie';


Vue.config.productionTip = false;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
Vue.use(VueAxios, axios);
Vue.use(mavonEditor);

new Vue({
  router,
  store,
  Cookies,
  vuetify,
  jwt_decode,
  render: (h) => h(App),
}).$mount("#app");
