<template>
  <div id="app">
    <link
      href="https://fonts.googleapis.com/earlyaccess/nikukyu.css"
      rel="stylesheet"
    />
    <div id="container">
      <div id="side"><SideBar></SideBar></div>
      <div id="main">
        <!-- {{ message }} -->
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

export default {
  components: {
    SideBar,
  },
  computed: {
    message() {
      return this.$store.state.message;
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
  background: rgb(247, 247, 247);
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
