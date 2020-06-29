<template>
  <div>
    <v-dialog hide-overlay v-model="isDisplay" width="1500px" heigh="1200px">
      <!-- <v-card color="#f0f0f0f5" tag max-height="1000px"> -->
      <div class="background">
        <v-container>
          <br />
          <br />

          <!-- Goal -->
          <v-row>
            <v-col cols="7">
              <h4 class="goal-title">
                > Create Web SPA Todo App at use Django Rest Framework and Vue.
              </h4>
            </v-col>

            <!-- Step -->
            <v-col cols="3">
              <SoloStep></SoloStep>
            </v-col>

            <!-- Board -->
            <v-col cols="2">
              <v-chip
                class="ma-2"
                label
                color="#4465c0"
                text-color="#f0f0f0"
                large
              >
                Todo
              </v-chip>
            </v-col>
          </v-row>
          <br />

          <v-row>
            <template>
              <v-divider></v-divider>
            </template>
          </v-row>
          <br />
          <br />

          <!-- task info -->
          <AfterTask>{{ task_info }}</AfterTask>
          <br /><br />

          <!-- Discover -->
          <Discover></Discover>

          <!-- AfterGiveUp -->
          <AfterGiveUp></AfterGiveUp>

          <!-- Motivasion -->
          <AfterMotivation></AfterMotivation>

          <!-- expectation -->
          <AfterExpectation></AfterExpectation>
        </v-container>
        <!-- </v-card> -->
      </div>
    </v-dialog>
  </div>
</template>

<script>
import SoloStep from "../../../components/SoloStep";
import AfterExpectation from "./expectation/AfterExpectation";
import AfterTask from "./task_info/AfterTask";
import Discover from "./discover/Discover";
import AfterGiveUp from "../task/giveup/AfterGiveUp";
import AfterMotivation from "../task/motivation/Motivation";

export default {
  components: {
    AfterExpectation,
    AfterTask,
    SoloStep,
    Discover,
    AfterGiveUp,
    AfterMotivation,
  },
  data: () => ({
    isDisplay: false,
    task_info: "",
  }),
  methods: {
    open() {
      this.isDisplay = true;
    },
    close() {
      this.isDisplay = false;
    },
  },
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 34px;
  line-height: 40px;
  color: #088dda;
}

.category-title {
  font-family: Roboto;
  font-size: 24px;
  /* text-align: center; */
  line-height: 30px;
  color: #4d4d4d;
  padding-bottom: 15px;
}

.sub-title {
  font-family: Roboto;
  font-size: 18px;
  /* text-align: center; */
  line-height: 30px;
  color: #666666;
  padding-bottom: 15px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: #2e2e2e;
  margin-block-end: 0em;
}

.back {
  background: #f0f0f0f5;
}

.goal-title {
  font-style: normal;
  font-weight: normal;
  color: #4465c0;
  /* Match position to SoloStep */
  padding: 10px 0px;
}

.background {
  background: #f0f0f0f7;
}
</style>
