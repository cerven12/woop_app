<template>
  <div id="app">
    <link
      href="https://fonts.googleapis.com/earlyaccess/nikukyu.css"
      rel="stylesheet"
    />
    <div id="container">
      <div id="main">
        <nav>
          <!-- サインインしているかどうか (v-if='"authorized"') でページを遷移 -->
          <router-link to="/">Goal</router-link>
          <router-link to="/sign-in">Sign in</router-link>
        </nav>

        <router-view />
      </div>
    </div>
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
</style>
