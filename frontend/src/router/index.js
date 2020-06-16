import Vue from "vue";
import VueRouter from "vue-router";
import CreateGoal from "@/views/CreateGoal/CreateGoal.vue";
import SignIn from "@/views/SignIn/signin.vue";
import Goal from "../views/goal/Goal.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: CreateGoal,
  },
  {
    path: "/sign-in",
    component: SignIn,
  },
  {
    path: "/goal",
    component: Goal,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
