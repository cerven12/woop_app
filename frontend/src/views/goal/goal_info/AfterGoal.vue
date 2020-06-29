<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <!-- Step -->
        <v-row justify="center">
          <v-col cols="8">
            <Step> </Step>
          </v-col>
        </v-row>
        {{ goal }}

        <v-row><v-col></v-col><v-col></v-col></v-row>
        <!-- Vew Goal Title -->
        <v-row justify="center">
          <v-col cols="8">
            <h1 class="goal_title">
              {{ goal.goal_title }}
            </h1>
          </v-col>
        </v-row>
        <v-row justify="center">
          <v-col cols="8">
            <p class="writing-text">
              {{ goal.goal_description }}
            </p>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="8">
            <h2 class="category-title">
              Success criteria
            </h2>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="8">
            <p class="writing-text">🔥{{ goal.criteria }}</p>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import Step from "./Step";
import api from "@/services/api";

export default {
  components: {
    Step,
  },
  data: function() {
    return {
      goal: "",
    };
  },

  //  Get Goal information of the accessed pages.
  mounted: function() {
    let vm = this;
    api
      .get("goals/55a04a5e-8cdb-4317-b6ea-4bfb46142740/")
      .then(function(response) {
        vm.goal = response.data;
        vm.$store.commit("setGoaldata", response.data);
      });
  },
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
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

/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.goal_title {
  color: #4465c0;
  font-style: normal;
  font-weight: normal;
  font-size: 50px;
  line-height: 56px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 1.6;
  color: #292929;
  /* letter-spacing: 0.05em; */
}

.category-title {
  border-radius: 25px;
  font-size: 24px;
  text-align: center;
  line-height: 30px;
  color: #3a3a3a;
}

.center {
  position: relative;
}
</style>
