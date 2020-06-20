<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <div id="box">
          <v-row justify="center">
            <v-col cols="8">
              <h1 class="goal_title">
                Create Web SPA Todo App at use Django Rest Framework and Vue.
              </h1>
            </v-col>
          </v-row>

          <v-row justify="center">
            <v-col cols="8">
              <v-text-field label="Email"></v-text-field>
            </v-col>
          </v-row>

          <v-row justify="center">
            <v-col cols="8">
              <v-text-field label="password"></v-text-field>
            </v-col>
          </v-row>

          <v-row justify="center">
            <v-col cols="8">
              <v-btn
                class="btn-color"
                style="background-color: #f0f0f0;"
                rounded
                >Sign In !! <v-icon>mdi-heart</v-icon></v-btn
              >
            </v-col>
          </v-row>
        </div>
      </v-container>

      <!--  -->
      <!--  -->
      <!--  -->
      <!--  -->
      <!-- <form class="login form">
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
      <button
        @click.prevent="authenticate()"
        class="button primary"
        type="submit"
      >
        Log In
      </button>
    </form> -->
    </div>
  </div>
</template>

<script>
import api from "@/services/api";
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
      api
        .post(vm.$store.state.endpoints.obtainSessionID, payload)
        .then((response) => {
          vm.$store.commit("setSessionId", response.data);
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

#box {
  /* margin: 100px; */
  padding: 50px;
  border-radius: 77px;
  box-shadow: 5px 5px 5px #b9b9b9, -5px -5px 5px #fafafa;
}

.btn-color {
  color: rgb(84, 136, 214);
}

.goal_title {
  color: #5f75b0;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 48px;
  line-height: 56px;
}
</style>
