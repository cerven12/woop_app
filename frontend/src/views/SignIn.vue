<template>
  <div>
    <!--  -->
    <!--  -->
    <!--  -->
    <p>Token is  -> {{ token.data }}</p>

    <div class="field">
      <v-text-field
        v-model="email"
        type="text"
        placeholder="Email"
        autofocus="autofocus"
        maxlength="150"
        id="email"
      ></v-text-field>
    </div>

    <div class="field">
      <v-text-field
        v-model="password"
        type="password"
        placeholder="Password"
        id="id_password"
      ></v-text-field>
    </div>
    <button
      @click.prevent="authenticate()"
      class="button primary"
      type="submit"
    >
      Log In
    </button>
  </div>
</template>

<script>
import api from "@/services/api";
export default {
  data() {
    return {
      email: "",
      password: "",
      token: "",
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
      api
        .post(vm.$store.state.endpoints.obtainSessionID, payload)
        .then((response) => {
          vm.$store.commit("setSessionId", response.data);
          vm.token = response;
        });
    },
  },
};
</script>

<style scoped>
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 100%;
  grid-template-areas: "view";
  background-color: #f0f0f0;
}

#view-area {
  grid-area: view;
}

.btn-color {
  color: rgb(84, 136, 214);
}
</style>
