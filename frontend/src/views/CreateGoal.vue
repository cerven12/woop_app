<template>
  <div>
    <v-app>
      <div id="back">
        <div id="main"></div>
        <v-btn @click="toggle">表示の切り替え</v-btn>
        <div id="goal" class="reg">
          <template v-if="reg">
            <v-container>
              <v-row
                >{{ url }}
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
          </template>
          <!-- 登録後 -->
          <template v-else>
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
            </v-container>
          </template>
        </div>

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
const IS_REGISTERED = "IS_REGISTERED";
const IS_STANDBY = "IS_STANDBY";

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
      goal_description: "",
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",

      reg: true,
    };
  },

  computed: {
    url() {
      return this.$store.state.url;
    },
  },

  // Goalモデルの新規登録と、登録完了:new_goal_registered = True
  methods: {
    toggle: function() {
      if (this.reg === true) {
        this.reg = false;
      } else {
        this, (this.reg = true);
      }
    },

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
  background-color: #f0f0f0;
  border-radius: 50px;
  padding: 40px 40px 40px 40px;
  margin: 40px 40px 40px 40px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);

  /* border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}
#goal:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

h1 {
  color: #394e86;
}

h2,
h3 {
  color: rgb(83, 83, 83);
}
.v-stepper {
  box-shadow: none;
}

#back {
  background: #f0f0f0;
}
</style>
