<template>
<div><h2>挫折をしないために準備する</h2>
  <div id="countermeasure" class="input_group">



    <div>
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col cols="4">
              <v-text-field
                label="資料"
                hint="参考にしたい資料を前もって登録しておきましょう"
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-text-field
                label="用途"
                hint="この資料の用途を書きましょう"
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-text-field label="URL"></v-text-field>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
          </v-row>
        </v-container>
      </v-form>
    </div>
  </div>
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
      url: "http://127.0.0.1:8000/api/v1/goals/",
      start_date: "",
      goal_description: "",
      motive: "",
      self_transcendence_goal: "",
      future_self: "",
      worry: "",
      idea: "",
      now_worry: "",

      worryList: [{ worry: "" }],
    };
  },
  methods: {
    addWorryForm: function() {
      const form = { worry: "" };
      this.worryList.push(form);
    },

    worryRegister: function() {
      const vm = this;
      this.worryList.forEach(function(worries) {
        const judgementStr = worries.worry.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgementStr) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "worries/", {
              goal: vm.goal_id,
              worry: worries.worry,
            })
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log(`その文字列はだめです`);
        }
      });
    },
  },

  //   newGoalRegister: function(goal_title) {
  //     const vm = this;
  //     vm.axios
  //       .post(vm.url, { goal_title: goal_title })
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .catch((error) => {
  //         console.log(error);
  //       })
  //       .then((vm.new_goal_registered = true));
  //   },
  //   updateGoal: function(goal_description, start_date, deadline_date) {
  //     const vm = this;
  //     vm.axios.put(vm.url + vm.this_time_goal_data.id + "/", {
  //       id: vm.this_time_goal_data.id,
  //       goal_title: vm.this_time_goal_data.goal_title,
  //       goal_description: goal_description,
  //       start_date: start_date,
  //       deadline: deadline_date,
  //     });
  //   },
  //   newGoalChildRegister: function() {
  //     const vm = this;
  //     vm.axios
  //       .get(vm.url + vm.this_time_goal_data.id)
  //       .then((response) => (vm.this_time_goal_data = response.data));
  //     vm.axios
  //       .post(vm.url + vm.this_time_goal_data.id + "/" + "motives/", {
  //         goal: vm.this_time_goal_data.goal_id,
  //         motive: vm.motive,
  //       })
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //     vm.axios
  //       .post(
  //         vm.url +
  //           vm.this_time_goal_data.id +
  //           "/" +
  //           "self_transcendence_goals/",
  //         {
  //           goal: vm.this_time_goal_data.goal_id,
  //           self_transcendence_goal: vm.self_transcendence_goal,
  //         }
  //       )
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //     vm.axios
  //       .post(vm.url + vm.this_time_goal_data.id + "/" + "future_selves/", {
  //         goal: vm.this_time_goal_data.goal_id,
  //         future_self: vm.future_self,
  //       })
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //     vm.axios
  //       .post(vm.url + vm.this_time_goal_data.id + "/" + "worries/", {
  //         goal: vm.this_time_goal_data.goal_id,
  //         worry: vm.worry,
  //       })
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .then(console.log(vm.this_time_goal_data))
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //     vm.axios
  //       .post(
  //         vm.url +
  //           vm.this_time_goal_data.id +
  //           "/" +
  //           "worries/" +
  //           vm.this_time_goal_data.worry_id +
  //           "/" +
  //           "ideas/",
  //         { worry: vm.this_time_goal_data.worry_id, idea: vm.idea }
  //       )
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  //   newWorryAndIdeaRegister: function() {
  //     const vm = this;
  //     vm.axios
  //       .post(vm.url + vm.this_time_goal_data.id + "/" + "worries/", {
  //         goal: vm.this_time_goal_data.goal_id,
  //         worry: vm.worry,
  //       })
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .catch((error) => {
  //         console.log(error);
  //       })
  //       .then(
  //         (response) => (vm.now_worry = response.data.goal.worries.worry_id)
  //       )
  //       .then(console.log(vm.response.data.goal.worries.worry_id));
  //     vm.axios
  //       .post(
  //         vm.url +
  //           vm.this_time_goal_data.id +
  //           "/" +
  //           "worries/" +
  //           vm.this_time_goal_data.id.worries.worry_id +
  //           "/" +
  //           "ideas" +
  //           "/",
  //         { worry: vm.this_time_goal_data.worries.worry_id, idea: vm.idea }
  //       )
  //       .then((response) => (vm.this_time_goal_data = response.data))
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  // },
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
.v-messages__message {
  padding-top: 2px;
}
</style>
