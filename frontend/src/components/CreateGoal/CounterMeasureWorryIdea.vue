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
                outlined
                auto-grow
                v-model="worries.worry"
              ></v-textarea>
            </div>
          </v-col>
        </v-row>

        <div v-for="(ideas, index) in ideaList" v-bind:key="ideas.id">
          <template v-if="index >= 1">
            <v-row justify="end">
              <v-col cols="2"></v-col>
              <v-col cols="19">
                <v-textarea
                  rows="1"
                  auto-grow
                  outlined
                  v-model="ideas.idea"
                ></v-textarea></v-col
              ><v-col cols="1">
                <v-btn
                  @click="deleteIdeaForm(index)"
                  text
                  depressed
                  height="55"
                  color="error"
                  >✘</v-btn
                ></v-col
              ></v-row
            >
          </template>
          <template v-else>
            <v-row justify="end">
              <v-col cols="2"></v-col>
              <v-col cols="10">
                <v-textarea
                  name="解決策"
                  label="解決策"
                  hint="前もって障壁に対する解決策を考えておきましょう"
                  rows="1"
                  auto-grow
                  outlined
                  v-model="ideas.idea"
                ></v-textarea>
              </v-col>
            </v-row>
          </template>
        </div>
        <v-row justify="end">
          <v-col cols="1"
            ><v-btn depressed small @click="addIdeaForm">＋</v-btn></v-col
          >
        </v-row>
        <v-btn outlined @click="worryIdeaRegister">障害と対策の登録OK</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
"use strict";

export default {
  name: "CreateGoal",
  props: ["goal_id"],

  data: function() {
    return {
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",

      worryList: [{ worry: "" }],
      ideaList: [{ idea: "" }],
      parentWorryId: "",

      worryList: [{ worry: "", ideaList: [{ ides: "" }] }],
    };
  },
  conputed: {
    url() {
      return this.$store.state.url;
    },
  },

  methods: {
    addIdeaForm: function() {
      const form = { idea: "" };
      this.ideaList.push(form);
    },

    // Delete Form
    deleteIdeaForm(index) {
      this.ideaList.splice(index, 1);
      console.log(this.ideaList);
    },

    worryIdeaRegisterX: function() {},

    // Posting `Worry` and `Idea` at the same time `axios.post`.
    worryIdeaRegister: function() {
      let vm = this;
      vm.worryList.forEach(function(worries) {
        let judgeStr = worries.worry.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgeStr) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "worries/", {
              goal: vm.goal_id,
              worry: worries.worry,
            })
            .then((res) => {
              vm.parentWorryId = res.data.worry_id;
              // Take the `idea` for the current `worry` one by one from
              // the `ideaList` and post `axios.post` them in turn.
              vm.ideaRegister(vm.parentWorryId);
            })
            .catch((error) => {
              console.log(`ideaのエラーです${error}`);
            });
          // If the `worries` is `false`.
        } else {
          console.log("そのworryの文字列は認められませんね。");
        }
      });
    },

    // Call with a `worryIdeaRegister`
    ideaRegister: function(parentWorryId) {
      const vm = this;
      vm.ideaList.forEach(function(ideas) {
        let judgeStr = ideas.idea.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgeStr) {
          vm.axios
            .post(
              vm.url + vm.goal_id + "/worries/" + parentWorryId + "/ideas/",
              {
                worry: parentWorryId,
                idea: ideas.idea,
              }
            )
            .then((res) => (vm.this_time_goal_data = res.data))
            .catch((error) => {
              console.log(`worryのエラーです${error}`);
            });
        } else {
          console.log(`そのideaの文字列はだめです`);
        }
      });
    },
  },
};
</script>

<style scoped></style>
