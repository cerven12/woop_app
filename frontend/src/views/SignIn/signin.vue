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
export default {
  data() {
    return {
     email: "",
      password: "",
    };
  },
  methods: {
    authenticate() {
      const vm = this;
      const payload = {
        email: vm.email,
        password: vm.password,
      };
      this.axios
        .post(vm.$store.state.endpoints.obtainSessionID, payload,)
        .then((response) => {
          console.log(response.data)
          vm.$store.commit("setSessionId", response.data);
          // get and set auth user
          // const base = {
          //   baseURL: this.$store.state.endpoints.baseUrl,
          //   headers: {
          //     // Set your Authorization to 'JWT', not Bearer!!!
          //     Authorization: `JWT ${this.$store.state.jwt}`,
          //     "Content-Type": "application/json",
          //   },
          //   xhrFields: {
          //     withCredentials: true,
            // },
          // };
        });
    },
  },
};
</script>

<style lang="css"></style>
