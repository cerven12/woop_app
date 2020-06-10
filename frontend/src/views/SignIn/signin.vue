<template lang="html">
  <form class="login form">
    <div class="field">
      <label for="id_username">Username</label>
      <input
        v-model="email"
        type="text"
        placeholder="Email"
        autofocus="autofocus"
        maxlength="150"
        id="email"
      />
    </div>
    <div class="field">
      <label for="id_password">Password</label>
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        id="id_password"
      />
    </div>
    <button @click.prevent="authenticate()" class="button primary" type="submit">
      Log In
    </button>
  </form>
</template>

<script>
import api from '@/services/api'
export default {
  data() {
    return {
     email: "",
      password: "",
    };
  },
  methods: {
    // auth & axios of initialize.
    authenticate() {
      const vm = this;
      const payload = {
        email: vm.email,
        password: vm.password,
      };
      api.post(vm.$store.state.endpoints.obtainSessionID, payload,)
        .then((response) => {
          vm.$store.commit("setSessionId", response.data);
        });
    },
  },
};
</script>

<style lang="css"></style>
