<template>
  <div>
    <v-app>
      <div id="back">
  <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"></v-parallax>

        <div id="goal" class="input_group">
          <v-container>
            <v-row>
              <v-col cols="12" md="12">
                <h3>あなたが達成したい目標を書きましょう{{ this_time_goal_data }}</h3>
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
            </v-row>

            <v-row>
              <v-col cols="10" md="10">
                <v-textarea
                  name="詳しく"
                  label="詳しく"
                  hint="達成したとみなす水準"
                  rows="3"
                  solo
                  auto-grow
                  placeholder="どこで、なにを、どのように、どの水準で達成したいか"
                  v-model="goal_description"
                ></v-textarea>
              </v-col>
            </v-row>
            
            <v-col>
                <v-btn
                  class="ma-2"
                  outlined
                  color="primary"
                  block
                  @click="newGoalRegister(goal_title, goal_description)"
                  >決定</v-btn
                >
              </v-col>

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



<CreateGoalMotivation :goal_id='this_time_goal_data.goal_id'></CreateGoalMotivation>
<CounterMeasureWorryIdea :goal_id='this_time_goal_data.goal_id'></CounterMeasureWorryIdea>
<CreateGoalCounterMeasure></CreateGoalCounterMeasure>
<CreateGoalSchedule></CreateGoalSchedule>




      <v-btn @click='updateGoal(goal_description, start_date, deadline_date)'>Goalモデルの追加項目を登録！</v-btn>
    <v-btn @click="newGoalChildRegister()">子モデルmotiveの登録！！！</v-btn>
    <v-btn @click="newWorryAndIdeaRegister()">心配と解決策の同時登録</v-btn>
      </div>

      <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
    </v-app>
  </div>
</template>

<script>
import CounterMeasureWorryIdea from "../components/CreateGoal/CounterMeasureWorryIdea.vue"
import CreateGoalCounterMeasure from "../components/CreateGoal/CreateGoalCounterMeasure.vue"
import CreateGoalMotivation from "../components/CreateGoal/CreateGoalMotivation.vue"
import CreateGoalSchedule from "../components/CreateGoal/CreateGoalSchedule.vue"


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
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: 'http://127.0.0.1:8000/api/v1/goals/',
      start_date: '',
      goal_description: '',
      motive: '',
      self_transcendence_goal: '',
      future_self: '',
      worry: '',
      idea: '',
      now_worry: '',
    };
  },
  methods: {
    newGoalRegister: function(goal_title, goal_description) {
      const vm = this;
      vm.axios.post(vm.url, { goal_title : goal_title, goal_description: goal_description })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      .then(vm.new_goal_registered = true);
    },



    updateGoal: function(goal_description, start_date, deadline_date){
      const vm = this;
      vm.axios.put(vm.url+vm.this_time_goal_data.id+'/',
      {
        id: vm.this_time_goal_data.id,
        goal_title: vm.this_time_goal_data.goal_title,
        goal_description: goal_description,
        start_date: start_date,
        deadline: deadline_date,
        })
    },
    newGoalChildRegister: function(){
      const vm = this;
      vm.axios.get(vm.url+vm.this_time_goal_data.id)
      .then(response => vm.this_time_goal_data = response.data)
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'motives/',
      { goal: vm.this_time_goal_data.goal_id, motive: vm.motive })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'self_transcendence_goals/',
      { goal: vm.this_time_goal_data.goal_id, self_transcendence_goal: vm.self_transcendence_goal })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'future_selves/',
      { goal: vm.this_time_goal_data.goal_id, future_self: vm.future_self })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'worries/',
      { goal: vm.this_time_goal_data.goal_id, worry: vm.worry })
      .then(response => vm.this_time_goal_data = response.data)
      .then(console.log(vm.this_time_goal_data))
      .catch((error) =>{ console.log(error) })
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'worries/'+vm.this_time_goal_data.worry_id+'/'+'ideas/',
      { worry: vm.this_time_goal_data.worry_id, idea: vm.idea })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
    },
  newWorryAndIdeaRegister: function(){
    const vm = this;
    vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'worries/',
    { goal: vm.this_time_goal_data.goal_id, worry: vm.worry })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      .then(response => vm.now_worry = response.data.goal.worries.worry_id)
      .then(console.log(vm.response.data.goal.worries.worry_id))
    vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'worries/'+vm.this_time_goal_data.id.worries.worry_id+'/'+'ideas'+'/',
    { worry: vm.this_time_goal_data.worries.worry_id, idea: vm.idea })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
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
