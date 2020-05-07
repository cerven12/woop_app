<template>
  <div id="app">
    <link
      href="https://fonts.googleapis.com/earlyaccess/nikukyu.css"
      rel="stylesheet"
    />
    <div id="container">
      <div id="side"><SideBar></SideBar></div>
      <div id="main">
        {{ state.number }}
        <nav>
          <router-link to="/"></router-link>
        </nav>

        <router-view />
      </div>
    </div>
  </div>
</template>
<script>
import SideBar from "./views/sidebar.vue";
// import store from "./store/index.js";

export default {
  components: {
    SideBar,
  },
  computed: {
    state() {
      return this.$store.state;
    },
  },
};
</script>

<style>
/* css grid  */
#container {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-areas: "side main space";
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
