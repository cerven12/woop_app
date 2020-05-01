<template>
  <div id="schedule" class="input_group">
    <v-form v-model="valid">
      <v-container>
        <h2>スケジュールを組もう</h2>
        <v-row>
          <v-col cols="6" md="6">
            <v-menu
              ref="start"
              v-model="start"
              :close-on-content-click="false"
              :return-value.sync="start_date"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="start_date"
                  label="開始日"
                  prepend-icon=""
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="start_date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn text color="#37474F" @click="start = false"
                  >Cancel</v-btn
                >
                <v-btn
                  text
                  color="#37474F"
                  @click="$refs.start.save(start_date)"
                  >OK</v-btn
                >
              </v-date-picker>
            </v-menu>
          </v-col>

          <v-col cols="6" md="6">
            <v-menu
              ref="deadline"
              v-model="deadline"
              :close-on-content-click="false"
              :return-value.sync="deadline_date"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="deadline_date"
                  label="締め切り"
                  prepend-icon=""
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="deadline_date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn text color="#37474F" @click="deadline = false"
                  >Cancel</v-btn
                >
                <v-btn
                  text
                  color="#37474F"
                  @click="$refs.deadline.save(deadline_date)"
                  >OK</v-btn
                >
              </v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </div>
</template>
<script>
export default {
  name: "CreateGoal",

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
    newGoalRegister: function(goal_title) {
      const vm = this;
      vm.axios.post(vm.url, { goal_title : goal_title })
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
