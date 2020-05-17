<template>
  <div></div>
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
