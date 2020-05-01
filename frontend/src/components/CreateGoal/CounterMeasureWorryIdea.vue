<template>
  <div>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12" md="12">
            <div v-for="worries in worryList" v-bind:key="worries.id">
              <v-textarea
                name="障壁"
                label="障壁"
                hint="行動するにあたって、不安やわからないことをたくさん書いておきましょう"
                rows="1"
                auto-grow
                v-model="worries.worry"
              ></v-textarea>
            </div>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="2"></v-col>
          <v-col cols="9">
             <div v-for="ideas in ideaList" v-bind:key="ideas.id">
            <v-textarea
              name="解決策"
              label="解決策"
              hint="前もって障壁に対する解決策を考えておきましょう"
              rows="1"
              auto-grow
              v-model="ideas.idea"
            ></v-textarea>
             </div>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="1"><v-btn depressed small @click="addIdeaForm">＋</v-btn></v-col>
        </v-row>
      </v-container>

      <v-btn @click="worryIdeaRegister"></v-btn>
    </v-form>

  </div>
</template>

<script>
export default {
  name: "CreateGoal",
  props: ["goal_id"],

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
      ideaList: [{ idea: "" }],
      parentWorryId: '',
    };
  },
  methods: {
    addIdeaForm: function() {
      const form = { idea: "" };
      this.ideaList.push(form);
    },

    worryRegister: function() {
      const vm = this;
      vm.worryList.forEach(function(worries) {
        const judgementStr = worries.worry.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgementStr) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "worries/", {
              goal: vm.goal_id,
              worry: worries.worry,
            })
            .then((response) => (vm.this_time_goal_data = response.data))
            .then((response) => console.log(vm.this_time_goal_data.worry_id))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log(`その文字列はだめです`);
        }
      });
    },

    ideaRegister: function(parentWorryId) {
      const vm = this;
      vm.ideaList.forEach(function(ideas) {
        const judgementStr = ideas.idea.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgementStr) {
          vm.axios
            .post(`${vm.url}${vm.goal_id}/worries/${parentWorryId}/ideas/`, {
              worry: parentWorryId,
              idea: ideas.idea,
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

  worryIdeaRegister: function(){
    const vm = this
    vm.worryRegister()
    vm.axios.get(vm.url + vm.goal_id)
      .then((response) => (vm.parentWorryId = response.data.worries))
      .catch((error) => { console.log(error); });
    vm.ideaRegister(vm.parentWorryId)
      },
      },
      }

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
