<template>
  <div class="background">
    <v-dialog fullscreen scrollable hide-overlay v-model="isDisplay">
      <v-card>
        <v-container>
          <br />
          <br />

          <!-- Goal -->
          <v-row>
            <h4 class="goal-title">
              Create Web SPA Todo App at use Django Rest Framework and Vue.
            </h4>
          </v-row>

          <v-row>
            <template>
              <v-divider></v-divider>
            </template>
          </v-row>
          <br />
          <br />

          <v-row>
            <v-col cols="12">
              <h1 class="message-title">{{ task_info }}</h1>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12">
              <h1 class="writing-text ">
                A task management app that incorporates the Woop concept. When
                you set goals, it asks various questions to motivate you and
                prevent setbacks. Set small goals (tasks) to reach your goals
                and complete them one by one.A task management app that
                incorporates the Woop concept. When you set goals, it asks
                various questions to motivate you and prevent setbacks. Set
                small goals (tasks) to reach your goals and complete them one by
                one.
              </h1>
            </v-col>
          </v-row>

          <br /><br />
          <!-- expectation -->
          <Expectation></Expectation>
        </v-container>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Expectation from "./task_info/Expectation";

export default {
  components: {
    Expectation,
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
  color: #6d6d6d;
  margin-block-end: 0em;
}

.back {
  background: #f0f0f0;
}

.goal-title {
  font-style: normal;
  font-weight: normal;
  color: #4465c0;
  padding: 30px 0px;
}
</style>
