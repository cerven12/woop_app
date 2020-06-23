<template>
  <div>
    <v-dialog fullscreen scrollable hide-overlay v-model="isDisplay">
      <v-card color="#f0f0f0f5" tag>
        <v-container>
          <br />
          <br />

          <!-- Goal -->
          <v-row>
            <h4 class="goal-title">
              > Create Web SPA Todo App at use Django Rest Framework and Vue.
            </h4>
          </v-row>

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

          <!-- expectation -->
          <AfterExpectation></AfterExpectation>
        </v-container>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import AfterExpectation from "./expectation/AfterExpectation";
import AfterTask from "./task_info/AfterTask";

export default {
  components: {
    AfterExpectation,
    AfterTask,
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
  color: #24a5f0;
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
  padding: 30px 0px;
}
</style>
