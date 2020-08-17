<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <!--  Goal Title -->


        <v-row justify="end">
          <v-col cols="2">
            <v-btn fab small depressed color="gray" @click="switchEdit">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="8" md="9" lg="8" sm="11" xs="12">
            <h1 class="goal_title">
              {{ Goal.goal_title }}
            </h1>
          </v-col>
        </v-row>

        <br />
        <v-row justify="center">
          <v-col cols="8" md="9" lg="8" sm="11" xs="12">
            <p class="writing-text">
              {{ Goal.goal_description }}
            </p>
          </v-col>
        </v-row>
        <br /><br />
        <v-row justify="center">
          <v-col cols="8" md="9" lg="8" sm="11" xs="12">
            <h2 class="category-title">
              Success criteria
            </h2>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="8" md="9" lg="8" sm="11" xs="12">
            <p class="writing-text">{{ Goal.criteria }}</p>
          </v-col>
        </v-row>
        <br />
      </v-container>
    </div>
  </div>
</template>

<script>
import Step from "./Step";
import api from "@/services/api";

export default {
  name: "Goal",
  props: ["Goal", "Steps"],

  components: {
    Step
  },
  data: function () {
    return {
      goal: "",
    };
  },
  methods: {
    switchEdit: function () {
      this.$emit("startGoalEdit");
    }
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

.edit-button {
  position: absolute;
  left: 95%;
}

@media only screen and (max-width: 600px) {

.col-8 {
    flex: 0 0 100%;
    max-width: 100%;
}
.goal_title {
  font-size: 40px;
  line-height: 56px;
}
}

</style>
