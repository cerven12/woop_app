import Vue from "vue";
import VueRouter from "vue-router";
import CreateGoal from "@/views/CreateGoal.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: CreateGoal,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
