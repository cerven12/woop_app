<template>
  <div>
    <v-app>
      <div id="back">
        <div id="main"></div>
        <div id="goal" class="input_group">
          <v-container>
            <v-row>
              <v-col cols="12" md="12">
                <h3>
                  あなたが達成したい目標を書きましょう
                </h3>
              </v-col>
            </v-row>

            <v-row justify="start">
              <v-col cols="8" md="12" lg="8"
                ><h1>{{ goal_title }}</h1>
              </v-col>
              <v-spacer></v-spacer>
              <v-col cols="2">
                <v-icon
                  x-large
                  color="#3f5eb5"
                  v-show="new_goal_registered"
                  id="check"
                  >mdi-check-bold</v-icon
                >
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="12">
                <div style="white-space: pre-line;">
                  {{ goal_description }}
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="目標を決めよう"
                  placeholder=""
                  outlined
                  v-model="goal_title"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="12">
                <!-- <mavon-editor
                  v-model="goal_description"
                  language="en"
                  :toolbars="toolbars"
                /> -->
                <v-textarea
                  name="詳しく"
                  label="詳しく"
                  hint="達成したとみなす水準"
                  rows="5"
                  outlined
                  auto-grow
                  placeholder="どこで、なにを、どのように、どの水準で達成したいか"
                  v-model="goal_description"
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-btn
                  class="ma-2"
                  outlined
                  @click="newGoalRegister(goal_title, goal_description)"
                  >決定</v-btn
                >
              </v-col>
            </v-row>
          </v-container>
        </div>

        <!-- <div id="step">
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-stepper alt-labels>
                  <v-stepper-header>
                    <v-stepper-step color="blue" complete step="1">
                      目標を決める
                    </v-stepper-step>
                    <v-divider></v-divider>
                    <v-stepper-step color="orange" complete step="2"
                      >モチベーションを高める</v-stepper-step
                    >
                    <v-divider></v-divider>
                    <v-stepper-step color="brown" complete step="3">
                      挫折をしないために準備する
                    </v-stepper-step>
                    <v-divider></v-divider>
                    <v-stepper-step color="green" complete step="4">
                      スケジュールを組もう
                    </v-stepper-step>
                  </v-stepper-header>
                </v-stepper>
              </v-col>
            </v-row>
          </v-container>
        </div> -->

        <CreateGoalMotivation
          :goal_id="this_time_goal_data.goal_id"
        ></CreateGoalMotivation>

        <CreateGoalCounterMeasure
          :goal_id="this_time_goal_data.goal_id"
        ></CreateGoalCounterMeasure>

        <CreateGoalSchedule
          :goal_id="this_time_goal_data.goal_id"
        ></CreateGoalSchedule>
        <br /><br /><br /><br /><br /><br /><br /><br />
      </div>
    </v-app>
  </div>
</template>

<script>
import CounterMeasureWorryIdea from "../components/CreateGoal/CounterMeasureWorryIdea.vue";
import CreateGoalCounterMeasure from "../components/CreateGoal/CreateGoalCounterMeasure.vue";
import CreateGoalMotivation from "../components/CreateGoal/CreateGoalMotivation.vue";
import CreateGoalSchedule from "../components/CreateGoal/CreateGoalSchedule.vue";

export default {
  components: {
    CounterMeasureWorryIdea,
    CreateGoalCounterMeasure,
    CreateGoalMotivation,
    CreateGoalSchedule,
  },

  data: function() {
    return {
      goal_title:
        "Django Rest FrameworkとVue CLI&Vuetifyで、SPAなタスク管理アプリケーションを作成する。",
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: "http://127.0.0.1:8000/api/v1/goals/",
      goal_description: "",
    };
  },
  methods: {
    // Goalモデルの新規登録と、登録完了:new_goal_registered = True
    newGoalRegister: function(goal_title, goal_description) {
      const vm = this;
      vm.axios
        .post(vm.url, {
          goal_title: goal_title,
          goal_description: goal_description,
        })
        .then((response) => (vm.this_time_goal_data = response.data))
        .then((reaponse) => (vm.new_goal_registered = true))
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
#goal {
  background-color: rgb(247, 247, 247);
  border-radius: 50px;
  padding: 40px 20px 40px 20px;
  margin: 40px 20px 40px 20px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);

  /* border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}
#goal:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255);
}

h1 {
  color: #3f5eb5;
}

h2,
h3 {
  color: rgb(83, 83, 83);
}
.v-stepper {
  box-shadow: none;
}

#back {
  background: rgb(247, 247, 247);
}
</style>
