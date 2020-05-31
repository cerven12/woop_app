<template>
  <div id="app">
    <link
      href="https://fonts.googleapis.com/earlyaccess/nikukyu.css"
      rel="stylesheet"
    />
    <div id="container">
      <div id="side"><SideBar></SideBar></div>
      <div id="main">
        <nav>
          <!-- サインインしているかどうか (v-if='"authorized"') でページを遷移 -->
          <router-link to="/"></router-link>
          <router-link to="/sign-in">Sign in</router-link>
        </nav>

        <router-view />
      </div>
    </div>
  </div>
</template>
<script>
import SideBar from "./views/sidebar.vue";

export default {
  components: {
    SideBar,
  },
  computed: {
    url() {
      return this.$store.state.url;
    },
  },
};
</script>

<style>
/* css grid  */

#container {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-areas: "side main ";
}

#side {
  grid-area: side;
  background: #f0f0f0;
  border-top-left-radius: 0%;
  border-top-right-radius: 0%;
  border-bottom-right-radius: 0%;
  border-bottom-left-radius: 0%;
}

#main {
  grid-area: main;
}
/* css grid  */

body {
  font-family: "Roboto", sans-serif;
}
</style>
