<template>
  <div id="app">
    <nav>
      <!-- サインインしているかどうか (v-if='"authorized"') でページを遷移 -->
      <router-link to="/mypage" class="hide">MyPage</router-link>
      <router-link to="/signin"class="hide">Sign in</router-link>
    </nav>
    <router-view />
  </div>
</template>
<script>
export default {
  computed: {
    url() {
      return this.$store.state.url;
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");

body {
  background: #f0f0f0;
}
#app {
  font-family: "Roboto", sans-serif;
}
.hide{
 position: absolute
 }

/*  Gray Scale */
/* body {
  -webkit-filter: grayscale(1);
  -ms-filter: grayscale(1);
  filter: grayscale(1);
}  */

/*  Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> */
</style>
