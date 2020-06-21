<template>
  <div id="app">
    <link
      href="https://fonts.googleapis.com/earlyaccess/nikukyu.css"
      rel="stylesheet"
    />
    <nav>
      <!-- サインインしているかどうか (v-if='"authorized"') でページを遷移 -->
      <router-link to="/">Goal</router-link>
      <router-link to="/sign-in">Sign in</router-link>
    </nav>
    <router-view />
  </div>
</template>
<script>
export default {
  components: {},
  computed: {
    url() {
      return this.$store.state.url;
    },
  },
};
</script>

<style>
body {
  font-family: "Roboto", sans-serif;
  background: #f0f0f0;
}

/*  Gray Scale */
/* body {
  -webkit-filter: grayscale(1);
  -ms-filter: grayscale(1);
  filter: grayscale(1);
} */
</style>
