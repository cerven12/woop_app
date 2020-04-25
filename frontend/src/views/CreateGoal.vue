<template>
  <div>
    <v-app>
      <div id="back">
        <div id="goal" class="input_group">
          <v-container>
            <v-row>
              <v-col cols="12" md="12">
                <h3>あなたが達成したい目標を書きましょう</h3>
              </v-col>
            </v-row>
            <v-row justify="start">
              <v-col cols="9" md="10" lg="9"
                ><h1>{{ goal_title }}</h1>
              </v-col>
              <v-spacer></v-spacer>
              <v-col cols="2">
                <v-icon
                  x-large
                  color="blue"
                  v-show="new_goal_registered"
                  id="check"
                  >mdi-check-bold</v-icon
                >
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="10">
                <v-text-field
                  label="目標を決めよう"
                  placeholder=""
                  solo
                  v-model="goal_title"
                ></v-text-field>
              </v-col>
              <v-col cols="2">
                <v-btn
                  class="ma-2"
                  outlined
                  color="black"
                  @click="new_goal_register(goal_title)"
                  >決定</v-btn
                >
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="12">
                <v-textarea
                  name="詳しく"
                  label="詳しく"
                  value=""
                  hint="達成したとみなす水準"
                  rows="3"
                  auto-grow
                  placeholder="どこで、なにを、どのように、どの水準で達成したいか"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
        </div>

        <div id="step">
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
        </div>

        <CreateGoalMotivation></CreateGoalMotivation>
        <CreateGoalCounterMeasure></CreateGoalCounterMeasure>
        <CreateGoalSchedule></CreateGoalSchedule>
      </div>

      <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
    </v-app>
  </div>
</template>

<script>
import CreateGoalMotivation from "@/components/CreateGoalMotivation.vue";
import CreateGoalCounterMeasure from "@/components/CreateGoalCounterMeasure.vue";
import CreateGoalSchedule from "@/components/CreateGoalSchedule.vue";

export default {
  components: {
    CreateGoalMotivation,
    CreateGoalCounterMeasure,
    CreateGoalSchedule,
  },

  data: function() {
    return {
      goal_title:
        "Django Rest FrameworkとVue CLI&Vuetifyで、SPAなタスク管理アプリケーションを作成する。",
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      new_goal_registered: false,
      valid: "",
    };
  },
  methods: {
    new_goal_register: function(goal_title) {
      const vm = this;
      vm.axios.post('http://127.0.0.1:8000/api/v1/goals/', { goal_title : goal_title })
      .then((response) => vm.new_goal_registered = true)
    },
  },
};
</script>

<style scoped>
.input_group {
  margin: 20px;
  transition: all 0.2s;
}

#motivation {
  /* background: rgba(105, 105, 105, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#countermeasure {
  /* background: rgba(79, 79, 80, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#goal {
  padding: 20px;
}
.v-stepper {
  box-shadow: none;
}
</style>

<style>
.v-messages {
  font-size: 15px;
}
.v-messages__message{
  padding-top: 2px;
}
</style>
