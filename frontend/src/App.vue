<template>
  <div id="app">
    {{ message }}
    <nav>
      <router-link to="/"></router-link>
    </nav>

    <router-view />
  </div>
</template>
<script>
// import CreateGoal from "./components/CreateGoal";

export default {

  computed: {
    message() {
      return this.$store.state.message
    },
  },
};
</script>
