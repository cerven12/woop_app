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
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


body {
  background: #f0f0f0;
}
#app{
font-family: 'Roboto', sans-serif;
}

/*  Gray Scale */
/* body {
  -webkit-filter: grayscale(1);
  -ms-filter: grayscale(1);
  filter: grayscale(1);
}  */


/*  Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> */
</style>
