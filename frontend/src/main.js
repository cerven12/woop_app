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
import Cookies from "js-cookie";
import draggable from "vuedraggable";
import VueFormWizard from 'vue-form-wizard';
import 'vue-form-wizard/dist/vue-form-wizard.min.css';

Vue.config.productionTip = false;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
Vue.use(VueAxios, axios);
Vue.use(VueFormWizard);
Vue.use(mavonEditor);

new Vue({
  router,
  store,
  draggable,
  Cookies,
  vuetify,
  jwt_decode,
  render: (h) => h(App),
}).$mount("#app");
