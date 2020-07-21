import Vue from "vue";
import VueRouter from "vue-router";
import SignIn from "../views/SignIn.vue";
import Goal from "../views/goal/Goal.vue";
import MyPage from "../views/MyPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/signin",
    component: SignIn
  },
    {
    path: "/mypage",
    name: "mypage",
    component: MyPage
  },
  {
    path: "/mypage/goal/:id",
    name: "goal",
    component: Goal,
    props: true
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
