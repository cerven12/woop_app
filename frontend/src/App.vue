<template>
  <div id="app">
    <div id="container">
      <div id="side">side bar</div>
      <div id="main">
        {{ message }}
        <nav>
          <router-link to="/"></router-link>
        </nav>

        <router-view />
      </div>
    </div>
  </div>
</template>
<script>
// import CreateGoal from "./components/CreateGoal";

export default {
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
  background: rgb(239, 239, 239);
  border-top-left-radius: 0%;
  border-top-right-radius: 0%;
  border-bottom-right-radius: 0%;
  border-bottom-left-radius: 0%;
}

#main {
  grid-area: main;
}
/* css grid  */
</style>
